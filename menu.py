"""
menu.py file is for the people payroll applicaiton by Chris Carabine

This is the menu file for a command line interface payroll system for
displaying each of the menus.
"""


def welcome_menu():
    """
    Displays the welcome screen on load
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("------------------------- Welcome ---------------------------")
    print("-------------------------------------------------------------\n")


def main_menu():
    """
    Displays the Main menu
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("------------------------ Main Menu --------------------------")
    print("-------------------------------------------------------------\n")
    print("1 Display payroll")
    print("2 Process / Amend payroll")
    print("3 Add / Amend employee details")
    print("4 Close application\n")


def display_payroll_menu():
    """
    Displays the Display payroll menu
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("---------------------- Display Payroll ----------------------")
    print("-------------------------------------------------------------\n")
    print("1 Overall employees' pay for week selected")
    print("2 Employee pay for week selected")
    print("3 Employers summary for week")
    print("4 Main menu\n")


def process_amend_payroll_menu():
    """
    Displays the Process / Amend menu
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("----------------- Process / Amend Payroll -------------------")
    print("-------------------------------------------------------------\n")
    print("")
    print("1 Add employees' hours")
    print("2 Amend employee's hours")
    print("3 Main menu\n")


def add_amend_employee_menu():
    """
    Displays the Add / Amend Employee's Details menu
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("-------------- Add / Amend Employee's Details ---------------")
    print("-------------------------------------------------------------\n")
    print("\n Feature in next update, returning to main menu \n")


def employees_pay_menu():
    """
    Displays the Employees' Details menu
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("---------------------- Employees' pay -----------------------")
    print(
        "---------------------------------------------------------"
        "----\n"
        )


def employers_payment_summary_menu():
    """
    Displays the Employees' Details menu
    """
    print("-------------------------------------------------------------")
    print("---------------- People Payroll Application -----------------")
    print("----------------- Employers payment summary -----------------")
    print("-------------------------------------------------------------\n")
