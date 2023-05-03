Describe an 8 * 8 chessboard with coordinates 0-7.

To put 8 queens on with no attacks
you can start with an empty board
and put each queen one by one on
each file.  That means each choice
is one number 0-7 for the rank coordinate.

Doing this in a backtracking style and
checking for attacks only involving the
new queen keeps the amount of work low.

You don't need to quit when you have one
solution but can keep crunching till you
have them all.


file test_a.py
Testing the attack check.

file queen_backtrack.py
Produce the list of 8-queen arrangements.
