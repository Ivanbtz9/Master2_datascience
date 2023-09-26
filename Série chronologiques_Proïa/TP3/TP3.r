library(datasets)
library(tseries)



p <- 4 
Phi <- rnorm(p) #vecteur de taille p
q <- 4 
Theta <- rnorm(q) #vecteur de taille q
s2 = 2

n=100
m=2

simulerARMA <- function(n, m, Phi, Theta, s2){
  E = rnorm(n,0,sqrt(s2))
  x = rep(c(0),n)
  p = length(Phi)
  q= length(Theta)
  r = max(p,q)
  Y = rep(0,n)
  Y[1:r]=E[1:r]
  for (i in ((r+1):n)){
    ar = ifelse(p>0,t(Phi) %*% Y[(i-p):(i-1)],0)
    ma = ifelse(q>0,t(Theta) %*% E[(i-q):(i-1)],0)
    Y[i]= ma + ar + E[i]
  X = Y+m
  plot(X,type='l',col='red')
  
  }
}


simulerARMA(500, 5, c(0.8), c(), 1) #on voit que le bruit n'est pas un bruit blanc 

simulerARMA(500, 5, c(-0.8), c(), 1) # il y a des variations très rapide 
