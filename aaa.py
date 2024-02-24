import sys

print(f'args: {sys.argv}')

def print_hello(i):
    print(f"Hello {i}")

i = 0
while True:
    print_hello(i)
    i += 1
