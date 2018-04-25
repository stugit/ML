#!/usr/bin/env python

import numpy.matlib 
import numpy as np 

# Scalar Projection
r = np.array([3, -4, 0]) 
s = np.array([10, 5, -6]) 
vrs = r * np.vdot(r, s) / np.linalg.norm(r) ** 2
print(vrs)
