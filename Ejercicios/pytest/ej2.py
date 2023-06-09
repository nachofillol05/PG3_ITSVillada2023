def roman_to_decimal(roman_number):
    numeros ={'I': 1, 'V': 5,'X': 10, 'L': 50,'C': 100, 'D': 500,'M': 1000}
    
    roman_back = list(reversed(list(roman_number)))  
    value = 0
    right_val = numeros[roman_back[0]]  
    for num in roman_back:
        left_val = numeros[num]
        if left_val < right_val:
            value -= left_val
        else:
            value += left_val
        right_val = left_val
    return value
    