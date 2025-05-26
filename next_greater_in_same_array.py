def next_greater_element(nums: list[int]) -> list[int]:
    lista = []
    
    for i in range(len(nums)):
        number = -1                 
        for i2 in range(i+1,len(nums)):            
            if nums[i2] > nums[i]:
                number = nums[i2]
                break
        lista.append(number)
    return lista

arr = [4, 5, 2, 25]
resultado = next_greater_element(arr)
print(resultado)  # Output: [5, 25, 25, -1]