class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
       """
        return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]


cases = [
        (21,),
        (22,),
        (23,),
        (24,),
        (25,),
        (26,),
        (27,),
        (28,),
        (29,),
        (30,),
        (31,),
        (32,),
        (33,),
        (34,)
    ]
sol = Solution()
print [sol.fizzBuzz(x[0]) for x in cases]
