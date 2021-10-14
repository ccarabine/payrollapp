"""
menu.py file is for the people payroll applicaiton by Chris Carabine

This is the menu file for a command line interface payroll system for
displaying each of the menus.
"""

menu_welcome = ["----------------------------------------------"
                "---------------",
                "---------------- People Payroll Application ------------"
                "-----",
                "------------------------- Welcome ----------------------"
                "-----",
                "--------------------------------------------------------"
                "-----\n"]


menu_main_menu = ["------------------------------------------------------"
                  "-------",
                  "---------------- People Payroll Application ------------"
                  "-----",
                  "------------------------ Main Menu ---------------------"
                  "-----",
                  "--------------------------------------------------------"
                  "-----\n",
                  "1 Display payroll",
                  "2 Process / Amend payroll",
                  "3 Add / Amend employee details",
                  "4 Close application\n"]

menu_display_payroll = ["------------------------------------------------"
                        "-------------",
                        "---------------- People Payroll Application -------"
                        "----------",
                        "---------------------- Display Payroll ------------"
                        "----------",
                        "---------------------------------------------------"
                        "----------\n",
                        "1 Overall employees' pay for week selected",
                        "2 Employee pay for week selected",
                        "3 Employers summary for week",
                        "4 Main menu\n"]

menu_process_amend_payroll = ["---------------------------------------------"
                              "----------------",
                              "---------------- People Payroll Application ---"
                              "--------------",
                              "----------------- Process / Amend Payroll -----"
                              "--------------",
                              "-----------------------------------------------"
                              "--------------\n",
                              "1 Add employees' hours",
                              "2 Amend employee's hours",
                              "3 Main menu\n"]


menu_add_amend_employee = ["--------------------------------------------------"
                           "-----------",
                           "---------------- People Payroll Application ------"
                           "-----------",
                           "-------------- Add / Amend Employee's Details ----"
                           "-----------",
                           "--------------------------------------------------"
                           "-----------\n",
                           "\n Feature in next update, returning to main menu "
                           "\n"]

menu_employees_pay = ["-------------------------------------------------------"
                      "------",
                      "---------------- People Payroll Application -----------"
                      "------",
                      "---------------------- Employees' pay -----------------"
                      "------",
                      "-------------------------------------------------------"
                      "------\n"]


menu_employers_payment_summary = ["-------------------------------------------"
                                  "------------------",
                                  "---------------- People Payroll Application"
                                  "------------------",
                                  "----------------- Employers payment summary"
                                  "------------------",
                                  "-------------------------------------------"
                                  "------------------\n"]


def welcome_menu():
    """
    Displays the welcome screen on load
    """
    for header in menu_welcome:
        print(header)


def main_menu():
    """
    Displays the Main menu
    """
    for header in menu_main_menu:
        print(header)


def display_payroll_menu():
    """
    Displays the Display payroll menu
    """
    for header in menu_display_payroll:
        print(header)


def process_amend_payroll_menu():
    """
    Displays the Process / Amend menu
    """
    for header in menu_process_amend_payroll:
        print(header)


def add_amend_employee_menu():
    """
    Displays the Add / Amend Employee's Details menu
    """
    for header in menu_add_amend_employee:
        print(header)


def employees_pay_menu():
    """
    Displays the Employees' Details menu
    """
    for header in menu_employees_pay:
        print(header)


def employers_payment_summary_menu():
    """
    Displays the Employees' Details menu
    """
    for header in menu_employers_payment_summary:
        print(header)
