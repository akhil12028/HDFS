#!/usr/bin/env python
 
import sys
 
last_key = None
running_total = 0

next_key = None

max_key = None
max_total = 0
for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key1,value = input_line.split()
   value = int(value)
 
   if last_key == this_key1:
       running_total += value
   else:
       if last_key:
           print( "%s\t%d" % (last_key,running_total) )
	   if max_total<running_total :
	      max_total=running_total
	      max_key=last_key
       running_total = value
       last_key = this_key1
       
 
if last_key == this_key1:
   print( "%s\t%d" % (last_key,running_total) )
   if max_total<running_total :
	      max_total=running_total
	      max_key=last_key

