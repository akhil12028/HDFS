#!/usr/bin/env python

import sys
import re


value=1

for line1 in sys.stdin:
	for line2 in open('ref'):
		k1,k2,k3=line1.split()
		k4,k5,k6=line2.split()
		if k1==k4 and k2==k5:
					print("%s\t%s\t%d"%(k3,k6,value))
					break

	
	
