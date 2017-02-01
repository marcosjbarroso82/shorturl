import random
import uuid

def random_hash_generator():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(6))

def uuid4_hash_generator():
    return '%s32x' % str(uuid.uuid4()).replace('-','')[:8]