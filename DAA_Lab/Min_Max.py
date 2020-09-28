from datetime import datetime
import time

start =time.time()

INF = float('inf')

def findMinAndMax(A, L, R, min, max):

	if L == R:		   
		if min > A[R]:	  
			min = A[R]
		if max < A[L]:	   
			max = A[L]
		return min, max
	
	if R - L == 1:	   
		if A[L] < A[R]:  
			if min > A[L]:  
				min = A[L]
			if max < A[R]:  
				max = A[R]
		else:
			if min > A[R]:  
				min = A[R]
			if max < A[L]:   
				max = A[L]

		return min, max

	mid = (L + R) // 2
	min, max = findMinAndMax(A, L, mid, min, max)
	min, max = findMinAndMax(A, mid + 1, R, min, max)

	return min, max

if __name__ == '__main__':
    A=[]
    n= int(input("\nEnter total no of elements : "))
    for i in range(n): 
        print("\nEnter value",i+1," : ")        
        A.append(int(input()))
	    
    (min, max) = (INF, -INF)
    (min, max) = findMinAndMax(A, 0, len(A) - 1, min, max)
    print("\nMinimum Element is : ", min)
    print("\nMaximum Element is : ", max)

# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

end = time.time()

print(f"Runtime of the program is {end - start}")