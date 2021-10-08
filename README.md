# People Payroll Applicaton

## A command Line Interface Application

___


![Screenshot of home screen](docs/images/people_payroll_welcomescreen.PNG)


**People Payroll is a terminal based application providing a solution to common pain points experienced by many small business owners. The application enables employers to process employee hours, and simultaneously calculate their pay/liabilities efficiently, eliminating the risk of manual calculation errors, and resulting in increased productivity.**

### View my deployed site. <a href="https://people-payroll-application.herokuapp.com/"> People Payroll Applicaiton </a>

[Here](https://docs.google.com/spreadsheets/d/1tZfgo8_TkdA9EdJyrj58YbFePcTcciv-zyC2UBqY6-g/edit?usp=sharing) is the link to the Google Spreadsheet, to see the updates made.

***
## Table of Contents <a name="Home"></a>

1. [User Experience (UX)](#ux)<br>
    i.  [Strategy](#strategy)<br>
    ii. [Scope](#scope)<br>
    iii. [Structure](#Structure)<br>
    iv. [Skeleton](#skeleton)<br>
    v. [Surface](#surface)<br>
      
2. [Features](#features)<br>
    i. [Current Features](#features-current)<br>
    ii. [Features to implement](#features-toimplement)<br>

3. [Testing](#testing)

    * [Features testing](#features-testing)
    * [User Stories Testing](#user-stories-testing)
    * [Known issues during testing](#known-issues)
    * [Validation Testing -HTML ](#validation-testing-html)
    * [Bugs left](#unfixed-bugs)
4. [Deployment](#deployment)
5. [Technologies Used](#technology-used)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)


---
# 1. User Experience (UX) <a name="ux"></a> 
 
## Project Goals 
___

Project Goals for intended use are:

Create a payroll application: 

- to process employee hours quickly and efficiently by calculating their pay/liabilities effectively, resulting in increased accuracy and productivity.
- that enables users to navigate with ease.
- that is intuitive to all users.

Personal Goal:
- Having spent many years working in the hospitality industry and managing a food production site, I have experienced much pain whilst implementing the payroll process, such as the amount of time it can take and the risk of creating manual errors/miscalculations and their repercussions. I wish to create a painless process and excellent user experience for any user, drawing upon my familiarity of the process to provide meaningful solutions and implement an algorithm.

## User Goals 

- Payroll staff should find the system intuitive to navigate and easy to use.

- The system should give feedback to let the user know where the program is at every stage and be able to submit the payroll via Google Sheets, ready for the ‘accountant’ to make payments.

- The target audience for this terminal based application are employers who want to process their employees payroll and submit for deployment via Google Sheet.

---

# i. Strategy <a name="strategy"></a>


## User Stories: 


### Site User stories:
1.	As a user, I  want a secure application/login to protect against unauthorised access 
2.	As a user, I want a terminal based application to import/export data via google sheets
3.	As a user, I want to easily navigate through the different functions to view and process payroll
4.	As a user, I want to process employees hours and receive feedback if I duplicate data inputted already for an employee in that particular week
5.	As a user, I want an application that calculates Basic pay, Holiday pay, Employee NI contributions, Pension Contributions, Net pay, Employee NI contributions, Pension Contributions
6. As a user, I want full visibility of an employee’s payment summary before submission to payroll (send to google sheets spreadsheet)
7. As a user, I want full visibility of all employees payment summaries for any week at any time
8. As a user, I want full visibility of an employee’s payment summary for the previous week with the ability to modify inputted hours for the previous week if required
9. As a user, I want full visibility of the business’s payment summary, consolidated by week 
10. As a user I want to be able to locate an employee and their details quickly/efficiently
11. As a user with no formal finance training/qualifications I need simple and easy to understand terminology
12. As a user I need to be able to trust the application to calculate payments accurately
13. As a user I need quick painless process, in order to free up more time to be productive in other areas of my role.

### Site Owner Goals 

14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors
	
### [Contents table ](#home)
---
# ii. Scope <a name="scope"></a>

## Strategy Trade-offs
I have rated the features on a scale of 1 to 5 in terms of importance (how important is it for the project now) and viability (how realistic is that we can implement a solution)

To achieve the strategy goals, the following features highlighted in dark/light green will be implemented to create a minimal viable  product due to timescale and technical ability. The additional features in red will be added at a further stage

![Strategy trade offs table](docs/images/strategytradeoffs.PNG) 

### [Contents table ](#home)
---
# iii. Structure <a name="structure"></a> 

The payroll system relies on user input from the menu system.  The user will navigate to the different options via the main menu system.

An option to return to the main menu is easily/consistently visible on each page.

It is important that the application is easy to navigate and provides feedback to the user to inform them at what stage/status of the process they are at.


### **1.	Welcome and security screen**
<details>
    <summary>Click here to view the home screen</summary>
![Screenshot of Home screen](docs/images/people_payroll_welcomescreen.PNG)
</details>
This welcomes the user to the application, to access the application the user needs to enter a (non-visible) password. The main menu will then be displayed

____

### **2.	Main menu**
<details>
    <summary>Click here to view the main menu</summary>
![Screenshot of main menu](docs/images/menu/main_menu.PNG)
</details>

People Payroll Application<br>

Main menu<br>
1 Display payroll <br>
2 Process / Amend payroll<br>
3 Add / Amend employee details<br>
4 Close application<br>

___
### **3. Display payroll menu<br>**
<details>
    <summary>Click here to view the display payroll menu</summary>
![Screenshot of display payroll menu](docs/images/menu/display_pauroll_menu.PNG)
</details>

### **User inputs** numeral 1, the first option 1 in main menu. The next step is the ‘Display Payroll’ menu 


People Payroll Application<br>

Display payroll menu<br>
1 Overall employees’ pay for week selected<br>
2 Employee pay for week selected<br>
3 Employers summary by week<br>
4 Main menu<br>

### **User inputs** numeral 1, the first option in the ‘Display Payroll’ menu. 

The next step is ‘Enter Payroll Week (1-52) :’<br>
User enters required fiscal/calendar week by inputting the relevant numeral, then all employees payroll is displayed to the terminal for relevant week

### **User inputs** numeral 2, the second option in the ‘Display Payroll’ menu.

The next step is ‘Enter Payroll Week (1-52) :’
User enters required fiscal/calendar week by inputting the relevant numeral

The next step is ‘Enter Employee Number e.g. 100014 :’ 
User enters required employee number, the terminal then displays the employees pay summary for relevant week

### **User inputs** numeral 3, the third option in the ‘Employer’s summary for the week’

Immediately the employers payment summary is displayed by week

### **User inputs** numeral 4, the fourth option in the ‘Main menu’

The main menu is displayed
___
### **4. Process / amend payroll menu<br>**
<details>
    <summary>Click here to view the process / amend payroll menu</summary>
![Screenshot of process / amend payroll menu](docs/images/menu/process_amend_menu.PNG
</details>

### **User inputs** numeral 2, the second option in main menu. The next step is the ‘Process / amend payroll’ menu 

People Payroll Application<br>

Process / amend payroll<br>
1 Add Employees hours<br>
2 Amend employees hours<br>
3 Main menu<br>

### **User inputs** numeral 1, the first option in the ‘Process / amend payroll’ menu.

The next step is ‘Enter Employee Number e.g. 100014 :’ 
User enters required employee number in numerals,

The next step is ‘Enter number of hours worked :’
User enters required hours in numerals,

The amounts are displayed to the screen
The next step is “if the amounts are correct”
User enters required Y,

The values are added to google sheet employee payroll sheet 

### **User inputs** numeral 2, the second option in the ‘Process / amend payroll’ menu.

The next step is ‘Enter Employee Number e.g. 100014 :’ 
User enters required employee number in numerals,

The next step is ‘Enter number of hours worked :’
User enters required hours in numerals,

The amounts are displayed to the screen
The next step is “if the amounts are correct”
User enters required Y,

The values are added to google sheet employee payroll sheet 

### **User inputs** numeral 3, the third option in the ‘Main menu’

The main menu is displayed


User inputs numeral 3, the third option in main menu. The next step is the Feature in next update, returning to main menu is displayed

### **User inputs** numeral 4, the fourth option in the ‘Main menu’

Application closes

### [Contents table ](#home)

---
# iv. Skelton <a name="skeleton"></a> 

## Flowcharts

I used <a href=" https://www.lucidchart.com/">Lucid Chart</a> to create flowcharts for my project in order to plan out flow of the application
INSERT FLOW CHARTS
Link to flow chart page

DO TO

### [Contents table ](#home)
___

# iv. Surface <a name="surface"></a> 

## Visual Design

As this is a terminal based application the styling is very limited so I have focused/prioritised optimizing functionality, especially in providing the user feedback required at the correct points of the application, coupled with ease of navigation.

---
# 2. Features <a name="features"></a> 

## i. Current Features (short term objectives): <a name="features-current"></a>
___
SCREENSHOTS

### **Feature 1: Welcome Message and security**
The user is welcomed to the payroll application and prompted to enter a username and password (no password characters are visible)<br>
If the user enters: <br>
- the correct password, the main menu is displayed
- an incorrect password, the user will be prompted to try again 

**User stories covered:**<br>
*1.	As a user, I  want a secure application/login to protect against unauthorised access*
___
### **Feature 2: Menu system**
The menu system consists of all the options required to facilitate all stages of the payroll process as follows:

___
People Payroll Application<br>

**Main menu**<br>
1 Display payroll<br>
2 Process / Amend payroll<br>
3 Add / Amend employee details<br>
4 Close Application<br>

___
*Option 1* from the main menu typed , display the payroll menu
People Payroll Application<br>

**Display payroll menu**<br>
1 Overall employees’ pay for week selected<br>
2 Employee pay for week selected<br>
3 Employers summary by week<br>
4 Main menu<br>
___
*Option 2* from the main menu typed , display the payroll menu
People Payroll Application<br>

**Process / amend payroll menu**<br>
1 Add Employees hours<br>
2 Amend employees hours<br>
3 Main menu<br>
___
If an incorrect number option is typed during any of the menu selections, the user will receive feedback: ‘Invalid data, please try again.’

**User stories covered:**<br>
*3.	As a user, I want to easily navigate through the different functions to view and process payroll<br>
11. As a user with no formal finance training/qualifications I need simple and easy to understand terminology<br>
13. As a user I need quick painless process, in order to free up more time to be productive in other areas of my role.<br>
14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors<br>*
	
___
### **Feature 3: Display payroll**
From the main menu, the user will be prompted to select an option by typing the relevant numeral.

*Option 1* from the main menu typed , the payroll menu will be displayed
People Payroll Application<br>
___
**Display payroll menu**<br>
1 Overall employees’ pay for week selected<br>
2 Employee pay for week selected<br>
3 Employers summary by week<br>
4 Main menu<br>
___
The user will be prompted to select an option by typing the relevant numeral

*Option 1* typed from the display payroll menu( 1 Overall employees’ pay for week selected)
User will be prompted to enter the payroll week which must be before the current payroll week. 

If the user inputs invalid data, they will receive feedback: 
‘Invalid week number, please try again’

After validation, the  API request is made and displays all employees payroll information for the week

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

then the display payroll menu is displayed

___

*Option 2* selected from the display payroll menu - 2 Employee pay for week <br>
User will be prompted to enter the payroll week which must be before the current payroll week. After validation, the user will be then prompted to enter the employee number <br>
If the user has entered an incorrectly, an error message will be displayed ‘Invalid employee number, please try again.’<br>
Then the user will be prompted ‘Do you want to try again? type y or n :’<br>
If no they will be taken back to the main menu

There is further validation to check if the employee number has a record in the employee detail sheet.  

If the employee number has been found the employees payroll sheet for the week, the data is displayed

If there is no record, a error message will be displayed
“No payroll record found for employee number: xx in xx”

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

then the display payroll menu is displayed
___
*Option 3* selected from the display payroll menu - Employers summary for week<br>
The data is summarised for each heading and grouped by week and displayed to the terminal

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

then the display payroll menu is displayed
___
*Option 4* selected from the display payroll menu -  Main menu<br>
The main menu is displayed

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
___
People Payroll Application<br>

**Process / amend payroll**<br>
1 Add Employees hours<br>
2 Amend employees hours<br>
3 Main menu<br>
___
The user will be prompted to select an option by typing in the relevant numeral

*Option 1* typed from the process / amend payroll menu (1. Add Employee’s hours)<br>
The user will be then prompted to enter the employee number, validation will check if the employee number is in the google sheets employee detail sheet.  

There is additional validation to ensure there is no employee record already entered into google sheets employee payroll sheet, to avoid duplicates.

If there is already an existing employee record in the payroll sheet, the application will provide feedback to the user 

“Employees hours already entered in wkxx, please go to option 2 to amend”

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information

Providing there is no record already entered, 
‘No entry found in payroll’ message will be displayed

The user will be then prompted to enter the hours worked, validation will check if the value is a float.  If incorrect then ‘Invalid data, please try again.’ Is displayed and the user is prompted to enter the hours worked again

The system will now calculate all the values for basic pay, holiday pay, NI contribution, pension contribution, net pay, employers NI contribution and employers contribution and display these values.

The user will be prompted ‘Are the amounts correct?’. If the values are incorrect , the user type ‘n’ a message “re enter details’ is displayed and the user is prompted to ‘enter the hours worked’

If the values are correct, a message will be displayed “Ready to upload into payroll spreadsheet" then the information uploads the values to the google sheets. When successfully ‘employeepayroll worksheet updated successfully’ is displayed

The user will then prompted if they would like to process another employees hours which they can add another employees hours or go back to the main menu
___
*Option 2* typed from the  process / amend payroll menu (2 Amend employees hours)<br>
The user will be prompted to enter the employee number, validation will check if the employee number is in the google sheets employee detail sheet.  

There is additional validation to ensure there is an employee record already entered into google sheets employee payroll sheet to ensure we can amend the result
If no record is found ‘No payroll record found for 100017 in week wk26, returning to main menu.’ Will be displayed

‘Press any key to clear the screen and return to the display payroll menu’ message will be displayed to give the user time to view the information and then the process /amend payroll menu will be displayed

If an record is found, ‘Employment record located’ message will be displayed . This record will be deleted and the user will be prompted to enter the employees hours again which will follow the add employees detail features above


# GOOGLE SHEET SNIPIT  NEED TO DO!!!!
___

Option 3 typed from the  process / amend payroll menu  ( 3 Main menu)

Display the main menu

**User stories covered:**<br>
*2.	As a user, I want a terminal based application to import/export data via google sheets<br>
3.	As a user, I want to easily navigate through the different functions to view and process payroll<br>
4.	As a user, I want to process employees hours and receive feedback if I duplicate data inputted already for an employee in that particular week<br>
5.	As a user, I want an application that calculates Basic pay, Holiday pay, Employee NI contributions, Pension Contributions, Net pay, Employee NI contributions, Pension Contributions<br>
6. As a user, I want full visibility of an employee’s payment summary before submission to payroll (send to google sheets spreadsheet)<br>
11. As a user with no formal finance training/qualifications I need simple and easy to understand terminology<br>
12. As a user I need to be able to trust the application to calculate payments accurately<br>
13. As a user I need quick painless process, in order to free up more time to be productive in other areas of my role.<br>*

Owners stories covered:
14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors
	
___	
### **Feature 5:  Add / Amend employee details**
___
This is a future feature

**User stories covered:**<br>
*10. As a user I want to be able to locate an employee and their details quickly/efficiently*

**Owners stories covered:**<br>
*14. I want a terminal based application containing validated Python code which allows the user to navigate the system intuitively without returning errors*












![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome ccarabine,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!