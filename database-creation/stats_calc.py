"""
created: 8 December, 2022
author: Frank Saunders Jr
description: This script calculates some basic statistics for each Institution including the 
minimim and maximum mean score, the range of mean scores, the weighted average of all mean scores,
the weighted varaince, and the weighted standard deviation.
"""

import sqlite3
import math

#Functions for calculating the weighted mean and weighted standard deviation.

def get_wmean(vals, weight):
    weighted_vals = []
    for tup in vals_n_weight:
        weighted_vals.append(tup[0]*tup[1]/sum(weight))    
    answer = round(sum(weighted_vals), 3)
    return answer


def get_var(vals, weight):
    numerator = []
    for i in range(0, len(weight)):
        numerator.append(weight[i]*(vals[i]-get_wmean(vals, weight))**2)
    if len(weight) > 1:
        var = sum(numerator)/(((len(weight)-1)*sum(weight))/len(weight))
    else:
        var = 0
    return round(var, 3)

def get_wstd(vals, weight):
    wstdev = round(math.sqrt(get_var(vals, weight)), 3)
    return wstdev

#Connect to PGR database
connection = sqlite3.connect('pgr-db-2.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

#Create table for institution stats
create_table = ''' DROP TABLE IF EXISTS stats; CREATE TABLE stats(
"institution_id" INTEGER PRIMARY KEY,
"max_mean" NUMERIC,
"min_mean" NUMERIC,
"mean_range" NUMERIC,
"weighted_mean" NUMERIC,
"weighted_var" NUMERIC,
"weighted_stdev" NUMERIC)
'''
cursor.executescript(create_table)

#SQL variables for min, max, and all mean acquisition and insertion
get_max_mean = '''SELECT MAX(mean) FROM Overall WHERE institution_id = ? '''
get_min_mean = '''SELECT MIN(mean) FROM Overall WHERE institution_id = ? '''
get_means = '''SELECT mean FROM Overall WHERE institution_id = ? '''
get_evalnos = '''SELECT num_of_evals FROM Overall WHERE institution_id = ? '''
insert_stats = "INSERT OR IGNORE INTO stats (institution_id, max_mean, min_mean, mean_range, weighted_mean, weighted_var, weighted_stdev) VALUES ( ?, ?, ?, ?, ?, ?, ? )"

#Identify all institution IDs and put them in a list
cursor.execute("SELECT institution_id FROM Overall")
inst_id_tups = cursor.fetchall()

#convert institution ID tuples into integers w/o dupilcates
inst_id_list = []
for item in inst_id_tups:
    if item[0] not in inst_id_list:
        inst_id_list.append(item[0])
        
print(inst_id_tups)

for item in inst_id_list:
# List min, max, and difference btwn mean values for a particular institution_id
    cursor.execute(get_max_mean, ( item, ))
    max_mean = cursor.fetchone()[0]
    cursor.execute(get_min_mean, ( item, ))
    min_mean = cursor.fetchone()[0]
    diff = max_mean - min_mean
# Get all means for a particular institution
    cursor.execute(get_means, ( item, ))
    means_tups = cursor.fetchall()
    means = []
    for mean in means_tups:
        means.append(mean[0])
        print(means)
#Get evaluator numbers for a particular institution
    cursor.execute(get_evalnos, ( item, ))
    evalnos_tups = cursor.fetchall()
    evalnos = []
    for evalno in evalnos_tups:
        evalnos.append(evalno[0])
        print(evalnos)
#Turn means and evaluator numbers into tuples for use in functions.
    vals_n_weight = [(means[i], evalnos[i]) for i in range(0, len(evalnos))]
    print("Institution ID", item, 
          "Max", max_mean, 
          "Min", min_mean, 
          "Difference", round(diff, 2), 
          "Weighted Mean", get_wmean(means, evalnos),
          "Weighted Variance", get_var(means, evalnos),
          "Weighted SD", get_wstd(means, evalnos))
#Add the values to the Spread table
    cursor.execute(insert_stats, ( item, max_mean, min_mean, round(diff, 2), get_wmean(means, evalnos), get_var(means, evalnos), get_wstd(means, evalnos) ) )
    
connection.commit()

result = cursor.execute('''SELECT * FROM stats LIMIT 10''')
print(result.fetchall())
    
