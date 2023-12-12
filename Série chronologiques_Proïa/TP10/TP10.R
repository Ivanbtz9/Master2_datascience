library("tseries")
library("forecast")

data("AirPassengers")

plot(AirPassengers)

LAP = log(AirPassengers)
plot(LAP,main="log passenger",xlab='time')

LAPd1 = diff(LAP)
plot(LAPd1,main="log passenger d1",xlab='time') #Reste périodique avec un motif

LAPD12 = diff(LAP,lag = 12)
plot(LAPD12,main="log passenger D12",xlab='time')#Semble non stationnaire

LAPd1D12 = diff(diff(LAP,lag = 12))
plot(LAPd1D12,main="log passenger d1 et D12",xlab='time')# semble stationnaire
adf.test(LAPd1D12)#rejeté
kpss.test(LAPd1D12)#non rejeté


# ACF/PACF
ACF = acf(as.numeric(LAPd1D12), lag = 100, plot = FALSE)
plot(ACF, xlab = "", ylab = "", main = "")
title("ACF - LAPd1D12  - lagmax")


PACF = pacf(as.numeric(LAPd1D12), lag = 100, plot = FALSE)
plot(PACF, xlab = "", ylab = "", main = "")
title("PACF - LAPd1D12  - lagmax")


#SARIMA(1, 0, 1) × (0, 1, 1)12
SARIMA = Arima(LAP,order=c(1, 0, 1), seasonal= list (order = c(0,1,1),period=12), include.drift = TRUE)

summary(SARIMA) #BIC=-474.77

checkupRes(SARIMA$residuals,lagmax=40, lblag=5)
dev.off()


plot(LAP,type="l",lwd=2,xlab = 'Time')
lines(fitted(SARIMA), col = "red")
lines(fitted(SARIMA) - sqrt(SARIMA$sigma2)*1.96,type="l",lty = 2,col = "purple")
lines(fitted(SARIMA) + sqrt(SARIMA$sigma2)*1.96,type="l",lty = 2,col = "purple")
grid()

##AUTO ARIMA
model_auto = auto.arima(LAP, ic = "bic",max.p = 5, max.q = 5,max.d=1,max.P = 1, max.Q = 1,max.D=1) 
summary(model_auto) #BIC=-474.77

plot(LAP,type="l",lwd=2,xlab = 'Time')
lines(fitted(model_auto), col = "red")
lines(fitted(model_auto) - sqrt(model_auto$sigma2)*1.96,type="l",lty = 2,col = "purple")
lines(fitted(model_auto) + sqrt(model_auto$sigma2)*1.96,type="l",lty = 2,col = "purple")
grid()

checkupRes(model_auto$residuals,lagmax=40, lblag=5)
dev.off()


### Comment choisir le meilleur modèle avec de la cross validation

n= length(LAP)
LAP_T = LAP[1:(n-12)]
LAP_Tp = LAP[(n-11):n]

model1T = Arima(LAP_T,order=c(1, 0, 1), seasonal= list (order = c(0,1,1),period=12), include.drift = TRUE)
model2T =  Arima(LAP_T,order=c(0, 1, 1), seasonal= list (order = c(0,1,1),period=12))


Pred1T = forecast(model1T,h=12) #prediction à 12 temps plus tard
plot(Pred1T)

Pred2T = forecast(model2T,h=12)
plot(Pred2T)

# Tracer les vraies valeurs
plot(LAP_Tp, main="Prédictions ARIMA", ylab="Valeurs", xlab="Temps", col="blue", type="o")
# Ajouter les prédictions du modèle 1
lines(as.numeric(Pred1T$mean), col="red", type="o")
# Ajouter les prédictions du modèle 2
lines(as.numeric(Pred2T$mean), col="green", type="o")
# Ajouter une légende
legend("topright", legend=c("Vraies Valeurs", "Modèle 1", "Modèle 2"), 
       col=c("blue", "red", "green"), lty=1, cex=0.8)


###Caluler le risque quadratique au carré

# Pour le modèle 1
erreurs1 = LAP_Tp - Pred1T$mean
MSE1 = mean(erreurs1^2)

# Pour le modèle 2
erreurs2 = LAP_Tp - Pred2T$mean
MSE2 = mean(erreurs2^2)

# Afficher les erreurs
print(paste("MSE pour le modèle 1 :", MSE1))
print(paste("MSE pour le modèle 2 :", MSE2))

####Retour aux vraies valeurs avec prédiction de deux nouvelles années  
model2 =  Arima(LAP,order=c(0, 1, 1), seasonal= list (order = c(0,1,1),period=12))
pred24 = forecast(model2,h=24) #2 ans 


pred_init = exp(as.numeric(pred24$mean)+model2$sigma2/2)
Ntps = (n+1):(n+24)
# Tracé des vraies valeurs
plot((1:n), AirPassengers, type = 'l', lwd=2,xlab = 'Mois', ylab = "Nombre de passagers",xlim=c(1, n+24), ylim=c(min(AirPassengers), max(c(AirPassengers, pred_init))))
lines(Ntps, pred_init, col='red')
lines(c(n+1,n+48),exp(as.numeric(pred24$lower)), col='purple',type = 'l',lty = 2)
lines(c(n+1,n+48),exp(as.numeric(pred24$upper)), col='purple',type = 'l',lty = 2)

length(exp(as.numeric(pred24$upper)))
title("Prédictions ARIMA avec intervalles de confiance")










