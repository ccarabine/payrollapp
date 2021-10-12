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
import termios
from google.oauth2.service_account import Credentials
from datetime import date
from os import system, name, path
import os
if path.exists("env.py"):
    import env
from menu import main_menu, display_payroll_menu, process_amend_payroll_menu, \
    add_amend_employee_menu, welcome_menu, employees_pay_menu, \
    employers_payment_summary_menu


"""
Imports for all modules for application to function fully:

Getpass: Prompt the user for a username and password without echoing.

gspread:  A Python API for Google Sheets. Read, write, and format cell ranges.

Pandas:  allows importing data displaying data

sys: System-specific parameters and functions module used in wait_key function

termios: The termios module provides an interface the terminal control \
    facilities used in wait_key function

google.oauth2.service_account: So the application can access the account that
the sheet is on with the credentials

datetime: to get the current week of the year

os: The OS module in Python provides functions for interacting with the
operating system. Used for the clear function and to access the environment
varaibles

menu:  Import the functions listed from the menu file

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


class Employee():
    def __init__(
        self, employee_num, employee_surname, employee_firstname,
            employee_rate_of_pay, employee_pension_pc):
        self.employee_num = employee_num
        self.employee_surname = employee_surname
        self.employee_firstname = employee_firstname
        self.employee_rate_of_pay = employee_rate_of_pay
        self.employee_pension_pc = employee_pension_pc

    def validate_employee_num(self, employee_num):
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
            print(answer)
        #  if answer:
        #      get_employee_num(self)
        # else:
        #      return False

    def get_employee_num(self):
        """
        Get employee number from user,validate to check that the employee
        is in the employee details list and retrieve details
        @returns: employee_num(str):Employee number given by user
        """
        while True:
            employee_num = input("Enter employee number : \n")
            print("Finding employment record")
            if self.validate_employee_num(employee_num):
                print("Employment record located")
                return(employee_num)
            else:
                clear()
                menu = Menu
                menu.main_menu
                
    def calculate_employee_payslip_data(self, payroll_week, employee_num):
        """
        Get Employees details from spreadsheet,
        calculate values and updates worksheet
        @param payroll_week(str): payroll week
        @param employee_num : Employee number
        """
        payroll = Payroll
        employee_row = self.validate_employee_num(employee_num)
        employee_retrived_data = payroll.get_employee_data(self, employee_row)
        self.employee_num = (employee_retrived_data[0])
        self.employee_surname = (employee_retrived_data[1])
        self.employee_firstname = (employee_retrived_data[2])
        self.employee_rate_of_pay = float(employee_retrived_data[3])
        self.employee_pension = float(employee_retrived_data[4])

        self.employee_hours_data = (payroll.get_employee_hours(self))
        self.employee_hours = float(self.employee_hours_data)
        self.employee_basic_pay = round(
            self.employee_hours * self.employee_rate_of_pay, 2)
        self.employee_holiday = round(self.employee_basic_pay * HOL_PC, 2)
        self.employee_basic_hol = (
            self.employee_basic_pay + self.employee_holiday)
        if (
            self.employee_basic_pay + self.employee_holiday
                ) < EMPLOYEES_NI_AMOUNT:
            self.employee_ni = 0
        else:
            self.employee_ni = round(
                ((self.employee_basic_hol) - EMPLOYEES_NI_AMOUNT) *
                EMPLOYEES_NI_PC, 2)
        self.employee_pension = round(
            self.employee_pension * self.employee_basic_hol, 2)
        self.employee_net_pay = round(
            self.employee_basic_hol - self.employee_ni - self.employee_pension,
            2)
        if (
            self.employee_basic_pay + self.employee_holiday
                ) < EMPLOYERS_NI_AMOUNT:
            self.employers_ni = 0
        else:
            self.employers_ni = round(
                (self.employee_basic_hol - EMPLOYERS_NI_AMOUNT)
                * EMPLOYERS_NI_PC, 2)
        self.employers_pension = round(
            self.employee_basic_hol * EMPLOYERS_PENSION_PC, 2)
        print(
            f'\n Employee : {self.employee_num} - '
            f'{self.employee_firstname} {self.employee_surname}'
            )
        print(f' Basic Pay : £{self.employee_basic_pay}')
        print(f' Holiday Pay : £{self.employee_holiday}')
        print(f' NI contribution: £{self.employee_ni}')
        print(f' Pension contribution: £{self.employee_pension}')
        print(f' Net Pay: £{self.employee_net_pay}')
        if yesorno("Are the amounts correct? type y or n "):
            print("\nReady to upload into payroll spreadsheet \n")
            row_data = [
                    payroll_week, self.employee_num,
                    self.employee_surname, self.employee_firstname,
                    self.employee_hours, self.employee_basic_pay,
                    self.employee_holiday, self.employee_ni,
                    self.employee_pension, self.employee_net_pay,
                    self.employers_ni, self.employers_pension
            ]
            update_worksheet(row_data, "employeepayroll")
            return ()
        else:
            print("Re enter details \n")
            payroll.calculate_employee_payslip_data(
                self, payroll_week, employee_num
                )

    def get_employee_data(self, employee_row):
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
        self.employee_surname = employeedetail.cell(employee_row, 2)
        self.employee_firstname = employeedetail.cell(employee_row, 3)
        self.employee_rateofpay = employeedetail.cell(employee_row, 4)
        self.employee_pension = employeedetail.cell(employee_row, 5)
        return employee_num.value,\
            self.employee_surname.value,\
            self.employee_firstname.value,\
            self.employee_rateofpay.value,\
            self.employee_pension.value


class Payroll(Employee):
    def __init__(
                self, payroll_week, employee_num, employee_surname,
            employee_firstname, employee_hours, employee_basic_pay,
            employee_holiday, employee_ni, employee_pension,
            employee_net_pay, employers_ni, employers_pension
            ):
        self.payroll_week = payroll_week
        self.employee_hours = employee_hours
        self.employee_basic_pay = employee_basic_pay
        self.employee_holiday = employee_holiday
        self.employee_ni = employee_ni
        self.employee_pension = employee_pension
        self.employee_net_pay = employee_net_pay
        self.employers_ni = employers_ni
        self.employers_pension = employers_pension

        Employee.__init__(
            self, employee_num, employee_surname, employee_firstname,
            employee_rate_of_pay, employee_pension_pc
            )

    def get_payroll_week(self):
        """
        Get payroll week from user and validate
        @returns: payroll_week(str)

        """
        try:
            while True:
                self.payroll_week = input("Enter payroll week (numeral) : \n")
                if validate_data_int(self.payroll_week, 1, 52):
                    if int(self.payroll_week):
                        self.payroll_week = "wk" + self.payroll_week
                        return(self.payroll_week)
        except KeyError:
            print('Invalid week number, please try again.\n')
            return False

    def get_employee_hours(self):
        """
        Get employees hours for week from user ( maximum 100 hours)
        and validate
        @returns: employee_hours(float):Employee hours given by user
        """
        while True:
            self.employee_hours = input("Enter number of hours worked : \n")
            if validate_data_float(self.employee_hours, 1, 100):
                return(self.employee_hours)

    def check_for_records_in_payroll_sheet(self, payroll_week, employee_num):
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

# Display menu functionality
    def display_all_employeepay_for_week(self):
        """
        Request user to input payroll week,display data for week
        groupby referenced from
        https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
        """
        try:
            payroll = Payroll
            menu = Menu
            week = payroll.get_payroll_week(self)
            data_by_week = df.groupby('Week Number')
            filtered_data_by_week = data_by_week.get_group(week)
            employees_pay_menu()
            print(filtered_data_by_week)
            print(
                '\nPress any key to clear the screen and return to '
                'the display payroll menu'
                )
            wait_key()
            clear()
            menu = Menu
            menu.get_display_payroll_option(self)
        except KeyError:
            print('Invalid week number, please try again.\n')
            print(
                '\nPress any key to clear the screen and return '
                'to the display payroll menu'
                )
            wait_key()
            clear()
            menu.get_display_payroll_option(self)

    def display_ind_employee_pay_for_week(self):
        """
        Request user to enter payroll week and employee number,
        validation to ensure there is a record displays employee pay record
        """
        payroll = Payroll
        employee = Employee
        payroll_week = payroll.get_payroll_week(self)
        employee_num = employee.get_employee_num(self)
        display_employee_data = df.loc[
            (df['Week Number'] == (payroll_week)) & (
                df['Employee Number'] == (employee_num)), [
                        'Week Number', 'Employee Number',
                        'First Name', 'Surname', 'Basic Pay', 'Holiday Pay',
                        'Employees NI', 'Employees Pension', 'NET Pay'
                        ]]
        if display_employee_data.empty:
            print(
                f'\nNo payroll record found for employee number: '
                f'{self.employee_num} in {self.payroll_week}.\n')
            print(
                'Press any key to clear the screen and return to the'
                ' display payroll menu')
            wait_key()
            clear()
            display = Menu()
            display.get_display_payroll_option()
        else:
            print(
                "-------------------------------------------------------------"
                )
            print(
                "---------------- People Payroll Application -----------------"
                )
            print(
                f'---------------------- Employee {employee_num} -------------'
                '---------'
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
            display.get_display_payroll_option()

    def get_employerssummary_option(self):
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
                    'Employers NI', 'Employers Pension'
                    ]].agg(lambda x: sum(x.astype(float)))
        employers_payment_summary_menu()
        print(company_payroll_data)
        print(
            '\nPress any key to clear the screen and return to the display'
            ' payroll menu'
            )
        wait_key()
        clear()
        display = Menu()
        display.get_display_payroll_option()

    # Add / amend payroll functionality
    def process_payroll_option_1(self):
        """
        Process payroll option 1 -run functions below to add employees hours
        """
        employee = Employee
        payroll = Payroll
        menu = Menu
        payroll_week = payroll_week_for_processing()
        print(f'\nPayroll week for processing is {payroll_week}\n')
        employee_num = employee.get_employee_num(self)
        row_num = payroll.check_for_records_in_payroll_sheet(
            self, payroll_week, employee_num)
        row_num = int(row_num)
        if row_num >= 1:
            print(
                f'Employees hours already entered in {payroll_week}'
                f', please go to option 2 to amend \n')
            print(
                '\nPress any key to clear the screen and return to the '
                'Process amend payroll menu'
                )
            wait_key()
            clear()
            menu.get_process_payroll_option(self)
        else:
            calculate_employee_payslip_data(
                self, payroll_week, employee_num)
            next_employee_to_process(self)

    def next_employee_to_process(self):
        """
        Requests user input if they would like to process
        another employees hours
        """
        while True:
            payroll = Payroll
            if yesorno(
                'Would you like to process another '
                'employees hours? type y or n :  '
                    ):
                payroll.process_payroll_option_1(self)
                return()
            else:
                clear()
                menu = Menu
                menu.main_menu(self)

    def process_payroll_option_2(self):
        """
        Process payroll option 2 -run functions below to amend employees hours
        payrolls_weeks is the previous week
        """
        employee = Employee
        payroll = Payroll
        payroll_week = payroll_week_for_processing()
        print(f'\nPayroll week for processing is {payroll_week}\n')
        employee_num = employee.get_employee_num(self)
        payroll.amend_employees_hours(self, payroll_week, employee_num)

    def amend_employees_hours(self, payroll_week, employee_num):
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
            payroll = Payroll
            menu = Menu
            row_to_delete = payroll.check_for_records_in_payroll_sheet(
                self, payroll_week, employee_num)
            if (row_to_delete == 0):
                raise IndexError()
            employeepayroll.delete_rows(row_to_delete)
            payroll.calculate_employee_payslip_data(
                self, payroll_week, employee_num,)
            print(
                '\nPress any key to clear the screen and return to the'
                ' Process / amend payroll menu')
            wait_key()
            clear()
            menu.get_process_payroll_option(self)
        except IndexError:
            payroll = Payroll
            print(
                f'\nNo payroll record found for {employee_num} in week'
                f' {payroll_week}, returning to main menu.\n')
            print(
                '\nPress enter to clear the screen and return to the Process '
                '/ amend payroll menu'
                )
            wait_key()
            clear()
            menu = Menu
            menu.get_process_payroll_option(self)


# Menu options functionality
class Menu:
    def __init__(self):
        self.main_choices = {
            "1": self.get_display_payroll_option,
            "2": self.get_process_payroll_option,
            "3": self.get_add_amend_employee_option,
            "4": self.quit
        }
        payroll = Payroll
        self.display_choices = {
            "1": payroll.display_all_employeepay_for_week,
            "2": payroll.display_ind_employee_pay_for_week,
            "3": payroll.get_employerssummary_option,
            "4": self.main_menu
        }

    def main_menu(self):
        while True:
            clear()
            main_menu()
            choice = input(
                'Please enter number option from the menu : \n'
                )
            if validate_data_int(choice, 1, 4):
                action = self.main_choices.get(choice)
                if action:
                    clear()
                    action()
            else:
                print("{0} is not a valid choice".format(choice))

    def get_display_payroll_option(self):
        """
        Display menu
        Get display payroll option input from user
        Run function related to input
        """
        while True:
            clear()
            display_payroll_menu()
            choice = input(
                'Please enter number option from the menu : \n'
                )
            if validate_data_int(choice, 1, 4):
                action = self.display_choices.get(choice)
                if action:
                    clear()
                    action()
            else:
                print("{0} is not a valid choice".format(choice))

    def get_process_payroll_option(self):
        """
        Display menu
        Get process / Amend payroll option input from user
        Run function related to input
        """
        process_amend_payroll_menu()
        while True:
            payroll = Payroll
            process_payroll_option_data = input(
                'Please enter number option from the menu : \n'
                )
            if validate_data_int(process_payroll_option_data, 1, 3):
                if process_payroll_option_data == "1":
                    payroll.process_payroll_option_1(self)
                elif process_payroll_option_data == "2":
                    payroll.process_payroll_option_2(self)
                elif process_payroll_option_data == "3":
                    clear()
                    menu = Menu
                    main_menu()
                    menu.main_menu

# Add / amend employee functionality
    def get_add_amend_employee_option(self):
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
            self.main_menu()

    def quit(self):
        quit()


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


def payroll_weeks():
    """
    Get current tax week number, minus 13 weeks to start in april for
    payroll week to get the previous payroll week, minus 1 week
    @returns: last_week_payroll_week_number(str): payroll week to process
    @returns: current_payroll_week_number(str): current payrool week
    isocalender code reference from
    http://week-number.net/programming/week-number-in-python.html
    """
    tax_week_number = date.today().isocalendar()[1]
    current_payroll_week_number = tax_week_number - 13
    last_week_payroll_week_number = current_payroll_week_number - 1
    return (last_week_payroll_week_number, current_payroll_week_number)


def payroll_week_for_processing():
    """
    Function get the previous payroll week and return the value
    @return payroll_week(str): week to process employees hours
    """
    payroll_week = payroll_weeks()
    payroll_week = payroll_week[0]
    payroll_week = "wk" + str(payroll_week)
    return(payroll_week)


def payroll_week_current():
    """
    Function get the current payroll week and return the value
    @return payroll_week(str): current payroll week
    """
    payroll_week = payroll_weeks()
    payroll_week = payroll_week[1]
    payroll_week = "wk" + str(payroll_week)
    return(payroll_week)


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
    referenced from slack post  - How to set up environment variables \
    anna_ci Dec 19th, 2019 at 8:25 AM
    """
    payroll_week = payroll_week_current()
    print(f'       Current Payroll week is {payroll_week}\n')
    print("Login (Characters will not be visible on screen when typed)")
    while True:
        username = os.environ.get('username')
        password = os.environ.get('password')
        username_input = getpass.getpass(
                prompt='\nPlease enter your username: \n')
        password_input = getpass.getpass(
                prompt='\nPlease enter your password: \n')
        if username_input == username and password_input == password:
            print("Correct credentials!")
            clear()
            return True
        else:
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
    answer = input(f'{question}\n')
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


def main():
    """
    Run all program functions
    """
    # password()
    display = Menu()
    display.main_menu()


clear()
welcome_menu()
main()
