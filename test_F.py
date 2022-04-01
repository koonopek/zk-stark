import unittest
unittest.TestLoader.testMethodPrefix = 'should'
from unittest import TestCase as Specification
from F import F,xgcd

F7 = F.WithPrime(7)

class Testxgcd(Specification):

    def should_work(self):
        (a,b,g) = xgcd(10, 15)
        self.assertEqual(a * 10 + b* 15, g)
        self.assertEqual(g, 5)


class TestF(Specification):

    def should_add_two_fields(self):
        self.assertEqual(F7(5), F7(5) + F7(21))
    
    def should_mul_two_fields(self):
        self.assertEqual(F7(5) * F7(3), F7(1))

    def should_sub_two_fields(self):
        self.assertEqual(F7(13) - F7(5), F7(1))
        self.assertEqual(F7(5) - F7(13), F7(6))

    def should_inverse(self):
        self.assertEqual(F7(36).inverse(), F7(1))
        self.assertEqual(F7(3).inverse().value, -2)

    def should_div(self):
        # F7(3).inverse => -2
        # F7(15) => 1
        # F7(1) * F7(-2) => -F7(2) => F7(5)
        self.assertEqual(F7(15) / F7(3), F7(5))

    def should_neg(self):
        self.assertEqual(-F7(2), F7(5))

    def should_modular_exponentiation(self):
        # 10 * 10 => 9 => F7(2)
        # 10 * 2  => 20 => F7(6)
        self.assertEqual(F7(10) ^ 3, F7(6))

    def should_return_sub_group_for_given_n(self):
        P = F.WithPrime()
        P(0).sub_group_generator(4)
    
    def should_return_generator(self):
        P = F.WithPrime()
        P(0).generator()

