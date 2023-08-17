#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length <= 0:
        sequence = []
    elif length == 1:
        sequence = [0]
    elif length == 2:
        sequence = [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < length:
            next_sequence = sequence[-1] + sequence[-2]
            sequence.append(next_sequence)
    print(sequence)

