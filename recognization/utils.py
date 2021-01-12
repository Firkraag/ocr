import os
import random
import time


def random_image_name(filename):
    ext = os.path.splitext(filename)[1]
    return str(int(time.time()) + random.randint(1, 10000)) + ext