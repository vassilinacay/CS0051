from threading import Thread
from time import sleep
from random import random
import threading

# initialized global variables
balance = 1000
lock = threading.Lock()

# function to display transactions
def show_transaction():
    sleep(2)
    print(f"\n{'*' * 50}")
    # reading the transactions.txt file to display transactions list
    with open("transactions.txt", "r") as myFile:
        print("Transaction List:")
        for line in myFile:
            print(line.rstrip())
    myFile.close()

# task function to perform a load transaction 
def task(lock, amount, mobile_number):
    global balance

    # acquire lock
    lock.acquire()

    # modifying balance and saving transactions into file
    balance -= amount

    # the file acts as a database named "transactions.txt"
    myFile = open("transactions.txt", "a") 
    myFile.write(f">>> Sent load {amount} pesos to mobile number +63 {mobile_number}\n")
    myFile.close()
    sleep(random())
    
    # successful message
    print(f">>> Sending {amount} pesos of load to +63 {mobile_number}\n>>> Please wait for confirmation...")
    sleep(random())
    print(f">>> Transaction Completed.")

    # release lock
    lock.release()

# main function
def main():
    print(f"\n{'*' * 50}")
    print(f"Load Balance: {balance}")

    mobile_number = int(input("Enter mobile number: "))
    amount = float(input("Enter amount: "))
    # checks if balance is greater than amount to start the thread
    if balance >= amount:
        Thread(target=task, args=(lock, amount, mobile_number)).start()
    else:
        print(f"\nInsufficient balance.\n")
        sleep(3)
        main()

# main program
if __name__ == '__main__':
    counter = True
    while (counter):
        main()
        show_transaction()

        # ask and check if the user whether want to continue or exit the program
        counter1 = True
        while (counter1):    
            counter_input = input("\nPass load again? (y/n) ").lower()
            if counter_input == 'y':
                counter = True
                counter1 = False
            elif (counter_input == 'n'):
                counter = False
                counter1 = False
            else:
                print("\nInvalid input! Please try again...")
            
