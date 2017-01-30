import random


def random_hash_generator():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(6))