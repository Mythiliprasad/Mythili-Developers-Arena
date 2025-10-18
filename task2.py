#  import random
# secret_number = random.randint(1, 10)
# guess = 0

# print("Guess a number between 1 and 10!")
# while guess != secret_number:
#     guess = int(input("Enter your guess: "))
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#          print(" Correct! You guessed it!")

# age = int(input("Enter your age: "))

# if age < 13:
#     print("You are a Child")
# elif age < 20:
#     print("You are a Teen")
# elif age < 60:
#     print("You are an Adult")
# else:
#     print("You are a Senior Citizen")

# shopping_list = []

# while True:
#     print("\n1. Add item\n2. Remove item\n3. View list\n4. Exit")
#     choice = input("Choose an option: ")

#     if choice == "1":
#         item = input("Enter item to add: ")
#         shopping_list.append(item)
#         print(f" '{item}' added to your list.")
#     elif choice == "2":
#         item = input("Enter item to remove: ")
#         try:
#             shopping_list.remove(item)
#             print(f"🗑️ '{item}' removed.")
#         except ValueError:
#             print(" Item not found in list.")
#     elif choice == "3":
#         print("🛒 Your Shopping List:", shopping_list)
#     elif choice == "4":
#         print("Exiting... Bye!")
#         break
#     else:
#         print(" Invalid choice, try again.")

# num = int(input("Enter a number: "))
# print(f"Multiplication Table of {num}")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# username = "manju"
# password = "mythili"

# u = input("Enter username: ")
# p = input("Enter password: ")

# if u == username and p == password:
#     print(" Login Successful")
# else:
#     print(" Invalid Credentials")

# numbers = [5, 3, 8, 6]

# numbers.append(10)
# numbers.insert(1, 20)
# numbers.remove(3)
# numbers.sort()

# print("Updated list:", numbers)
# print("Length:", len(numbers))
# print("Max:", max(numbers))
# print("Min:", min(numbers))

students = []

while True:
    name = input("\nEnter student name (or type 'exit' to finish): ")
    if name.lower() == "exit":
        break

    marks = int(input(f"Enter marks of {name} (0-100): "))

    if marks >= 90:
        grade = "A"
        comment = "Excellent "
    elif marks >= 75:
        grade = "B"
        comment = "Good "
    elif marks >= 50:
        grade = "C"
        comment = "Average "
    else:
        grade = "F"
        comment = "Fail "

    students.append([name, marks, grade, comment])

print("\n Student Result List:")
for s in students:
    print(f"Name: {s[0]}, Marks: {s[1]}, Grade: {s[2]}, Comment: {s[3]}")





