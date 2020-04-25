#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:24:32 2020

@author: murillojessica
"""

#import dependencies
import os
import csv

#File Path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Variables
total_months = 0
total_revenue = 0
previous_value = 0
revenue_dif = 0
min_dif= 0
max_dif =0
rev_dif_list=[]


#opening CSV File 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',') 
    csv_header = next(csvreader)

    for row in csvreader:
        
        date_column = row[0]
        revenue_column = row[1]
        revenue_column_int = int(revenue_column)
        
        #Calculate the difference between two rows
        revenue_dif= revenue_column_int - previous_value
        previous_value = revenue_column_int
        
        #Capture the differences in alist
        rev_dif_list = rev_dif_list + [revenue_dif] 
        
        
        if max_dif < revenue_dif:
            max_dif = revenue_dif
            max_date = date_column
            
        if min_dif > revenue_dif:
            min_dif = revenue_dif
            min_date = date_column
            
        #previous_value = revenue_column_int
        #Count Month
        total_months = total_months + 1
        
        #Sum net revenue 
        total_revenue = total_revenue + revenue_column_int  
        revenue_avg = round(sum(rev_dif_list)/len(rev_dif_list))
        
        
        
#Print Results
output =(f'Financial Analysis\n'
         f'-----------------------------------------------------\n'   
         f'Total Months : {total_months}\n'
         f'Total: $ {total_revenue}\n'
         f'Average Change: {revenue_avg}\n'
         f'Greatest Increase in Profits: {max_date} : $ ({max_dif})\n'
         f'Greatest Decrease in Profits: {min_date} : ($ {min_dif})\n')
print(output)
"""
print(rev_dif_list)
print(len(rev_dif_list))
print(sum(rev_dif_list))
#Export to TXT File 
file_to_output = os.path.join("Analysis", "final.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)



        
        
    
    
    
    
    
    
    
    
    
    """