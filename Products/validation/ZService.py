from AccessControl import ClassSecurityInfo
from AccessControl import ModuleSecurityInfo
from AccessControl.class_init import InitializeClass
from Acquisition import Implicit
from Products.validation.service import Service


# make validator service public
security = ModuleSecurityInfo('Products.validation.config')
security.declarePublic('validation')

class ZService(Service, Implicit):
    """Service running in a zope site - exposes some methods"""

    security = ClassSecurityInfo()

    security.declarePublic('validate')
    security.declarePublic('__call__')
    security.declarePublic('validatorFor')

InitializeClass(ZService)
