# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 19:48:49 2021

@author: Gerald
"""

#!/usr/bin/python3
import os
# This is the function that removes duplicates and keeps one sentence if there are 2 or more sentences
# It also deletes empty rows
def remove_duplicates():
#Loading the csv file   
    with open(r"C:\Users\Gerald\Desktop\DataScienceProject\sentences.csv", "r+", encoding="utf-8") as f:
# Reading each line in the csv       
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)
                f.truncate()
            
    #Deleting duplicates
    with open("sentences.csv", "r") as csv_file:
        new_data = list(set(csv_file))
        return new_data
 

# deleting sentences with more than 14 words
def delete_line_by_condition(original_file, condition):
    """ In a file, delete the lines at line number in given list"""
    dummy_file = original_file + '.bak'
    is_skipped = False
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Line by line copy data from original file to dummy file
        for line in read_obj:
            # if current line matches the given condition then skip that line
            if condition(line) == False:
                write_obj.write(line)
            else:
                is_skipped = True
    # If any line is skipped then rename dummy file as original file
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)