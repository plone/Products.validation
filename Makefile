VIRTUALENV=virtualenv-2.7

all: test

test: bin/test
	bin/test

bin/python:
	$(VIRTUALENV) .

bootstrap.py:
	wget https://bootstrap.pypa.io/bootstrap-buildout.py -O $@

bin/buildout: bin/python bootstrap.py buildout.cfg
	bin/python bootstrap.py --version=2.2.5 --setuptools-version=7.0
	touch $@

bin/instance: bin/buildout buildout.cfg setup.py
	bin/buildout -Nvt 5 install instance
	touch $@

bin/test: bin/buildout buildout.cfg setup.py
	bin/buildout -Nvt 5 install test
	touch $@
