"""
Main File run.py, for payroll applicaiton by Chris Carabine

This is the main file for a command line interface payroll system for
staff to process employees hours for payroll.

The data is pushed to and read from google sheet, stored on google drive
"""
import getpass
import gspread
import pandas as pd
import sys
import os
import termios
from google.oauth2.service_account import Credentials
from menu import main_menu, display_payroll_menu, process_amend_payroll_menu, \
    add_amend_employee_menu, welcome_menu
from datetime import date
from os import system, name

"""
Imports for all modules for application to function fully:

Getpass: Prompt the user for a password without echoing.

gspread:  A Python API for Google Sheets. Read, write, and format cell ranges.

Pandas:  allows importing data and manipulation operations such as merging,
reshaping, selecting, as well as data cleaning, and data wrangling features.

google.oauth2.service_account: So the application can access the account that
the sheet is on with the credentials

datetime: to get the current week of the year

os: The OS module in Python provides functions for interacting with the
operating system. Used for the clear function

sys:

"""


"""
SCOPES, CREDS, SCOPED_CREDS,GSPREAD_CLIENT,SHEET : used with Google API Client
to gain access to and modify data on Google Sheets.
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


# Puts the data from employeepayroll in to a pandas data frame
data = employeepayroll.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

# Constant variables
HOL_PC = 0.1208
EMPLOYEES_NI_PC = 0.12
EMPLOYEES_NI_AMOUNT = 184

EMPLOYERS_PENSION_PC = 0.03
EMPLOYERS_NI_PC = 0.138
EMPLOYERS_NI_AMOUNT = 170


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

    try:
        while True:
            payroll_week = input("Enter payroll week (numeral) : ")
            if validate_data_int(payroll_week, 1, 52):
                if week_status == "normal":
                    if int(payroll_week) == last_week_payroll_week_number:
                        payroll_week = "wk" + payroll_week
                        return(payroll_week)
                    else:
                        print(
                            'You can only enter / '
                            'amend payroll for the current week '
                            f'which is week {last_week_payroll_week_number}')
                elif week_status == "any week":
                    payroll_week = "wk" + payroll_week
                    return(payroll_week)
    except KeyError:
        print('Invalid week number, please try again.\n')
        return False


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
    while True:
        employee_num = input("Enter employee number : ")
        print("Finding employment record")
        if validate_employee_num(employee_num):
            print("Employment record located")
            return(employee_num)
        else:
            clear()
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
            'No entry found in payroll'
            )
        return(0)


# Menu options functionality
def get_main_menu_option():
    """
    Display menu
    Get Main menu option input from user
    Run function related to input
    """
    while True:
        main_menu()
        main_menu_option_data = input(
            'Please enter number option from the menu : ')
        if validate_data_int(main_menu_option_data, 1, 4):
            if main_menu_option_data == "1":
                clear()
                get_display_payroll_option()
            if main_menu_option_data == "2":
                clear()
                get_process_payroll_option()
            if main_menu_option_data == "3":
                clear()
                get_add_amend_employee_option()
            if main_menu_option_data == "4":
                quit()


def get_display_payroll_option():
    """
    Display menu
    Get display payroll option input from user
    Run function related to input
    """
    while True:
        display_payroll_menu()
        display_payroll_option_data = input(
            'Please enter number option from the menu : '
            )
        if validate_data_int(display_payroll_option_data, 1, 4):
            if display_payroll_option_data == "1":
                display_all_employeepay_for_week()
            if display_payroll_option_data == "2":
                display_ind_employee_pay_for_week()
            if display_payroll_option_data == "3":
                get_employerssummary_option()
            if display_payroll_option_data == "4":
                clear()
                get_main_menu_option()


def get_process_payroll_option():
    """
    Display menu
    Get process / Amend payroll option input from user
    Run function related to input
    """
    while True:
        process_amend_payroll_menu()
        process_payroll_option_data = input(
            'Please enter number option from the menu : '
            )
        if validate_data_int(process_payroll_option_data, 1, 3):
            if process_payroll_option_data == "1":
                process_payroll_option_1()
            if process_payroll_option_data == "2":
                process_payroll_option_2()
            if process_payroll_option_data == "3":
                clear()
                get_main_menu_option()
        return()


# Display menu functionility
def display_all_employeepay_for_week():
    """
    Request user to input payroll week,display data for week

    groupby referenced from
    https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
    """
    try:
        week = get_payroll_week("any week")
        data_by_week = df.groupby('Week Number')
        filtered_data_by_week = data_by_week.get_group(week)
        print("------------------------------------------")
        print("------- People Payroll Application -------")
        print("------------ All employees' pay ----------")
        print("------------------------------------------")
        print("\n")
        print(filtered_data_by_week)
        print(
            '\nPress any key to clear the screen and return to the display '
            'payroll menu'
            )
        wait_key()
        clear()
    except KeyError:
        print('Invalid week number, please try again.\n')
        print(
            '\nPress any key to clear the screen and return to the display '
            'payroll menu'
            )
        wait_key()
        clear()
        return False


def display_ind_employee_pay_for_week():
    """
    Request user to enter payroll week and employee number,
    validation to ensure there is a record displays employee pay record
    """
    week = get_payroll_week("any week")
    employee_num = get_employee_num()
    display_employee_data = df.loc[
        (df['Week Number'] == (week)) & (
            df['Employee Number'] == (employee_num)), [
                    'Week Number', 'Employee Number',
                    'First Name', 'Surname', 'Basic Pay', 'Holiday Pay',
                    'Employees NI', 'Employees Pension', 'NET Pay'
                    ]]
    if display_employee_data.empty:
        print(
            f'\nNo payroll record found for employee number: {employee_num}'
            f' in {week}.\n')
        print(
            'Press any key to clear the screen and return to the'
            ' display payroll menu')
        wait_key()
        clear()
    else:
        print("------------------------------------------")
        print("------- People Payroll Application -------")
        print(f'------------ Employee {employee_num} pay ---------')
        print("------------------------------------------")
        print("\n")
        print(display_employee_data)
        print(
            '\nPress any key to clear the screen and return to the'
            ' display payroll menu')
        wait_key()
        clear()


def get_employerssummary_option():
    """
    Displays Employers amounts to pay out
    summarising data reference from
    https://stackoverflow.com/questions/43745301/converting-column-from- /
    dataframe-to-float-for-sum-usage-python-pandas
    """
    company_payroll_data = df.groupby(
        ['Week Number'])[[
                'NET Pay',
                'Employees NI', 'Employees Pension',
                'Company NI', 'Company Pension'
                ]].agg(lambda x: sum(x.astype(float)))
    print("------------------------------------------")
    print("------- People Payroll Application -------")
    print("------- Employers payment summary --------")
    print("------------------------------------------")
    print("\n")
    print(company_payroll_data)
    print(
        '\nPress any key to clear the screen and return to the display'
        ' payroll menu'
        )
    wait_key()
    clear()


# Add / amend payroll functionality
def process_payroll_option_1():
    """
    Process payroll option 1 -run functions below to add employees hours
    """
    payroll_week = payroll_weeks()
    payroll_week = "wk" + str(payroll_week)
    print(f'Payroll week is {payroll_week}\n')
    employee_num = get_employee_num()
    row_num = check_for_records_in_payroll_sheet(payroll_week, employee_num)
    row_num = int(row_num)
    if row_num >= 1:
        print(
            f'Employees hours already entered in {payroll_week}'
            f', please go to option 2 to amend \n')
        print(
            '\nPress any key to clear the screen and return to the Process '
            'amend payroll menu'
            )
        wait_key()
        clear()
        get_process_payroll_option()
    else:
        calculate_employee_payslip_data(payroll_week, employee_num)
        next_employee_to_process()


def next_employee_to_process():
    """
    Requests user input if they would like to process another employees hours
    """
    while True:
        if yesorno(
            'Would you like to process another '
            'employees hours? type y or n :  '
                ):
            process_payroll_option_1()
            return()
        else:
            clear()
            get_main_menu_option()


def calculate_employee_payslip_data(payroll_week, employee_num):
    """
    Get Employees details from spreadsheet,
    calculate values and updates worksheet
    @param payroll_week(str): payroll week
    @param employee_num : Employee number
    """
    employee_row = validate_employee_num(employee_num)
    employee_retrived_data = get_employee_data(employee_row)
    employee_num = (employee_retrived_data[0])
    employee_surname = (employee_retrived_data[1])
    employee_firstname = (employee_retrived_data[2])
    employee_rate_of_pay = float(employee_retrived_data[3])
    employee_pension = float(employee_retrived_data[4])

    employee_hours_data = (get_employee_hours())
    employee_hours = float(employee_hours_data)
    employee_basic_pay = round(employee_hours * employee_rate_of_pay, 2)
    employee_holiday = round(employee_basic_pay * HOL_PC, 2)
    employee_basic_hol = (employee_basic_pay + employee_holiday)
    if (employee_basic_pay + employee_holiday) < EMPLOYEES_NI_AMOUNT:
        employee_ni = 0
    else:
        employee_ni = round(
            ((employee_basic_hol) - EMPLOYEES_NI_AMOUNT) * EMPLOYEES_NI_PC, 2
            )
    employee_pension = round(employee_pension * employee_basic_hol, 2)
    employee_net_pay = round(
        employee_basic_hol - employee_ni - employee_pension, 2
        )
    if (employee_basic_pay + employee_holiday) < EMPLOYERS_NI_AMOUNT:
        employers_ni = 0
    else:
        employers_ni = round(
            ((employee_basic_hol) - EMPLOYERS_NI_AMOUNT) * EMPLOYERS_NI_PC, 2
            )
    employers_pension = round(employee_basic_hol * EMPLOYERS_PENSION_PC, 2)
    print(
        f'\n Employee : {employee_num} - '
        f'{employee_firstname} {employee_surname}'
        )
    print(f' Basic Pay : £{employee_basic_pay}')
    print(f' Holiday Pay : £{employee_holiday}')
    print(f' NI contribution: £{employee_ni}')
    print(f' Pension contribution: £{employee_pension}')
    print(f' Net Pay: £{employee_net_pay}')
    if yesorno("Are the amounts correct? "):
        print("\nReady to upload into payroll spreadsheet \n")
        row_data = [
                payroll_week, employee_num,
                employee_surname, employee_firstname,
                employee_hours, employee_basic_pay,
                employee_holiday, employee_ni,
                employee_pension, employee_net_pay,
                employers_ni, employers_pension
        ]
        update_worksheet(row_data, "employeepayroll")
        return ()
    else:
        print("Re enter details \n")
        calculate_employee_payslip_data(
            payroll_week, employee_num)


def get_employee_data(employee_row):
    """
    Gets the values from employee detail Google Sheets and returns values
    @param employee_row(string): Employee row in google sheets
    @returns: employee_num(str) :Employee number
    @returns: employee_surname(str) :Employee Surname
    @returns: employee_firstname(str) :Employee first name
    @returns: employee_rate_of_pay(float)
    @returns: employee_pension(float)
    """
    employee_num = employeedetail.cell(employee_row, 1)
    employee_surname = employeedetail.cell(employee_row, 2)
    employee_firstname = employeedetail.cell(employee_row, 3)
    employee_rateofpay = employeedetail.cell(employee_row, 4)
    employee_pension = employeedetail.cell(employee_row, 5)
    return employee_num.value,\
        employee_surname.value,\
        employee_firstname.value,\
        employee_rateofpay.value,\
        employee_pension.value


def process_payroll_option_2():
    """
    Process payroll option 2 -run functions below to amend employees hours
    payrolls_weeks is the previous week
    """
    payroll_week = payroll_weeks()
    payroll_week = "wk" + str(payroll_week)
    print(f'Payroll week is {payroll_week}\n')
    employee_num = get_employee_num()
    amend_employees_hours(payroll_week, employee_num)


def amend_employees_hours(payroll_week, employee_num):
    """
    Try: Delete the payroll information for the employee and
        request user to put the hours again
    except IndexError if there isn't a value in the sheet
        then returns to the process/amend menu

    @param payroll_week(string): Payroll week
    @param employee_num(string): Employee number

    @raise indexError: if no record is found
    """
    try:
        row_to_delete = check_for_records_in_payroll_sheet(
            payroll_week, employee_num)
        if (row_to_delete == 0):
            raise IndexError()
        employeepayroll.delete_rows(row_to_delete)
        calculate_employee_payslip_data(
            payroll_week, employee_num,)
        print(
            '\nPress any key to clear the screen and return to the Process '
            '/ amend payroll menu')
        wait_key()
        clear()
        get_process_payroll_option()
    except IndexError:
        print(
            f'\nNo payroll record found for {employee_num} in week'
            f' {payroll_week}, returning to main menu.\n')
        print(
            '\nPress enter to clear the screen and return to the Process '
            '/ amend payroll menu'
            )
        wait_key()
        clear()
        get_process_payroll_option()


# Add / amend employee functionality
def get_add_amend_employee_option():
    """
    Get add / amend employee option input from user
    Run function related to input
    Future feature
    """
    while True:
        add_amend_employee_menu()
        print('\nPress any key to clear the screen and return to the Main menu')
        wait_key()
        clear()
        get_main_menu_option()


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
        employee_row = employeedetail.find(employee_num).row
        return employee_row
    except AttributeError:
        print('\nInvalid employee number, please try again.\n')
        answer = yesorno("Do you want to try again? type y or n :  ")
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
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


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
        print("Login (Characters will not be visible on screen when typed)")
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


def main():
    """
    Run all program functions
    """
    password()
    get_main_menu_option()


def wait_key():
    """
    Wait for a key press on the console
    referenced from https://stackoverflow.com/questions/983354/ \
    how-to-make-a-script-wait-for-a-pressed-key
    """
    try:
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    
clear()
welcome_menu()
main()
