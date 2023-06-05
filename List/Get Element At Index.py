Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/get-element-at-index
    
#User function Template for python3

def getByIndex(arr,n,idx):
    
    # return required ans

        
    if idx < n:
        return arr[idx]
    else:
        return -1

         


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        idx=int(input())
        
        print(getByIndex(arr,n,idx))
# } Driver Code Ends
