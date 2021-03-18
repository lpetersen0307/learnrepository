#!/usr/bin/python
import csv
from typing import NamedTuple
class Employee(NamedTuple):
    id: int
    full_name: str
    email: str
    phone: str

message= print("Welcome to Contact Manager!")
e1 = Employee(1, 'Guido van Rossum', 'guido@rossum.com', '215-555-5555')
e2 = Employee(2, 'Eric Idle', 'eric@ericidle.com', '+44 20 7946 0958')

employees = [e1, e2]
def get_email():
                while True:
                    email = input("Enter employee email address:     ").strip()
                    at_index = email.find('@')
                    dot_index = email.find(".", at_index)
                    if at_index == -1 or dot_index == -1:
                        print("Please enter valid email address:", email)
                    else:
                        return email
def get_phone_number():
    while True:
        phone = input("Enter phone number:       ").strip()
        phone = phone.replace("-","")
        phone = phone.replace(" ","")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        phone = phone.replace(".", "")
        allnumbers = phone.isdigit()
        if len(phone) < 10 or allnumbers == -1:
            print("Please enter valid phone number.")
        else:
            return phone
## Show menu ##
def print_menu():
    print (30 * '-')
    print ("   COMMAND MENU")
    print (30 * '-')
    print ("1. List - Display all contacts")
    print ("2. View - View a contact")
    print ("3. Add - Add a contact")
    print ("4. Delete - Delete a contact")
    print ("5. Exit - Exit Program")
    print (30 * '-')

loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()     ## Displays menu

## Get input ###
    choice = input('Enter your choice [1-5] : ')
    choice = int(choice)
    ### Take action as per selected menu-option ###
    if choice == 1:
            print ("Displaying all contacts")
            print (30 * '-')
            for employee in employees:
                print (str(employee.id) + " " + str(employee.full_name))
            continue
    elif choice == 2:
            print ("Viewing a contact")
            selection = input('Enter the employee id : ')
            selection = int(selection)
            for employee in employees:
                try:
                    if selection == employee.id:
                        print ("Viewing Employee Information:")
                        print (30 * '-')
                        print (str(employee.full_name) + " " + str(employee.email) + " " + str(employee.phone))
                        print (30 * '-')
                except:
                    print ("Invalid number. Try again...")
                continue
    elif choice == 3:
            print ("Adding a contact")
            first_name = input('Enter the employee first_name : ')
            # add a contact
            last_name= input("Last name: ")
            full_name= first_name + " " + last_name
            email = get_email()
            phone = get_phone_number()
            new_id = employees[-1].id + 1
            new_employee = []
            e3 = Employee(new_id, full_name, email, phone)
            employees.append(e3)
            print("Adding new employee " + full_name)
            print (30 * '*')
            continue
    elif choice == 4:
            print ("Deleting a contact")
            deletion = input('Enter the employee id you want to delete: ')
            deletion = int(deletion)
            for employee in employees:
                index = employees.index(employee)
                #print (index)
                try:
                    if deletion == employee.id:
                        del employees[index]
                        print ('Deleted employee: ' + str(employee.full_name))
                        print (30 * '*')
                except:
                    print ("Invalid number. Try again...")
            continue
    elif choice == 5:
            print ("Exiting program")
            loop=False
            break
    else:    ## default ##
            print ("Invalid number. Try again...")
