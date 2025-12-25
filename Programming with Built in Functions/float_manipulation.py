import statistics

floats = []
for i in range(10):
    while True:

        enter_ten_numbers = float(input(f"Please enter 10 digits #{i + 1}: "))

        floats.append(enter_ten_numbers)
        break
print(floats)

sum_floats = sum(floats)
print(sum_floats)

float_max = max(floats)
max_index = floats.index(float_max)
print(max_index)

float_min = min(floats)
min_index = floats.index(float_min)
print(min_index)

float_mean = statistics.mean(floats)
float_mean_round = round(float_mean, 2)
print(float_mean_round)

float_median = statistics.median(floats)
print(float_median)