"""
created: 8 December, 2022
author: Frank Saunders Jr
description: This script calculates the score spread for each Institution and
lists the minimum and maximum.
"""

import sqlite3

#Connect to PGR database
connection = sqlite3.connect('pgr-db-2.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

#Create table for institution spread
create_table = ''' DROP TABLE IF EXISTS Spread; CREATE TABLE Spread(
"institution_id" INTEGER PRIMARY KEY,
"max_mean" NUMERIC,
"min_mean" NUMERIC,
"spread" NUMERIC)
'''
cursor.executescript(create_table)

#SQL variables for min and max mean acquisition and insertion
get_max_mean = '''SELECT MAX(mean) FROM Overall WHERE institution_id = ? '''
get_min_mean = '''SELECT MIN(mean) FROM Overall WHERE institution_id = ? '''
insert_spread = "INSERT OR IGNORE INTO Spread (institution_id, max_mean, min_mean, spread) VALUES ( ?, ?, ?, ? )"

#Identify all institution IDs and put them in a list
cursor.execute("SELECT institution_id FROM Overall")
inst_id_tups = cursor.fetchall()

#convert institution ID tuples into integers w/o dupilcates
inst_id_list = []
for item in inst_id_tups:
    if item[0] not in inst_id_list:
        inst_id_list.append(item[0])
        
print(inst_id_list)

#List min, max, and difference btwn mean values for a particular institution_id
for item in inst_id_list:
    cursor.execute(get_max_mean, ( item, ))
    max_mean = cursor.fetchone()[0]
    cursor.execute(get_min_mean, ( item, ))
    min_mean = cursor.fetchone()[0]
    diff = max_mean - min_mean
    print("Institution ID", item, "Max", max_mean, "Min", min_mean, "Difference", round(diff, 2))
#Add the values to the Spread table
    cursor.execute(insert_spread, ( item, max_mean, min_mean, round(diff, 2) ) )

    
connection.commit()

result = cursor.execute('''SELECT * FROM Spread LIMIT 10''')
print(result.fetchall())


#For loop to iterate through each institution id
#for row in range(inst_max - 1):
#    mean_list
    
