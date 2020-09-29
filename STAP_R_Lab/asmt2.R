library(lsr)
library(psych)
BMI <- read.csv("BMI2.csv")
print(BMI)
cat('\ngender\theight\t\t\tweight\t\t\tage\t\tisMale')

# Min & Max
cat('\n\nMinimum value\nNA\t',min(BMI$height),'\t\t\t',min(BMI$weight),'\t\t\t',min(BMI$age),'\t\t',min(BMI$isMale))
cat('\n\nMaximum value\nNA\t',max(BMI$height),'\t\t\t',max(BMI$weight),'\t\t\t',max(BMI$age),'\t\t',max(BMI$isMale))

# Mean
cat('\n\nMean value\nNA\t',mean(BMI$height),'\t\t\t',mean(BMI$weight),'\t\t\t',mean(BMI$age),'\t\t',mean(BMI$isMale))

# Median
cat('\n\nMedian value\nNA\t',median(BMI$height),'\t\t\t',median(BMI$weight),'\t\t\t',median(BMI$age),'\t\t',median(BMI$isMale))

# Mode
cat('\n\nMode value\n',modeOf(BMI$gender),'\t',modeOf(BMI$height),'\t',modeOf(BMI$weight),'\t\t\t',modeOf(BMI$age),'\t\t',modeOf(BMI$isMale))

# Quantile
q <- c(0.25,0.5,0.75,1)
cat('\n\nQuantile values for',q,'\nNA','\t',quantile(BMI$height,probs=q),'\t',quantile(BMI$weight,probs=q),'\t',quantile(BMI$age,probs=q),'\t',quantile(BMI$isMale,probs=q))

# Standard Deviation
cat('\n\nStandard Deviation value\nNA\t',sd(BMI$height),'\t\t',sd(BMI$weight),'\t\t',sd(BMI$age),'\t',sd(BMI$isMale))

# Variance
cat('\n\nVariance value\nNA\t',var(BMI$height),'\t\t',var(BMI$weight),'\t\t',var(BMI$age),'\t',var(BMI$isMale))

# Range
cat('\n\nRange value\nNA\t',range(BMI$height),'\t\t',range(BMI$weight),'\t\t\t',range(BMI$age),'\t\t',range(BMI$isMale))

# IQR
cat('\n\nIQR value\nNA\t',IQR(BMI$height),'\t\t\t',IQR(BMI$weight),'\t\t\t',IQR(BMI$age),'\t\t',IQR(BMI$isMale))

# Skewness
cat('\n\nSkew value\nNA\t',skew(BMI$height),'\t\t',skew(BMI$weight),'\t\t ',skew(BMI$age),'\t ',skew(BMI$isMale))

cat('\n\n\nIf skew > 0 Right Skewed, skew = 0 Symmetric, skew < 0 Left Skewed')
v<-c(2:5)
s<-c()
for(i in v){
  if(skew(BMI[i])>0)
  {
    s[i-1]<-"Right Skewed"
    # print("Right Skewed")
  } else if(skew(BMI[i])==0)
  {
    s[i-1]<-"Symmetric"
    # print("Symmetric")
  } else
  {
    s[i-1]<-"Left Skewed"
    # print("Left Skewed")
  }
}

cat('\n\nSkewness\nNA\t',s[1],'\t\t',s[2],'\t\t',s[3],'\t',s[4],'\n\n\n')

