import doctest
import unittest


def test_suite():
    from unittest import TestSuite

    suite = TestSuite()

    doctests = ("Products.validation.validators.ExpressionValidator",)
    for module in doctests:
        suite.addTest(doctest.DocTestSuite(module))

    return suite
