# Vector
print('1. Vector')
v <- c('Shounak', 2185043)
print(v)

# Lists
print('2. List')
l <- list('a', v, TRUE, 1)
print(l)

# Factor
print('3. Factor')
v1 <- c('a', 'b', 'a', 'a', 'c', 'b')
fact <- factor(v1)
print(is.factor(fact))
print(fact)
sprintf('Total no of levels : %s',nlevels(fact))

# Matrix
print('4. Matrix')
M <- matrix(c(1:12), nrow = 3, byrow = TRUE)
print(M)
r <- c('R1', 'R2', 'R3')
c <- c('C1', 'C2', 'C3', 'C4')
print('Matrix after adding dimnames')
M2 <- matrix(c(1:12), nrow = 3, byrow = TRUE, dimnames = list(r,c))
print(M2)

# Array
print('5. Array')
A <- array(c(v,v1), dim = c(3,3,2))
print(A)

# Data Frame
print('6. Data Frame')
BMI <- data.frame(
  gender = c('M','M','F'), height = c(152, 171.5, 165), weight = c(76,89,65), 
  age = c(42,38,26), stringsAsFactors = FALSE
)
print(BMI)
str(BMI)
print('Summary of Dataframe')
print(summary(BMI))
print('Printing 1st Row')
print(BMI[1,])
print('Printing 1st Column')
print(BMI[1])
print('Printing few 1,2 Rows with 1,2 Columns')
print(BMI[c(1,2),c(1,2)])
print('Printing a particular value')
print(BMI[1,2])

# File writing and reading
print('Writing and reading a csv file')
write.csv(BMI,"BMI.csv")
BMI_df <- read.csv("BMI.csv")
print(BMI_df)
sprintf('No of Rows : %s',nrow(BMI_df))
sprintf('No of Columns : %s',ncol(BMI_df))