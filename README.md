# People Payroll application

People Payroll is a command line terminal based application providing a solution to common pain points experienced by many small business owners. The application enables employers to process employee hours, and simultaneously calculate their pay/liabilities efficiently, eliminating the risk of manual calculation errors, and resulting in increased productivity.

<details>
    <summary>Click here to view the login screen</summary>

![Screenshot of login screen](/docs/images/people_payroll_welcomescreen.PNG)
</details><br>

___
## Points to note when using People Payroll application for the first time:

To gain access use the following login details

Username : *admin*

Password: *google1*

From the login screen take note of the current payroll week e.g. 30, you will only be able to add/amend new records for the previous payroll week (hours from Monday to Sunday just gone)  e.g. 29, this feature is automated.  This is important to note when displaying records

When you launch the application for the first time you will probably be in a new payroll week and there will be no records entered

To add new records, click on option 2 from the main menu then option 3.
Hours are the hours worked for the full week e.g., 40

The following employee numbers are registered :

- 100014

- 100015

- 100016

- 100017

The user can email admin@peoplepayroll.com to add additional employees until the future feature is released

Click here to view: 

* [People Payroll application](https://people-payroll-application.herokuapp.com/), to go to my deployed site.

* [User manual](https://github.com/ccarabine/payroll/blob/main/docs/user_manual.md), to operate the application.

* [Google Sheets](https://docs.google.com/spreadsheets/d/1Mh0WaeqPiZRDhHZpLVrVSoBcV8L4cPMKQXs2a-Z90Uo/edit?usp=sharing), to access changes made.


___
## Table of Contents <a name="Home"></a>

1. [User Experience (UX)](#ux)<br>
    i.  [Strategy](#strategy)<br>
    ii. [Scope](#scope)<br>
    iii. [Structure](#Structure)<br>
    iv. [Skeleton and technical design](#skeleton)<br>
    v. [Surface](#surface)<br>
      
2. [Features](#features)<br>
    i. [Current Features](#features-current)<br>
    ii. [Features to implement](#features-toimplement)<br>

3. [Testing](#testing)<br>

    i. [User Stories/feature testing](#user-stories-testing)<br>
    ii.  [Known issues during testing](#known-issues)<br>
    iii. [Validation testing  ](#validation-testing)<br>
    iv. [Unfixed bugs](#unfixed-bugs)<br>
4. [Deployment](#deployment)<br>
5. [Technologies Used](#technology-used)<br>
6. [Credits](#credits)<br>
7. [Acknowledgements](#acknowledgements)<br>


---
# 1. User Experience (UX) <a name="ux"></a> 

## Goals 

### Project Goals:

- Create a payroll application:

    - to process employee hours quickly and efficiently by calculating their pay/liabilities effectively, resulting in increased accuracy and productivity.
    - that enables users to navigate with ease.
    - that is intuitive to all users.

### Personal Goal:
- Having spent many years working in the hospitality industry and managing a food production site, I have experienced much pain whilst implementing the payroll process, such as the amount of time it can take and the risk of creating manual errors/miscalculations and their repercussions. I wish to create a painless process and excellent user experience for any user, drawing upon my familiarity of the process to provide meaningful solutions and implement an algorithm.

### User Goals:

- Payroll staff should find the system intuitive to navigate and easy to use.

- The system should give feedback to let the user know where the program is at every stage and be able to submit the payroll via Google Sheets, ready for the ‘accountant’ to make payments.

- The target audience for this terminal based application are employers who want to process their employees payroll and submit for deployment via Google Sheet.

---

## i. Strategy <a name="strategy"></a>

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
	
___
## ii. Scope <a name="scope"></a>

### Strategy Trade-offs
I have rated the features on a scale of 1 to 5 in terms of importance (how important is it for the project now) and viability (how realistic is that we can implement a solution)

To achieve the strategy goals, the following features highlighted in dark/light green will be implemented to create a minimal viable  product due to timescale and technical ability. The additional features in red will be added at a further stage
<details>
    <summary>Click here to view the Strategy trade offs table</summary>

![Strategy trade offs table](/docs/images/strategytradeoffs.PNG)
</details><br>

___
## iii. Structure <a name="structure"></a> 

The payroll system relies on user input from the menu system.  The user will navigate to the different options via the main menu system.

An option to return to the main menu is easily/consistently visible on each page.

It is important that the application is easy to navigate and provides feedback to the user to inform them at what stage/status of the process they are at.

[Click on link to go to the structure](https://github.com/ccarabine/payroll/blob/main/docs/structure.md)


---
## iv. Skeleton / Technical design <a name="skeleton"></a> 

### Data model, application features and business logic

I used <a href=" https://www.lucidchart.com/">Lucid Chart</a> to create flowcharts/data models for my project in order to plan out the flow of the application to manage, query and manupulate data

### Click here to view the following flowcharts: 

<details>
<summary>Security and menu</summary>

![Screenshot of flowchart - Security and menu ](/docs/images/flow_charts/menus.png)
</details>
<details>
<summary>Display payroll option 1 </summary>

![Screenshot of flowchart - display payroll option 1](/docs/images/flow_charts/display_payroll_option_one.png)
</details>
<details>
<summary>Display payroll option 2 </summary>

![Screenshot of flowchart - display payroll option 2 ](/docs/images/flow_charts/display_payroll_option_two.png)
</details>
<details>
<summary>Display payroll option 3 </summary>

![Screenshot of flowchart - display payroll option 3 ](/docs/images/flow_charts/display_payroll_option_three.png)
</details>
<details>
<summary>Process payroll add / amend </summary>

![Screenshot of flowchart - Process payroll add /amend ](/docs/images/flow_charts/process_payroll_add_amend.png)
</details>
<details>
<summary>Data relationship </summary>
![Screenshot of flowchart - Data relationship ](/docs/images/flow_charts/data_relationship.png)
</details>
<details>
<summary>Formulas and variables </summary>

![Screenshot of formulas ](/docs/images/flow_charts/formulas_variables.png)
</details> <br>

I have structured my program using functional programming, rather than OOP for this app. This is because, the data that is being inputted needs to be immutable and is based around having one user inputting data. 
There isn't a case for objects in my program as it is just interacting with the database where the data is stored. 

Having collaborated with both my mentor and tutor about the use of OOP for this application, they both advised it would not be required but instead a ‘nice to have’ 
___
## v. Surface <a name="surface"></a> 

### Visual Design

As this is a terminal based application the styling is very limited so I have focused/prioritised optimizing functionality, especially in providing the user feedback required at the correct points of the application, coupled with ease of navigation.

[Table of Contents ](#home)

---

# 2. Features <a name="features"></a> 

## i. Current Features (short term objectives): <a name="features-current"></a>
[Click on link to go to current features](https://github.com/ccarabine/payroll/blob/main/docs/features.md)

---
## ii. Features remaining to implement (long term objectives): <a name="features-toimplement"></a>
### Next update
- Add / amend employee details

### Future updates
- Statutory sick pay, maternity/paternity leave
- Bonuses
- Payroll for salary staff
- Account managemeent

[Table of Contents ](#home)

___
# 3. Testing <a name="testing"></a> 

## i. User stories testing  <a name="user-stories-testing"></a>

User stories are tested with the current features. All user stories passed the tests.

[Click on link to go to user stories testing ](https://github.com/ccarabine/payroll/blob/main/docs/testing.md)

---
## ii. Known issues during development and testing <a name="known-issues"></a>

[Click on link to go to issues that were identified and corrected during development and testing](https://github.com/ccarabine/payroll/blob/main/docs/known_issues.md)


---
## iii. Validation testing:<a name="validation-testing"></a>

### PEP8
<details>
<summary>Click here to view the results from PEP8 on run.py</summary>

![screenshot results from PEP8 on run.py](/docs/images/testing/validation/pep8_runpy.PNG)
</details>

<details>
<summary>Click here to view the results from PEP8 on menu.py</summary>

![screenshot results from PEP8 on run.py](/docs/images/testing/validation/pep8_menupy.PNG)
</details>

___
### Pylint

<details>
<summary>Click here to view the results from pylint on run.py</summary>

![screenshot results from pylint on run.py](/docs/images/testing/validation/pylint_runpy.png)
</details>

<details>
<summary>Click here to view the results from pylint on menu.py</summary>
![screenshot results from pylint on run.py](/docs/images/testing/validation/pylint_menupy.png)
</details><br>

Initial Errors
<details>
<summary>Click here to view the initial errors from pylint</summary>

![screenshot the initial errors from pylint](/docs/images/testing/validation/pylint_initial_validation_errors.jpg)
</details><br>

**Fixes to the initial errors above**

Standard imports errors -  moved the imports in the correct order as suggested by pylint

Variable name em, wk, fd changed to employee, week and fd_int

Unnecessary parens - removed them

Redefining data and password - changed to data_1 and password_1

___
**Other errors**

run.py:185:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements) <br>
added "return None" to the revelent expressions

run.py:442:0: R0914: Too many local variables (19/15) (too-many-locals)

changed the structure from a list to a dictionary and took the values straight out of the dictionary rather then assigning variables to them

___
**I have disabled the following false errors:**

pylint: disable=unused-import   import env  
'env' imported but unused
unused import env  **this is used to get the username and password**

pylint: disable=pointless-string-statement    Pylint states the imports docstring is pointless 
i have used a doc string to comment all of the imports for all modules for application

pylint: disable=no-else-return  Unnecessary "elif" after "return" 
used on function  yesorno(question):
    if answer == 'y': 
        return True
    elif answer == 'n':
        return False
    print('Invalid entry')
    return yesorno(question)

Needed to keep the elif in, so if the user typed "n" it would return False

---
## iv. Unfixed Bugs <a name="unfixed-bugs"></a> 

- On  Google Pixel 6 phone, chrome browser user can see their username and password when entering.


[Table of Contents ](#home)

---

# 4. Deployment <a name="deployment"></a> 

## Github

This is the process i took to deploy my project to the hosting platform GitHub
1.	Open Github page up in browser
2.	Log in using your username and password
3.	Select "ccarabine/payroll" from repositories displayed on left-hand side of screen
4.	Click "settings” displayed in the navigation toolbar menu
5.	Click “Pages” on the left hand side navigation menu
6.	Select "Master Branch" in the dropdown under the Source heading
7.	Finally, click “save”

 The live link can be found here 
 <a href="https://ccarabine.github.io/payroll/">People Payroll Application </a>

___
## Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at [heroku.com](https://.heroku.com/)
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data 
creds.json for example type `CREDS` in the
key field and the code in the value field.<br>
You must then create another called `PORT`. Set this to `8000`
6. For this project, I set buildpacks to `Python` and `NodeJS` in that order. Ensure python is on ontop
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click search, then connect
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
11. Click deploy branch
 <a href="https://people-payroll-application.herokuapp.com/">People Payroll Application </a>

### Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

___
## Google API

Here's how you can set up your own API:

1. Login or create a Google account and navigate to https://console.cloud.google.com/
2. Create a new Project by clicking on the New Project icon
3. Add Project name and details
4. Under API's and services, enable the relevant API for your project (in this case Google Drive and Sheets )
5. If the API requires, create a credential (service account in this case) for your project
6. Download the credential and upload it to your workspace a a json-file
7. Under API's and services, enable the relevant API for your project (in this case Google Drive and Sheets)

[Table of Contents ](#home)

---
# 5. Technologies Used <a name="technology-used"></a>  <a name="Home"></a>
## Languages

- [Python 3](https://www.python.org/) - Was used solely to create this project.

I have also utilised the following applications, platforms  and libraries:

* [GitPod](https://www.gitpod.io/) :  I used GitPod as the IDE for this project and Git has been used for Version Control.

* [GitHub](https://www.github.com/) : GitHub has been used to create a repository to host the project and receive updated commits from GitPod.

* [Heroku](https://id.heroku.com) : Used to deploy the application.

* [Google Cloud Platform](https://console.cloud.google.com/home/dashboard?project=payroll-326612) : Google Cloud Platform has been used for APIs and credentials to be able to access Google Sheets with the relevant data.

- [Google Sheets](https://docs.google.com/spreadsheets/u/0/): Spreadsheet to store the data for employees details and employee payroll 

- [PEP8 Online Validation Service](http://pep8online.com/): The PEP8 Online Validation Service was used to validate the Python document for this project and to identify any issues with the code.

* [Lucid Chart](https://www.lucidchart.com/): Lucid Chart was used to create flowcharts

___
## Python Libraries
A library is a collection of pre-combined codes that can be used iteratively to reduce the time required to code. They are particularly useful for accessing the pre-written frequently used codes, instead of writing them from scratch every single time. 

I have used these Python and third party libraries for this project for the following reasons:

- Getpass: getpass has been used to prompt the user for a username and password without showing the characters used in the password function.

- from datetime import date: date has been used to get the current week of the year used in the payroll_weeks function

- os: The OS module has ben used to provides functions for interacting with the operating system. Used for the clear function and to access the environment varaibles in the password function.

- system : System provides functions for interacting with the operating system, used in the clear function

- name: name has been used in the clear function. os module provides the operating system interface from Python

- sys: sys has been used in wait_key function

- termios: The termios module has been used to provide an interface the terminal control facilities used in wait_key function

___
## Third Party Libraries

- gspread:  gspread has been used to access, update and manipulate data from Google Sheets

- Pandas:  Pandas has been used to allow for the creation of Dataframes, importing data  and displaying data

- google.oauth2.service_account: google.oauth2.service_account has been used to allow the application to access the account that the sheet is on with the credentials

[Table of Contents ](#home)

___
# 6. Credits <a name="credits"></a>

## Code
I used the following websites and videos for inspiration and code for my project

[Yes/ no function](https://gist.github.com/garrettdreyfus/8153571)

[To check two lists for a value](https://learncodingfast.com/how-to-find-intersection-of-two-lists-in-python/)

[To get the week number using datetime](http://week-number.net/programming/week-number-in-python.html)

[Used for passwords](https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/)

[Delay printing before next function](https://www.codegrepper.com/code-examples/python/how+to+pause+after+a+print+statement+in+python)

[Clearing the terminal before next function](https://www.geeksforgeeks.org/clear-screen-python/)

[Use of gspread](https://docs.gspread.org/en/latest/user-guide.html)

[Using gspread-Finding and Updating Cells in google sheers](https://www.youtube.com/watch?v=yPQ2Gk33b1U)

[Using gspread to select a worksheet](https://docs.gspread.org/en/latest/user-guide.html#selecting-a-worksheet)

[Using pandas](https://kanoki.org/2020/01/21/pandas-dataframe-filter-with-multiple-conditions/)

[Stack over flow – to group by and sum values using pandas](https://stackoverflow.com/questions/43745301/converting-column-from-dataframe-to-float-for-sum-usage-python-pandas)

[Group by and sum using pandas](https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum)

[Summing in pandas](https://datagy.io/pandas-cumulative-sum/)

[National insurance calculation](https://www.gov.uk/national-insurance-rates-letters)

[Press any key](https://stackoverflow.com/questions/983354/how-to-make-a-script-wait-for-a-pressed-key)

[Table of Contents ](#home)

___
# 7. Acknowledgements <a name="acknowledgements"></a>
A big thank you to my mentor Mo for his help and guidance throughout my third project

Thank you to to the following:

* My wife for her help and constructive feedback throughout the project. 
* The tutors for help and support.
