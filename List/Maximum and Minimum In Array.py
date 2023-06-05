Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/maximum-and-minimum-of-array-elements1523
   
#User function Template for python3

# inf has been imported in driver code

def maximumElement(arr,n,):
    #return required result
    
    #code here
    #arr.sort()
    return arr[-1]



def minimumElement(arr,n):
    #return required result
    
    #code here
    arr.sort()
    return arr[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    from math import inf
    
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        
        max_=maximumElement(arr,n,)
        min_=minimumElement(arr,n)
        print(max_,min_)
# } Driver Code Ends
