#!/usr/bin/env python

import sys
import re

for line1 in sys.stdin:
	for line2 in open('ref1'):
		k1,k3=line1.split()
		k4,k6=line2.split()
		if k1==k4:
			if(int(k6)>1.5*int(k3)):
				print("%s"%(k1[3:6]))
			break
	
	
