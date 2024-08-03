def geometric_sequence(start, ratio, terms):
    sequence = [start * (ratio ** i) for i in range(terms)]
    return sequence
print(geometric_sequence(2, 3, 6))