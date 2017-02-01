import random
import uuid
import base64


def random_hash_generator():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(6))


def uuid4_hash_generator():
    return str(base64.b64encode(str(uuid.uuid4()).encode('utf-8')))[-7:]
