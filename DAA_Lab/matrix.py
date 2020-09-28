import time
from datetime import datetime

start = time.time()
while(True):
        print("\n\nFor First Matrix")
        size = int(input("\nEnter number of rows and columns : "))
        a = [] 
        print("\nRow wise entries : ") 
       
        for i in range(size):         
            x =[] 
            for j in range(size):      
                 x.append(int(input())) 
            a.append(x) 
                 
        print("Enter values into first matrix : ")    
        for i in range(size): 
            print("Row:",i+1)
            for j in range(size): 
                print(a[i][j]) 
        
        print("For Second Matrix")
        b= [] 

        print("\nRow wise entries : ") 
        
        for i in range(size):          
            y=[] 
            for j in range(size):     
                 y.append(int(input())) 
            b.append(y) 
        print("Enter values into second matrix : ")    
        for i in range(size): 
            print("Row:",i+1)
            for j in range(size): 
                print(b[i][j])

        def new_m(p, q): 
            matrix = [[0 for size in range(p)] for size in range(q)]
            return matrix

        def straight(a, b): 
            if len(a[0]) != len(b): 
                return "Matrices are not m*n and n*p format"
            else:
                p_matrix = new_m(len(a), len(b[0]))
                for i in range(len(a)):
                    for j in range(len(b[0])):
                        for k in range(len(b)):
                            p_matrix[i][j] += a[i][k]*b[k][j]
            return p_matrix

        def split(matrix): 
            a = matrix
            b = matrix
            c = matrix
            d = matrix
            while(len(a) > len(matrix)/2):
                a = a[:len(a)/2]
                b = b[:len(b)/2]
                c = c[len(c)/2:]
                d = d[len(d)/2:]
            while(len(a[0]) > len(matrix[0])/2):
                for i in range(len(a[0])/2):
                    a[i] = a[i][:len(a[i])/2]
                    b[i] = b[i][len(b[i])/2:]
                    c[i] = c[i][:len(c[i])/2]
                    d[i] = d[i][len(d[i])/2:]
            return a,b,c,d
                    
        def add_m(a, b):
            if type(a) == int:
                d = a + b
            else:
                d = []
                for i in range(len(a)):
                    c = []
                    for j in range(len(a[0])):
                        c.append(a[i][j] + b[i][j])
                    d.append(c)
            return d

        def sub_m(a, b):
            if type(a) == int:
                d = a - b
            else:
                d = []
                for i in range(len(a)):
                    c = []
                    for j in range(len(a[0])):
                        c.append(a[i][j] - b[i][j])
                    d.append(c)
            return d


        def strassen(a, b, q):
         
            if q == 1:
                d = [[0]]
                d[0][0] = a[0][0] * b[0][0]
                return d
            else:
                
                a11, a12, a21, a22 = split(a)
                b11, b12, b21, b22 = split(b)
                
                p1 = strassen(add_m(a11,a22), add_m(b11,b22), q/2)
                p2 = strassen(add_m(a21,a22), b11, q/2)
                p3 = strassen(a11, sub_m(b12,b22), q/2)
                p4 = strassen(a22, sub_m(b12,b11), q/2)
                p5 = strassen(add_m(a11,a12), b22, q/2)
                p6 = strassen(sub_m(a21,a11), add_m(b11,b12), q/2)
                p7 = strassen(sub_m(a12,a22), add_m(b21,b22), q/2)
                
                c11 = add_m(sub_m(add_m(p1, p4), p5), p7)
                c12 = add_m(p3, p5)           
                c21 = add_m(p2, p4)              
                c22 = add_m(sub_m(add_m(p1, p3), p2), p6)

                c = new_m(len(c11)*2,len(c11)*2)
                for i in range(len(c11)):
                    for j in range(len(c11)):
                        c[i][j]                   = c11[i][j]
                        c[i][j+len(c11)]          = c12[i][j]
                        c[i+len(c11)][j]          = c21[i][j]
                        c[i+len(c11)][j+len(c11)] = c22[i][j]
            
                return c
        print ("\nResultant Matrix : ")
        print (straight(a,b))
        break

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

end = time.time()
print(f'Running time : {end-start}')