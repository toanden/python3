def lucky_sum(a, b, c):
    li = [a, b, c]
    sum = 0
    for num in li:
        if num == 13: break
        sum += num
    return sum

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 13))
