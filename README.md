# usmsWebScraper

Uses:
This web scraper can be used to scrape the website https://www.usms.org/reg/members to find if the inputted name(s) have a registration number linked to them using JSON parsing. Inputs that return no value will return an empty list.


Input syntax:
python programName “firstName” “LastName” “firstName” “LastName” “firstName” “LastName”. . .


Special Cases:
If the name member in question has multiple first names or last names (i.e. De La Cruz, Mary Jane) the parameters are to be kept the same, first name in one set of quotations and last name in a second set of quotations. Ex: “Mary Jane” “De La Cruz”.


Functionality:
This web scraper functions by using primarily the urllib.request and json modules for python. The urllib.request module allows a program to open and read URLs (https://docs.python.org/3/library/urllib.request.html#module-urllib.request). The json module allows a program to store and read JSON strings (https://docs.python.org/3/library/json.html?highlight=json#module-json). When the program is given member names via the inputs provided by the user, it will inject the string value of the inputs into the URL of the searchmembers.php fetch request into the keys FirstName and LastName respectively. The contents of the resulting URL include an object of the search's return values in JSON format. The program will then parse through this JSON retrieving the values of the RegNumber key.


JSON URL Example:
The boilerplate for this URL can be found in the url variable.
https://www.usms.org/reg/members/jqs/searchmembers.php?RegYear=2022&FirstName=Jim&LastName=Teisher&oper=grid&_search=false&nd=1647295293780&rows=200&page=1&sidx=BinaryLastName%20asc%2C%20FirstName%20asc%2C%20RegDate&sord=asc&totalrows=-1


JSON String Example:
{"records":"1","page":1,"total":1,"rows":[{"FirstName":"Jim","MI":null,"LastName":"Teisher","LMSCAbbr":"OR","ClubAbbr":"OREG","WOGroupAbbr":"THB","RegNumber":"372T-025UE","RegDate":"2021-11-02","WOGroupID":"1104","ClubID":"372-001","LMSCID":"37","BinaryLastName":"TEISHER"}]}



Errors:
There are recorded cases that are guaranteed to throw errors if the criteria is met, these include:
Not including a last name. There must be a first and last name for each member.
Not including space between each argument.


Testing/Troubleshooting Comments:
I have left a few lines of commented code that will function as print tests to ensure that aspects of the program are working as intended, if needed.
Line 17: Prints the number of arguments the user has inputted.
Line 20: Prints the number of full names (first and last) the user has inputted.
Line 23: Prints the name of the program.
Line 57: Prints the first and last name for each user entered, this functions in tandem with the next comment.
Line 60: Prints all returned registration numbers for the name referenced on line 57.


Difference in Year:
It was brought up that at certain times a year, the website allows for you to change the year in question by increments of 1 (i.e. 2021 and 2022) as of now the program does not have the ability to take a user input to change this value in the JSON string, however the value is currently set to the value of whatever the current year is using Python's datetime module. This value can be found on line 34, contained in the yearArg variable.


Helpful Links:
JSON documentation - https://www.json.org/json-en.html
json python module documentation - https://docs.python.org/3/library/json.html?highlight=json#module-json

urllib python module documentation - https://docs.python.org/3/library/urllib.html


Drake Brewer - 2022
