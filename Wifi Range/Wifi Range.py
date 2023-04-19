class Solution:
    def wifiRange(self, N, S, X): 
        #code here
        r = 0
        count = 0
        for i in range(N):
            if S[i]=='1':
                count += 1
                if i-r-1>2*X:
                    return 0
                r = i
            if count == 1:
                if r>X:
                    return 0
        if N-r-1>X:
            return 0
        return 1