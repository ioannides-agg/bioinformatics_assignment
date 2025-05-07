import util
import sys
import numpy as np

gap_penalty = -1
match_score = 1
mismatch_score = -1/2

def calc(match, i , j, table):
    return util.max_node(
        [table[i][j][0] + (match_score * match) + (mismatch_score * (not match)), i, j], 
        [table[i+1][j][0] + gap_penalty, i+1, j], 
        [table[i][j+1][0] + gap_penalty, i, j+1]
    )

def trace(s1, s2):
    mxn = [[[-1 for d in range(3)] for i in range(len(seq2) + 1)] for j in range(len(seq1) + 1)]

    for i in range(len(s1) + 1):
        mxn[i][0][0] = gap_penalty * i

    for i in range(len(s2) + 1):
        mxn[0][i][0] = gap_penalty * i

    for i in range(len(s1)):
        for j in range(len(s2)):
            match = False
            if(s1[i] == s2[j]):
                match = True

            mxn[i+1][j+1] = calc(match, i, j, mxn)

    last_element_row = mxn[-1][-1]
    i = last_element_row[1]
    j = last_element_row[2]
    path = []

    while i > -1 and j > -1:
        path.append( mxn[i][j] )
        next = mxn[i][j]

        i = next[1]
        j = next[2]

    return path

def align(seq1, seq2):
    path = list(reversed(trace(seq1, seq2)))
    seq1 = list(seq1)
    seq2 = list(seq2)
    s1 = ""
    s2 = ""
    i = 0
    j = 0
    c = 0
    gap = False

    while c < len(path) - 1:
        x = path[c]
        next = path[c+1]

        if not gap:
            c += 1
        else:
            gap = False
            j_gap = next[1] - x[1] # if next[1] - x[1] == 0, that means that the algortihm chose the top node, thus a gap is created in the left sequence
            i_gap = next[2] - x[2] # same logic for the i_gap

            # print( i_gap, j_gap )
            if j_gap == 0:
                s1 += "-"
                s2 += seq2[j]
                j += 1
                continue

            if i_gap == 0:
                s1 += seq1[i]
                s2 += "-"
                i += 1
                continue

        state = next[0] - x[0]
        if state != gap_penalty:
            s1 += seq1[i]
            s2 += seq2[j]
            i += 1
            j += 1
            continue
        else: 
            gap = True

    s1 += seq1[-1]
    s2 += seq2[-1]
    return (s1, s2)
        



if __name__ == "__main__":
    sequences = []

    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            sequences.append(line)

    seq1 = sequences[0]
    seq2 = sequences[1]

    print(seq1, len(seq1), seq2, len(seq2))
    s1, s2 = align(seq1, seq2)
    print("--------------")
    print(s1, len(s1))
    print(s2, len(s2))
    print("--------------")