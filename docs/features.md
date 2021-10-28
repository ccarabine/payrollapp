[Click here to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md#features)

# 2. Features <a name="features"></a> 

## i. Current Features (short term objectives): <a name="features-current"></a>
___
### **Feature 1: Welcome Message and security**
___
<details>
<summary>Click here to view the home screen</summary>

![Screenshot of Home screen](/docs/images/people_payroll_welcomescreen.PNG)
</details><br>
The user is welcomed to the payroll application and prompted to enter a username and password (no password characters are visible)<br>
If the user enters: <br>
- the correct password, the main menu is displayed<br>
- an incorrect password, the user will be prompted to try again 

**User stories covered:**<br>
*1.	As a user, I  want a secure application/login to protect against unauthorised access*
___
### **Feature 2: Menu system**
___
The menu system consists of all the options required to facilitate all stages of the payroll process as follows:

<details>
<summary>Click here to view the main menu</summary>

![Screenshot of main menu](/docs/images/menu/main_menu.PNG)
</details><br>

___
*Option 1* from the main menu typed , display the payroll menu
<details>
<summary>Click here to view the display payroll menu</summary>

![Screenshot of display payroll menu](/docs/images/menu/display_payroll_menu.PNG)
</details><br>

___
*Option 2* from the main menu typed , display the process /amend payroll menu
<details>
<summary>Click here to view the process / amend payroll menu</summary>

![Screenshot of process / amend payroll menu](/docs/images/menu/process_amend_menu.PNG)
</details><br>

___
If an incorrect number option is typed during any of the menu selections, the user will receive feedback: ‘Invalid data, please try again.’

**User stories covered:**<br>
*3.	As a user, I want to easily navigate through the different functions to view and process payroll<br>
11. As a user with no formal finance training/qualifications I need simple and easy to understand terminology<br>
13. As a user I need quick painless process, in order to free up more time to be productive in other areas of my role.<br>
14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors<br>*
	
___
### **Feature 3: Display payroll**
___
From the main menu, the user will be prompted to select an option by typing the relevant numeral.

*Option 1* from the main menu typed , the payroll menu will be displayed

<details>
<summary>Display Payroll menu</summary>

![screenshot Display Payroll menu](/docs/images/menu/display_payroll_menu.PNG)
</details><br>

The user will be prompted to select an option by typing the relevant numeral

*Option 1* typed from the display payroll menu (Overall employees’ pay for week selected)

User will be prompted to enter the payroll week which must be before the current payroll week. 

If the user inputs invalid data, they will receive feedback: 
‘Invalid week number, please try again’

After validation, the  API request is made and displays all employees payroll information for the week

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

then the display payroll menu is displayed
<details>
<summary>1. Overall employees’ pay for week selected report</summary>

![screenshot 1. Overall employees’ pay for week selected report](/docs/images/features/feature_3_1.PNG)
</details><br>

___
*Option 2* selected from the display payroll menu - 2 Employee pay for week selected <br>

User will be prompted to enter the payroll week which must be before the current payroll week. After validation, the user will be then prompted to enter the employee number <br>
If the user has entered incorrectly, an error message will be displayed ‘Invalid employee number, please try again.’<br>
Then the user will be prompted ‘Do you want to try again? type y or n :’<br>
If no they will be taken back to the main menu

There is further validation to check if the employee number has a record in the employee detail sheet.  

If the employee number has been found the employees payroll sheet for the week, the data is displayed

If there is no record, a error message will be displayed
'No payroll record found for employee number: xx in xx'

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

then the display payroll menu is displayed

<details>
<summary>2. Employee pay for week selected report</summary>

![screenshot Employee pay for week selected report](/docs/images/features/feature_3_2.PNG)
</details><br>

___
*Option 3* selected from the display payroll menu - 3. Employers summary for week<br>

The data is summarised for each heading and grouped by week and displayed to the terminal

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

then the display payroll menu is displayed

<details>
<summary>3. Employers summary by week report</summary>

![screenshot 3 Employers summary by week report](/docs/images/features/feature_3_3.PNG)
</details><br>

___
*Option 4* selected from the display payroll menu -  Main menu<br>

The main menu is displayed
<details>
<summary>4. Main menu</summary>

![screenshot Main menu](/docs/images/features/feature_3_4.PNG)
</details><br>

___
**User stories covered:**<br>
*3. As a user, I want to easily navigate through to the different functions to view and process payroll<br>
7. As a user, I want full visibility of all employees payment summaries for any week at any time<br>
8. As a user, I want full visibility of an employee’s payment summary for the previous week with the ability to modify inputted hours for the previous week if required<br>
9. As a user, I want full visibility of the business’s payment summary, consolidated by week <br>
11. As a user with no formal finance training/qualifications I need simple and easy to understand terminology<br>
12. As a user I need to be able to trust the application to calculate payments accurately<br>
13. As a user I need a quick painless process, in order to free up more time to be productive in other areas of my role.*<br>

**Owners stories covered:**<br>
14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors<br>

___
### **Feature 4: Process /Amend payroll**
___
From the main menu, the user will be prompted to select an option by typing in the relevant numeral

Option 2 from the main menu typed, the process / amend payroll menu will be displayed

<details>
<summary>Click here to view the process / amend payroll menu</summary>

![Screenshot of process / amend payroll menu](/docs/images/menu/process_amend_menu.PNG)
</details><br>

___
The user will be prompted to select an option by typing in the relevant numeral

*Option 1* typed from the 'process / amend payroll menu' to go 'Add Employee’s hours' option<br>
The user will then be prompted to enter the employee number, validation will check if the employee number is in the google sheets employee detail sheet.  

There is additional validation to ensure there is no employee record already entered into google sheets employee payroll sheet, to avoid duplicates.

If there is already an existing employee record in the payroll sheet, the application will provide feedback to the user 

'Employees hours already entered in wkxx, please go to option 2 to amend'

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

Providing there is no record already entered, 
‘No entry found in payroll’ message will be displayed

The user will be then prompted to enter the hours worked, validation will check if the value is a float.  If incorrect then ‘Invalid data, please try again.’ Is displayed and the user is prompted to enter the hours worked again

The system will now calculate all the values for basic pay, holiday pay, NI contribution, pension contribution, net pay, employers NI contribution and employers contribution and display these values.

The user will be prompted ‘Are the amounts correct?’.

If the values are incorrect , the user will type ‘n’

a message “re enter details’ is displayed and the user is prompted to ‘enter the hours worked’

If the values are correct, a message will be displayed 

'Ready to upload into payroll spreadsheet' then the information uploads to google sheets. When successful ‘employeepayroll worksheet updated successfully’ message is displayed.

The user will then prompted if they would like to process another employees hours which they can add or go back to the main menu

<details>
<summary>Click here to view add employees' hours</summary>

![screenshot Add employees' hours](/docs/images/features/feature_4.PNG)
</details><br>

___
*Option 2* typed from the  'process / amend payroll menu' to go  'Amend employees hours' option<br>
The user will be prompted to enter the employee number, validation will check if the employee number is in the google sheets employee detail sheet.  

There is additional validation to ensure there is an employee record already entered into google sheets employee payroll sheet.

If no record is found ‘No payroll record found for xx in week wk xx, returning to main menu.’ will be displayed

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information and then the process /amend payroll menu will be displayed

If a record is found, ‘Employment record located’ message will be displayed . This record will be deleted and the user will be prompted to enter the employees hours again .

Validation will check if the value is a float.  

If incorrect then ‘Invalid data, please try again.’ is displayed and the user is prompted to enter the hours worked again

The system will now calculate all the values for basic pay, holiday pay, NI contribution, pension contribution, net pay, employers NI contribution and employers contribution and display these values.

The user will be prompted ‘Are the amounts correct?’.

If the values are incorrect , the user will type ‘n’

a message “re enter details’ is displayed and the user is prompted to ‘enter the hours worked’

If the values are correct, a message will be displayed 

'Ready to upload into payroll spreadsheet' then the information uploads to google sheets. When successful ‘employeepayroll worksheet updated successfully’ message is displayed.

The user will then prompted if they would like to process another employees hours which they can add or go back to the main menu

<details>
<summary>Click here to view the results </summary>

![screenshot Amend employees' hours](/docs/images/features/feature_4_2.PNG)
</details><br>

<details>
<summary>Click here to view the data in Google sheets</summary>

![screenshot Amend employees' hours -google sheets](/docs/images/features/feature_4_2_1.PNG)
</details><br>

___

Option 3 typed from the  'process / amend payroll menu' to go to the 'main menu'

Display the main menu
<details>
<summary>Click here view display the main menu</summary>

![screenshot Display the main menu](/docs/images/features/feature_4_3.PNG)
</details><br>

**User stories covered:**<br>
2.	As a user, I want a terminal based application to import/export data via google sheets<br>
3.	As a user, I want to easily navigate through the different functions to view and process payroll<br>
4.	As a user, I want to process employees hours and receive feedback if I duplicate data inputted already for an employee in that particular week<br>
5.	As a user, I want an application that calculates Basic pay, Holiday pay, Employee NI contributions, Pension Contributions, Net pay, Employee NI contributions, Pension Contributions<br>
6. As a user, I want full visibility of an employee’s payment summary before submission to payroll (send to google sheets spreadsheet)<br>
11. As a user with no formal finance training/qualifications I need simple and easy to understand terminology<br>
12. As a user I need to be able to trust the application to calculate payments accurately<br>
13. As a user I need quick painless process, in order to free up more time to be productive in other areas of my role.*<br>

**Owners stories covered:**<br>
*14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors*
	
___	
### **Feature 5:  Add / Amend employee details**
___
This is a future feature

**User stories covered:**<br>
*10. As a user I want to be able to locate an employee and their details quickly/efficiently*

**Owners stories covered:**<br>
*14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors*

[Click here to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md#features)