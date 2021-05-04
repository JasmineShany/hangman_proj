import math
import this

math.cos(3.14159265359)


def collatz(num):
    if num % 2 == 0:
        return num // 2

    return 3 * num + 1
