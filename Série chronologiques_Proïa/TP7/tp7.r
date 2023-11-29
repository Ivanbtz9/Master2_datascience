library(forecast)
library(zoo) #for the linear aproximation
library(TTR)
library(TSA)
library(xts)
library(quantmod)
library(tseries)
# plot of gold 
plot(gold)
ng = length(gold)

#without None data
X = gold[(ng-364):ng]

plot(X,type ='l')

# linear intepolation with the library zoo 
## Question 1
X_interp = na.approx(X)


## Question 2
plot(X_interp,type ='l') # a linear tendance is clearly see here

# test de non sta
adf.test(X_interp) # on ne rejette la non stat pas car p-value = 0.1798 > 0.05

# test de sta
kpss.test(X_interp) # on rejette la stationnarité car p-value = 0.01 < 0.05

## Question 3

DX = diff(X_interp) #Incrementation differentielle discrète
plot(DX,type = 'l')

# test de non sta
adf.test(DX) # on rejette la non stat pas car p-value = 0.01 < 0.05

# test de sta
kpss.test(DX) # on ne rejette pas la stationnarité car p-value = 0.1 > 0.05

acf(DX) # on pense à un modèle MA(1)
pacf(DX) #écroissance exponentielle 

#On voit que l'ACF a un pic en 1 puis plus rien

## Question 4
auto.arima(X_interp)
# Un ARIMA(0,1,1) centré est suggéré

#include.drift  = TRUE non significatif 
ARIMA = Arima(X_interp, order = c(0, 1, 1), include.drift  = TRUE)
ARIMA

plot(X_interp, type="l")
lines(fitted(ARIMA), type="l", col="red")
title("ARIMA(0,1,1)")


checkupRes(ARIMA$residuals,lagmax=40, lblag=5)# voir TP3 à charger 
#Test de Ljung-Box : p-val=0.743302 On ne rejette pas l'hypose de bruit blanc 
#Test de Shapiro : p-val=2.093974e-30 En revanche les résidus
#ne sont pas gaussiens au seuil d'erreur de 1%
dev.off()
 

## Question 5

FORECAST = forecast(ARIMA, h=50)
plot(FORECAST,type = "l")


