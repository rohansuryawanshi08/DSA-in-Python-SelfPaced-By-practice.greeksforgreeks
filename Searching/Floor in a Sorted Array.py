Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/searching-basic-python/problem/floor-in-a-sorted-array-1587115620
    
class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        if X<A[0]:
            
            return -1
        target = -1
        s = 0
        l = N-1
        while s<=l:
            m = (s+l)//2
            if A[m]==X:
                return m
            elif A[m]>X:
                l = m-1
                target = m-1
            else:
                s = m+1
                target = m
        return target
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
