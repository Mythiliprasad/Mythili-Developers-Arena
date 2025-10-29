# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Cannot divide by zero!"

# print("Addition:", add(10, 5))
# print("Subtraction:", subtract(10, 5))
# print("Multiplication:", multiply(10, 5))
# print("Division:", divide(10, 5))

# def usd_to_inr(usd):
#     return usd * 83.2

# def eur_to_inr(eur):
#     return eur * 88.5

# def gbp_to_inr(gbp):
#     return gbp * 101.4

# def converter():
#     print("1. USD to INR")
#     print("2. EUR to INR")
#     print("3. GBP to INR")
#     choice = int(input("Choose option (1-3): "))
#     amount = float(input("Enter amount: "))

#     if choice == 1:
#         print(f"{amount} USD = {usd_to_inr(amount)} INR")
#     elif choice == 2:
#         print(f"{amount} EUR = {eur_to_inr(amount)} INR")
#     elif choice == 3:
#         print(f"{amount} GBP = {gbp_to_inr(amount)} INR")
#     else:
#         print("Invalid choice!")

# converter()
# students = {}

# def add_student(name, roll):
#     students[roll] = name

# def display_students():
#     print("\n--- Student List ---")
#     for roll, name in students.items():
#         print(f"Roll No: {roll}, Name: {name}")

# def search_student(roll):
#     if roll in students:
#         print(f"Student Found: {students[roll]}")
#     else:
#         print("Student not found!")


# add_student("Mythili", 101)
# add_student("Arjun", 102)
# add_student("Ankith",103)
# add_student("sunny",104)
# add_student("boby",105)
# display_students()
# search_student(104)

# def text_analyzer(text):
#     words = text.split()
#     num_words = len(words)
#     num_chars = len(text)
#     print("Number of Words:", num_words)
#     print("Number of Characters:", num_chars)

# sample_text = "Python is fun to learn!"
# text_analyzer(sample_text)

# account = {"name": "Mythili", "balance": 0}

# def deposit(amount):
#     account["balance"] += amount
#     print(f"Deposited ₹{amount}. Current balance: ₹{account['balance']}")

# def withdraw(amount):
#     if amount <= account["balance"]:
#         account["balance"] -= amount
#         print(f"Withdrew ₹{amount}. Current balance: ₹{account['balance']}")
#     else:
#         print("Insufficient balance!")

# def display_balance():
#     print(f"Account Holder: {account['name']}")
#     print(f"Balance: ₹{account['balance']}")

# deposit(1000)
# withdraw(400)
# display_balance()

# msg = "hello python learners"

# print(msg.upper())     
# print(msg.lower())      
# print(msg.title())      
# print(msg.split())      
# print(msg.replace("python", "world"))  

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact added: {name} - {phone}")

def search_contact(name):
    if name in contacts:
        print(f"{name}'s Phone Number: {contacts[name]}")
    else:
        print("Contact not found!")

def display_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
    else:
        print("No contacts available!")

def menu():
    while True:
        print("\n📞 Contact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter Name to Search: ")
            search_contact(name)
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")


menu()




