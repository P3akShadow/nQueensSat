#!/usr/bin/python3
import sys


def nQueensClauses(n):
    clauses = []
    for i in range(n):
        #one queen per line
        clauses.append([n*i+j+1 for j in range(n)])
        for j in range(n):
            for k in range(n):
                if k != j:
                    clauses.append([-(n*i+j+1), -(n*i+k+1)])
                if i != k:
                    clauses.append([-(n*i+j+1), -(n*k+j+1)])
            x = i
            y = j
            while x < n-1 and y < n-1:
                x += 1
                y += 1
                clauses.append([-(n*i+j+1), -(n*x+y+1)])
            x = i
            y = j
            while x < n-1 and y > 0:
                x += 1
                y -= 1
                clauses.append([-(n*i+j+1), -(n*x+y+1)])
            x = i
            y = j
            while x > 0 and y < n-1:
                x -= 1
                y += 1
                clauses.append([-(n*i+j+1), -(n*x+y+1)])
            x = i
            y = j
            while x > 0 and y > 0:
                x -= 1
                y -= 1
                clauses.append([-(n*i+j+1), -(n*x+y+1)])
    return clauses


n = int(sys.argv[1])

clauses = nQueensClauses(n)

print(f"p cnf {n*n} {len(clauses)}")
for clause in clauses:
    print(*clause, sep=" ", end=" 0\n")

