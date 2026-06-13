class Solution(object):
    def getHint(self, secret, guess):
        bulls=0
        cows=0

        countS={}
        countG={}

        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                countS[secret[i]]=countS.get(secret[i],0)+1
                countG[guess[i]]=countG.get(guess[i],0)+1

        for digit in countG:
            if digit in countS:
                cows+=min(countS[digit],countG[digit])

        return str(bulls)+"A"+str(cows)+"B"
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        