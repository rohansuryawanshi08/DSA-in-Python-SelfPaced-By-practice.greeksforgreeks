Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/mathematics-basics-python/problem/digits-in-factorial
 

#User function Template for python3

class Solution:
    def digitsInFactorial(self,N):
        # code here
        fac=1
        result=0
        count=0
        for i in range(1,N+1):
            fac=fac*i
            
        while fac>0:
            
            count=count+1
            fac=fac//10
    
        return count
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        print(ob.digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code End
