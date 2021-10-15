# User Manual for People Payroll Application

## Table of Contents <a name="Home"></a>
1. [Login](#login)<br>
2. [The menu system](#menu)<br>
3. [View reports](#reports)<br>
4. [Process / Amend payroll data](#process_amend)<br>


[Click to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md)
___

## **1. Login** <a name="login"></a> 
<details>
    <summary>Click here to view login screen</summary>

![Screenshot of Home screen](/docs/images/people_payroll_welcomescreen.PNG)
</details><br>

___

1. Type username  and press enter
2. Type password and press enter <br>
(Username and password characters will not be visible on screen)<br>

If the user enters the username and password correctly,  the main menu will be displayed <br>

- **Error handling:** *If the user enters an incorrect username or password, the user will be prompted to try again*

___

## **2. The menu system** <a name="menu"></a> 
The menu system consists of all the options required to facilitate all stages of the payroll process as follows:
___
### Main Menu
<details>
    <summary>Click here to view the main menu</summary>

![Screenshot of main menu](/docs/images/menu/main_menu.PNG)
</details><br>


### Display Payroll menu
Type "1" from the main menu and press enter, the payroll menu will be displayed.
<details>
    <summary>Click here to view the menu</summary>

![Screenshot of display payroll menu](/docs/images/menu/display_payroll_menu.PNG)
</details><br>

### Process / amend payroll menu
Type "2" from the main menu and press enter, the process / amend payroll menu will be displayed.
<details>
    <summary>Click here to view the menu</summary>

![Screenshot of process / amend payroll menu](/docs/images/menu/process_amend_menu.PNG)
</details><br>

### Add / amend employee details

Type "3" from the main menu and press enter, the add / amend employee details menu  will be displayed 
<details>
    <summary>Click here to view the  menu</summary>

![Screenshot of add / amend employee details menu](/docs/images/menu/add_amend_employees_details_menu.PNG)
</details><br>

### Close Application
Type "4" from the main menu and press enter, the application closes

___

The Menu system
- **Error handling:** *If an incorrect number option is typed during any of the menu selections, the user will receive feedback: ‘Invalid data, please try again.’*
___

## **3. View reports** <a name="reports"></a> 
### Display payroll menu
Type "1" from the main menu and press enter, the display payroll menu will be displayed<br>
<details>
    <summary>Click here to view the menu</summary>

![Screenshot of add / amend employee details menu](/docs/images/menu/display_payroll_menu.PNG)
</details><br>

___
### Overall employees’ pay for week selected report
Type "1" from the display payroll menu and press enter to go to the "Overall employees’ pay for week selected" report

Enter the payroll week 

- **Error handling:** *If the user inputs invalid data, they will receive feedback: 
‘Invalid week number, please try again’*

The report will be displayed to the screen
<details>
<summary>Click here to view the report</summary>

![screenshot 1. Overall employees’ pay for week selected report](/docs/images/features/feature_3_1.PNG)
</details><br>
Press any key to return to the the display payroll menu<br>

___
### Employee pay for week selected report
Type "2" and press enter to go to "Employee pay for week selected" report<br>

Enter the payroll week 

- **Error handling:** *If the user inputs invalid data, they will receive feedback: 
‘Invalid week number, please try again’*

Enter the employee number <br>
- **Error handling:** *If the user has entered incorrectly, an error message will be displayed ‘Invalid employee number, please try again.’*

    *Then the user will be prompted ‘Do you want to try again? type y or n :’*

    *If no they will be taken back to the main menu*

There is further validation to check if the employee number has a record in the employee detail sheet.

If the employee number has been found the employees payroll sheet for the week, the data is displayed

<details>
<summary>Click here to view the report</summary>

![screenshot Employee pay for week selected report](/docs/images/features/feature_3_2.PNG)
</details><br>

If there is no record, a error message will be displayed

“No payroll record found for employee number: xx in xx”*

Press any key to return to the display payroll menu

___
### Employers summary for week report
Type "3" and press enter to go to "Employers summary for week" report<br>

<details>
<summary>Click here to view the report</summary>

![screenshot 3 Employers summary by week report](/docs/images/features/feature_3_3.PNG)
</details><br>

Press any key to return to the display payroll menu is displayed
___
### Main menu
Type "4" and press enter to go to the Main menu<br>

The main menu will be displayed
<details>
<summary>Click here to view the menu</summary>

![screenshot Main menu](/docs/images/features/feature_3_4.PNG)
</details><br>

___
## **4.Process / Amend payroll data**
<a name="process_amend"></a> 
### Process / amend payroll menu
Type "2" from the main menu and press enter to go to the process / amend payroll menu 
<details>
<summary>Click here to view the menu</summary>

![screenshot Main menu](/docs/images/menu/process_amend_menu.PNG)
</details><br>

___
### Add Employee's hours

Type "1" from the process / amend payroll menu and press enter to go to Add employee’s hours<br>

Enter the employee number

- **Error handling:** *If the user has entered incorrectly, an error message will be displayed ‘Invalid employee number, please try again.’*

    *Then the user will be prompted ‘Do you want to try again? type y or n :’*

    *If no they will be taken back to the main menu*

Validation will check if the employee number is in the  google sheets employee detail sheet.  

There is additional validation to ensure there is no employee record already entered into google sheets employee payroll sheet, to avoid duplicates.

If there is already an existing employee record in the payroll sheet, the application will provide feedback to the user

“Employees hours already entered in wk xx, please go to option 2 to amend”

Press any key to return to the Display payroll menu

Providing there is no record already entered, ‘No entry found in payroll’ message will be displayed

Enter the hours worked

- **Error Handling:** *Validation will check if the value is a float.*

    *If incorrect then ‘Invalid data, please try again.’ Is displayed and the user is prompted to enter the hours worked again*

The system will now calculate all the values for basic pay, holiday pay, NI contribution, pension contribution, net pay, employers NI contribution and employers contribution and display these values.

The user will be prompted ‘Are the amounts correct?’. 

If the values are incorrect , a message “re enter details’ is displayed and the user is prompted to ‘enter the hours worked’

If the values are correct, type ‘y’

A message will be displayed “Ready to upload into payroll spreadsheet" then the information uploads to the google sheets. When successful ‘employeepayroll worksheet updated successfully’ is displayed

The user will then prompted if they would like to process another employee's hours which they can add or go back to the main menu.

<details>
    <summary>Click here to see an example</summary>

![screenshot Add employees' hours](/docs/images/features/feature_4.PNG)
</details><br>

___
### Amend Employee's hours
Type "2" from the  process / amend payroll menu and press enter to go to Amend employees hours<br>

Enter the employee number

- **Error handling:** *If the user has entered incorrectly, an error message will be displayed ‘Invalid employee number, please try again.’*

    *Then the user will be prompted ‘Do you want to try again? type y or n :’*

    *If no they will be taken back to the main menu*

Validation will check if the employee number is in the google sheets employee detail sheet.

There is additional validation to ensure there is an employee record already entered into employee payroll Google Sheet

If no record is found ‘No payroll record found for xx in week wk xx, returning to main menu.’ Will be displayed

Press any key to return to the display payroll menu

If an record is found, ‘Employment record located’ message will be displayed . This record will be deleted and the user will be prompted to enter the employees hours again which will follow the add employees detail features above

<details>
<summary>Click here to view an example</summary>

![screenshot Amend employees' hours](/docs/images/features/feature_4_2.PNG)
</details><br>



___
### Main menu
Type "3" from the  process / amend payroll menu and press enter to go the main menu

Display the main menu
<details>
<summary>Click here view the menu</summary>

![screenshot Display the main menu](/docs/images/features/feature_4_3.PNG)
</details><br>

___

[Click to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md)

