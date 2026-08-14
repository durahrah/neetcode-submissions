class Solution:
    def calPoints(self, operations: List[str]) -> int:
      
        score = []
        for n in (operations):
            if (n!='C') and (n!='D') and (n!='+'):
                score.append(int(n))
                
            elif (n=='+'):
                score.append((score[-1]+score[-2]))
                
            elif (n=='D'):
                score.append((score[-1]*2))
        
            elif (n=='C'):
                score.pop()
                
        return sum(score)        





        