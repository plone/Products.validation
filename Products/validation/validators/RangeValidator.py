from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implements
from Products.validation.i18n import PloneMessageFactory as _
from Products.validation.i18n import recursiveTranslate

class RangeValidator:
    implements(IValidator)

    def __init__(self, name, minval=0.0, maxval=0.0, title='', description=''):
        self.name = name
        self.minval = minval
        self.maxval = maxval
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):
        if len(args)>=1:
            minval=args[0]
        else:
            minval=self.minval

        if len(args)>=2:
            maxval=args[1]
        else:
            maxval=self.maxval

        assert(minval <= maxval)
        try:
            nval = float(value)
        except ValueError:
            msg = _(u"Validation failed($name): could not convert '$value' to number",
                    mapping = { 'name' : self.name, 'value': value})
            return recursiveTranslage(msg, **kwargs)
        if minval <= nval < maxval:
            return 1

        msg = _(u"Validation failed($name): '$value' out of range($min, $max)",
                mapping = { 'name' : self.name, 'value': value, 'min' : minval, 'max' : maxval,})
        return recursiveTranslate(msg, **kwargs)
