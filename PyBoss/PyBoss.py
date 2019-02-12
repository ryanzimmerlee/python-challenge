# # PyBoss

# In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, 
# a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. 
#The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee 
# records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required 
# format. Your script will need to do the following:

# * Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:

# ```csv
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# ```

# * Then convert and export the data to use the following format instead:

# ```csv
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# ```

# * In summary, the required conversions are as follows:

#   * The `Name` column should be split into separate `First Name` and `Last Name` columns.
#   * The `DOB` data should be re-written into `MM/DD/YYYY` format.
#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.
#   * The `State` data should be re-written as simple two-letter abbreviations.

# * Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).

import csv
import datetime

# Create dynamic list
empData = []

# Define CSV path on local harddrive
csvPath = (r"C:\Users\ryanz\Desktop\Data Analytics Bootcamp\Resources\RICH201901DATA3\03-Python\Homework\ExtraContent\Instructions\PyBoss\employee_data.csv")

# Open CSV file, identify each new line with blank space at the end
with open(csvPath, newline='') as csvfile:
    
    # Define separators for each data value
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Give my data list a header and append it to the top of my list
    csv_header = next(csvreader)
    empData.append(csv_header)
    
    # for every single iteration (row) in the csv, append it to my new list
    for row in csvreader:
        empData.append(row)

# Test my list
# print(empData)
        
# # Create a list of state abbreviations based off the key value
state_abb = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# remove the Name element from the Employee data list and
# insert a First Name and Last Name Element
empData[0].remove("Name")
empData[0].insert(1, "First Name")
empData[0].insert(2, "Last Name")

# Test
# print(empData)

# Create the state abbreviation dictionary
state_list = [state_abb[x[4]] for x in empData[1:]]
# print(state_list)

# Split the name by finding the space in between of the full name 
name_list = [x[1].split(" ") for x in empData[1:]]
# print(name_list)

# Create dates with the appropriate format
#   * The `DOB` data should be re-written into `MM/DD/YYYY` format.
date_list = [(datetime.datetime.strptime(x[2], '%Y-%m-%d')).strftime('%m/%d/%Y') for x in empData[1:]] 
# print(date_list)

# # Create a list of lists where the SSN is split at "-"
ssn_list = [x[3].split("-") for x in empData[1:]]

# # remove the old indexes for every row in the empData list
# except for the header row
for row in empData[1:]:
    row.remove(row[1])
    row.remove(row[1])
    row.remove(row[1])
    row.remove(row[1])
    
# Create a counter to be used in iterating through all of the lists created...don't grab the header row...insert new list elements
#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.
counter = 0    
for row in empData[1:]:
    row.insert(1, name_list[counter][0])
    row.insert(2, name_list[counter][1])
    row.insert(3, date_list[counter])
    row.insert(4, "***-***-" + str(ssn_list[counter][2]))
    row.insert(5, state_list[counter])
    counter += 1

print("")
for row in empData:
    print(", ".join(row))
    
txt = open("EmployeeData.txt", "a")

for row in empData:
    txt.write(", ".join(row))
    txt.write("\n")
txt.close()

    