import global_alignment as ga
import sys

if __name__ == "__main__":
    sequences = []

    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            sequences.append(line)

    nxn = [[0 for i in range(len(sequences))] for _ in range(len(sequences))]