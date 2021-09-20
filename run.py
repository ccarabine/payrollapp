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
    
    print("Example:  1\n")

    main_menu_data = input("Please enter number option from the menu : ")
   
    validate_data(main_menu_data)

def validate_data(value):
    """

    """
    try:
       
        if int(value) < 1 or int(value) > 4:
            raise ValueError(
               f"Number between 1 and 4 required, you typed {value}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_main_menu_option()