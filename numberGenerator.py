import random

def generate_random_numbers(num_count):
    random_numbers = []
    for _ in range(num_count):
        # Generate a random number between 1 and 9999
        rand_num = random.randint(1, 9999)
        # Format the number to have leading zeros if needed
        formatted_num = '{:04d}'.format(rand_num)
        random_numbers.append(formatted_num)
    return random_numbers

# Number of random numbers to generate
num_count = 50

# Generate and print the random numbers
random_numbers = generate_random_numbers(num_count)
for num in random_numbers:
    print(num)