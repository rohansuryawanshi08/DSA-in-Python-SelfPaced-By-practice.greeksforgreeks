Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/array-update-at-index
  
#User function Template for python3

def updateArray(arr,n,idx,element):
    #code here
   
    arr.insert(idx,element)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs= int(input())
    
    for _ in range(tcs):
        
        n=int(input())
        idx,element=[int(x) for x in input().split()]
        
        arr=[i+1 for i in range(n)]
        
        updateArray(arr,n,idx,element)
        
        print(arr[idx])
        
# } Driver Code Ends
