#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 03:30:38 2018

@author: JamesFan
"""

# the csv library allows us to easily create a csv file
import csv

#open the csv file and assign it to source variable
with open("NYC_death.csv","r") as source:
    #use the csv module to read the source
    reader= csv.reader( source )
    #then open output.csv in order to make a new csv file with scrubbed data
    with open("output.csv","w") as result:
        #create assign writing to csv file to wtr variable
        writer = csv.writer( result )
        #loop through all rows in rdr/source
        for row in reader:
            #delete rows with no data or "." in it
            if row[4] != ".":
                #delete the last 2 rows which we do not want
                writer.writerow( (row[0], row[1], row[2], row[3], row[4]) )
            
           
#close the file
source.close()
result.close()





