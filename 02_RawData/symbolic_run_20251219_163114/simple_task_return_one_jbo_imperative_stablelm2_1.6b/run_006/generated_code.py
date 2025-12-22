R
# Función return_1
return_1 <- function(x) {
  # Verifica si el valor es un número real
  if (is.numeric(x)) {
    # Si lo es, devuelve el valor
    return(x)
  } else {
    # Si no es un número real, intenta convertirlo a uno y luego devuelva la función llamada 'return_1'
    return(apply(x, 2, function(x) ifelse(is.na(x), return_1(x), x)))
  }
}

# Ejemplo de uso
x <- c(1, 2, 3)
print(return_1(x))