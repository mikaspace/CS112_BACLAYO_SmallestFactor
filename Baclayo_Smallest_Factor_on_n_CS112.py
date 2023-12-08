while True:
    num_int = int(input('Enter a number greater or equal to 2: '))
    if num_int < 2:
        print('Invalid number. Please enter a number greater or equal to 2')
        break

    else:
        smallest = None
        for i in range(2, int(num_int**0.5) + 1):
            if num_int % i == 0:
                smallest = i
                break
        if smallest:
            print(f'The smallest factor of {num_int} is {smallest}')
        else:
            print(f'{num_int} is a prime number. Its smallest factor is itself.')