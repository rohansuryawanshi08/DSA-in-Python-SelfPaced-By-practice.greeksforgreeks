Link : https://practice.geeksforgeeks.org/batch/ds-with-python/track/mathematics-basics-python/problem/absolute-value
    
class Solution:
    def absolute(self,I):
        # code here
        if I <0:
            return I*(-1)
        else :
            return I


#{ 
 # Driver Code Starts.
def main():
    T = int(input()) #Input the number of testcases
    while(T > 0):
        I = int(input()) #input number
        ob=Solution()
        print(ob.absolute(I)) #Call function and print
        T -= 1 #Reduce number of testcases


if __name__ == "__main__":
    main()

# } Driver Code Ends
