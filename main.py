from hashlib import sha3_256
import itertools
from string import ascii_letters
import time


def brute_force(hash_to_decrypt, password_size: int):
    numbers_str = ''.join(str(x) for x in range(10))
    symbols = numbers_str + ascii_letters
    for counter, _ in enumerate(itertools.product(
            symbols,
            repeat=password_size)):
        password_variant = ''.join(_)
        password_hash = sha3_256(password_variant.encode()).hexdigest()
        if counter % 50000 == 0:
            print(f'Variants busted => {counter}')
        if password_hash == hash_to_decrypt:
            return password_variant


def main():
    message = '0' * 4092 + '1' * 4

    hashed_arr = sha3_256(message.encode())
    print(f'message      => {message}')
    print(f'message hash => {hashed_arr.hexdigest()}')

    start_time = time.time()
    hacked_password = brute_force(
        hashed_arr.hexdigest(),
        len(message))
    end_time = time.time()

    print(f'Password hacked! Result is {hacked_password}')
    print(f"Total brute force time: {end_time - start_time} seconds")


if __name__ == '__main__':
    main()
