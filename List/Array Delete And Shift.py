Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/array-delete-and-shift
    
#User function Template for python3

def deleteFromArray(arr,n,idx):
    #code here
    arr.pop(idx) and arr.append(0)
    return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#CONTRIBUTED BY RavinderSinghPB
if __name__ == '__main__':
    tcs= int(input())
    
    for _ in range(tcs):
        n=int(input())
        idx=int(input())
        
        arr=[i+1 for i in range(n)]
        
        deleteFromArray(arr,n,idx)
        
        for e in arr:
            print(e,end=' ')
        print()
        
# } Driver Code Ends
