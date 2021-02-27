num = int(input("Enter the number"))

def check_prime(num):

  is_prime = True

  for i in range(2, num):
    if num % i == 0:
      is_prime = False

  if is_prime:
    print("It is a prime")
  else:
    print("Not a prime")  

check_prime(num)