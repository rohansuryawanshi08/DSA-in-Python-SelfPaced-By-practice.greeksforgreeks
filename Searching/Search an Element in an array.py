Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/searching-basic-python/problem/search-an-element-in-an-array-1587115621
    
  #User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        count=0
        for i in arr:
            count=count+1
            if i==X:
                return count-1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            
            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            ob=Solution()
            print(ob.search(A,N,x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
