"""
Main File run.py, for payroll applicaiton by Chris Carabine

This is the main file for a command line interface payroll system for
staff to process employees hours for payroll.

The data is pushed to and read from google sheet, stored on google drive
"""

import sys
import getpass
import termios
import os
from datetime import date
from os import system, name, path
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from menu import main_menu, display_payroll_menu, process_amend_payroll_menu, \
    add_amend_employee_menu, welcome_menu, employees_pay_menu, \
    employers_payment_summary_menu
if path.exists("env.py"):
    import env  # pylint: disable=unused-import  # noqa #
    # This is used to get the username and password

# Pylint states the string below is pointless so have bypassed the message.
# pylint: disable=pointless-string-statement
"""
Imports for all modules for application to function fully:

Getpass: getpass has been used to Prompt the user for a username and password
without showing the characters.

gspread:  gspread has been used to access, update and manipulate data from
Google Sheets

Pandas:  Pandas has been used to allow for the creation of Dataframes,
importing data  and displaying data

sys: sys has been used in wait_key function

termios: The termios module has been used to provide an interface the terminal
control and facilities used in wait_key function

google.oauth2.service_account: google.oauth2.service_account has been used to
allow the application to access the account that the sheet is on with the
credentials

datetime: datetime has been used to get the current week of the year

os: The OS module has ben used to provides functions for interacting with the
operating system. Used for the clear function and to access the environment
varaibles

system : System provides functions for interacting with the operating system,
used in the clear function

name: name has been used in the clear function. os module provides the
operating system interface from Python

menu:  Import the functions listed from the menu file
"""

# SCOPES, CREDS, SCOPED_CREDS  used with Google API Client
# to gain access to and modify data on Google Sheets.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)


# Constant variables
HOL_PC = 0.1208
EMPLOYEES_NI_PC = 0.12
EMPLOYEES_NI_AMOUNT = 184

EMPLOYERS_PENSION_PC = 0.03
EMPLOYERS_NI_PC = 0.138
EMPLOYERS_NI_AMOUNT = 170


def get_data_from_api():
    """
    try: GSPREAD_CLIENT,SHEET used with Google API Client to gain access
    to and modify data on Google Sheets.
    except: If the API fails, print error message and go to the main menu

    @return employeedetail, employeepayroll, SHEET (Turple):
    Worksheet 'employeedetail', 'employeepayroll' and
    Spreadsheet 'companypayroll'
    @raises gspread.exceptions.APIError: Api error
    @return

    """

    try:
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('companypayroll')
        employeedetail = SHEET.worksheet('employeedetail')
        employeepayroll = SHEET.worksheet('employeepayroll')
        return(employeedetail, employeepayroll, SHEET)
    except gspread.exceptions.APIError as error:
        api_error("return to the main menu", error)
        clear()
        get_main_menu_option()
        return()


def api_error(next_step, error):
    """
    Print error message when a api error occurs and wait for
    user to press any key to continue
    @param next_step(String): go to menu
    @param error(String): Error message
    """
    print(f' Error Message {error}\n')
    print('Api error occurred for gspread due to authentication\n')
    print(f'Press any key to {next_step}')
    wait_key()


def get_df():
    """
    try: Gets the data from employeepayroll in to a pandas data frame
    except NameError: when api fails
    except indexError: when api fails, dataframe is empty
    @return: dataframe
    @raises NameError: when api fails
    @return
    @raises indexError: when api fails, dataframe is empty
    @return
    """
    try:
        employeepayroll = get_data_from_api()
        data = employeepayroll[1].get_all_values()
        headers = data.pop(0)
        dataframe = pd.DataFrame(data, columns=headers)
        return dataframe
    except NameError:
        clear()
        get_main_menu_option()
        return()
    except IndexError:
        clear()
        get_main_menu_option()
        return()


def get_payroll_week():
    """
    try: Get payroll week from user and validate
    except: When input is incorrect
    @return: payroll_week(str): payroll week
    @raises KeyError: if value is in correct
    @return: payroll_week(boolean): False
    """
    try:
        while True:
            payroll_week = input("Enter payroll week (numeral) : \n")
            if validate_data_int(payroll_week, 1, 52):
                if int(payroll_week):
                    payroll_week = "wk" + payroll_week
                    return payroll_week
    except KeyError as error:
        print('Invalid week number, please try again.\n')
        print(f'Error message, {error}')
        return False


def payroll_weeks() -> tuple:
    """
    To get the payroll week we first gets current tax week we are in now
    and minus 13 weeks so the payroll week starts from april.
    To get the previous payroll week which we are processing the hours for,
    we minus 1 week
    @return payroll_week (turple): payroll week to process and
    current payroll week
    isocalender code reference from
    http://week-number.net/programming/week-number-in-python.html
    """
    tax_week_number = date.today().isocalendar()[1]
    current_payroll_week_number = tax_week_number - 13
    last_week_payroll_week_number = current_payroll_week_number - 1
    return (last_week_payroll_week_number, current_payroll_week_number)


def payroll_week_for_processing() -> str:
    """
    Get the previous payroll week and return the value
    @return payroll_week(str): week to process employees hours
    """
    payroll_week = payroll_weeks()
    payroll_week = payroll_week[0]
    payroll_week = "wk" + str(payroll_week)
    return payroll_week


def payroll_week_current() -> str:
    """
    Get the current payroll week and return the value
    @return payroll_week(str): current payroll week
    """
    payroll_week = payroll_weeks()
    payroll_week = payroll_week[1]
    payroll_week = "wk" + str(payroll_week)
    return payroll_week


def get_employee_num() -> str:
    """
    Get employee number from user,validate to check that the employee
    is in the employee details list and retrieve details
    @return: employee_num(str):Employee number given by user
    """
    while True:
        employee_num = input("Enter employee number : \n")
        if len(employee_num) == 6:
            print("Finding employment record")
            if validate_employee_num(employee_num):
                print("Employment record located")
                return employee_num
        else:
            print("Employee number format incorrect, try this format 100010 ")


def get_employee_hours() -> float:
    """
    try:
    Get employees hours for week from user ( maximum 100 hours) and validate
    except: when input is incorrect and request the user to re-enter hours
    @return: employee_hours(float):Employee hours given by user
    @raises: ValueError: when input is incorrect
    @return: employee_hours(float):Employee hours given by user
    """
    try:
        while True:
            employee_hours = input("Enter number of hours worked : \n")
            employee_hours = float(employee_hours)
            if validate_data_float(employee_hours, 1, 100):
                return employee_hours
    except ValueError as error:
        print(f'Error message, {error}')
        print('Invalid data, please try again.\n')
        employee_hours = get_employee_hours()
        return employee_hours


def check_for_records_in_payroll_sheet(payroll_week, employee_num):
    """
    Try:    Checks to see if there is a record for the week and
            employee number in spreadsheet.
            If there is it will return the row to delete
    except IndexError: if there isn't a value in the sheet
            then returns to the menu
    except NameError: when api fails
    @param payroll_week(string): Payroll week
    @param employee_num(string): Employee number
    @return matched_row(int): Row to delete in spreadsheet
    @raises indexError: if no record is found
    @return : 0
    @raises NameError: when api fails
    @return : 0
    intersect part of code referenced to
    https://learncodingfast.com/how-to-find-intersection-of-two-lists-in-python/
    """
    try:
        employeepayroll = get_data_from_api()
        employee_num_found = employeepayroll[1].findall(employee_num)
        week_found = employeepayroll[1].findall(payroll_week)
        employee = []
        for i in employee_num_found:
            employee.append(i.row)
        week = []
        for i in week_found:
            week.append(i.row)
        set1 = set(employee)
        set2 = set(week)
        intersect = list(set1 & set2)
        matched_row = int(intersect[0])
        if matched_row >= 1:
            return matched_row
        return 0
    except IndexError:
        print(
            'No entry found in payroll'
            )
        return 0
    except NameError as error:
        api_error("return to the main menu", error)
        get_main_menu_option()
        return 0


# Menu options functionality
def get_main_menu_option():
    """
    Display menu
    Get Main menu option input from user
    Run function related to input
    """
    main_menu()
    while True:
        main_menu_option_data = input(
                'Please enter number option from the menu : \n'
                )
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
                sys.exit()


def get_display_payroll_option():
    """
    Display menu
    Get display payroll option input from user
    Run function related to input
    """
    display_payroll_menu()
    while True:
        display_payroll_option_data = input(
            'Please enter number option from the menu : \n'
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
    process_amend_payroll_menu()
    while True:
        process_payroll_option_data = input(
            'Please enter number option from the menu : \n'
            )
        if validate_data_int(process_payroll_option_data, 1, 3):
            if process_payroll_option_data == "1":
                process_payroll_option_1()
            if process_payroll_option_data == "2":
                process_payroll_option_2()
            if process_payroll_option_data == "3":
                clear()
                get_main_menu_option()


# Display menu functionality
def display_all_employeepay_for_week():
    """
    try:
        Request user to input payroll week,display data for week
    except AttributeError: when api fails
    except IndexError: when api fails
    @raises AttributeError: Api error
    @raises IndexError: Api error
    groupby referenced from
    https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
    """
    try:
        dataframe = get_df()
        week = get_payroll_week()
        display_employee_data = dataframe.loc[
            (dataframe['Week Number'] == (week)), [
                        'Employee Number', 'Basic Pay', 'Hol Pay',
                        'EE NI', 'EE Pension', 'NET Pay'
                        ]]
        if display_employee_data.empty:
            print('Invalid week number, please try again.\n')
            print(
                '\nPress any key to clear the screen and return to the '
                'display payroll menu'
                )
            wait_key()
            clear()
            get_display_payroll_option()
        else:
            employees_pay_menu()
            print(display_employee_data)
            print(
                '\nPress any key to clear the screen and return to the '
                'display payroll menu'
                )
            wait_key()
            clear()
            get_display_payroll_option()
    except IndexError:
        clear()
        get_main_menu_option()
    except AttributeError:
        clear()
        get_main_menu_option()


def display_ind_employee_pay_for_week():
    """
    try:
        Request user to input payroll week,display data for week
    except AttributeError: when api fails
    except IndexError: when api fails
    @raises AttributeError: Api error
    @raises IndexError: Api error
    """
    try:
        dataframe = get_df()
        week = get_payroll_week()
        employee_num = get_employee_num()
        display_employee_data = dataframe.loc[
            (dataframe['Week Number'] == (week)) & (
                dataframe['Employee Number'] == (employee_num)), [
                        'Surname', 'Basic Pay', 'Hol Pay',
                        'EE NI', 'EE Pension', 'NET Pay'
                        ]]
        if display_employee_data.empty:
            print(
                f'\nNo payroll record found for employee number: '
                f'{employee_num} in {week}.\n')
            print(
                'Press any key to clear the screen and return to the'
                ' display payroll menu')
            wait_key()
            clear()
            get_display_payroll_option()
        else:
            print('--------------------------------------------------------'
                  '-----')
            print('---------------- People Payroll Application ------------'
                  '-----')
            print(
                f'---------------------- Employee {employee_num} -----------'
                '-----------'
                )
            print(
                '----------------------------------------------------------'
                '---\n'
                )
            print(display_employee_data)
            print(
                '\nPress any key to clear the screen and return to the'
                ' display payroll menu')
            wait_key()
            clear()
            get_display_payroll_option()
    except IndexError:
        clear()
        get_main_menu_option()
    except AttributeError:
        clear()
        get_main_menu_option()


def get_employerssummary_option():
    """
    try:
        Displays Employers amounts to pay out
    except AttributeError: when api fails
    except IndexError: when api fails
    @raises AttributeError: Api error
    @raises IndexError: Api error
    summarising data reference from
    https://stackoverflow.com/questions/43745301/converting-column-from- /
    dataframe-to-float-for-sum-usage-python-pandas
    """
    try:
        dataframe = get_df()
        company_payroll_data = dataframe.groupby(
            ['Week Number'])[[
                    'NET Pay',
                    'EE NI', 'EE Pension',
                    'Er NI', 'Er Pension'
                    ]].agg(lambda x: sum(x.astype(float)))
        employers_payment_summary_menu()
        print(company_payroll_data)
        print(
            '\nPress any key to clear the screen and return to the display'
            ' payroll menu'
            )
        wait_key()
        clear()
        get_display_payroll_option()
    except IndexError:
        clear()
        get_main_menu_option()
    except AttributeError:
        clear()
        get_main_menu_option()


# Add / amend payroll functionality
def process_payroll_option_1():
    """
    Process payroll option 1 - run functions below to add employees hours
    """
    payroll_week = payroll_week_for_processing()
    print(f'\nPayroll week for processing is {payroll_week}\n')
    employee_num = get_employee_num()
    row_num = check_for_records_in_payroll_sheet(payroll_week, employee_num)
    if row_num == 0:
        calculate_employee_payslip_data(payroll_week, employee_num)
        next_employee_to_process()
    else:
        row_num = int(row_num)
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


def next_employee_to_process():
    """
    Requests user input if they would like to process another employees hours
    """
    while True:
        answer = yesorno(
            'Would you like to process another '
            'employees hours? type y or n :  '
                )
        if answer is True:
            process_payroll_option_1()
        elif answer is False:
            clear()
            get_main_menu_option()
        print("Try again")


def calculate_employee_payslip_data(payroll_week, employee_num):
    """
    try:
        Get Employees details from spreadsheet,
        calculate values and updates worksheet
    except: when api fails
    @param payroll_week(str): payroll week
    @param employee_num : Employee number
    @raises NameError: Api error
    """
    try:
        employee_row = validate_employee_num(employee_num)
        employee_dict = get_employee_data(employee_row)
        employee_hours = get_employee_hours()
        employee_basic_pay = round(
            float(employee_hours) * float(employee_dict[
                "employee_rate_of_pay"].value), 2)
        employee_holiday = round(employee_basic_pay * HOL_PC, 2)
        if (employee_basic_pay + employee_holiday) < EMPLOYEES_NI_AMOUNT:
            employee_ni = 0
        else:
            employee_ni = round(
                ((employee_basic_pay + employee_holiday) -
                    EMPLOYEES_NI_AMOUNT) * EMPLOYEES_NI_PC, 2)
        employee_pension = round(
            float(employee_dict[
                    "employee_pension"].value) * (employee_basic_pay +
                                                  employee_holiday), 2)
        employee_net_pay = round(
            (employee_basic_pay + employee_holiday) - employee_ni -
            employee_pension, 2)
        if (employee_basic_pay + employee_holiday) < EMPLOYERS_NI_AMOUNT:
            employers_ni = 0
        else:
            employers_ni = round(
                ((employee_basic_pay + employee_holiday) -
                 EMPLOYERS_NI_AMOUNT) * EMPLOYERS_NI_PC, 2)
        employers_pension = round((employee_basic_pay + employee_holiday) *
                                  EMPLOYERS_PENSION_PC, 2)
        print(
            f'\n Employee : {employee_num} - '
            f'{employee_dict["employee_firstname"].value} '
            f'{employee_dict["employee_surname"].value}'
            )
        print(f' Basic Pay : £{employee_basic_pay}')
        print(f' Holiday Pay : £{employee_holiday}')
        print(f' NI contribution: £{employee_ni}')
        print(f' Pension contribution: £{employee_pension}')
        print(f' Net Pay: £{employee_net_pay}')
        row_data = []
        answer = yesorno("Are the amounts correct? type y or n ")
        if answer:
            print("\nReady to upload into payroll spreadsheet \n")
            row_data = [
                    payroll_week, employee_num,
                    employee_dict[
                        "employee_surname"].value,
                    employee_dict[
                        "employee_firstname"].value,
                    employee_hours, employee_basic_pay,
                    employee_holiday, employee_ni,
                    employee_pension, employee_net_pay,
                    employers_ni, employers_pension
            ]
            update_worksheet(row_data, "employeepayroll")
        if answer is False:
            print("Re-enter details \n")
            calculate_employee_payslip_data(
                payroll_week, employee_num)
    except NameError as error:
        api_error("return to the main menu", error)
        get_main_menu_option()


def get_employee_data(employee_row):
    """
    try:
        Gets the values from employee detail Google Sheets and returns values
    except: When the api fails
    @param employee_row(string): Employee row in google sheets
    @return: employee_dic(dict) : Employee number, surname, first name,
        rate of pay and pension
    @raises NameError: Api error
    @raises AttributeError: Api error
    """
    try:
        employeedetail = get_data_from_api()
        employee_num = employeedetail[0].cell(employee_row, 1)
        employee_surname = employeedetail[0].cell(employee_row, 2)
        employee_firstname = employeedetail[0].cell(employee_row, 3)
        employee_rate_of_pay = employeedetail[0].cell(employee_row, 4)
        employee_pension = employeedetail[0].cell(employee_row, 5)
        employee_dic = {
            "employee_num": employee_num,
            "employee_surname": employee_surname,
            "employee_firstname": employee_firstname,
            "employee_rate_of_pay": employee_rate_of_pay,
            "employee_pension": employee_pension
            }
        return employee_dic
    except NameError:
        clear()
        get_main_menu_option()
        return employee_row
    except AttributeError:
        clear()
        get_main_menu_option()
        return employee_row


def process_payroll_option_2():
    """
    Process payroll option 2 -run functions below to amend employees hours
    payrolls_weeks is the previous week
    """
    payroll_week = payroll_week_for_processing()
    print(f'\nPayroll week for processing is {payroll_week}\n')
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

    @raises indexError: if no record is found
    @raises gspread.exceptions.APIError: Api error

    """
    try:
        row_to_delete = check_for_records_in_payroll_sheet(
            payroll_week, employee_num)
        if row_to_delete == 0:
            raise IndexError()
        employeepayroll = get_data_from_api()
        employeepayroll[1].delete_rows(row_to_delete)
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
    except NameError as error:
        api_error("return to the main menu", error)
        get_main_menu_option()


# Add / amend employee functionality
def get_add_amend_employee_option():
    """
    Get add / amend employee option input from user
    Run function related to input
    Future feature
    """
    while True:
        add_amend_employee_menu()
        print(
            '\nPress any key to clear the screen and return'
            ' to the Main menu'
            )
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
    @return validate_data_int: True
    @raises ValueError: raises an exception
    @return ValueError : False
    """
    try:
        if int(value) < minvalue or int(value) > maxvalue:
            raise ValueError(
                f'Number between {minvalue} and {maxvalue} required,'
                f' you typed {value}'
                )
    except ValueError as error:
        print(f'Error message, {error}')
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
    @raises ValueError: raises an exception, if the value is incorrect
    """
    try:
        if float(value) < minvalue or float(value) > maxvalue:
            raise ValueError(
                f'Number between {minvalue} and {maxvalue} '
                f'required, you typed {value}'
                )
    except ValueError as error:
        print(f'Error message, {error}')
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
    @return employee_row(int): Employee row in sheet
    @raise AttributeError: raises an exception if the employee
    number is incorrect
    @return
    @raises NameError: API error
    @return

    """
    try:
        employeedetail = get_data_from_api()
        employee_row = employeedetail[0].find(employee_num).row
        return employee_row
    except AttributeError as error:
        print(f'Error message, {error}')
        print('\nInvalid employee number, please try again.\n')
        answer = yesorno("Do you want to try again? type y or n :  ")
        if answer:
            return ()
        clear()
        get_main_menu_option()
        return ()
    except NameError as error:
        api_error("return to the main menu", error)
        return ()


# General functions
def update_worksheet(data_1, worksheet):
    """
    Receives a list to be inserted into a worksheet
    Update the relevant worksheet with the data provided

    @param data(string): list of values to upload
    @param worksheet(string): google sheet name

    Code reference from code institute love sandwiches project

    """
    SHEET = get_data_from_api()
    worksheet_to_update = SHEET[2].worksheet(worksheet)
    worksheet_to_update.append_row(data_1)
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
    referenced from slack post  - How to set up environment variables \
    anna_ci Dec 19th, 2019 at 8:25 AM
    """
    payroll_week = payroll_week_current()
    print(f'       Current Payroll week is {payroll_week}\n')
    print("Login (Characters will not be visible on screen when typed)")
    while True:
        username = os.environ.get('username')
        password_1 = os.environ.get('password')
        username_input = getpass.getpass(
                prompt='\nPlease enter your username: \n')
        password_input = getpass.getpass(
                prompt='\nPlease enter your password: \n')
        if username_input == username and password_input == password_1:
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


def yesorno(question) -> bool:
    """
    Function to take user input yes or no
    validate input
    @param question(string): Question
    Code used from https://gist.github.com/garrettdreyfus/8153571
    @return yesorno(string)
     """
    answer = str(input(f'{question}\n')).lower()
    if answer == 'y':  # pylint: disable=no-else-return
        return True
    elif answer == 'n':
        return False
    print('Invalid entry')
    return yesorno(question)


def wait_key():
    """
    Wait for a key press on the console
    referenced from https://stackoverflow.com/questions/983354/ \
    how-to-make-a-script-wait-for-a-pressed-key
    """
    try:
        fd_int = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd_int)
        newattr = termios.tcgetattr(fd_int)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd_int, termios.TCSANOW, newattr)
        sys.stdin.read(1)
    except IOError as error:
        print(f'Error message, {error}')
    finally:
        termios.tcsetattr(fd_int, termios.TCSAFLUSH, oldterm)


def main():
    """
    Run all program functions
    """
    clear()
    welcome_menu()
    password()
    get_main_menu_option()


main()
