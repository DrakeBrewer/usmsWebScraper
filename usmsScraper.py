# USMS Registration Number Scraper
# imports
from urllib.request import urlopen
from datetime import date

import json
import sys


# counts the number of arguments
n = len(sys.argv)

# parent list for final output
parentList = []

# argument count *Uncomment for debugging*
# print('argument count: ', n)

# name count *Uncomment for debugging*
# print('name count: ', int((n - 1) / 2))

# program name *Uncomment for debugging*
# print("Program name ", sys.argv[0])

# loading...
print('Retreiving Registration Numbers . . .\n')

# main loop
for i in range(1, n, 2):

# Argument variables
    try:
        firstNameArg = sys.argv[i].strip()
        lastNameArg = sys.argv[i+1].strip()
        yearArg = str(date.today().year)
    except IndexError:
        print("Oops, You have a misinput! check your inputs and try again.")

# JSON url boilerplate
    url = "https://www.usms.org/reg/members/jqs/searchmembers.php?RegYear={year}&FirstName={firstName}&LastName={lastName}&oper=grid&_search=false&nd=1643355539541&rows=200&page=1&sidx=BinaryLastName%20asc%2C%20FirstName%20asc%2C%20RegDate&sord=asc&totalrows=-1".format(year = yearArg, firstName = firstNameArg, lastName = lastNameArg)

# store the response of URL
    response = urlopen(url)

# list of registration numbers
    regNumList = []

# storing the JSON response from url in data
    data_json = json.loads(response.read())

# print the json response
    for r in data_json['rows']:
        regNumList.append(r['RegNumber'])

# append registration numbers to parent list
    parentList.append(regNumList)

# print statements

    # first and last name *Uncomment for debugging*
    # print("First Name: ", sys.argv[i].strip(), " Last Name: ", sys.argv[i+1].strip())

    # registration number array *Uncomment for debugging*
    # print(regNumList)

    # print('\n')

# Final output list
print(parentList)




# Drake Brewer - 2022