# This module gathers a list of validators, and registers them to the service.
#
# Three of these are backwards compatibility imports, marked with 'noqa F401'
# for flake8.  Of these, the RangeValidator and RegexValidator are included in
# baseValidators, so that is fine.
# ExpressionValidator is not included.  This is because you need to create an
# instance of a validator class and register this.  The ExpressionValidator
# class is fine as base for your custom validators, but no one thought of
# a default instance to add here.
from Products.validation.validators.BaseValidators import baseValidators
from Products.validation.validators.EmptyValidator import (
    validatorList as emptyValidators,
)
from Products.validation.validators.ExpressionValidator import (  # noqa F401
    ExpressionValidator,
)
from Products.validation.validators.IdValidator import validatorList as idValidators
from Products.validation.validators.RangeValidator import RangeValidator  # noqa F401
from Products.validation.validators.RegexValidator import RegexValidator  # noqa F401
from Products.validation.validators.SupplValidators import (
    validatorList as supplValidators,
)


validators = []
validators.extend(baseValidators)
validators.extend(emptyValidators)
validators.extend(supplValidators)
validators.extend(idValidators)


def initialize(service):
    for validator in validators:
        service.register(validator)
