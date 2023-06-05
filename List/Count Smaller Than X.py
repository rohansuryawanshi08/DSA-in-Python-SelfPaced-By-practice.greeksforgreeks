Link :  https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/count-smaller-than-x
    
#User function Template for python3

class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        res=[]
        for i in arr:
            if i<x:
                res.append(i)
                
        return len(res)
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    from math import inf
    t= int(input())
    
    for _ in range(t):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        ob=Solution()
        ans=ob.smallerThanX(arr,n,x)
        print(ans)
# } Driver Code Ends
