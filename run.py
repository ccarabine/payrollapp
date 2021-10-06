"""
Main File run.py, for payroll applicaiton by Chris Carabine

This is the main file for a command line interface payroll system for
staff to process employees hours for payroll.

The data is pushed to and read from google sheet, stored on google drive
"""
import gspread
import pandas as pd
import time
from google.oauth2.service_account import Credentials
from menu import main_menu, display_payroll_menu, process_amend_payroll_menu, \
    add_amend_employee_menu
from utility_functions import get_payroll_week, get_employee_num, \
    get_employee_hours, yesorno, update_worksheet, validate_data_int, \
    validate_employee_num, password, clear, check_for_records_in_payroll_sheet

"""
Imports for all modules for application to function fully:

gspread:  A Python API for Google Sheets. Read, write, and format cell ranges.

Pandas:  allows importing data and manipulation operations such as merging,
reshaping, selecting, as well as data cleaning, and data wrangling features.

Time: The sleep() function delays execution of the current thread for the
given number of seconds.

google.oauth2.service_account: So the application can access the account that
the sheet is on with the credentials

menu: importing functions locally from menu.py

utility_functions: importing functions locally from utility_functions.py

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
                clear()
                process_payroll_option_1()
            if process_payroll_option_data == "2":
                clear()
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
            f' in {week}, returning to main menu.\n')
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
        ['Week Number'])[[
                'NET Pay',
                'Employees NI', 'Employees Pension',
                'Company NI', 'Company Pension'
                ]].agg(lambda x: sum(x.astype(float)))
    print(company_payroll_data)
    time.sleep(3)


# Add / amend payroll functionality
def process_payroll_option_1():
    """
    Process payroll option 1 -run functions below to add employees hours
    """
    payroll_week = get_payroll_week("normal")
    employee_num = get_employee_num()
    row_num = check_for_records_in_payroll_sheet(payroll_week, employee_num)
    row_num = int(row_num)
    if row_num >= 1:
        print(
            f'Employees hours already entered in {payroll_week}'
            f', please go to option 2 to amend \n')
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
        print("Ready to upload into payroll spreadsheet")
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
    """
    payroll_week = get_payroll_week("normal")
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
        employeepayroll.delete_rows(row_to_delete)
        calculate_employee_payslip_data(
            payroll_week, employee_num,)
        print('Updated payroll information')
    except IndexError:
        print(
            f'\nNo payroll record found for {employee_num} in week'
            f' {payroll_week}, returning to main menu.\n')
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
        get_main_menu_option()


def main():
    """
    Run all program functions
    """
    password()
    get_main_menu_option()


# clear()
print("Welcome to Payroll application")
main()
