Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/searching-basic-python/problem/who-will-win-1587115621
    
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        arr=sorted(arr)
    

        for i in range(0,N):
            if arr[i] == K:
                return 1
        return -1
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends
