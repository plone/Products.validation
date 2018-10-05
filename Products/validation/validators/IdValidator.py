from Acquisition import aq_parent
from Acquisition import aq_inner
from Acquisition import aq_base
from Acquisition import aq_get
from zExceptions import BadRequest
from OFS import ObjectManager
from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implementer
from Products.validation.i18n import PloneMessageFactory as _
from Products.validation.i18n import recursiveTranslate
from Products.validation.i18n import safe_unicode


def fallback_check_id(instance, id, **kwargs):
    # space test
    if ' ' in id:
        msg =  _(u'Spaces are not allowed in ids')
        return recursiveTranslate(msg, **kwargs)

    # in parent test
    parent = aq_parent(aq_inner(instance))
    # If the id is given to a different object already
    if (id in parent.objectIds() and
            getattr(aq_base(parent), id) is not aq_base(instance)):
        msg = _(u'Id $id is already in use',
                mapping = {'id': safe_unicode(id)})
        return recursiveTranslate(msg, **kwargs)

    # object manager test
    try:
        # Note: we used to pass 'self' (the validator) instead of 'instance',
        # which makes no sense.
        ObjectManager.checkValidId(instance, id, allow_dup=1)
    except BadRequest as m:
        return str(m)
    return 1


@implementer(IValidator)
class IdValidator:

    def __init__( self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, id, instance, *args, **kwargs):
        # Try to get a check_id from the instance,
        # for example a Python skin script or a method,
        # like Products/CMFPlone/skins/plone_scripts/check_id.py
        # until Plone 5.1.
        check_id = aq_get(instance, 'check_id', None, 1)
        if check_id is None:
            try:
                # try to use the check_id script of CMFPlone
                # Import here to avoid a hard dependency and
                # possible cyclic imports.
                from Products.CMFPlone.utils import check_id
            except ImportError:
                # Use our own fallback function.
                check_id = fallback_check_id
        result = check_id(instance, id, **kwargs)
        return result or 1


validatorList = [
    IdValidator('isValidId', title='', description=''),
    ]

__all__ = ('validatorList', )
