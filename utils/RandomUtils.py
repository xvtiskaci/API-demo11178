import random
import string


class RandomUtils:

    @staticmethod
    def string(length):
        return ''.join(random.choices(string.ascii_lowercase +
                                      string.digits, k=length))

    @staticmethod
    def integer(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return random.randint(range_start, range_end)

    @staticmethod
    def password():
        length = 8
        while True:
            password = ''.join(
                random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            if (any(c.islower() for c in password) and
                    any(c.isupper() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                return password
