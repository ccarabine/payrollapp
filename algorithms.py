from datetime import date
"""Imports for all modules for application to function fully:

datetime: to get the current week of the year
"""


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
