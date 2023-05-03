#!/usr/bin/python3

import queen_backtrack

i = 1
a = queen_backtrack.attack([0])
print(i, " result ", a)

i = 2
a = queen_backtrack.attack([0])
print(i, " result ", a)

i = 3
a = queen_backtrack.attack([0,2,3,6])
print(i, " result ", a)

i = 4
a = queen_backtrack.attack([0,1])
print(i, " result ", a)

i = 5
a = queen_backtrack.attack([0,3,6])
print(i, " result ", a)

i = 6
a = queen_backtrack.attack([0,5])
print(i, " result ", a)

i = 7
a = queen_backtrack.attack([0,2,4,6,1,3,5,7])
print(i, " result ", a)

i = 8
a = queen_backtrack.attack([0,2,4,6,1,3,7,5])
print(i, " result ", a)
