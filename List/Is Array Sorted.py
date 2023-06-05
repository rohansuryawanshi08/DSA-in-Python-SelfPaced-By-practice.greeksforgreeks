Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/is-array-sorted
    
#User function Template for python3

class Solution:
    def isSorted(self,arr,n):
        #code here
        s1=sorted(arr)
        s2=s1[::-1]
        if arr==s1 or arr==s2:
            return '1'
        return '0'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(Solution().isSorted(arr,n))
# } Driver Code Ends
