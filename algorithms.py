from datetime import date
"""Imports for all modules for application to function fully:

datetime: to get the current week of the year
"""
# Constant variables
HOL_PC = 0.1208
EMPLOYEES_NI_PC = 0.12
EMPLOYEES_NI_AMOUNT = 184

EMPLOYERS_PENSION_PC = 0.03
EMPLOYERS_NI_PC = 0.138
EMPLOYERS_NI_AMOUNT = 170


def calculate_payroll_values(payroll_week, employee_num, employee_surname, employee_firstname, \
        employee_rate_of_pay, employee_pension, employee_hours):
    """
    Get Employees details from spreadsheet,
    put into variables, calculate values and updates worksheet
    @param payroll_week(str): payroll week
    @param employee_num : Employee number
    @param status(str) : Status
    @returns: payroll_wk(str) : Payroll week
    """


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
    return (payroll_week, employee_num, employee_surname, employee_firstname, employee_basic_pay,\
        employee_holiday, employee_ni, employee_pension, employee_net_pay, employers_ni, employers_pension)
   

def payroll_weeks():
    """
    Get current tax week number, minus 13 weeks to start in april for
    payroll week to get the previous payroll week, minus 1 week
    @returns: last_week_payroll_week_number(str)
    isocalender code reference from
    http://week-number.net/programming/week-number-in-python.html
    """
    tax_week_number = date.today().isocalendar()[1]
    current_payroll_week_number = tax_week_number - 13
    last_week_payroll_week_number = current_payroll_week_number - 1
    return(last_week_payroll_week_number)