def sum_of_digits(num):
    sum = 0
    for digit in str(num): sum += int(digit)
    return sum

print(sum_of_digits(123))