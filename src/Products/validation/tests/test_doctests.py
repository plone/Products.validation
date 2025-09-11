from unittest import TestSuite

import doctest


def test_suite():
    suite = TestSuite()
    suite.addTest(
        doctest.DocTestSuite("Products.validation.validators.ExpressionValidator")
    )
    return suite
