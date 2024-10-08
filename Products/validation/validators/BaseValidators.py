from Products.validation.i18n import PloneMessageFactory as _
from Products.validation.validators.RangeValidator import RangeValidator
from Products.validation.validators.RegexValidator import RegexValidator


# protocols for isURL validator, the secure (*s) variants are automagically
# added
protocols = (
    "http",
    "ftp",
    "irc",
    "news",
    "imap",
    "gopher",
    "jabber",
    "webdav",
    "smb",
    "fish",
    "ldap",
    "pop3",
    "smtp",
    "sftp",
    "ssh",
    "feed",
)

# email re w/o leading '^'
EMAIL_RE = r"([0-9a-zA-Z_&.'+-]+!)*[0-9a-zA-Z_&.'+-]+@(([0-9a-zA-Z]([0-9a-zA-Z-]*[0-9a-z-A-Z])?\.)+[a-zA-Z]{2,}|([0-9]{1,3}\.){3}[0-9]{1,3})$"

baseValidators = [
    RangeValidator("inNumericRange", title="", description=""),
    RegexValidator(
        "isDecimal",
        r"^([+-]?)(?=\d|(\.|\,)\d)\d*((\,|\.)\d*)?([Ee]([+-]?\d+))?$",
        title="",
        description="",
        errmsg=_("is not a decimal number."),
    ),
    RegexValidator(
        "isInt",
        r"^([+-])?\d+$",
        title="",
        description="",
        errmsg=_("is not an integer."),
    ),
    RegexValidator(
        "isPrintable",
        r"[a-zA-Z0-9\s]+$",
        title="",
        description="",
        errmsg=_("contains unprintable characters"),
    ),
    RegexValidator(
        "isSSN",
        r"^\d{9}$",
        title="",
        description="",
        errmsg=_("is not a well formed SSN."),
    ),
    RegexValidator(
        "isUSPhoneNumber",
        r"^\d{10}$",
        ignore=r"[\(\)\-\s]",
        title="",
        description="",
        errmsg=_("is not a valid us phone number."),
    ),
    RegexValidator(
        "isInternationalPhoneNumber",
        r"^\d+$",
        ignore=r"[\(\)\-\s\+]",
        title="",
        description="",
        errmsg=_("is not a valid international phone number."),
    ),
    RegexValidator(
        "isZipCode",
        r"^(\d{5}|\d{9})$",
        title="",
        description="",
        errmsg=_("is not a valid zip code."),
    ),
    RegexValidator(
        "isURL",
        r"(%s)s?://[^\s\r\n]+" % "|".join(protocols),
        title="",
        description="",
        errmsg=_("is not a valid url."),
    ),
    RegexValidator(
        "isEmail",
        "^" + EMAIL_RE,
        title="",
        description="",
        errmsg=_("is not a valid email address."),
    ),
    RegexValidator(
        "isMailto",
        "^mailto:" + EMAIL_RE,
        title="",
        description="",
        errmsg=_("is not a valid email address."),
    ),
    RegexValidator(
        "isUnixLikeName",
        r"^[A-Za-z][\w\d\-\_]{0,7}$",
        title="",
        description="",
        errmsg=_("this name is not a valid identifier"),
    ),
]

__all__ = ("baseValidators",)
