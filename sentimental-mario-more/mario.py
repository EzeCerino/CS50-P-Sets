# TODO
from cs50 import get_int


def main():
    height = get_height()
    s = height-1
    for i in range(height):
        print(" "*s + "#"*(i+1), end=" ")
        print("#"*(i+1))
        s = s - 1


def get_height():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:
            return n


main()