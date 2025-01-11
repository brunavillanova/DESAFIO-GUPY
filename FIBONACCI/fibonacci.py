def pertence_a_fibonacci(numero):
  
    a, b = 0, 1


    while a <= numero:
        if a == numero:
            return True  
        a, b = b, a + b  
    
    return False  


numero = int(input("Digite um número: "))


if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
