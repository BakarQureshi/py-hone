def prime_Numbers(number):

    if number == 1:

        return False
    
    elif number == 2:

        return True
    
    else:

        for i in range(2, number):

            if(number % i == 0):

                return False
            

        return True


number = int(input("Enter a number : "))

print(prime_Numbers(number))