import getpass
import gspread
import time
from google.oauth2.service_account import Credentials
from datetime import date
from os import system, name

"""Imports for all modules for application to function fully:

Getpass: Prompt the user for a password without echoing.

gspread:  A Python API for Google Sheets. Read, write, and format cell ranges.

Time: The sleep() function delays execution of the current thread for the
given number of seconds

google.oauth2.service_account: So the application can access the account that
the sheet is on with the credentials

datetime: to get the current week of the year

os: The OS module in Python provides functions for interacting with the
operating system.

"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('companypayroll')

employeedetail = SHEET.worksheet('employeedetail')
employeepayroll = SHEET.worksheet('employeepayroll')


def get_payroll_week(week_status):
    """
    Get payroll week from user and validate
    if week status is normal then the user can only enter the previous week
    else if week status is any week, then can enter any week between
        1 to 52 for displaying purposes
    Can only process and amend payroll for previous week
    @param week_status(str): "normal" or "any week" coded in
    @returns: payroll_week(str)

    """
    last_week_payroll_week_number = payroll_weeks()

    while True:
        payroll_week = input("Enter Payroll Week (1-52) : ")
        if validate_data_int(payroll_week, 1, 52):
            if week_status == "normal":
                if int(payroll_week) == last_week_payroll_week_number:
                    payroll_week = "wk" + payroll_week
                    return(payroll_week)
                else:
                    print(
                        'You can only enter / '
                        'amend payroll for the current week'
                        f'which is Week {last_week_payroll_week_number}')
            elif week_status == "any week":
                payroll_week = "wk" + payroll_week
                return(payroll_week)
        else:
            print(
                'You can only enter / '
                'amend payroll for the previous week which'
                f' is Week {last_week_payroll_week_number}')


def payroll_weeks():
    """
    Get current tax week number, minus 13 weeks to start in april for
    payroll week to get the previous payroll week, minus 1 week
    @returns: last_week_payroll_week_number(str)
    isocalender code reference from
    http://week-number.net/programming/week-number-in-python.html
    """
    tax_week_number = date.today().isocalendar()[1]
    current_payroll_week_number = tax_week_number - 13
    last_week_payroll_week_number = current_payroll_week_number - 1
    return(last_week_payroll_week_number)


def get_employee_num():
    """
    Get employee number from user,validate to check that the employee
    is in the employee details list and retrieve details
    @returns: employee_num(str):Employee number given by user
    """
    from run import get_main_menu_option
    while True:
        employee_num = input("Enter Employee number e.g. 100014  : ")
        print("Finding Employment record")
        print("get_employee_num()")
        if validate_employee_num(employee_num):
            print("Employment record retrieved")
            return(employee_num)
        else:
            print("i'm here")
            get_main_menu_option()


def get_employee_hours():
    """
    Get employees hours for week from user ( maximum 100 hours) and validate
    @returns: employee_hours(float):Employee hours given by user
    """
    while True:
        employee_hours = input("Enter number of hours worked : ")
        if validate_data_float(employee_hours, 1, 100):
            return(employee_hours)


def check_for_records_in_payroll_sheet(payroll_week, employee_num):
    """
    Try:    Checks to see if there is a record for the week and
            employee number in spreadsheet.
            If there is it will return the row to delete
    except IndexError: if there isn't a value in the sheet
            then returns to the menu
    @param payroll_week(string): Payroll week
    @param employee_num(string): Employee number
    @return matched_row(int): Row to delete in spreadsheet
    @raise indexError: if no record is found
    @return :0
    intersect part of code referenced to
    https://learncodingfast.com/how-to-find-intersection-of-two-lists-in-python/
    """
    try:
        employee_num_found = employeepayroll.findall(employee_num)
        week_found = employeepayroll.findall(payroll_week)
        em = []
        for i in employee_num_found:
            em.append(i.row)
        wk = []
        for i in week_found:
            wk.append(i.row)
        set1 = set(em)
        set2 = set(wk)
        intersect = list(set1 & set2)
        matched_row = int(intersect[0])
        if matched_row >= 1:
            return (matched_row)
    except IndexError:
        print(
            'No record found, please try again, '
            'returning to main menu '
            )
        return(0)


# Validate functions
def validate_data_int(value, minvalue, maxvalue):
    """
    Inside the try, converts value to integer
    raise ValueError if strings cannot be converted into int
    or less than min or greater than max values
    @param value(string): value converted to an interger
    @param minvalue(int): Min value
    @param maxvalue(int): Max value
    @raise ValueError: raises an exception
    """
    try:
        if int(value) < minvalue or int(value) > maxvalue:
            raise ValueError(
                f'Number between {minvalue} and {maxvalue} required,'
                f' you typed {value}'
                )
    except ValueError:
        print('Invalid data, please try again.\n')
        return False

    return True


def validate_data_float(value, minvalue, maxvalue):
    """
    Inside the try, converts value to float
    raise ValueError if strings cannot be converted into float
    or less than min or greater than max value
    @param value(string): value converted to a float
    @param minvalue(int): Min value
    @param maxvalue(int): Max value
    @raise ValueError: raises an exception, if the value is incorrect
    """
    try:
        if float(value) < minvalue or float(value) > maxvalue:
            raise ValueError(
                f'Number between {minvalue} and {maxvalue} '
                f'required, you typed {value}'
                )
    except ValueError:
        print('Invalid data, please try again.\n')
        return False
    return True


def validate_employee_num(employee_num):
    """
    Try: Find employee number in employee detail sheet
    except AttributeError if there isn't a value in the sheet
        then asks the user if they want to try again or return
        to the main menu

    @param employee_num(string): Employee number
    @raise AttributeError: raises an exception if the employee
    number is incorrect
    @return employee_row(int): Employee row in sheet
    """

    try:
        print("Validating employee number")
        employee_row = employeedetail.find(employee_num).row
        print(employee_row)
        return employee_row
    except AttributeError:
        print('\nInvalid employee number, please try again.\n')
        answer = yesorno("Do you want to try again? type y or n :  ")
        print(answer)
        if answer:
            get_employee_num()
        else:
            return False


# General functions
def update_worksheet(data, worksheet):
    """
    Receives a list to be inserted into a worksheet
    Update the relevant worksheet with the data provided

    @param data(string): list of values to upload
    @param worksheet(string): google sheet name

    Code reference from code institute love sandwiches project

    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")
    time.sleep(1)
    clear()


def password():
    """
    Prompts user for password
    getpass referenced from
    https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password \
        -without-echo/
    checking the file and that the username and password are correct
        referenced from
    https://stackoverflow.com/questions/46738966/how-to-check-text-file- \
        for-usernames-and-passwords
    """
    while True:
        username = getpass.getpass(
                prompt='\nPlease enter your username: ')
        password = getpass.getpass(
                prompt='\nPlease enter your password: ')
        for line in open("credentials.txt", "r").readlines():  # Read the lines
            login_info = line.split()  # Split on the space, and store the \
            # results in a list of two strings
            if username == login_info[0] and password == login_info[1]:
                print("Correct credentials!")
                clear()
                return True
        print("Incorrect credentials, please try again.")


def clear():
    """
    Brings the function called text to the top of the terminal
    code is referenced from https://www.geeksforgeeks.org/clear-screen-python/
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def yesorno(question):
    """
    Function to take user input yes or no
    validate input

    @param question(string): Question

     Code used from https://gist.github.com/garrettdreyfus/8153571
     """
    answer = input(f'{question}')
    try:
        if answer[0] == 'y':
            return True
        elif answer[0] == 'n':
            return False
        else:
            print('Invalid entry')
            return ()
    except Exception as error:
        print("Please enter valid entry")
        print(error)
        return ()
