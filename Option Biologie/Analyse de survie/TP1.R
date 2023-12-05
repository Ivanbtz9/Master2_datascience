library(survival)
library(survminer)

X = diabetic

data = c(X$time[rank(X$time)],X$status[rank(X$time)]) 
