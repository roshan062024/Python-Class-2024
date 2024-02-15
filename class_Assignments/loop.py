#!/usr/bin/python
"""
Purpose:
    break     - breaks the complete loop
	continue  - skip the current loop
	pass      - will do nothing. it is like a todo
	sys.exit  - will exit the script execution
"""
import sys

students = ["akram", "trusha", "bhavana", "jaya", "chaitra","akash","."]

for i in students:
    if i == "akash":
        pass
    if i == "bhavana":
        print(f"{i}")
    if i == "trusha":
        print(f"{i}")
        continue
    if i == ".":
        sys.exit("cannot divide")
        a= 100/i
        
        

    

