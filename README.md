## nQueens sat ecncoder
This is a sat encoder for the n Queens problem.
It generates a sat encoding in dimacs format, where the chessboard is represented by numbers. eg n=4:  
1 2 3 4  
5 6 7 8  
9 10 11 12  
13 14 15 16  

It does this by:
Creating a disjunction for every line.
For each two cells x,y that are in "line of sight" creating not x or not y.

### Experiments
I tried some experiments (using ./encoder.py n | ./cadical).
As expected, for 1 < n < 4, it's unsat, and for n > 4, cadical could find a solution.
I tried it with n=10, and wrote down the solution to verify that it makes sense.
Conveniently, the version of cadical I used prints useful statistics.
The runtime of the solver stays below 1 second on my computer unitl n=80, and it goes up from there.
It's remarkable that the solver is considerably faster than the encoder (1sec vs ~3.5sec)
At n=200, the solver takes 30s.
I haven't tested for higher n values, as the pyhton memory is apparently getting exhausted on my pc.
