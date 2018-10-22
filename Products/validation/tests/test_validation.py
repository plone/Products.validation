# -*- coding: utf-8 -*-
from Products.validation import validation

import doctest
import six
import unittest


class Dummy(object):
    """Dummy object with basic zope-like containment."""
    portal_type = 'dummy'  # needed in Plone 5.2 test

    def __init__(self, _id=None):
        self.id = _id
        self._ids = []
        self._items = []

    def add(self, item):
        self._ids.append(item.id)
        self._items.append(item)
        item.__parent__ = self

    def getId(self):
        return self.id

    def getParentNode(self):
        return self.__parent__

    def objectIds(self):
        return self._ids

    def __contains__(self, id):
        return id in self._ids

    def __getattr__(self, name, default=None):
        if name in self._ids:
            for obj in self._items:
                if obj.getId() == name:
                    return obj
            return default
        return super(Dummy, self).__getattr__(name, default)

    def dummy_checker(self, _id, **kwargs):
        if _id == 'good':
            return 1
        return 'bad id'


class TestValidation(unittest.TestCase):

    def test_inNumericRange(self):
        v = validation.validatorFor('inNumericRange')
        self.assertEqual(v(10, 1, 20), 1)
        self.assertEqual(v('10', 1, 20), 1)
        self.assertEqual(v(0, 4, 5), u"Validation failed(inNumericRange): '0' out of range(4, 5)")

    def test_isDecimal(self):
        v = validation.validatorFor('isDecimal')
        self.assertEqual(v('1.5'), 1)
        self.assertEqual(v('1,5'), 1)
        self.assertEqual(v('NaN'), u"Validation failed(isDecimal): 'NaN' is not a decimal number.")

    def test_isPrintable(self):
        v = validation.validatorFor('isPrintable')
        self.assertEqual(v('text'), 1)
        self.assertEqual(
            v('\\u203'),
            u"Validation failed(isPrintable): '\\u203' contains unprintable characters"
        )
        if six.PY3:
            int_type = "<class 'int'>"
        else:
            int_type = "<type 'int'>"
        self.assertEqual(
            v(10),
            u"Validation failed(isPrintable): 10 of type {0}, expected 'string'".format(int_type)
        )

    def test_isSSN(self):
        v = validation.validatorFor('isSSN')
        self.assertEqual(v('111223333'), 1)
        self.assertEqual(v('111-22-3333', ignore=r'-'), 1)

    def test_isUSPhoneNumber(self):
        v = validation.validatorFor('isUSPhoneNumber')
        self.assertEqual(v('(212) 555-1212',
                               ignore=r'[\s\(\)\-]'), 1)
        self.assertEqual(v('2125551212',
                               ignore=r'[\s\(\)\-]'), 1)

        self.assertEqual(v('(212) 555-1212'), 1)

    def test_isURL(self):
        v = validation.validatorFor('isURL')
        self.assertEqual(v('http://foo.bar:8080/manage'), 1)
        self.assertEqual(v('https://foo.bar:8080/manage'), 1)
        self.assertEqual(v('https://be.brussels:8080/manage'), 1)
        self.assertEqual(v('irc://tiran@irc.freenode.net:6667/#plone'), 1)
        self.assertEqual(v('fish://tiran:password@myserver/~/'), 1)
        self.assertEqual(v('http://\n'), u"Validation failed(isURL): 'http://\n' is not a valid url.")
        self.assertNotEqual(v('../foo/bar'), 1)

    def test_isEmail(self):
        v = validation.validatorFor('isEmail')
        self.assertEqual(v('test@test.com'), 1)
        self.assertEqual(v('test@be.brussels'), 1)
        self.assertNotEqual(v('@foo.bar'), 1)
        self.assertEqual(v('me'), u"Validation failed(isEmail): 'me' is not a valid email address.")

    def test_isMailto(self):
        v = validation.validatorFor('isMailto')
        self.assertEqual(v('mailto:test@test.com'), 1)
        self.assertEqual(v('mailto:test@be.brussels'), 1)
        self.assertNotEqual(v('test@test.com'), 1)
        self.assertNotEqual(v('mailto:@foo.bar'), 1)
        self.assertNotEqual(v('@foo.bar'), 1)
        self.assertNotEqual(v('mailto:'), 1)
        self.assertEqual(v('me'), u"Validation failed(isMailto): 'me' is not a valid email address.")

    def test_isUnixLikeName(self):
        v = validation.validatorFor('isUnixLikeName')
        self.assertEqual(v('abcd'), 1)
        self.assertTrue(v('a_123456'), 1)
        self.assertNotEqual(v('123'), 1)
        self.assertNotEqual(v('ab.c'), 1)
        self.assertEqual(v('ab,c'), u"Validation failed(isUnixLikeName): 'ab,c' this name is not a valid identifier")
        self.assertNotEqual(v('aaaaaaaab'), 1) # too long

    def test_isValidId_basic(self):
        from Products.validation.validators import IdValidator

        v = validation.validatorFor('isValidId')
        obj = Dummy('foo')

        # Use a specific checker.
        obj.check_id = obj.dummy_checker
        self.assertEqual(v('good', obj), 1)
        self.assertEqual(v('a b', obj), 'bad id')

    def test_isValidId_plone(self):
        from Products.validation.validators import IdValidator
        try:
            from Products.CMFPlone.utils import check_id
        except ImportError:
            return

        v = validation.validatorFor('isValidId')
        obj = Dummy('foo')
        obj2 = Dummy('foo2')
        parent = Dummy('parent')
        parent.add(obj)
        parent.add(obj2)

        self.assertEqual(v('good', obj), 1)
        self.assertEqual(v('foo', obj), 1)
        # This error message would be translated usually, but we do not care.
        self.assertEqual(
            v('foo', obj2),
            u'There is already an item named ${name} in this folder.')
        # Plone seems to allow spaces.
        self.assertEqual(v('a b', obj), 1)
        # Some ids are forbidden in Plone.  We get an i18n message back.
        # Problem: on Plone 5.1, utils.check_id simply looks for a
        # check_id script/attribute on the context.  This will fail.
        # So only test this in Plone 5.2+, not on 5.1.
        import pkg_resources
        version = pkg_resources.get_distribution('Products.CMFPlone').version
        if version.startswith('5.1'):
            return
        self.assertEqual(v('layout', obj), '${name} is reserved.')

    def test_isValidId_fallback(self):
        from Products.validation.validators import IdValidator
        # We can only check this if utils.check_id gives an ImportError.
        try:
            from Products.CMFPlone.utils import check_id as plone_check_id
        except ImportError:
            plone_check_id = None
        else:
            import Products.CMFPlone.utils
            del Products.CMFPlone.utils.check_id

        try:
            v = validation.validatorFor('isValidId')
            obj = Dummy('foo')
            parent = Dummy('parent')
            parent.add(obj)
            self.assertEqual(v('good', obj), 1)
            self.assertEqual(v('foo', obj), 1)
            self.assertEqual(v('a b', obj), u'Spaces are not allowed in ids')
        finally:
            if plone_check_id:
                Products.CMFPlone.utils.check_id = plone_check_id


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestValidation))

    doctests = (
        'Products.validation.validators.ExpressionValidator',
        )
    for module in doctests:
        suite.addTest(doctest.DocTestSuite(module))

    return suite
