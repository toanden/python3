def caught_speeding(speed, is_dob = False):
    if is_dob: speed -= 5
    s = {
        speed in range(61): 0,
        speed in range(61, 81): 1,
        speed not in range(0, 81): 2,
    }
    return s.get(True)


""" 
print(caught_speeding(60))
print(caught_speeding(65))
print(caught_speeding(65, True))
print(caught_speeding(80)) """