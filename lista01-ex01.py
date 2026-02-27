def classificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0: 
        return "negativo"
    else:
        return "neutro"
    
numero = int(input("Informe o número: "))
resultado = classificar_numero(numero)
print(f"O número {numero} é {resultado}")

