
## User stories testing  <a name="user-stories-testing"></a>

[Click to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md)

I have tested the user/site owner stories to ensure the MPV has been achieved.
___

## Testing of user story 1
*“As a user, I want additional security so other colleagues can’t access the application”*

**Covered by Feature 1: Welcome Message and security**

___
Test 1
- **Action** - *User enters correct username and password*

- **Expected Result** - *Main menu is displayed*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us1_1.PNG)
</details><br>

___
Test 2
- **Action** - *User enters incorrect password*

- **Expected Result** - *Display ”Incorrect credentials, please try again.”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us1_2.PNG)
</details><br>

___
Test 3
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ”Incorrect credentials, please try again”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us1_2.PNG)
</details><br>

___


## Testing of user story 2

*“As a user, I want a terminal based application to import / exporting data form google sheets”*

**Covered by Feature 3: Display payroll & Feature 4: Process /Amend payroll**

___
Test 1

- **Action** - *From the main menu, type “2”, then “1”, user prompted to Enter Payroll Week : type “25” , then type Employee number “100017”, then Enter number of hours worked “25”*

Note: Importing employee number to check that there is a record in google sheets to retrieve the employees rate of pay and pension %<br>
Exporting all the calculated values to google sheet

- **Expected Result** -
Message displayed if the employee record is found against the employee number<br>
"Employment record located"<br>
Letting us know that the record has been exported 

    After the hours have been entered, the following message displayed <br>

    "employeepayroll worksheet updated successfully" <br>to let use know the information has been imported to google sheets

    "Would you like to process another employees hours? type y or n :"
 
- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us2_1.PNG)
</details><br>

<details>
    <summary>Click here to view result- Google sheet updated</summary>

![Screenshot of result](//docs/images/testing/userstory2test1.png)
</details><br>


___

## Testing of user story 3

*“As a user, I want to easily navigate through to the different functions to view and process payroll”*


**Covered by Feature 2: Menu system**

___
## Main menu testing

Test 1
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ” Invalid data, please try again.” And prompts the user to enter again*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_1.PNG)
</details><br>

___
Test 2
- **Action** - *User enters “0” or 5*

- **Expected Result** - *Display ” Invalid data, please try again.” And displays the main menu*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_2.PNG)
</details><br>

___
Test 3
- **Action** - *User enters “1”*

- **Expected Result** - *Displays “Display Payroll” menu*

- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_3.PNG)
</details><br>

___
Test 4
- **Action** - *User enters “2”*

- **Expected Result** - *Displays “Process / Amend” menu *

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_4.PNG)
</details><br>

___

Test 5
- **Action** - *User enters “3”*

- **Expected Result** - *Displays “Feature in next update, returning to main menu” 
“Press any key to clear the screen and return to the Main menu”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_5.PNG)
</details><br>

___

## Display Payroll menu testing<br>
Test 6
- **Action** - *User enters “1”*

- **Expected Result** - *user is prompted to enter payroll week *

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_6.PNG)
</details><br>

____

Test 7
- **Action** - *User enters “2”*

- **Expected Result** - *User is prompted Enter Payroll Week  :”*

- **Actual Result** - *Works as intended*
Image Us 3_7
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_7.PNG)
</details><br>


___

Test 8
- **Action** - *User enters “3”*

- **Expected Result** - *summarised employers data is displayed by week*

- **Actual Result** - *Works as intended*
Image Us 3_8
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_8.PNG)
</details><br>

___
Test 9
- **Action** - *User enters “4”*

- **Expected Result** - *main menu is displayed*

- **Actual Result** - *Works as intended*
Image Us 3_9
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_9.PNG)
</details><br>

___
Test 10
- **Action** - *User enters “0” or 5*

- **Expected Result** - *Display ”Invalid data, please try again.”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_10.PNG)
</details><br>

___
Test 11
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ” Invalid data, please try again.”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_11.PNG)
</details><br>

___

##  Process / Amend Payroll menu testing
Test 12
- **Action** - *User enters “1”*

- **Expected Result** - *User is prompted to enter employee number ”*
- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_12.PNG)
</details><br>

___
Test 13

- **Action** - *User enters “2”*

- **Expected Result** - *User is prompted to enter employee number ”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_13.PNG)
</details><br>

___
Test 14
- **Action** - *User enters “3”*

- **Expected Result** - *Displays main menu*
- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_14.PNG)
</details><br>

___

Test 15
- **Action** - *User enters “0” or 4*

- **Expected Result** - *Display ” Invalid data, please try again.”*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_15.PNG)
</details><br>

___
Test 16
- **Action** - *User enters a string of numbers and letters*

- **Expected Result** - *Display ”Invalid data, please try again.”*

- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us3_16.PNG)
</details><br>

___

## Testing of user story 4

*“As a user, I want to process employees hours and get feedback if i have entered them already”*

**Covered by Feature  4: Process /Amend payroll**

___
Test 1

- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100017*

- **Expected Result** -
*Employees hours already entered in wk26, please go to option 2 to amend*

- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us4_1.PNG)
</details><br>

___

Test 2

- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015*
- **Expected Result** - 
*No entry found in payroll

    Enter number of hours worked :*

- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us4_2.PNG)
</details><br>

___ 

## Testing of user story 5

*“As a user, I want an application that calculates	Basic pay, holiday pay, Employee NI contributions, Pension Contributions, Net pay, Employer NI contributions, Pension Contributions"*<br>
**Covered by Feature  4: Process /Amend payroll**

___
Test 1
- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015, enter number of hours worked “25”
- **Expected Result** - <br>
Employee : 100015 - Hadley Light<br>
 Basic Pay : £525.0<br>
 Holiday Pay : £63.42<br>
 NI contribution: £48.53<br>
 Pension contribution: £17.65<br>
 Net Pay: £522.24<br>
- **Actual Result** - *Works as intended*
<details>
    <summary>Click here to view result</summary>

![Screenshot of result](//docs/images/testing/test_us5_1.PNG)
</details><br>

<details>
    <summary>Click here to view result in Google Sheets</summary>

![Screenshot of result](//docs/images/testing/test_us5_2.PNG)
</details><br>

___

## Testing of user story 6
*"As a user, I want to be able to view an employees figures before I submit them to the payroll(send to google sheets spreadsheet)"<br>

**Covered by Feature  4: Process /Amend payroll**
___
Test 1
- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015, enter number of hours worked “25”*
- **Expected Result** - <br>
*Employee : 100015 - Hadley Light<br>
 Basic Pay : £525.0<br>
 Holiday Pay : £63.42<br>
 NI contribution: £48.53<br>
 Pension contribution: £17.65<br>
 Net Pay: £522.24*<br>
- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us6_1.PNG)
</details><br>

___
Test 2
- **Action** - *From the main menu, type “2”, then “1” user prompted to type Employee number “100015, enter number of hours worked “25”, are the amount correct? “n”
- **Expected Result** - 
    *Re enter details* 

    *Enter number of hours worked :* 

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us6_2.PNG)
</details><br>

___
## Testing of user story 7
*"As a user, I want to be able to view all employees figures for any week"*

**Covered by Feature 3: Display payroll**
___
Test 1
- **Action** - *From the main menu, type “1”, then “1”, user prompted to Enter Payroll Week : type “26”*
- **Expected Result** - 
*Records displayed*
- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us7_1.PNG)
</details><br>

___
Test 2
- **Action** - *From the main menu, type “1”, then “1”, user prompted to Enter Payroll Week : type “2”  *** no records

- **Expected Result** - 
Invalid week number, please try again.

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us7_2.PNG)
</details><br>

___

## Testing of user story 8
*"As a user, I want to be able to view an employee figures for a week and be able to amend them"*<br>
**Covered by Feature 3: Display payroll”**<br>
**Covered by Feature  4: Process /Amend payroll**

___
Test 1
- **Action to view the record** - *From the main menu, type “1”, then “2” user prompted to Enter Payroll Week : type “26”, then type Employee number “100015”*, 

- **Expected Result** - 
*Record displayed*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us8_1.PNG)
</details><br>


- **Action to amend the record** - *From the main menu, type “2”, then “2” type Employee number “100015”*, enter number of hours worked “27”

- **Expected Result** - 
*Employee : 100015 - Hadley Light<br>
 Basic Pay : £567.0<br>
 Holiday Pay : £68.49<br>
 NI contribution: £54.18<br>
 Pension contribution: £19.06<br>
 Net Pay: £562.25<br>
Are the amounts correct?<br>*
- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us8_2.PNG)
</details><br>

___
## Testing of user story 9<br>
*"As a user, I want to be able to view all employers figures summarised and grouped by week"*<br> 

**Covered by Feature 3: Display payroll**

___

- **Action** - *From the main menu, type “1”, then “1”, user prompted to Enter Payroll Week :26*

- **Expected Result** - *Records displayed*

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us9_1.PNG)
</details><br>

___
## Testing of user story 10
*"As a user I want to be able to add/amend employee details"*<br>

___

Future feature<br>

___
## Site owner stories testing  <a name="user-stories-testing"></a>
___
## Testing of user story 11
**"I want a terminal based application which allows the user to navigate the system intuitively without returning errors"**<br>

**Covered by Feature 1: Welcome Message and security, <br>
Feature 2: Menu system <br>
Feature 3: Display payroll<br>
Feature 4: Process /Amend payroll <br>**

___

- **Action** - On load, the application welcomes the user and prompted for a password

- **Expected Result** - Displays Welcome

- **Actual Result** - *Works as intended*

<details>
    <summary>Click here to view result </summary>

![Screenshot of result](//docs/images/testing/test_us11_1.PNG)
</details><br>

All testing above covers this user story

[Click to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md)