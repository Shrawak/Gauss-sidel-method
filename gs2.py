import numpy
from prettytable import PrettyTable

n = int(input("Enter the number of variables or the number of eqn - "))
ac = int(input("Input the number of decimal accuracy places"))
accuracy = float(0.5 * (10**(-ac)))
mat = numpy.zeros((n,n + 1))


var = []
prev_var = []
col_name = []


for i in range(0,n):
    col_name.append(input("Enter the variable name for  " + str(i + 1) + " variable - "))


# eqn data input from the user
for i in range(0,n):
    for j in range (0,n + 1):
        if j < n : 
            mat[i][j] = float(input("Enter the coefficient of " + col_name[j] + " varaiable of  equation number  " + str(i + 1) + " - "  ))
        else:
            mat[i][j] = float(input("Enter the constant term of equation number " + str(i + 1) + " - "))

print(mat) 


#initial assumption of data from the user
for i in range(0,n):
    var.append(float(input("Enter the inital value for  " + col_name[i] + " - ")))
    prev_var.append(0.0)




table = PrettyTable(col_name)
ftable = PrettyTable(col_name)
table.title = "Gauss siedal method"


print(var)


process = True
data_valid = True
count = 1


#data validation
for i in range(0,n):
    for j in range(0, n):
        if (mat[i][j] < mat[i][i]) or ((i == j) and mat[i][j] == mat[i][i]):
            data_valid = True
        else:
            data_valid = False
            process = False
           

if data_valid == False:
    print("The input data in not in diagonal dominant form")



while process == True :

    #calculation part
    for i in range(0,n):
        y = 0
        for j in range(0 , n + 1):
            if (i == j):
                x = 1/mat[i][j]
            elif ((i != j) and (j != n)):
                y = y + (-1)*(mat[i][j])*var[j]
            elif (j == n):
                y = y + mat[i][j]

        var[i] = x * y
        var[i] = round(var[i],ac)


    ans_valid = 0


    table.add_row(var)


    #accuracy check
    for i in range(0,n):
        diff = abs(prev_var[i] - var[i])
        if (diff < accuracy):
        
            ans_valid = ans_valid + 1
        else:
            prev_var[i] = var[i]
            ans_valid = 0

    if ans_valid == n:
        process = False
        print(table)
        print("The final value of the variables are")
        ftable.add_row(var)
        print(ftable)

    

 