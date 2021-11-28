
def LevenshteinDistance(s1,s2):
    
    m = [[0]*(len(s2)+1)]*(len(s1)+1)

    for i in range(0,len(s1)+1):
        m[i][0] = i
    for j in range(0,len(s2)+1):
        m[0][j] = j

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                m[i][j] = min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1])
            else:
                m[i][j] = min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+1)

    return m[len(s1)][len(s2)]       


s1 = input('string-1 :')
s2 = input('string-2 :')

print(LevenshteinDistance(s1, s2))