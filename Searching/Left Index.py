Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/searching-basic-python/problem/left-index1524
   
class Solution:
    def leftIndex (self, N, arr, X):
        
        # code here 
        for i in range(0,N):
          
            if arr[i]==X:
                return i
        return -1
                
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        X = int(input())

        ob = Solution()
        print(ob.leftIndex(N, arr, X))

# } Driver Code Ends
