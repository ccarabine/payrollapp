## Known issues during development and testing <a name="known-issues"></a>

[Click here to go to the Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md#known-issues)

### During development, the following issues were identified and corrected

 - **Issue:** 
 
    *When I selected 'display payroll' option 2, to display employee payment details, i entered an employee number that wasn't found in google sheets, an index error occurred*

-	**Corrective Action:** 

    *Added an except indexerror and error message "No record found"*
___
- **Issue:** 

    *When I selected option 1, option1 "Overall employees' pay for week selected".  I then input a week with no data, this displayed an error message as it only allows the previous week to be entered*

- **Corrective Action:** 

    *Put in a “status” for the week with “normal” and “any week” for this function, the status would be “any week”*

-   **I have further removed this code so they display any week**
___
- **Issue:** 

    *Add employees hours, it would only allow the user to enter the  current week payroll when the payroll needs to be the previous week*

- **Corrective Action:** 

    *Add in function previous_week = current week -1*
___
- **Issue:** 

    *On the main menu screen, the user could type in “4 “*

- **Corrective Action:** 

    *Change maxvalue to 3*
___
- **Issue:** 

    *The result of the employee's pension contribution was incorrect as it was calculating only the basic pay  * pension % when it needs to be based on basic plus holiday pay * pension %*

- **Corrective Action:** 

    *Changed from employee basic pay to employee_basic_hol ( basic plus holiday)*
___
- **Issue:** 

    *To display employees' payroll records, the function used getallvalues.  There were multiple employees' with e.g."25" hours and I wanted to display all records for the week "25", the data displayed all the employees' hours as well as matching week 25*

- **Corrective Action:** 

    *Get payroll week function, I added concatenate so the week is "wk34" rather than just 34 so now we can getallvalues "wk34"*
___
- **Issue:** 

    *User entered a letter when entering the payroll week, an error occurred*

- **Corrective Action:** 

    *Added an if, else statement to handle, with an error message*
___

- **Issue:**

    *The user entered a payroll week that wasn’t in the payroll spreadsheet a keyerror occurred*

- **Corrective Action:** 

    *Added except keyError  and error message*
___

- **Issue:** 

    *Display Employee payroll for week, the data frame was empty then it displayed an empty dataframe*

- **Corrective Action:** 

    *Created an if statement to handle if the dataframe is empty, display error message and if it has data to display*

___

- **Issue:** 

    *When selecting option 3, Employers summary for week selected, this message is displayed*

    *run.py:510: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.*

- **Corrective action**

    [Warning indexing with multiple keys](https://stackoverflow.com/questions/60999753/pandas-future-warning-indexing-with-multiple-keys)

    Add brackets around DF selection
___

- **Issue:** 

    *To add/amend employees hours, The user had to enter the week ( which could only be the previous week)*

- **Corrective action:**

    *No user input required just added code to put the previous week into the variable payroll_week as it will always be the previous week*

___

### During testing, the following issues were identified and corrected

- **Issue:** 

    *Display records in display menu options 1,2 and 3 would only show a limited amount of fields due to the constraints of the deployment terminal, which is set to 80 characters*

- **Corrective action:**

    *Reduced the descriptions of* 

    *- Employee NI & Employee Pension to EE NI & EE Pension*

    *- Employer NI & Employer Pension to Er NI & Er Pension*

    *- Holiday pay to Hol pay*

    *- Reduced the number of fields in the reports*

___

- **Issue:** 

    *When I entered a string  for ‘enter number of hours worked’ it returned a value error – ‘could not convert string to float’*

- **Corrective action:**

    *I added a ValueError statement to catch the error and provide feedback to the user that the input is invalid and  ask the user to re-enter the hours again*
 
___
 
- **Issue:** 

    *Whilst further testing after implementing the corrective action above, I found an additional error, if the user typed a string twice for the hours entered, the error would occur again*

- **Corrective action:**

    *I changed the code so if the user enters a string instead of a float then it will provide feedback to let the user know the input is invalid and call ‘get_employee_num’ until ‘validate_employee_num’ is true, it will then return the employees hours.*

    *I also noticed that the ‘Update_worksheet’  function was running after the ‘if true’ statement due to the indent being incorrect.  I moved the line so it runs inside the function*

___

- **Issue:** 

    *When displaying the reports, I noticed the data was not accurate due to the dataframe loading at the start of the code, resulting in inaccurate data when the user requested the report.*

- **Corrective action:**

    *I called the dataframe at the start of each function call when displaying data*

___

- **Issue:** 

    *When amending the employee’s hours. I typed an incorrect employee number that was 6 characters, it displayed an error message and asked me to enter  “y” or “n” to re-enter the employee's number.*

    *When I typed “y”, it prompted me to re-enter the employee's number, I typed the correct employee's number and an error occurred - it asked me to enter the employee number again instead of asking me to enter in the hours worked. After the second time of entering the employee's number, it moved on to request the hours worked*

- **Corrective action:**

    *1.	Removed calling the ‘get_employee_num’ from validate employee function*

    *2.	I changed the code so, if the answer is true, return none, it will request the employee number at the correct point of the code*

    ___

- **Issue:** 

    *run.py:490:0: R0914: Too many local variables (16/15) (too-many-locals) in calculate_employee_payslip_data function*

    
- **Corrective action:**

    *Deleted employee_basic_hol variable* 
    *and put (employee_basic_pay + employee_holiday) where it was referenced in the formulas*

     ___

- **Issue:** 

    *The list of Variables doesn't conform to the snake_case naming style*

    
- **Corrective action:**

    *Created a .pylintrc file and added variables*

   ___

- **Issue:** 

    *When the API fails, error messages would display and close the app*

    
- **Corrective action:**

    *Put the gspread_client, sheet and worksheets into a function together with a try and except statement to catch API fails.*
    
    *To catch API errors where functions were calling the spreadsheet I put in further try and except statements to catch Name or Index Errors*

[Click here to go to Readme file ](https://github.com/ccarabine/payroll/blob/main/README.md#known-issues)