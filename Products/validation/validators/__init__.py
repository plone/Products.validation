from Products.validation.validators.RegexValidator import RegexValidator
from Products.validation.validators.RangeValidator import RangeValidator
from Products.validation.validators.ExpressionValidator import ExpressionValidator

validators = []

from Products.validation.validators.BaseValidators import baseValidators
validators.extend(baseValidators)

from Products.validation.validators.EmptyValidator import validatorList
validators.extend(validatorList)

from Products.validation.validators.SupplValidators import validatorList
validators.extend(validatorList)

from Products.validation.validators.IdValidator import validatorList
validators.extend(validatorList)


def initialize(service):
    for validator in validators:
        service.register(validator)
