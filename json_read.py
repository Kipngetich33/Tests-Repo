import json
 
input = '''
{
    "FirstName":"Bhairav",
    "MiddleName":"S",
    "LastName":"Ram",
    "DateOfBirth":"09-01-1984",
    "Contact":{
        "Phone":9988776655,
        "Email":"bhairav@gmail.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":560056,
            "Street":"Nagarbhavi Road",
            "City":"Bangalore",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":560004,
            "Street":"Gandhi Bazaar Road",
            "City":"Bangalore",
            "Country":"India"
        }
    ]
}
        '''

# the code below is meant for different manipulation of the json data
# *********************************************************************************************************

#print the type of data type of the input above , the input in this case is a string
# print(type(input))

# the code below converts the json string into a dictionary
jsonObjectInfo = json.loads(input)

# prints the data type of the jsonObjectInfo
print(type(jsonObjectInfo))

# prints out the varibale on the terminal
# print(jsonObjectInfo)

# accessing the different items with the json dictionary
# print("First Name is {0}".format(jsonObjectInfo['FirstName']))
# print("Middle Name is {0}".format(jsonObjectInfo['MiddleName']))
# print("Last Name is {0}".format(jsonObjectInfo['LastName']))
# print("Date of Birth is {0}".format(jsonObjectInfo['DateOfBirth']))
# print("Phone Number is {0}".format(jsonObjectInfo['Contact']['Phone']))
# print("Email ID is is {0}".format(jsonObjectInfo['Contact']['Email']))
# print("-----------------**************---------------")

# looping throough a list containing json dictionary items
# for eachJsonObject in jsonObjectInfo['Address']:
#     print("Address Type is {0}".format(eachJsonObject['Type']))
#     print("Zip Number is {0}".format(eachJsonObject['ZipNumber']))
#     print("Street Name is {0}".format(eachJsonObject['Street']))
#     print("City Name is {0}".format(eachJsonObject['City']))
#     print("Country Name is {0}".format(eachJsonObject['Country']))
#     print("-----------------**************---------------")
 
 
# Reading JSON data back from a file called JSONData.json
#Use the method json.load()
#It's just load and not loads()
#Decode JSON Data
# with open('JSONData.json', 'r') as f:
#      data = json.load(f)
 
# print(data)





# the code below runs all the code above 
# ********************************************************************************************************************
# if __name__ == '__main__':
#     main()