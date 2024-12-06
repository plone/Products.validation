from zope.i18n import translate
from zope.i18nmessageid import Message
from zope.i18nmessageid import MessageFactory


PloneMessageFactory = MessageFactory("plone")


def safe_unicode(value):
    return value


def recursiveTranslate(message, **kwargs):
    """translates also the message mappings before translating the message.
    if kwargs['REQUEST'] is None, return the message untranslated
    """

    request = kwargs.get("REQUEST", None)

    map = message.mapping
    if map:
        for key in map.keys():
            if isinstance(map[key], Message):
                try:
                    map[key] = translate(map[key], context=request)
                except TypeError:
                    # In zope.i18nmessageid 7.0+ the mapping is an immutable
                    # 'mappingproxy' due to some C changes for Python 3.13
                    # support.  Without further investigation I don't know
                    # if this is properly fixable or even if recursiveTranslate
                    # is no longer needed.  For now work around it:
                    # leave this part untranslated.
                    break

    return translate(message, context=request)
