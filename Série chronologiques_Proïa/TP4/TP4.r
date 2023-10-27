
library(TSA)

# Donn?es réelles de conso électrique
data(electricity)
plot(electricity)
Y = log(electricity)
plot(Y)

# D?composition additive sur le log puis mod?lisation ARMA sur la fluctuation
Decomp = decompose(Y)
plot(Decomp)
Res = Decomp$random



checkupRes = function(Res){
  layout(matrix(c(1,1,1,2:7), nrow=3, ncol=3, byrow=TRUE))
  #plot1
  Res = Res[!is.na(Res)] #différent des Nan
  plot(Res,type = 'l',xlab='',ylab='',main = "Évolution de la série")
  #plot2
  ACF = acf(Res, lag.max = 20,plot = FALSE)
  plot(ACF,xlab='',ylab='',ylim=c(-1,1),main = "ACF")
  #plot3
  PACF = pacf(Res, lag.max = 50,plot = FALSE)
  plot(PACF,xlab='',ylab='',ylim=c(-1,1),main = "PACF")
  #plot4
  n = length(Res)
  plot(Res[1:(n-1)],Res[2:n],type='p',col='violet',main = 'Relation entre les résidus') # voir une structure ou non
  #plot5
  hist(Res, main= 'Histogramme des résidus', freq=FALSE) 
  curve(dnorm(x, mean=mean(Res), sd=sd(Res)),type = 'l',col='red', add=TRUE)
  #rajouter la densité Gaussienne sur l'histogramme
  
  #plot6
  qqnorm(Res)
  qqline(Res)
  
  #plot7
  z_scores = (Res - mean(Res)) / sd(Res)
  plot(z_scores, type = 'p', col = 'blue', main = 'Nuage de points de la série renormalisée')
  abline(h = c(-1.96, 1.96), col = 'red', lty = 2)

}

checkupRes(Res)

dev.off() #Pour ne plus utiliser l'env plot