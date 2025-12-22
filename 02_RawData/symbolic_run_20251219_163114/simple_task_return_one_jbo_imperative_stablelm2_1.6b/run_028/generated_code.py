R
# Función personalizada: return_1
return_1 <- function(x) {
  # Verifica si la entrada es un número real
  if (is.numeric(x)) {
    # Si es así, devuelve el número
    return(x)
  } else {
    # De lo contrario, genera una lista con los valores de x y une todas las listas en una sola lista
    result <- c(x, lapply(strsplit(gsub("[^0-9]", "", x), "\\s"), as.numeric)))
    return(result)
  }
}

# Ejemplo de uso:
x <- c(1, 2, 3, "a", "b")
result <- return_1(x)

print(result) # [1]   1   2   3  1  2
print(unlist(result)) # [1] 1 2 3