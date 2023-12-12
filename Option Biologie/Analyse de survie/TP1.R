library(survival)
library(ggplot2)
library(ggpubr)

library(survminer)

data(diabetic)
head(diabetic)

#vision global
fit.global <- survfit(Surv(time,status) ~ 1,data = diabetic)
ggsurvplot(fit.global, ggtheme = theme_minimal())

#Traitement ou non 
fit.trait <- survfit(Surv(time,status) ~ trt,data = diabetic)
ggsurvplot(fit.trait, ggtheme = theme_minimal())

#traitement et age , beacoup de cencuse pour le plus de 35 ans traité  
diabetic$age <- as.numeric(diabetic$age >= 35) #1 si plus de 35 ans 
fit.trait.age <- survfit(Surv(time,status) ~ trt + age,data = diabetic)
ggsurvplot(fit.trait.age, risk.table = TRUE, ggtheme = theme_minimal())






