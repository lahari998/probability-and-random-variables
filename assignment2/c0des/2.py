import random

def calculate_probability(num_trials):
    positive_count = 0

    for _ in range(num_trials):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0, 1)
        d = random.randint(0, 1)

        if a * d - b * c > 0:
            positive_count += 1

    probability = positive_count / num_trials
    return probability

# Set the number of trials for the simulation
num_trials = 9000000

# Calculate the probability
probability = calculate_probability(num_trials)

print(f"The probability that the value of the determinant is positive is: {probability}")
