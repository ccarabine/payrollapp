
## User stories testing  <a name="user-stories-testing"></a>

I have tested the site owner/user stories to ensure the MPV has been achieved.
___

### Testing of user story 1
*“As a user, I want additional security so other colleagues can’t access the application”*

**Covered by Feature 1: Welcome Message and security**

- **Action** - *User enters correct username and password*

- **Expected Result** - *Main menu is displayed”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](docs/images/testing/test_us1_1.PNG)
</details><br>

___

- **Action** - *User enters incorrect password*

- **Expected Result** - *Display ” Incorrect credentials, please try again.”*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image of date validation here</summary>

![User story 1, 2IMAGE  test-f1-2


</details>

___

- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ” Incorrect credentials, please try again”*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image of date validation here</summary>

![User story 1, 2IMAGE  test-f1-2

</details>

___


# Testing of user story 2

*“As a user, I want a terminal based application to import / exporting data form google sheets”*

**Covered by Feature 3: Display payroll & Feature 4: Process /Amend payroll**
Test 1

- **Action** - *From the main menu, type “2”, then “1” user prompted to Enter Payroll Week : type “25” , then type Employee number “100017”*, then Enter number of hours worked “25”

Note: Importing employee number to check that there is a record in google sheets to retrieve the employees rate of pay and pension %
Exporting all the calculated values to google sheet

- **Expected Result** -
Messaged displayed if the employee record is found against the employee number
Employment record located
Letting us know that the record has been exported 

- After the hours have been entered expecting the following message
employeepayroll worksheet updated successfully
to let use know the information has been imported to google sheets

- Would you like to process another employees hours? type y or n :
 
- **Actual Result** - *Works as intended*

Image Us2_1

___

### Testing of user story 3

*“As a user, I want to easily navigate through to the different functions to view and process payroll”*


**Covered by Feature 2: Menu system**
Main menu testing

Test 1
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ” Invalid data, please try again.” And prompts the user to enter again*

- **Actual Result** - *Works as intended*

Image Us3_1

___
Test 2
- **Action** - *User enters “0” or 5*

- **Expected Result** - *Display ” Invalid data, please try again.” And displays the main menu*

- **Actual Result** - *Works as intended*

Image Us3_2

___
Test 3
- **Action** - *User enters “1”*

- **Expected Result** - *Displays “Display Payroll” menu *

- **Actual Result** - *Works as intended*
Image Us3_3

___
Test 4
- **Action** - *User enters “2”*

- **Expected Result** - *Displays “Process / Amend” menu *

- **Actual Result** - *Works as intended*
Image Us3_4

___
Test 5
- **Action** - *User enters “3”*

- **Expected Result** - *Displays “Feature in next update, returning to main menu” 
“Press any key to clear the screen and return to the Main menu”*

- **Actual Result** - *Works as intended*
Image Us3_5

___

## Display Payroll menu testing<br>
Test 6
- **Action** - *User enters “1”*

- **Expected Result** - *user is prompted to enter payroll week *

- **Actual Result** - *Works as intended*
Image Us3_6

____

Test 7
- **Action** - *User enters “2”*

- **Expected Result** - *User is prompted Enter Payroll Week  :”*

- **Actual Result** - *Works as intended*
Image Us 3_7


___

Test 8
- **Action** - *User enters “3”*

- **Expected Result** - *summarised employers data is displayed by week, main menu is displayed*

- **Actual Result** - *Works as intended*
Image Us 3_8

___
Test 4
- **Action** - *User enters “4”*

- **Expected Result** - * main menu is displayed*

- **Actual Result** - *Works as intended*
Image Us 3_9

___
Test 5
- **Action** - *User enters “0” or 5*

- **Expected Result** - *Display ” Invalid data, please try again.” And displays the main menu*

- **Actual Result** - *Works as intended*
Image Us 3_10

___
Test 6
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ” Invalid data, please try again.” And displays the main menu*

- **Actual Result** - *Works as intended*

Image Us 3_11
___

##  Process / Amend Payroll menu testing
Test 1
- **Action** - *User enters “1”*

- **Expected Result** - *User is prompted to enter employee number ”*
- **Actual Result** - *Works as intended*
Image Us 3_12

___
Test 2

- **Action** - *User enters “2”*

- **Expected Result** - *User is prompted to enter employee number ”*

- **Actual Result** - *Works as intended*
___ Image Us 3-13
___
Test 3
- **Action** - *User enters “3”*

- **Expected Result** - *displays main menu*
- **Actual Result** - *Works as intended*
______ Image Us 3_14
___


Test 4
- **Action** - *User enters “0” or 4*

- **Expected Result** - *Display ” Invalid data, please try again.” And displays the main menu*

- **Actual Result** - *Works as intended*
___ Image Us 3_15

___
Test 5
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ” Invalid data, please try again.” And displays the main menu*

- **Actual Result** - *Works as intended*

___ Image Us 3_16

___


### Testing of user story 4

*“As a user, I want to process employees hours and get feedback if i have entered them already”*

**Covered by Feature  4: Process /Amend payroll**
Test 1

- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100017

Employees hours already entered in wk26, please go to option 2 to amend

# - **Expected Result** - 

- **Actual Result** - *Works as intended*
___ Image Us 4_1

___

Test 2

- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015
- **Expected Result** - 
No entry found in payroll
Enter number of hours worked :

- **Actual Result** - *Works as intended*
Image Us 4_2
___ 


## Testing of user story 5

*“As a user, I want an application that calculates	Basic pay, holiday pay, Employee NI contributions, Pension Contributions, Net pay, Employer NI contributions, Pension Contributions"*<br>
**Covered by Feature  4: Process /Amend payroll**

Test 1
- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015, enter number of hours worked “25”
- **Expected Result** - 
Employee : 100015 - Hadley Light
 Basic Pay : £525.0
 Holiday Pay : £63.42
 NI contribution: £48.53
 Pension contribution: £17.65
 Net Pay: £522.24
- **Actual Result** - *Works as intended*

___ Image Us 5-1
___ Image Us 5-2

___

## Testing of user story 6
*"As a user, I want to be able to view an employees figures before I submit them to the payroll(send to google sheets spreadsheet)"
**Covered by Feature  4: Process /Amend payroll**
- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015, enter number of hours worked “25”
- **Expected Result** - 
Employee : 100015 - Hadley Light
 Basic Pay : £525.0
 Holiday Pay : £63.42
 NI contribution: £48.53
 Pension contribution: £17.65
 Net Pay: £522.24
- **Actual Result** - *Works as intended*
___ Image Us 6-1

___
Test
- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015, enter number of hours worked “25”, are the amount correct? “n”
- **Expected Result** - 
Re enter details 

Enter number of hours worked : 

- **Actual Result** - *Works as intended*
___ Image Us 6-2

___
## Testing of user story 7
*"As a user, I want to be able to view all employees figures for any week"*
**Covered by Feature 3: Display payroll”

- **Action** - *From the main menu, type “1”, then “1”, user prompted to Enter Payroll Week : type “25”
- **Expected Result** - 
records displayed
- **Actual Result** - *Works as intended*

___ Image Us 7-1

___
Test
- **Action** - *From the main menu, type “1”, then “1”, user prompted to Enter Payroll Week : type “2”  *** no records

- **Expected Result** - 
Invalid week number, please try again.

- **Actual Result** - *Works as intended*

___ Image Us 7-2

___

## Testing of user story 8
*"As a user, I want to be able to view an employee figures for a week and be able to amend them"*<br>
**Covered by Feature 3: Display payroll”**
**Covered by Feature  4: Process /Amend payroll**
- **Action to view the record** - *From the main menu, type “1”, then “2” user prompted to Enter Payroll Week : type “25”, then type Employee number “100017”*, 

- **Expected Result** - 
Record displayed

- **Actual Result** - *Works as intended*

___ Image Us 8_1
- **Action to amend the record** - *From the main menu, type “2”, then “2” type Employee number “100017”*, enter number of hours worked “25”

- **Expected Result** - 
Employee : 100017 - Stobbs Harriet
 Basic Pay : £350.0
 Holiday Pay : £42.28
 NI contribution: £24.99
 Pension contribution: £11.77
 Net Pay: £355.52
Are the amounts correct?
- **Actual Result** - *Works as intended*
___ Image Us 8_2


## Testing of user story 9
"As a user, I want to be able to view all employers figures summarised and grouped by week"*<br> 
**Covered by Feature 3: Display payroll**

- **Action** - *From the main menu, type “1”, then “1”, user prompted to Enter Payroll Week :26  

- **Expected Result** - 

Records displayed

- **Actual Result** - *Works as intended*
___ Image Us 8_2

___
## Testing of user story 10
As a user I want to be able to add/amend employee details
Future feature

## Site owner stories testing  <a name="user-stories-testing"></a>


11. I want a terminal based application which allows the user to navigate the system intuitively without returning errors
**Covered by Feature 1: Welcome Message and security, Feature 2: Menu system, Feature 3: Display payroll & Feature 4: Process /Amend payroll**



Welcome and security features  us11_1

Testing as above
