
##Simuler une ARMA sur N

#set.seed(0)

Phi = c(0.5, 1, 0.7)
Theta = c(0.6, 0.4, 0.3)
n=100
m=3
s2 =1

simulerARMA <- function(n, m, Phi, Theta, s2){
  E = rnorm(n,0,sqrt(s2))
  p = length(Phi)
  q= length(Theta)
  r = max(p+1,q+1)
  Y = E
  for (i in (r:n)){
    ar = ifelse(p>0,t(Phi) %*% Y[(i-p):(i-1)],0)
    ma = ifelse(q>0,t(Theta) %*% E[(i-q):(i-1)],0)
    Y[i]= ma + ar + E[i]
  }
  return(Y+m)
}
X = simulerARMA(500, 5, c(0.5,0.1), c(0.4,0.2), 1)
X2 = simulerARMA(500, 5, c(0.5,0.3), c(0.2), 1)
  
plot(X,type='l',col='red', main = "Simulation d'un processus ARMA(2,2) VS ARMA(2,1)")
lines(X2,type='l',col='blue')

## Comparaison 

library(tseries)

require(graphics)
set.seed(0)
x = arima.sim(n = 500, list(ar =c(0.5,0.1), ma = c(0.4,0.2)),sd = sqrt(1))
x1 = simulerARMA(500, 0, c(0.5,0.1), c(0.4,0.2), 1)

plot(x,type='l',col='blue')
lines(x1,type='l',col='black')

## TEST ACF et PACF

set.seed(114)
n = 200
phi = c(0.2)
theta = c(0.5, 0.2,0.4)
sigma = 1

simulated_data = arima.sim(n = n, list( ar = phi,ma = theta), sd = sigma)

# Installer la bibliothèque "forecast" si ce n'est pas déjà fait
# install.packages("forecast")

# Charger la bibliothèque
library(forecast)

# Calculer et afficher l'ACF
acf(simulated_data, lag.max = 20, main = "ACF de la série simulée")

# Calculer et afficher la PACF
pacf(simulated_data, lag.max = 20, main = "PACF de la série simulée")






