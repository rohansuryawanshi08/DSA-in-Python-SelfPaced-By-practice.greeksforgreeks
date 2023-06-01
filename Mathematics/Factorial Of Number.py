Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/mathematics-basics-python/problem/factorial-of-number
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

# } Driver Code Ends
#User function Template for python3

class Solution:
    #You need to complete this function
    def factorial(self,N):
        #Your code here
        fac=1
        for i in range(1,N+1):
            fac=fac*i
        return fac
            
 #{ 
 # Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        
        print(ob.factorial(N))
        
        
        T-=1
    
   
if __name__=="__main__":
    main()
# } Driver Code Ends
