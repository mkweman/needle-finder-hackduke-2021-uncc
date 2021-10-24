
def nw(seq1,seq2):
    len1 = len(seq1)+1
    len2 = len(seq2)+1
    a = [['' for x in range(len(seq1) + 1)] for y in range(len(seq1) + 1)]
    b = [['' for x in range(len(seq1) + 1)] for y in range(len(seq1) + 1)]
    matchM = 1
    misMatch = -1
    gap = -2
    for i in range(len1):
        if i == 0:
            a[i][0] = 0
            b[i][0] = 0
        else:
            a[i][0] = a[i-1][0] + gap
            b[i][0] = seq1[i-1]
    for i in range(len2):
        if i == 0:
            a[0][i] = 0
        else:
            a[0][i] = a[0][i-1] + gap
            b[0][i] = seq2[i-1]
    for i in range(len1):
        for j in range(len2):
            if i == 0 or j == 0:
                print("")
            elif seq1[i-1] == seq2[j-1]:
                gScoreH = a[i - 1][j] + gap
                gScoreV = a[i][j - 1] + gap
                mScore = a[i - 1][j - 1] + matchM
                if mScore == max(mScore, gScoreH, gScoreV):
                    b[i][j] = b[i][j] + ('D')
                if gScoreV == max(mScore, gScoreH, gScoreV):
                    b[i][j] = b[i][j] + ('^')
                if gScoreH == max(mScore, gScoreH, gScoreV):
                    b[i][j] = b[i][j] + ('<')
                a[i][j] = max(mScore, gScoreH, gScoreV)
            else:
                gScoreH = a[i - 1][j] + gap
                gScoreV = a[i][j - 1] + gap
                mScore = a[i - 1][j - 1] + misMatch
                if mScore == max(mScore, gScoreH, gScoreV):
                    b[i][j] = b[i][j] + ('D')
                if gScoreV == max(mScore, gScoreH, gScoreV):
                    b[i][j] = b[i][j] + ('^')
                if gScoreH == max(mScore, gScoreH, gScoreV):
                    b[i][j] = b[i][j] + ('<')
                a[i][j] = max(mScore, gScoreH, gScoreV)
    for i in range(len(a)):
        print(a[i])
    for i in range(len(a)):
        print(b[i])