#!/usr/bin/env python
 
import sys

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count_max = 0
change = ""
# 1-2 1
# 1-3 2	
# 2-1 3
# 2-3 4
# 3-1 5
# 3-2 6

for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key1,this_key2,value = input_line.split()
   value = int(value)
 
   if this_key1 != this_key2:	
	count = count+value
	if int(this_key1) == 1:
		if int(this_key2) == 2:
			count1=count1+value
		elif int(this_key2) == 3:
			count2=count2+value
	elif int(this_key1) == 2:
		if int(this_key2) == 1:
			count3=count3+value
		elif int(this_key2) == 3:
			count4=count4+value
	elif int(this_key1) == 3:
		if int(this_key2) == 1:
			count5=count5+value
		elif int(this_key2) == 2:
			count6=count6+value

	#print ("%s\t%s\t%d"%(this_key1,this_key2,count))

print count
#print count1
#print count2
#print count3
#print count4
#print count5
#print count6

if count1>count_max:
	count_max=count1
	change = "1-2"

if count2>count_max:
	count_max=count2
	change = "1-3"

if count3>count_max:
	count_max=count3
	change = "2-1"

if count4>count_max:
	count_max=count4
	change = "2-3"

if count5>count_max:
	count_max=count5
	change = "3-1"

if count6>count_max:
	count_max=count6
	change = "3-2"

print ("The most common change is %s and %s times"%(change,count_max))
