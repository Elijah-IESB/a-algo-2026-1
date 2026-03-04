import random
import os

# List of sizes
sizes = [1000, 5000, 10000, 20000, 50000]

# Generate and save random lists
for size in sizes:
    random_list = [random.randint(0, 100) for _ in range(size)]
    filename = f'random_list_{size}.txt'
    with open(os.path.join('devores-de-casa', 'dever-01', filename), 'w') as f:
        for number in random_list:
            f.write(f'{number}\n')
