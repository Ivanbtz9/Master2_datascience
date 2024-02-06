
##Simuler une ARMA sur N

#set.seed(0)

Phi = c(0.5, 1, 0.7)
Theta = c(0.6, 0.4, 0.3)
n=100
m=3
s2 =1

simulerARMA <- function(n, m, Phi, Theta, s2){
  E = rnorm(n,0,sqrt(s2)) #céer un vecteur avec n gaussienne 
  p = length(Phi) 
  q= length(Theta)
  r = max(p+1,q+1)
  Y = E # initialise Y
  for (i in (r:n)){
    ar = ifelse(p>0,t(Phi) %*% Y[(i-p):(i-1)],0)
    ma = ifelse(q>0,t(Theta) %*% E[(i-q):(i-1)],0)
    Y[i]= ma + ar + E[i]
  }
  plot(Y+m,type='l',col='red', main = paste("Simulation d'un processus ARMA(",p,',',q,')'))
  return(Y+m)
  
}

#Plot1
X = simulerARMA(500, 5, c(0.5,0.1), c(0.4,0.2), 1)
X2 = simulerARMA(500, 5, c(0.5,0.3), c(0.2), 1)
  
plot(X,type='l',col='red', main = "Simulation d'un processus ARMA(2,2) VS ARMA(2,1)")
lines(X2,type='l',col='blue')

#plot 2

X = simulerARMA(500, 5, 1, c(), 1) # Marche aléatoire, non stationnarité en espérance
X2 = simulerARMA(500, 5, -1, c(), 1) # non stationnarité en varaince

# Crée une nouvelle fenêtre graphique avec une taille spécifique (largeur x hauteur en pouces)
windows(width = 8, height = 6)
plot(X,type='l',col='red', main = "Simulation d'un processus ARMA(1) ")
lines(X2,type='l',col='blue')

## Comparaison 

library(tseries)

require(graphics)
set.seed(0) # rendre l'aléa fixe

x = arima.sim(n = 500, list(ar =c(0.5,0.1), ma = c(0.4,0.2)),sd = sqrt(1))
x1 = simulerARMA(500, 0, c(0.5,0.1), c(0.4,0.2), 1)

plot(x,type='l',col='blue')
lines(x1,type='l',col='black')

## TEST ACF et PACF

# ACF et PACF d'un MA(5)
X = simulerARMA(10000, 0, c(), c(0.2, 0.3, 0.8, -0.5, 0.3), 1)
acf(X, lag.max = 50)
pacf(X, lag.max = 50)

# PACF et PACF d'un AR(3)
X = simulerARMA(1000, 0, c(0.1, 0.2,0.2), c(), 1)
acf(X, lag.max = 50)
pacf(X, lag.max = 50)

# PACF et PACF d'un ARMA(2, 2)
X = simulerARMA(1000, 0, c(0.3, 0.6), c(-0.3, 0.8), 1)
acf(X, lag.max = 50)
pacf(X, lag.max = 50)

##Simulation avec arima.sim

# Installer la bibliothèque "forecast" si ce n'est pas déjà fait
# install.packages("forecast")

n = 200
phi = c(0.2)
theta = c(0.5, 0.2,0.4)
sigma = 1

simulated_data = arima.sim(n = n, list( ar = phi,ma = theta), sd = sigma)

## Test de stationnarité

n=1000
X = arima.sim(n= n, list( ar = c(0.2,0.5),ma=c()), sd = 1) #Stationnaire par le cours 
adf.test(X) # doit rejeter la non-stationnarité 
kpss.test(X) # ne doit pas rejeter la stationnarité

n=200
X = arima.sim(n= n, list( ar = c(0.2,0.5),ma=c()), sd = 1) #Stationnaire par le cours 
adf.test(X) # doit rejeter la non-stationnarité 
kpss.test(X) # ne doit pas rejeter la stationnarité

#ATTENTION

X = c(1:1000) + 3*rnorm(1000) #Non stationnaire au visuel
plot(X)

kpss.test(X,null='Trend') # ne nous fait pas rejeter la stationnarité /!\

## Test sur les bruits Blancs

X = simulerARMA(200, 0, c(0.6,0.2), c(0.7), 1)
#Box.test(x, lag = 1, type = c("Box-Pierce", "Ljung-Box"), fitdf = 0)
#"Ljung-Box" gérer les séries de petites taille

Box.test(X, lag = 5,type = c("Ljung-Box") ,fitdf = 0) #Test l'autocorrélation 

help('Box.test')

## ARIMA trouver les coefficients
library(forecast)
#Test1
X = simulerARMA(200, m=2, c(0.2,0.4,0.2), c(0.3, 0.5,0.3), 1.5)
ARMA = Arima(X, order = c(3, 0, 3), include.mean = TRUE)
summary(ARMA)

#test2
X = simulerARMA(2000, m=0, c(0.6,0.2), c(0.7), 1)
ARMA = Arima(X, order = c(2, 0, 1), include.mean = FALSE)
summary(ARMA)

#Test3
X = simulerARMA(2000, m=0, c(0.6,0.2), c(0.7), 1)- simulerARMA(2000, m=0, c(0.6,0.2), c(0.7), 1)
plot(X,type = 'l')

Box.test(X, lag = 5,type = c("Ljung-Box") ,fitdf = 0) #Test l'autocorrélation



##ARIMA

# ... ainsi que la fonction auto.arima calibr?e sur le BIC
X = simulerARMA(100000, m=0, c(0.7,0.25), c(0.7), 1)
auto.arima(X, max.p = 5, max.q = 5, max.d = 0, ic = "bic") 





