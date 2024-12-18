Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

3.0.1 (2024-12-16)
------------------

Bug fixes:


- Remove unneeded code from ``recursiveTranslate`` that broke with latest Zope 5.11.
  ``zope.i18n`` already supports recursive translation out of the box since 2008.
  [maurits] (#70)


3.0.0 (2024-08-21)
------------------

Breaking changes:


- Removed `Products/validation/validators/validator.py`.
  This had backwards compatibility imports in a way that did not work on Python 3.
  So apparently no one needed this so far.
  [maurits] (#60)
- Drop support for Plone 5.2 and for Python 3.7 and lower.
  Only Plone 6.0 and 6.1 are supported now.
  Note that in Plone 6.1, this package is no longer tested together with the core.
  It has been moved to the ecosystem versions.
  [maurits] (#60)


New features:


- Move translations from plone.app.locales to here
  [erral] (#11)


Internal:


- Update configuration files.
  [plone devs]


2.1.3 (2020-06-24)
------------------

Bug fixes:


- Fixes #6 long deprecated InitializeClass import which did not work  in Zope 5.
  [jensens] (#6)


2.1.2 (2020-04-23)
------------------

Bug fixes:


- Minor packaging updates. (#1)


2.1.1 (2018-11-01)
------------------

Bug fixes:


- Use new utils.check_id from CMFPlone. [maurits] (#4)


2.1 (2017-08-27)
----------------

New features:

- Python 3 compatibility
  [tomgross]

Bug fixes:

- Remove unnecessary test dependencies
  [tomgross]


2.0.2 (2016-08-08)
------------------

Bug fixes:

- Use zope.interface decorator.
  [gforcada]

2.0.1 (2015-02-23)
------------------

- Accept base domain names longer than 6 chars like .brussels
  [gotcha]

2.0 (2010-07-18)
----------------

- No changes.

2.0b1 (2009-12-27)
------------------

- Added missing zope.i18n(messageid) dependencies.
  [hannosch]

2.0a1 (2009-11-13)
------------------

- Cleaned up package metadata.
  [hannosch]

- Declare test dependencies in an extra and fixed deprecation warnings
  for use of Globals.
  [hannosch]

- Removed useless assert statements. Assert is not a function.
  [hannosch]

- Purge old zope2 Interface interfaces for Zope 2.12 compatibility.
  Consider branching before this commit if release required before Plone 4.
  [elro]

- Cleaned up lots of old BBB code.
  [hannosch]

- Email validator did not allow apostrophe in the local part of an email
  address. This closes http://dev.plone.org/plone/ticket/7947.
  [hannosch]

- Relaxed EmptyValidator requirement that REQUEST has a form.
  This closes http://dev.plone.org/plone/ticket/7346.
  [bostrick, hannosch]

1.6.4 - unreleased
------------------

- Cut the validation short when there is only one validator and this
  validator is 'sufficient', which means it does not need to validate.
  [maurits]

- Removed an unnecessary call on Zope startup to the test method in chain.py.
  [maurits]

- Fix: ValidatorError was used (at least theoretically) in chain.py
  but not imported.
  [maurits]

1.6.3 (2009-04-23)
------------------

- Fixed the translated error messages to use Message objects correctly. The
  mapping attribute of Messages can only contain Unicode. Added a helper
  method `safe_unicode` to convert non-unicode string data into Unicode.
  [hannosch]

- Fixed a SyntaxError in RangeValidator.
  [hannosch]

1.6.2 (2009-04-02)
------------------

- Merged in translated error messages for validators from branches/1.6.
  (see http://dev.plone.org/archetypes/changeset/10942)
  This might break 3rd party doctests (unicode returned instead of string).
  [fRiSi]

1.5.1 (2007-08-16)
------------------

1.5.1-b2 (2006-03-20)
---------------------

- Removed tests/runalltests.py and tests/framework.py as they have
  outlived their usefulness. To run tests use Zope's testrunner:
  ./bin/zopectl test --nowarn -s Products.validation
  [stefan]

1.5.1-b1 (2006-02-27)
---------------------

- *cough*
  [nouri]

1.5.0-final (2006-12-15)
------------------------

- note for release-managers: The version-bump to 1.5 was a bit early, but now
  as we have it, i keep it and next release number in the cycle needed for
  Archetypes 1.4.2 (used for Plone 2.5.2) of PortalTransforms is then the 1.5
  final.
  We dont need increasing of release numbers because of Plone 3.0,
  Archetypes 1.5, ... if there's no change in the dependent product, like
  this one.
  [jensens]

1.5.0-a1 (2006-10-25)
---------------------

- Removed an unused import which caused a deprecation warning.
  [hannosch]

1.4.1-final (2006-09-08)
------------------------

1.3.9
-----

- Modify the email validator to allow capitals in the domain. This fixes
  http://dev.plone.org/archetypes/ticket/663.
  [wichert]

post 1.3.4-final02 (2006-01-15)
-------------------------------

- Spring-cleaning of tests infrastructure.
  [hannosch]

1.4.0-beta1 (2006-03-26)
------------------------

- removed marker for odd archetypes 1.3 styles version checks
  [jensens]

1.3.4-final02 (2006-01-15)
--------------------------

- nothing again - the odd version checking needs a version change to stick to
  Archetypes version again.
  [yenzenz]

1.3.4-RC1 (2005-12-29)
----------------------

- nothing again - the odd version checking needs a version change to stick to
  Archetypes version again.
  [yenzenz]

1.3.3-final06 (2005-10-11)
--------------------------

- nothing again - the odd version checking needs a version change to stick to
  Archetypes version again.
  [yenzenz]

1.3.3-final05 (2005-08-30)
--------------------------

- nothing again - the odd version checking needs a version change to stick to
  Archetypes version again.
  [yenzenz]

1.3.3-final04 (2005-08-07)
--------------------------

- nothing - the odd version checking needs a version change to stick to
  Archetypes version again.
  [yenzenz]

1.3.3-final03 (2005-08-01)
--------------------------

- nothing - the odd version checking needs a version change to stick to
  Archetypes version again.
  [yenzenz]

1.3.3-final02 (2005-07-17)
--------------------------

- nothing - the odd version checking needs a version change to stick to
  Archetypes version.
  [yenzenz]

1.3.3-final (2005-07-06)
------------------------

- added Expression Validator
  [zwork]

1.3.2-final02 (2005-05-20)
--------------------------

- nothing (I hate to write this. But the odd version checking needs it).
  [yenzenz]

1.3.2-rc1 (2005-03-25)
----------------------

- Added isMailto validator for mailto:user@host.tld
  [tiran]

- Added protocol list for isUrl validator with lot's of additional protocols:
  http, ftp, irc, news, imap, gopher, jabber, webdav, smb, fish, ldap, pop3,
  smtp, sftp, ssh
  The ``*s`` variants like https are included by the re.
  [tiran]

1.3.1-final (2005-03-05)
------------------------

- Added isValidId validator. Thanks to Francis J. Lacoste for
  his first implementation and Christian Theune for his CMF
  only implementation.
  [tiran]

- Fixed isUnixLikeName validator
  [tiran]

1.3.0-9 (2004-10-17)
--------------------

- Fixed [ 1040556 ] validators type mismatch (was [1036938])
  [tiran]

1.3.0-8
--------------------

- Fixed a bug in MaxSizeValidator, added some comments and made it much faster.
  [tiran]

1.3.0-7 (2004-09-25)
--------------------

- Updated README.txt
  [tiran]

- Fixed last failing unit tests
  [tiran]

1.3.0-6 (2004-09-17)
--------------------

- Removed old setup.py
  [tiran]

- Added isEmptyNoError validator to fix [ 1023153 ] isEmpty validator must
  return empty string when it failed.
  {tiran]

- Don't show error msg in chain when a validator doesn't return StringTypes. It
  was required for isEmptyNoError validator which is returning False.
  {tiran]

1.3.0-5 (2004-09-04)
--------------------

- Fixed typo in RegexValidator
  [tiran]

- Unit tests now based on ZopeTestCase
  [tiran]

1.3.0-4 (2004-08-16)
--------------------

- nothing changed

1.3.0-3 (2004-08-06)
--------------------

- Nothing changed

1.3.0-2 (2004-07-29)
--------------------

- Nothing changed
