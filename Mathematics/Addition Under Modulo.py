Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/mathematics-basics-python/problem/addition-under-modulo
    
#User function Template for python3
class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        
        MOD = 10**9 + 7


        return (a + b) % MOD

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        ob=Solution()
        print(ob.sumUnderModulo(a,b))

# } Driver Code Ends
