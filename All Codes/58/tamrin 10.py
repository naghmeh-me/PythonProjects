#1
def is_prime(number):
    if n<=1:
        return "False"
    else:
        if n<=3:
            return "True"
        else:
            if n%2==0 and n%3==0:
                return "False"
            else:
                i=5
                while i*i<=n:
                    if n%i==0 or n%(i+2)==0:
                        return "False"
                    else:
                        i+=6
                    return "True"

n=int(input("enter a number:"))

if is_prime(n)=="True":
    print(f"{n} is a prime number.")
else:
    print(f"{n} isn't a prime number.")
            
        
