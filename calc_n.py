#!/usr/bin/env python

# Calculate appropriate N for given memory size, desired memory utilization,
# and NB value.  The calculation is based on
# http://www.crc.nd.edu/~rich/CRC_Summer_Scholars_2014/HPL-HowTo.pdf

import math
import sys

if len(sys.argv) < 4:
    print "USAGE: %s <mem size> <mem util> <nb>" % sys.argv[0]
    exit(1)

sz_mem = int(sys.argv[1])
mem_util = float(sys.argv[2])
nb = int(sys.argv[3])

print int(math.sqrt(sz_mem / 8) * mem_util) / nb * nb
