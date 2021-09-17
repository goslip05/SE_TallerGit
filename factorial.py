def factorial(N): 
    if N < 0: 
        print("El factorial de un numero negativo no existe")
        return 
    elif N == 0: 
        return 1   
    else: 
        fact = 1
        while(N > 1): 
            fact *= N 
            N -= 1
        return fact 
N= int(input("Digite un numero: "))
print("El factorial de",N,"es: ", factorial(N))