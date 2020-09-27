
def merge(a, p, q, r): 
	n1 = q - p + 1
	n2 = r- q 

	L = [0] * (n1) 
	R = [0] * (n2) 

	for i in range(0 , n1): 
		L[i] = a[p + i] 

	for j in range(0 , n2): 
		R[j] = a[q + 1 + j] 

	i = 0	 
	j = 0	  
	k = p	 

	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			a[k] = L[i] 
			i += 1
		else: 
			a[k] = R[j] 
			j += 1
		k += 1

	while i < n1: 
		a[k] = L[i] 
		i += 1
		k += 1

	while j < n2: 
		a[k] = R[j] 
		j += 1
		k += 1

def mergeSort(a,p,r): 
	if p < r: 
		q = (p+(r-1))//2
		mergeSort(a, p, q) 
		mergeSort(a, q+1, r) 
		merge(a, p, q, r) 

a = [6, 5, 1, 8, 3, 10, 11, 12, 13] 
n = len(a) 
print ("Given array is") 
print(a)

mergeSort(a,0,n-1) 
print ("\n\nSorted array is") 
print(a)


