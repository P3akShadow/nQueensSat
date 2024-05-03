## nQueens sat ecncoder
This is a sat encoder for the n Queens problem. It generates a sat encoding in dimacs format, where the chessboard is represented by numbers. eg n=4:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

It does this by:
Creating a disjunction for every line.
For each two cells x,y that are in "line of sight" creating not x or not y.

### experiments

