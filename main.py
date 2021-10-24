
def find_direction(diagonal, top, left):
    direction = ""
    if diagonal == max(diagonal, top, left):
        direction = direction + 'D'
    if top == max(diagonal, top, left):
        direction = direction + 'T'
    if left == max(diagonal, top, left):
        direction = direction + 'L'

    return direction


def traceback(b):
    seq1 = len(b) - 1
    seq2 = len(b[0]) - 1

    i = 0
    j = 0

    c = []
    out_seg1 = []
    out_seq2 = []

    while seq1 > i or seq2 > j:
        node = b[seq1 - i][seq2 - j]
        if len(node) > 0:
            c.append([seq1-i, seq2-j])
            if node[0] == 'D':
                out_seq2.append(b[0][seq2-j])
                out_seg1.append(b[seq1-i][0])
                i += 1
                j += 1
            elif node[0] == 'L':
                out_seq2.append(b[0][seq2-j])
                out_seg1.append("-")
                j += 1
            elif node[0] == 'T':
                out_seq2.append("-")
                out_seg1.append(b[seq1-i][0])
                i += 1

    c.append([0, 0])
    print(c)
    print(out_seq2[::-1])
    print(out_seg1[::-1])
    return c


def main(seq1, seq2):
    # seq2 = input("What is the first input? ")
    # seq1 = input("What is the second input? ")
    match = 1
    mismatch = -1
    gap = -2

    a = [[0 for x in range(len(seq2) + 1)] for y in range(len(seq1) + 1)]
    b = [[0 for x in range(len(seq2) + 1)] for y in range(len(seq1) + 1)]

    for i in range(1, len(seq1) + 1):
        a[i][0] = a[i-1][0] + gap
        b[i][0] = seq1[i-1]

    for j in range(1, len(seq2) + 1):
        a[0][j] = a[0][j-1] + gap
        b[0][j] = seq2[j-1]

    for i in range(len(seq1) + 1):
        for j in range(len(seq2) + 1):
            if i > 0 and j > 0:
                if seq2[j-1] == seq1[i-1]:
                    diagonal = a[i - 1][j - 1] + match
                    top = a[i-1][j] + gap
                    left = a[i][j-1] + gap
                    a[i][j] = max(diagonal, top, left)
                    b[i][j] = find_direction(diagonal, top, left)
                else:
                    diagonal = a[i - 1][j - 1] + mismatch
                    top = a[i-1][j] + gap
                    left = a[i][j-1] + gap
                    a[i][j] = max(diagonal, top, left)
                    b[i][j] = find_direction(diagonal, top, left)

    for i in range(len(a)):
        print(a[i])
    print("")

    for i in range(len(b)):
        print(b[i])
    print("")

    traceback(b)


if __name__ == '__main__':
    main("AGTC", "AGG")
