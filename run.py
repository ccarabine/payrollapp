"""
Main File run.py, for payroll applicaiton by Chris Carabine

This is the main file for a command line interface payroll system for
staff to process employees hours for payroll.

The data is pushed to and read from google sheet, stored on google drive
"""
import gspread
import getpass
from datetime import date
import pandas as pd
import time
from os import system, name
from google.oauth2.service_account import Credentials
from menu import main_menu, display_payroll_menu, process_amend_payroll_menu, \
    add_amend_employee_menu
from algorithms import calculate_payroll_values, payroll_weeks

"""
Imports for all modules for application to function fully:

gspread:  A Python API for Google Sheets. Read, write, and format cell ranges.

Getpass: Prompt the user for a password without echoing.

datetime: to get the current week of the year

Pandas:  allows importing data and manipulation operations such as merging,
reshaping, selecting, as well as data cleaning, and data wrangling features.

Time: The sleep() function delays execution of the current thread for the
given number of seconds.

os: The OS module in Python provides functions for interacting with the
operating system.

google.oauth2.service_account: So the application can access the account that
the sheet is on with the credentials

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


"""
Puts the data from employeepayroll in tp a pandas data frame
"""
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
    @returns: payroll_wk(str)

    """
    last_week_payroll_week_number = payroll_weeks()

    while True:
        input_payroll_week = input("Enter Payroll Week (1-52) : ")
        if validate_data_int(input_payroll_week, 1, 52):
            if week_status == "normal":
                if int(input_payroll_week) == last_week_payroll_week_number:
                    payroll_wk = "wk" + input_payroll_week
                    return(payroll_wk)
                else:
                    print(
                        'You can only enter / '
                        'amend payroll for the current week'
                        f'which is Week {last_week_payroll_week_number}')
            elif week_status == "any week":
                payroll_wk = "wk" + input_payroll_week
                return(payroll_wk)
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
    @returns: input_employee_num(str):Employee number given by user
    @returns: status(str): Status coded in
    """
    while True:
        input_employee_num = input("Enter Employee number e.g. 100014  : ")
        print("Finding Employment record")
        if validate_employee_num(input_employee_num, 1):
            print("Employment record retrieved")
            status = "1"
            return(input_employee_num, status)


def get_employee_hours():
    """
    Get employees hours for week from user ( maximum 100 hours) and validate
    @returns: input_employee_hours(float):Employee hours given by user
    """
    while True:
        input_employee_hours = input("Enter number of hours worked : ")
        if validate_data_float(input_employee_hours, 1, 100):
            return(input_employee_hours)


def calculate_employee_payslip_data(
    entered_payroll_week, employee_num, status
        ):
    """
    Get Employees details from spreadsheet,
    calculate values and updates worksheet
    @param entered_payroll_week(str): payroll week
    @param employee_num : Employee number
    @param status(str) : Status
    @returns: payroll_wk(str) : Payroll week
    """
    employee_row = validate_employee_num(employee_num, "1")
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
        print("Ready to upload into payroll spreadsheet")
        row_data = [
                entered_payroll_week, employee_num,
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
            entered_payroll_week, employee_num, status)


def get_main_menu_option():
    """
    Get Main menu option input from user
    Run function related to input
    """
    while True:
        main_menu()
        main_menu_option_data = input(
            'Please enter number option from the menu : ')
        if validate_data_int(main_menu_option_data, 1, 3):
            if main_menu_option_data == "1":
                clear()
                get_display_payroll_option()
            if main_menu_option_data == "2":
                clear()
                get_process_payroll_option()
            if main_menu_option_data == "3":
                clear()
                get_add_amend_employee_option()


def get_display_payroll_option():
    """
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
                clear()
                display_all_employeepay_for_week()
            if display_payroll_option_data == "2":
                clear()
                display_ind_employee_pay_for_week()
            if display_payroll_option_data == "3":
                clear()
                get_employerssummary_option()
            if display_payroll_option_data == "4":
                clear()
                get_main_menu_option()


def get_process_payroll_option():
    """
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
                clear()
                process_payroll_option_1()
            if process_payroll_option_data == "2":
                clear()
                process_payroll_option_2()
            if process_payroll_option_data == "3":
                clear()
                get_main_menu_option()
        return()

def get_add_amend_employee_option():
    """
    Get add / amend employee option input from user
    Run function related to input
    Future feature
    """
    while True:
        add_amend_employee_menu()
        get_main_menu_option()

def process_payroll_option_1():
    """
    Process payroll option 1 -run functions below to add employees hours
    """
    entered_payroll_week = get_payroll_week("normal")
    employee_num = get_employee_num()
    status = "1"
    employee_num = employee_num[0]
    check_data_in_payroll_sheet(entered_payroll_week, employee_num, status)
    calculate_employee_payslip_data(entered_payroll_week, employee_num, status)
    next_employee_to_process()


def process_payroll_option_2():
    """
    Process payroll option 2 -run functions below to amend employees hours
    """
    entered_payroll_week = get_payroll_week("normal")
    employee_num = get_employee_num()
    amend_employees_hours(entered_payroll_week, employee_num)





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


def validate_employee_num(employee_num, status):
    """
    Try: find employee number in employee detail sheet
    except AttributeError if there isn't a value in the sheet
        then asks the user if they want to try again or return
        to the main menu

    @param employee_num(string): Employee number
    @param status(string): Status value coded in
    @raise AttributeError: raises an exception if the employee
    number is incorrect
    @return employee_row(int): Employee row in sheet
    """
    try:
        print("Validating employee number")
        employee_row = employeedetail.find(employee_num).row
        return employee_row
    except AttributeError:
        print('\nInvalid employee number, please try again.\n')
        while True:
            if yesorno("Do you want to try again? type y or n :  "):
                break
            get_main_menu_option()

def get_employee_data(employee_row):
    """
    Gets the values from employee detail Google Sheets and returns values

     @param employee_row(string): Employee number
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
  

    """
    Get Employees details from spreadsheet,
    and returns values
    @param entered_payroll_week(str): payroll week
    @param employee_num : Employee number
    @param status(str) : Status

    @returns: payroll_wk(str) : Payroll week
    @returns: employee_num(str) :Employee number
    @returns: employee_surname(str) :Employee Surname
    @returns: employee_firstname(str) :Employee
    @returns: employee_rate_of_pay(float)
    @returns: employee_pension(float)
    @returns: employee_hours(float)
    """
  
    #return (payroll_week, employee_num, employee_surname, employee_firstname,
     #   employee_rate_of_pay, employee_rate_of_pay, employee_pension,
     #   employee_hours)


def check_data_in_payroll_sheet(entered_payroll_week, employee_num, status):
    """
    Try:    Checks to see if there is a record for the week and
            employee number in spreadsheet.
            If there is it will return the row to delete
    except IndexError: if there isn't a value in the sheet
            then returns to the process/amend menu
    @param entered_payroll_week(string): Payroll week
    @param employee_num(string): Employee number
    @return row_to_delete(int): Row to delete in spreadsheet
    @raise indexError: if no record is found
    intersect part of code referenced to
    https://learncodingfast.com/how-to-find-intersection-of-two-lists-in-python/
    """
    try:
        employee_num_found = employeepayroll.findall(employee_num)
        week_found = employeepayroll.findall(entered_payroll_week)
        em = []
        for i in employee_num_found:
            em.append(i.row)
        wk = []
        for i in week_found:
            wk.append(i.row)
        set1 = set(em)
        set2 = set(wk)
        intersect = list(set1 & set2)
        row_to_delete = intersect[0]
        if row_to_delete >= 1:
            print(
                f'Record for {employee_num} found in '
                f'week {entered_payroll_week} '
                )
            if status == "1":
                print("Returning to menu")
                get_process_payroll_option()
            elif status == "2":
                return (row_to_delete)
            elif status == "3":
                return(row_to_delete)
    except IndexError:
        if status == "1":
            print('No payroll entry found, ready to process employee ')
            return(entered_payroll_week, employee_num[0])
        elif status == "2":
            print(
                'No record found, select option 1 to '
                'process employees hours '
                )
            get_process_payroll_option()
        elif status == "3":
            print(
                'No record found, select option 2, try again or'
                ' select another option '
                )
            get_display_payroll_option()


def amend_employees_hours(entered_payroll_week, employee_num):
    """
    Try: Delete the payroll information for the employee and
        request user to put the hours again
    except IndexError if there isn't a value in the sheet
        then returns to the process/amend menu

    @param entered_payroll_week(string): Payroll week
    @param employee_num(string): Employee number

    @raise indexError: if no record is found
    """
    try:
        employee_num = employee_num[0]
        row_to_delete = check_data_in_payroll_sheet(
            entered_payroll_week, employee_num, "2"
            )
        employeepayroll.delete_rows(row_to_delete)
        calculate_employee_payslip_data(
            entered_payroll_week, employee_num, "2"
            )
        print('Updated payroll information')
    except IndexError:
        print(
            f'\nNo payroll record found for {employee_num} in week'
            f' {entered_payroll_week}, returning to main menu.\n')
        get_process_payroll_option()


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


def update_worksheet(data, worksheet):
    """
    Receives a list to be inserted into a worksheet
    Update the relevant worksheet with the data provided

    @param data(string): list of values to upload
    @param worksheet(string): google sheet name

    Code reference from code institute love sandwiches project

    """
    print(data)
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")
    time.sleep(1)
    clear()


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
            get_main_menu_option()


def display_all_employeepay_for_week():
    """
    Request user to input payroll week,display data for week

    groupby referenced from
    https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
    """
    week = get_payroll_week("any week")
    data_by_week = df.groupby('Week Number')
    filtered_data_by_week = data_by_week.get_group(week)
    print(filtered_data_by_week)
    time.sleep(3)


def display_ind_employee_pay_for_week():
    """
    Request user to enter payroll week and employee number,
    validation to ensure there is a record displays employee pay record

    sleep referenced from
    https://www.codegrepper.com/code-examples/python/how+to+pause+after+a+print+statement+in+python
    """
    
    week = get_payroll_week("any week")
    employee_num = get_employee_num()
    employee_num = employee_num[0]
    clear()
    display_employee_data = df.loc[
        (df['Week Number'] == (week)) & (
            df['Employee Number'] == (employee_num)), [
                    'Week Number', 'Employee Number',
                    'First Name', 'Surname', 'Basic Pay', 'Holiday Pay',
                    'Employees NI', 'Employees Pension', 'NET Pay'
                    ]]
    if display_employee_data.empty:
        print(
            f'\nNo payroll record found for employee number: {employee_num} in '
            f'{week}, returning to main menu.\n')
    else:
        print(display_employee_data)
    time.sleep(3)
     

def get_employerssummary_option():
    """
    Displays Employers amounts to pay out
    summarising data reference from
    https://stackoverflow.com/questions/43745301/converting-column-from-dataframe-to-float-for-sum-usage-python-pandas
    """
    company_payroll_data = df.groupby(
        ['Week Number'])[
                'NET Pay',
                'Employees NI', 'Employees Pension',
                'Company NI', 'Company Pension'
                ].agg(lambda x: sum(x.astype(float)))
    print(company_payroll_data)
    time.sleep(3)


def password():
    """
    Prompts user for password
    getpass referenced from
    https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
    """
    while True:
        pass_word = getpass.getpass(
            prompt='Enter password (No characters show when typed): ')
        if pass_word == 'admin':
            print('Password Correct')
            clear()
            return
        else:
            print('Incorrect password, please try again')


def clear():
    """
    Brings the function called text to the top of the terminal
    code is referenced from https://www.geeksforgeeks.org/clear-screen-python/
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    """
    Run all program functions
    """
    password()
    get_main_menu_option()


print("Welcome to Payroll application")

main()