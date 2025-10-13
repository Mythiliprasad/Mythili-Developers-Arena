from dataclasses import dataclass, asdict
import json, os

DB_FILE = 'pim_db.json'

@dataclass
class Person:
    name: str
    age: int
    city: str
    hobbies: list
    def formatted(self): return f"Name: {self.name}\nAge: {self.age}\nCity: {self.city}\nHobbies: {', '.join(self.hobbies) or '—'}\n"

class PersonalInfoManager:
    def __init__(self): self.people = []

    def _get_index(self, msg):
        self.list_people()
        if not self.people: return None
        idx = input(msg).strip()
        return None if not idx else int(idx) - 1 if idx.isdigit() and 0 < int(idx) <= len(self.people) else None

    def add_person(self):
        name = input('Name: ')
        try: age = int(input('Age: '))
        except: age = 0
        city = input('City: ')
        hobbies = [h.strip() for h in input('Hobbies (comma separated): ').split(',') if h.strip()]
        self.people.append(Person(name, age, city, hobbies))
        print('\nAdded:\n', self.people[-1].formatted())

    def list_people(self):
        if not self.people: return print('\nNo entries yet.\n')
        print('\n--- People ---')
        for i, p in enumerate(self.people, 1): print(f"{i}. {p.name} ({p.age}) - {p.city}")
        print()

    def view_person(self):
        i = self._get_index('View which index? ')
        if i is not None: print('\n' + self.people[i].formatted())

    def edit_person(self):
        i = self._get_index('Edit which index? ')
        if i is None: return
        p = self.people[i]
        name = input(f'Name [{p.name}]: ') or p.name
        age = input(f'Age [{p.age}]: ') or p.age
        city = input(f'City [{p.city}]: ') or p.city
        hobbies = input(f'Hobbies [{", ".join(p.hobbies)}]: ')
        hobbies = [h.strip() for h in hobbies.split(',')] if hobbies else p.hobbies
        self.people[i] = Person(name, int(age), city, hobbies)
        print('\nUpdated:\n', self.people[i].formatted())

    def delete_person(self):
        i = self._get_index('Delete which index? ')
        if i is not None: print('Removed', self.people.pop(i).name)

    def save(self):
        with open(DB_FILE, 'w') as f: json.dump([asdict(p) for p in self.people], f, indent=2)
        print('Saved.')

    def load(self):
        if not os.path.exists(DB_FILE): return print('No database found.')
        with open(DB_FILE) as f: self.people = [Person(**d) for d in json.load(f)]
        print('Loaded.')

    def menu(self):
        actions = {'1':self.add_person,'2':self.list_people,'3':self.view_person,'4':self.edit_person,
                   '5':self.delete_person,'6':self.save,'7':self.load,'8':exit}
        while True:
            print('\n1.Add 2.List 3.View 4.Edit 5.Delete 6.Save 7.Load 8.Exit')
            actions.get(input('Choice: ').strip(), lambda: print('Invalid'))()

if __name__ == '__main__':
    mgr = PersonalInfoManager()
    if os.path.exists(DB_FILE): mgr.load()
    mgr.menu()
