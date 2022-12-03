#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:04:44 2022

@author: frankzi

Description: This script populates four existing tables based on a 
CSV file containing data about philosophy grad school rankings gathered by
the Philosophical Gourmet Report.

The Institutions, Regions, and Years of each entry has their own table.
The Overall table includes the numerical scores and ranks for each entry,
as well as the id values that point to the primary keys of the other three 
tables.

This script is for populating the database AFTER the tables have already been
created. The CSV files referenced here are for past iterations of the PGR.
"""


#Import 'csv' to read CSV files and sqlite3 to edit the database
import csv
import sqlite3

#Connect to PGR database
connection = sqlite3.connect('pgr-db-1.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()


fname = input('Input CSV file:')
if (len(fname) < 1): fname = 'PGR_COMBINED_2009.csv'

#Open the CSV file
fh = open(fname, newline='') 

#Read the CSV file
contents = csv.reader(fh)

#Variables for SQL insertion
#Insert values
insert_institution = "INSERT OR IGNORE INTO Institution (name) VALUES ( ? )"
insert_region = "INSERT OR IGNORE INTO Region (region) VALUES ( ? )"
insert_year = "INSERT OR IGNORE INTO Year (year) VALUES ( ? )"
insert_overall = "INSERT OR IGNORE INTO Overall (institution_id, mean, median, mode, lower_ci, upper_ci, geo_rank, region_id, overall_rank, year_id) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"


#Delete headers and empties
delete_i_header = "DELETE FROM Institution WHERE name = '\ufeffINSTITUTIONS' OR name = 'INSTITUTION' OR name = 'School'"
delete_i_empty = "DELETE FROM Institution WHERE name = ''"
delete_y_header = "DELETE FROM Year WHERE year = 'year ' OR year = 'year'"
delete_y_empty = "DELETE FROM Year WHERE year = ''"
delete_o_header = "DELETE FROM Overall WHERE mean = 'MEAN' OR overall_rank = 'overall_rank' "
delete_r_header = "DELETE FROM Region WHERE region = 'REGION' OR region = ' REGION'"

#Get IDs for Year, Region, and Institution
get_inst_id = "SELECT id FROM Institution WHERE name = ? "
get_year_id = "SELECT id FROM Year WHERE year = ? "
get_region_id = "SELECT id FROM Region WHERE region = ? "

#Write rows of CSV to database
for row in contents:
    #Identify row indices
    inst = row[0]
    mean = row[1]
    median = row[2]
    mode = row[3]
    lower_ci = row[4]
    upper_ci = row[5]
    region = row[6]
    geo_rank = row[7]
    overall_rank = row[8]
    year = row[9]
    print(row)
    #Populate institution, year, and region tables
    cursor.execute(insert_institution, ( inst, ) )
    cursor.execute(insert_year, ( year, ) )
    cursor.execute(insert_region, ( region, ))
    #get IDs for Overall table
    cursor.execute(get_inst_id, ( inst, ))
    inst_id = cursor.fetchone()[0]
    cursor.execute(get_year_id, ( year, ))
    year_id = cursor.fetchone()[0]
    cursor.execute(get_region_id, ( region, ))
    region_id = cursor.fetchone()[0]
    #Populate overall tables
    cursor.execute(insert_overall, ( inst_id, mean, median, mode, lower_ci, upper_ci, geo_rank, region_id, overall_rank, year_id ) )
    #Delete headers and nulls
    cursor.execute(delete_i_header)
    cursor.execute(delete_i_empty)
    cursor.execute(delete_y_header)
    cursor.execute(delete_r_header)
    cursor.execute(delete_y_empty)
    cursor.execute(delete_o_header)
connection.commit()

#Check results of Institution Table
res_i = cursor.execute('''SELECT * FROM Institution LIMIT 10''')
print(res_i.fetchall())
#Check results of Year table
res_y = cursor.execute('''SELECT * FROM Year LIMIT 10''')
print(res_y.fetchall())
#Check results of region Table
res_r = cursor.execute('''SELECT * FROM Region LIMIT 10''')
print(res_r.fetchall())
#Check results of Overall table
res_o = cursor.execute('''SELECT * FROM Overall LIMIT 10''')
print(res_o.fetchall())

connection.close()

    

        

#