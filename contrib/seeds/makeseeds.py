#!/usr/bin/env python
#
# Generate pnSeed[] from Pieter's DNS seeder
#

NSEEDS=600

import re
import sys
from subprocess import check_output

def main():
    lines = ["104.131.185.131:19833", "104.131.93.119:19833", "178.62.28.81:19833", "178.62.32.26:19833", "178.62.79.197:19833", "104.236.54.242:19833", "104.236.22.84:19833"
	     "104.131.93.119:19833", "104.131.185.131:19833"]

    ips = []
    pattern = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}):19833")
    for line in lines:
        m = pattern.match(line)
        if m is None:
            continue
        ip = 0
        for i in range(0,4):
            ip = ip + (int(m.group(i+1)) << (8*(i)))
        if ip == 0:
            continue
        ips.append(ip)

    for row in range(0, min(NSEEDS,len(ips)), 8):
        print "    " + ", ".join([ "0x%08x"%i for i in ips[row:row+8] ]) + ","

if __name__ == '__main__':
    main()
