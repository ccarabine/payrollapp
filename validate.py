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
employeepayroll = SHEET.worksheet('employeepayroll')


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
        and puts the values into variables and returns them
    except AttributeError if there isn't a value in the sheet
        then asks the user if they want to try again or return
        to the main menu

    @param employee_num(string): Employee number
    @param status(string): Status value coded in
    @raise AttributeError: raises an exception if the employee
    number is incorrect
    """
    try:
       
        print("Validating employee number")
        employee_row = employeedetail.find(employee_num).row
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
    except AttributeError:
        print('\nInvalid employee number, please try again.\n')
        while True:
            if yesorno("Do you want to try again? type y or n :  "):
                break
            get_main_menu_option()


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

