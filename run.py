import gspread
from google.oauth2.service_account import Credentials

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

data = employeedetail.get_all_values()

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
        
        if validate_data(main_menu_option_data):
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
        print("2 employee pay for week")
        print("3 Employers summary for week")
        print("4 Main menu\n")
        
        print("Example:  1\n")

        display_payroll_option_data = input("Please enter number option from the menu : ")
    
        if validate_data(display_payroll_option_data):
            print("Data is valid")
            break
        return display_payroll_option_data

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
    
        if validate_data(process_payroll_option_data):
            print("Data is valid")
            break
        return process_payroll_option_data

def validate_data(value):
    """
    Inside the try, converts value to integer
    raise ValueError if strings cannot be converted into int or less than 1 or greater than 4
    """
    try:
       
        if int(value) < 1 or int(value) > 4:
            raise ValueError(
               f"Number between 1 and 4 required, you typed {value}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

main_menu_option = get_main_menu_option()