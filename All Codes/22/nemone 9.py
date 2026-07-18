for number in range(2,51):
    is_prime=True
    for j in range(2,int(number**0.5)+1):
        if number%j==0:
            is_prime=False
            break
    if is_prime:
        print(number)
    
    
