#!/usr/bin/python3
#!/usr/bin/env python3

#Problem 3
#python script to display only the top 5 most frequently used amino acids and add their
#percentage use. The output should be like this:
#L: 139002 (10.7%)
#A: 123885 (9.6%)
#G: 95475 (7.4%)
#V: 91683 (7.1%)
#I: 77836 (6.0%

from collections import defaultdict

with open ("e_coli_k12_dh10b.faa") as ecoli:
        counts = defaultdict(int)
        for line in ecoli: #iterate the file
                if line.startswith(">"): #skip all lines beginning with ">"
                        continue
                for char in line: #interate over the character in the lines. in this block if we get a hit we're going to have our counter go up 1
                        if char in {"A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"}:
                                counts[char] += 1 #increase count to +1
                total = float(sum(counts.values()))
                #print (total)
                #start the sort process here start
        for i in range(0,5):
                result = max(counts.items(), key=lambda x: x[1])
                print("{}:{}, ({:.1%})".format(result[0], result[1], result[1] / total))  # printing and formatting
                del counts[result[0]]
