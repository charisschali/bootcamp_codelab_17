import unittest
from prime_number import gen_prime_number


class Generate_prime_numbers(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(gen_prime_number(10), [2, 3, 5, 7])

    def test_returns_error_msg_if_value_is_negative(self):
        self.assertEquals(gen_prime_number(-10), 'Invalid input')

    def test_returns_error_msg_if_value_is_zero(self):
        self.assertEquals(gen_prime_number(0), 'Invalid input')

    def test_returns_error_msg_if_value_not_variable_type(self):
        self.assertRaises(ValueError, gen_prime_number, 'ten')

    def test_if_list(self):
        try:
            assert type(gen_prime_number(10)) is list
        except AssertionError:
            raise(AssertionError("Wrong type"))

    def test_if_four_not_prime(self):
        self.assertNotIn(4, gen_prime_number(10))

if __name__ == '__main__':
    unittest.main()
