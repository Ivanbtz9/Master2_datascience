library(TTR)
library(TSA)
library(quantmod)
library(tseries)

getSymbols("BTC-USD", src = "yahoo", from = "2007-01-01", to = Sys.Date())

#Question 1
start_date = as.Date("2022-01-01")
end_date = as.Date("2023-01-01")
Log_BTC = log(BTC$`BTC-USD.Close`)
Log_BTC_subset = Log_BTC[(index(Log_BTC) >= start_date) & (index(Log_BTC)<=end_date )]
plot(Log_BTC_subset)

#Question 2 

# Créer une séquence de temps
time_seq <- 1:length(Log_BTC_subset)

# Ajuster un modèle linéaire à la série temporelle
model <- lm(Log_BTC_subset ~ time_seq)
summary(model)

# Retrancher la tendance linéaire
Res <- Log_BTC_subset - fitted(model)

# Tracer la série sans tendance
plot(Res, main="Série temporelle sans tendance linéaire")

#Vérifier que ce n'est pas un bruit blanc
checkupRes(as.numeric(Res))

# test de non sta
adf.test(Res) # on ne rejette pas

# test de sta
kpss.test(Res) # on ne rejette pa 

#Question 2 avec Arima 
library(forecast)
# Ajuster un modèle ARIMA sans dérive
model_Arima = Arima(Log_BTC_subset, order=c(1,0,0), include.drift=TRUE)
#utilisation de include.drift dans la commande Arima pour la tendance linéaire
# Obtenir les résidus du modèle ARIMA
arima_no_tendance <- residuals(model_arima)
# Tracer la série sans tendance
plot(arima_no_tendance, main="Série temporelle sans tendance (Arima avec dérive)")

adf.test(arima_no_tendance)
kpss.test(arima_no_tendance)

summary(model_Arima)

#Question 3

#Avec un AR(1)
ARMA = Arima(Res, order = c(1, 0, 0), include.drift = FALSE)
summary(ARMA) 
plot(as.numeric(Log_BTC_subset), type="l")
lines(fitted(ARMA) + as.numeric(fitted(model)), type="l", col="blue")

#Avec AUTO_ARIMA on trouve Un MA 5
ARIMA = auto.arima(Log_BTC_subset, d=0)
plot(as.numeric(Log_BTC_subset),type='l' ,col='black')
lines(fitted(ARIMA),type='l' ,col='red')

#Test avec avec les nouveaux résidus 

# Avec auto.ARIMA
Res1 = as.numeric(Log_BTC_subset) - fitted(ARIMA)
checkupRes(Res1)

# Avec auto.ARIMA
Res2 = as.numeric(Log_BTC_subset) - as.numeric(fitted(ARMA)) - as.numeric(fitted(model))
checkupRes(Res2)

Mod = as.numeric(fitted(ARMA)) + as.numeric(fitted(model))
n = length(BS)
BS = Mod +1.96*sqrt(ARMA$sigma2)
BI = Mod -1.96*sqrt(ARMA$sigma2)

plot(BS,col='red',type='l',lty = 2)
lines(BI,col='red',type='l',lty=2)
polygon(c(1:n, n:1), c(BI,rev(BS)),col='grey',border = 'red' )
lines(as.numeric(Log_BTC_subset), type="l")

#Repasser à l'expo
plot(exp(as.numeric(Log_BTC_subset)), type="l")
lines(exp(BS),col='red',type='l',lty = 2)
lines(exp(BI),col='red',type='l',lty=2)
grid()
title('BTC encadré par un modèle mutiplicatif: régression linéaire et AR(1)')




