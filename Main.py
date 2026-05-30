from Functions import verify_user
from Functions import calculate_tax
from Functions import save_to_csv
from Functions import read_from_csv
from Functions import save_user


user_file = "users.csv"
tax_file = "tax_records.csv"
filename = "tax_records.csv"

print("==== MALAYSIAN TAX INPUT PROGRAM ====")

registered_users = { }

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. View Tax Records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        user_id = input("Enter your user ID: ")
        ic_number = input(" Please enter your IC number:")

        if len(ic_number)!= 12 or not ic_number.isdigit():
           print("Invalid IC Number!")
           continue

        password = ic_number[-4]

        registered_users[user_id] = {
            "ic": ic_number,
            "password": password
        }

        user_data = {
            "User ID": user_id,
            "IC Number": ic_number,
            "Password": password
        }

        save_user(user_data, user_file)

        print("Registration successful!")
        print("Your password is the last 4 digits of your IC.")
        print("Password:", password)

    elif choice == "2":

        user_id = input("Enter User ID: ")

        if user_id not in registered_users:
            print("User not registered!")
            continue

        password = input("Enter Password: ")

        ic_number = registered_users[user_id]["ic"]

        valid = verify_user(ic_number, password)

        if valid:

            print("\nLogin successful!")

            while True:
                try:
                    income = float(input("Enter Annual Income (RM): "))

                    if income < 0:
                        print("Income cannot be negative!")
                    else:
                        break

                except ValueError:
                    print("Please enter a valid number!")

            while True:
                try:
                    tax_relief = float(input("Enter Total Tax Relief (RM): "))

                    if tax_relief < 0:
                        print("Tax relief cannot be negative!")
                    else:
                        break

                except ValueError:
                    print("Please enter a valid number!")

            tax_payable = calculate_tax(income, tax_relief)

            print("\n===== TAX RESULT =====")
            print("Annual Income: RM", income)
            print("Tax Relief: RM", tax_relief)
            print("Tax Payable: RM", tax_payable)


            data = {
                "User ID": user_id,
                "IC Number": ic_number,
                "Income": income,
                "Tax Relief": tax_relief,
                "Tax Payable": tax_payable
            }

            save_to_csv(data, filename)

            print("Data saved successfully!")

        else:
            print("Invalid password!")

    elif choice == "3":

        records = read_from_csv(filename)

        if records is not None:
            print("\n===== TAX RECORDS =====")
            print(records)

        else:
            print("No records found!")

    elif choice == "4":

        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.")
