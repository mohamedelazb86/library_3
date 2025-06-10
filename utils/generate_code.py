import random


def geneare_code(length=8):
    data='0123456789QWERTYUIOPLKJHGFDSAZXCVBNM'
    code=''.join(random.choice(data)for _ in range(length))
    return code