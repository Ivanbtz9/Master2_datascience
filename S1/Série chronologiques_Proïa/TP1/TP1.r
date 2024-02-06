library(datasets)
library(tseries)
# dataset et stat sont directement chargé à l'entrée

Data = AirPassengers #class(Data) --> "ts"

# Créer un graphique (plot) de la série temporelle
plot(AirPassengers, main = "Nombre de passagers aériens mensuels", xlab = "Année", ylab = "Nombre de passagers")
grid()

# avec la règle des parallèles on voit que le modèle est multiplicatif car elles s'écartent 

LData = log(Data)
plot(LData, main = "Nombre de passagers aériens mensuels", xlab = "Année", ylab = "Nombre de passagers")
grid()

Decomp = decompose(LData, type = c("additive"), filter = NULL) #> help(decompose)

# Diviser la zone graphique en trois colonnes
par(mfrow = c(1, 3))

plot(Decomp$trend) #tendance
plot(Decomp$seasonal) #périodicité
plot(Decomp$random) #bruit


plot(Decomp$figure,type ='l')


plot(Decomp) # plot de toutes les infod

#### Trouver la tendance linéaire 

n = length(Decomp$trend)
Time = 1:n 
ntps = (n+1):(n+24)
m_linear = lm( Decomp$trend ~ Time )

summary(m_linear)

a0 = m_linear$coefficients[1]
a1 = m_linear$coefficients[2]

plot(Time,Decomp$trend, type = 'l', ylab = 'ytrend')
lines(Time,a0+ a1*Time, type = 'l', lty=2, ylab = 'nb_passenger',col = 'red')


ntps = (n+1):(n+24)
PredT = a0+ a1*ntps
PredS = Decomp$figure
Pred = PredT + PredS

plot(Time,LData, type = 'l', ylab = 'Log passenger')


plot(ts(c(LData,Pred), frequency = 12,start = 1949),ylab = 'Log passenger')
lines(ts(Pred, frequency = 12,start = 1961),col = 'red')
grid()

plot(ts(exp(c(LData,Pred)), frequency = 12,start = 1949),ylab = 'passenger')
lines(ts(exp(Pred), frequency = 12,start = 1961),col = 'red')
grid()




