def HappyNumber(Number):
    
    result = Number

    while True:
        suma = 0

        for i in str(result):
            suma += int(i)**2

        result = suma

        if result == 1 or result == 4:
            break
            
    return result == 1


print(HappyNumber(7))
print(HappyNumber(9))
print(HappyNumber(19))
        #       3**2=9    sum = 10
        # result = sum  (10)
        #sum = 0
        #       1**2=1    sum = 1
        #       0**2=0    sum = 1
        #Numero feliz si la suma es 1
        #Numero no feliz si la suma es 4(llega al infinito)