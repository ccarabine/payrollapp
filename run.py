import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
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

PAYROLL_WEEK = 34

def get_payroll_week():
    """
    Get payroll week from user and validate
  
    """
    while True:
        input_payroll_week=input("Enter Payroll Week (1-52) : ")
       
        if validate_data(input_payroll_week,1,52):
            return(input_payroll_week)

def get_employee_num():
    """
    Get employee number from user and validate to check that the employee is in the employee details list
    """ 
    while True:
        input_employee_num = input("Enter Employee number e.g. 100014  : ")
        if validate_employee_num(input_employee_num):
            return(input_employee_num)
            ri=validate_employee_num
            print(ri)
        
      
def get_employee_hours():
    """
    Get employees hours for week from user ( maximum 15 hours) and validate
    """
    while True:
        input_employee_hours=input("Enter number of hours worked : ")
        if validate_data(input_employee_hours,1,15):
            return(input_employee_hours)




def get_payroll_data():
    """
    Get payroll week, employee's payroll, number, number of hour from user and rate of pay from spreadsheet
    """
    employee_entered_payroll_week = get_payroll_week()
    employee_num=get_employee_num()
    employee_rate_of_pay = validate_employee_num(employee_num)
    employee_hours = get_employee_hours()
    return (employee_entered_payroll_week,employee_num,employee_rate_of_pay,employee_hours)
   
 
"""

def search():
    employee_num=input("Employee num")
    search_value = employeedetail.findall(employee_num )
    print(search_value)
"""

def get_main_menu_option():
    """
    Get Main menu option input from user
    Run function related to input
    """
    while True:
        print("-------------- Main Menu -------------- ")
        print("1 Display payroll")
        print("2 Process / Amend payroll")
        print("3 Run payroll")
        print("4 Add / Amend employee details\n")
        print("Example:  1\n")

        main_menu_option_data = input("Please enter number option from the menu : ")
        if validate_data(main_menu_option_data,1,4):
            if main_menu_option_data == "1":
                get_display_payroll_option()
            if main_menu_option_data == "2":
                get_process_payroll_option()
            if main_menu_option_data == "3":
                get_run_payroll_option()
            if main_menu_option_data == "4":
                get_add_amend_employee_option()
                

def get_display_payroll_option():
    """
    Get display payroll option input from user
    Run function related to input
    """
    while True:
        print("-------------- Display Payroll -------------- ")
        print("1 All employees pay for week")
        print("2 Employee pay for week")
        print("3 Employers summary for week")
        print("4 Main menu\n")
        print("Example:  1\n")
        display_payroll_option_data = input("Please enter number option from the menu : ")
        if validate_data(display_payroll_option_data,1,4):
            if display_payroll_option_data == "1":
                get_allemployeepay_option()
            if display_payroll_option_data == "2":
                get_employeepay_option()
            if display_payroll_option_data == "3":
                get_employerssummaryay_option()
            if display_payroll_option_data == "4":
                get_main_menu_option()


def get_process_payroll_option():
    """
    Get process / Amend payroll option input from user
    Run function related to input
    """
    while True:
        print("-------------- Process / Amend Payroll -------------- ")
        print("1 Add Employees hours")
        print("2 Amend employees hours")
        print("3 Main menu\n")
        
        print("Example:  1\n")

        process_payroll_option_data = input("Please enter number option from the menu : ")
    
        if validate_data(process_payroll_option_data,1,3):
            print("Data is valid")
            break
        return process_payroll_option_data


def get_add_amend_employee_option():
    """
    Get add / amend employee option input from user
    Run function related to input

    Future feature
    """
    while True:
        print("\n Feature in next update, returning to main menu \n")
        get_main_menu_option()
        
       
def validate_data(value,minvalue,maxvalue):
    """
    Inside the try, converts value to integer
    raise ValueError if strings cannot be converted into int or less than 1 or greater than 4
    """
    try:
       
        if int(value) < minvalue or int(value) > maxvalue:
            raise ValueError(
               f"Number between {minvalue} and {maxvalue} required, you typed {value}"
        )
    except ValueError as e:
        print(f"Invalid data, please try again.\n")
        return False

    return True


def validate_employee_num(num):
    """
    Inside the try, converts value to integer
    raise ValueError if strings cannot be converted into int or less than 1 or greater than 4
    """
    try:
        employee_row = employeedetail.find(num).row 
        #print(employee_row)
        values_list = employeedetail.row_values(employee_row)
       # print(values_list)
        values_list = employeedetail.row_values(employee_row)
        employee_rateofpay =employeedetail.cell(employee_row,4)
        #print(employee_rateofpay.value)
        return employee_rateofpay.value
    except AttributeError as e:
        print(f"\nInvalid employee number, please try again.\n")
        decision = input('Do you want to try again? type y or n : ')
        if decision =="y":
            get_employee_num()
        elif decision == "n":
            main_menu_option = get_main_menu_option()
        return False
        
        

    return True
def main():
    """
    Run all program functions
    """
"""main_menu_option = get_main_menu_option()"""
#process_payroll=process_payroll()
get_payroll_data=get_payroll_data()
#get_employee_num=get_employee_num()
    
print("Welcome to Payroll application")
main()
