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
    """
    print("-------------- Main Menu -------------- ")
    print("1 View payroll")
    print("2 Process / Amend payroll")
    print("3 Run payroll")
    print("4 Add / Amend employee details\n")
    print("Please enter number option from the main menu")
    print("Example:  1\n")

get_main_menu_option()