##############################################################################
#
# TALESField - Field with TALES support for Archetypes
# Copyright (C) 2005 Sidnei da Silva, Daniel Nouri and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
##############################################################################
"""
$Id: __init__.py,v 1.2 2005/02/26 17:56:10 sidnei Exp $
"""

from Products.validation.interfaces.IValidator import IValidator
from Products.PageTemplates.Expressions import getEngine
from zope.interface import implements

class ExpressionValidator:
    """ Validator for TALES Expressions

    Basically, if the expression compiles it's a valid expression,
    otherwise it's invalid and you get a message saying that the
    expression has errors.

    
    >>> val=ExpressionValidator('python: int(value) == 5')
    >>> class C:i=1
    >>> c=C()
    >>> val(5,c) is True
    True

    now lets fail a test
    >>> val(4,c) 
    'validation failed, expr was:python: int(value) == 5'
    
    It is also possible to specify the error string
    
    >>> val=ExpressionValidator('python: int(value) == 5', 'value doesnt match %(value)s')
    >>> val(4,c) 
    'value doesnt match 4'
    
       
    """

    implements(IValidator)

    name = 'talesexpressionvalidator'
    
    def __init__(self,expression=None,errormsg=None):
        self.expression=expression
        self.errormsg=errormsg
        if expression:
            self.compiledExpression=getEngine().compile(expression)

    def __call__(self, value, instance, *args, **kwargs):
        kw={
           'here':instance,
           'object':instance,
           'instance':instance,
           'value':value,
           'args':args,
           'kwargs':kwargs,
           }
           
        context=getEngine().getContext(kw)
        res=self.compiledExpression(context)
        
        if res:
            return True
        else:
            if self.errormsg:
                return self.errormsg % kw
            else:
                return 'validation failed, expr was:'+self.expression
           

#validation.register(TALESExpressionValidator())
