library(evir)

path = "/home/ibotcazou/Bureau/Master_data_science/DATAS_M2/valeurs_extrêmes/Jeux de données-20240125"

files <- list.files(path = path, full.names = TRUE)

### Fréchet

F_inv = function (u,g){
  return (-log(u)**(-g))
}

n = 1000
uniform_vars <- runif(n, min = 0, max = 1)
g = 1

# Afficher les valeurs
Frechet_n = F_inv(uniform_vars,g)

hist(Frechet_n)

