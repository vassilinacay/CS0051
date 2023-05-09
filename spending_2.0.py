import os
import time

class Finance:
    def __init__(self):
        self.finance_ID = 0
        self.month = ''
        self.expense_Name = ''
        self.expense_Amount = 0
        self.income_Name = ''
        self.income_Amount = 0
        self.savings_Amount = 0
        self.total_Expense = 0
        self.total_Income = 0
        self.total_Savings = 0

def add_record():
    while True:
        os.system('cls')
        print("\n----- ADD RECORD -----")
        finance = Finance()
        finance.month = input("Enter month: ").lower()

        myFile = open(f"{finance.month}.txt", "a") 

        finance.finance_ID = int(input("Enter finance ID (yyyymmdd): "))
        finance.income_Amount = int(input("Enter Income Amount: "))
        finance.expense_Amount = int(input("Enter Expense Amount: "))

        myFile.write('{:<15}{:<15}{:<15}{:<15}\n'.format(finance.finance_ID, finance.income_Amount, finance.expense_Amount, (finance.income_Amount - finance.expense_Amount)))
        myFile.close()

        print("\nAdded Successfully!")
        while True:
            print("\n[1] Add Record Again")
            print("[2] Back to Menu")
            a = int(input("Enter: "))
            if a == 1:
                add_record()
            elif a == 2:
                mainMenu()
            else:
                print("Wrong Input! Please try again...")
                time.sleep(5)

def search_record():
    while True:
        os.system('cls')
        finance = Finance()
        print("\n----- SEARCH RECORD -----")
        finance.month = input("Enter Month: ").lower()
        finance.finance_ID = input("Enter the Finance ID: ")

        try:
            with open(f"{finance.month}.txt", "r") as myFile:
                record_found = False
                print("{:<15}{:<15}{:<15}{:<15}".format("\nFINANCE_ID", "INCOME", "EXPENSE", "SAVINGS"))
                for line in myFile:
                    if line.startswith(finance.finance_ID):
                        print(line)
                        record_found = True
                if not record_found: 
                    print(f"\nNo record found with Finance ID {finance.finance_ID}. Please try again in a few seconds!")
                    time.sleep(5)
                    search_record()
                myFile.close()
        except FileNotFoundError:
            print(f"\nNo record found with month {finance.month.upper()}. Please try again in a few seconds!")
            time.sleep(5)
            search_record()
        finally:
            print("\nCommand Successful!")

        while True:
            print("\n[1] Search Record Again")
            print("[2] Back to Menu")
            a = int(input("Enter: "))
            if a == 1:
                search_record()
            elif a == 2:
                mainMenu()
            else:
                print("Wrong Input! Please try again...")
                time.sleep(5)

def display_all_records():
    while True:
        os.system('cls')
        print("\n----- DISPLAYING ALL RECORDS -----")
        finance = Finance()
        finance.month = input("\nEnter month to view: ").lower()
        try:
            with open(f"{finance.month}.txt", "r") as myFile:
                print(f"\nMONTH: {finance.month.upper()}")
                print("{:<15}{:<15}{:<15}{:<15}".format("FINANCE_ID", "INCOME", "EXPENSE", "SAVINGS"))
                for line in myFile:
                    print(line.rstrip())
            myFile.close()
        except FileNotFoundError:
            print(f"No record found with month {finance.month.upper()}. Please try again!")
            time.sleep(5)
            display_all_records()

        print("\nCommand Successful!")
        while True:
            print("\n[1] Display Record Again")
            print("[2] Back to Menu")
            a = int(input("Enter: "))
            if a == 1:
                display_all_records()
            elif a == 2:
                mainMenu()
            else:
                print("Wrong Input! Please try again...")
                time.sleep(5)

def edit_record():
    while True:
        os.system('cls')
        print("\n----- EDIT RECORD -----")
        finance = Finance()
        finance.month = input("\nEnter Month: ").lower()
        finance.finance_ID = input("Enter Finance ID you want to edit: ")

        with open(f"{finance.month}.txt", "r") as myFile:
            lines = myFile.readlines()
            for i, line in enumerate(lines):
                if line.startswith(finance.finance_ID):
                    print("{:<15}{:<15}{:<15}{:<15}".format("\nFINANCE_ID", "INCOME", "EXPENSE", "SAVINGS"))
                    print(line)
                    finance.finance_ID = int(input("\nEnter New finance ID (yyyymmdd): "))
                    finance.income_Amount = int(input("Enter New Income Amount: "))
                    finance.expense_Amount = int(input("Enter New Expense Amount: "))

                    new_line = ('{:<15}{:<15}{:<15}{:<15}\n'.format(finance.finance_ID, finance.income_Amount, finance.expense_Amount, (finance.income_Amount - finance.expense_Amount)))
                    lines[i] = new_line

                    print("\nCommand Successful!")
                    break
                else:
                    print(f"\nNo record found with Finance ID {finance.finance_ID}. Please try again!")
                    time.sleep(5)
                    edit_record()

        with open(f"{finance.month}.txt", "w") as myFile:
            myFile.writelines(lines)

        while True:
            print("\n[1] Edit Record Again")
            print("[2] Back to Menu")
            a = int(input("Enter: "))
            if a == 1:
                edit_record()
            elif a == 2:
                mainMenu()
            else:
                print("Wrong Input! Please try again...")
                time.sleep(5)

def delete_record():
    while True:
        os.system('cls')
        finance = Finance()
        
        print("\n----- DELETE RECORD -----")
        print("[1] Delete Transaction")
        print("[2] Delete All Transaction in a Month")
        choice = int(input("Enter your selection: "))

        if choice == 1:
            finance.month = input("\nEnter Month: ").lower()
            finance.finance_ID = input("Enter Finance ID you want to delete: ")

            temp_file = open("temp.txt", "w") # create a temporary file to write the updated data

            with open(f"{finance.month}.txt", "r") as myFile:
                for line in myFile:
                    if finance.finance_ID not in line: # copy all the lines except the one with the given finance ID
                        temp_file.write(line)
    
            temp_file.close()
            os.remove(f"{finance.month}.txt") # remove the original file
            os.rename("temp.txt", f"{finance.month}.txt") # rename the temporary file to the original file name
    
            print(f"\nRecord with Finance ID {finance.finance_ID} has been deleted.")

        elif choice == 2:
            finance.month = input("\nEnter Month: ").lower()

            confirmation = input(f"\nDo you want to delete the all records in the month of {finance.month.upper()}? (y/n): ").lower()
            if confirmation == 'y':
                os.remove(f"{finance.month}.txt")
                print(f"\nAll records in the month of {finance.month.upper()} has been deleted!")
            elif confirmation == 'n':
                delete_record()
            else: 
                print("\nWrong Input! Please try again.\n")
                time.sleep(2)
        else:
            os.system('cls')
            print("Wrong Input! Please try again.\n")
            delete_record()

        while True:
            print("\n[1] Delete Record Again")
            print("[2] Back to Menu")
            a = int(input("Enter: "))
            if a == 1:
                delete_record()
            elif a == 2:
                mainMenu()
            else:
                print("Wrong Input! Please try again...")
                time.sleep(5)

def mainMenu():
    while True:
        os.system('cls')
        print("Welcome to your Finance Tracker!")
        print("*" * 45)
        print("\t[1] Add")
        print("\t[2] Search")
        print("\t[3] Display")
        print("\t[4] Edit")
        print("\t[5] Delete")
        print("\t[6] Exit")
        print("*" * 45)
        choice = int(input("Enter your selection: "))

        if choice == 1:
            add_record()
        elif choice == 2:
            search_record()
        elif choice == 3:
            display_all_records()
        elif choice == 4:
            edit_record()
        elif choice == 5:
            delete_record()
        elif choice == 6:
            os.system('cls')
            print("\nTrack your Finance, Save you money!")
            print("Thank you!\n")
            exit(0)
        else: 
            print("Wrong Input! Please try again...")
            time.sleep(5)
            mainMenu()

mainMenu()