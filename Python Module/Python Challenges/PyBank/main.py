#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:24:32 2020

@author: murillojessica
"""

import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_revenue = 0
previous_revenue = 0
months=[]
profit=[]
revenue_change= []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = next (csvreader, None)

    for row in csvreader:
        date_column = row[0]
        profit_column = int(row[1])

        total_months = total_months + 1
        total_revenue = total_revenue + profit_column
        
        revenue_change = profit_columnn-previous_revenue









'''
        months.append(date_comumn)
        profit.append(profit_column)

       
        
        
        
        
        
        
        
        
        
        
        
 """    


     months.append(date_comumn)
        profit.append(profit_column)   
       revenue_chnage[]
       
    for x in something :
        
        revenu_change = 
        
        total_profit = 
        total_months =len(months)
        
        
        
        
        
        
        
        
        
        
        
        #print(total_profit)
      
        #def max_num_in_list( list ):
2	    #max = list[ 0 ]
3	    #for a in list:
4	       # if a > max:
5	           # max = a
6	    #return max
     
