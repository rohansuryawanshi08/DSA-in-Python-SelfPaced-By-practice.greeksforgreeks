Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/list-basic-python/problem/count-elements-greater-than-x
    
#User function Template for python3

class Solution:
    def greaterThanX(self,arr,n,x):
        #return required result
        #code here
        max=[]
        for i in arr:
            if i>x:
                max.append(i)
                
        return len(max)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        ob=Solution()
        ans=ob.greaterThanX(arr,n,x)
        print(ans)
# } Driver Code En
