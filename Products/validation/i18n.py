from zope.i18n import translate
from zope.i18nmessageid import MessageFactory


PloneMessageFactory = MessageFactory("plone")


def safe_unicode(value):
    return value


def recursiveTranslate(message, **kwargs):
    """translates also the message mappings before translating the message.

    if kwargs['REQUEST'] is None, return the message untranslated

    Actually, recursive translation has been built into zope.i18n 3.5.0,
    which was already released in 2008.  See
    https://github.com/zopefoundation/zope.i18n/blob/master/CHANGES.rst#350-2008-07-10

    So we can simply call the translate function.
    This avoids a TypeError in Zope 5.11+, as `map[key]` is immutable there.
    """
    request = kwargs.get("REQUEST", None)
    return translate(message, context=request)
