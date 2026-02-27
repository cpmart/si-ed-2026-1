def classificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0: 
        return "negativo"
    else:
        return "neutro ou 0"
resultado = classificar_numero(0)
print(resultado)

