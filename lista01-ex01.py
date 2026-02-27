def classificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0: 
        return "negativo"
    else:
        return "neutro ou 0"
resultado = classificar_numero(0)
print(resultado)

