#                                   assertion test
# A test to compare the output of a function against a known expected value
#                                   commentation
# A combination of comment and documentation; the practice of using comments to document a piece of code
#                                   fuzzing
# A test where random input values are passed into a function to be tested
#                                 package manager
# A software tool that installs third-party packages and their dependencies
#                               third-party package
# A package that is not included in Python’s standard library; the largest such repository is called PyPI
#                                     venv
# A tool to create a virtual Python development environment that is isolated from the rest of the computer system

# Unlike Java, where there's a very specific directory structure you should follow, Python does not force you to a
# directory structure. You could have a single .py file or some directory structure.

# Our project is an early version of an NLP, natural language processing, package.

#                                       README.md
#
#  You should have a ReadMe file at your repository. It should provide some documentation about your project, and some
#  help for new developers on how to get by. It's very common to write ReadMe in Markdown format. GitHub and other
#  services well render this Markdown to nice HTML, as you can see here. The first lines of the ReadMe should be an
#  elevator pitch for your project. It should explain in short terms what your project is about. Usually after that
# comes uses, examples and more documentation. At the end we usually have some data for developers on how to get started
# hacking on the project. ReadMe is important, don't skip it and make sure it's updated.

#                                   __init__.py

# _init_.py tells Python that a directory can be imported as a package. _init_.py should start with a
# docstring for the whole module. As in readme, the docstring should contain an elevator page for your project, and some
# example usage. You should have a version for your project. The viable is usually _version_ and you should use semantic
# versioning, which means first number is the major number, stable API, second number is a minor version, editions only,
# and the last one is patch level. The version itself is usually a simple string, but it can be a more complex object
# like Python's sys.version_info. We'll cover versioning in depth in other episodes. Apart from that, you can have some
# code in _init_.py. Some people like to keep _init_.py clear of code and import all the functions and classes from
# other sub-models, and that' okay as well. _init_.py can be empty, and for sub-packages, it's okay. But make sure that
# top-level _init_.py has some content.

#                               testing

#  Do all you can to make sure tests don't run in production, including placing them in a separate directory. In our
#  case, this directory is called tests, because both test and testing are built-in models.
#  Apart from yourself in it when making changes and validating your code, they also send a signal to potential users
#  that you're serious about your code. Tests can also serve as the commentation. By reading test code, people will be
#  able to understand how to use your package. The tests directory mostly contains Python files, but it can also contain
#  some auxiliary data.
#
#                               makefile

#  Once you write all the steps to run the tests in a script they are there, documented and ready to execute. There are
#  several systems that support task automation. I tend to use Make utility. The reasons I like Make are it's simple,
#  it's already installed on most Unix-like systems, and there's a lot of knowledge around it.
# Let's have a look at the makefile. In a makefile we have a rule followed by a column. So the rule name is test and
# it's followed column. Then, all the commands this rule should invoke are prefixed by the top character. If a line is
# long, you can split it with a backslash.

# all:
# 	$(error please pick a target)
#
# env:
# 	# Create venv directory if not exist
# 	test -d venv || virtualenv venv
# 	./venv/bin/python -m pip install -r requirements.txt
#
# dev-env: env
# 	./venv/bin/python -m pip install -r requirements-dev.txt
#
# test:
# 	find . -name '*.pyc' -exec rm -f {} \;
# 	./venv/bin/flake8 nlp tests
# 	./venv/bin/python -m pytest \
# 	    --doctest-modules \
# 	    --disable-warnings \
# 	    --verbose \
# 	    nlp tests
#
# package:
# 	python setup.py sdist
#
# clean:
# 	rm -rf build dist nlp.egg-info

# . It might be that Make is not the right system for you, though I encourage you to give it a try. If you can't use
# Make, try to find another automation system.

#                           setup.py

# Setup.py is Python's way of defining a project. We import setup from functools and then we read the description from
# the readme file, and we load the requirements from the files. Requirements-dev and regular requirements. And we also
# have a utility function to read the version from _init_.py. The final step is calling the setup function. We say the
# project name is nlp, the version we read from the _init_, the package is nlpy. Entry points which will create a script
# called nlpd, then what is required for installation and what is required for tests. We have description, a long
# description, what is the license for the package, and then some information about the project.
#
#               Example of directory
# nlpy
#   LICENSE.txt
#   Makefile
#   MANIFEST.in
# nlp
#   README.md
#   requirements-dev.txt
#   requirements.txt
#   setup.py
# tests
#   conftest.py
#   test_httpd.py
#   test_nlp.py

#  The central location for third party packages is PyPI.  http://pypi.org

#               Package managers
# . Pip is the most widely used one and is a good choice. Pip is not the only package manager. There are others such as
# Poetry, Conda, Pipenv, and others.
# , Pip will install the latest version of a package. I highly recommend you specify which version of a package you want
# to install. It will save you from surprises in the future when someone accidentally introduces a bug or a change to a
# function parameters. You should also write your dependencies and their versions down and place this file in SuSE
# control so other team members and the operations team will be able to reproduce the same environment.

#               Example of requirements for project
# # Dependencies for our cool project
#
# pandas==0.25
# requests==2.22.0

# You can have comments like in line one and then in line three and four we specify the dependencies and we specify the
# version for every dependency. To install these requirements from
# python -m pip install -r and our requirements.txt
# Then the pip will install the dependencies and their dependencies. And now in our code we can use pandas for example.
# We put pandas as pd works.

#                   virtualenvs
#
# Selecting transcript lines in this section will navigate to timestamp in the video
# A python interpreter can work with only one version of a package at a time. If you work on two projects, one using
# pandas 0.22, and the other using pandas 0.25, this can be an issue. A lot of unit distributions, and also OSX, uses
# Python scripts to manage the system, which means that if you install a non-compatible version of a package, you broke
# the system. To solve these problems, we use virtual environments. A virtual environment is an isolated Python
# installation. You create a virtual environment for a project that you work on. To create a virtual environment, you
# can use the built-in venv model, or the popular third party virtualenv.

# virtualenv venv   will create a directory called venv with an isolated installation of Python. Now, once I have the
# virtual environmenent, I can install my dependencies. /venv/bin/python -m pip install- r, and then the requirements
# I have, and these are going to get installed into the virtual environment, not into the system Python. You need to use
# Python from a virtual environment in your project. Most Python IDs ,such as Pycharm, know about virtual environments
# and how to use them.

# # Dependencies for our cool project
# You might have dependencies that are used only in development. Test with Splinter is another. For example, our project
# might rely on pandas 0.25 and requests 2.22.0. However, in development, we need all of these, plus flake8 and pytest.
# The common practice is to have separate requirements file. One for production and another one for development. So
# requirements.txt is the one for production and dev-requirements.txt will be the one for development. Another issue is
# that depending on the operating system, you might need different packages. The common practice here is to specify only
# top-level dependencies and let the people decide what you need.

# pandas==0.25
# requests==2.22.0
# # Development requirements
#
# flake8==3.7.8
# pytest==5.1.1

# # Dependencies for our cool project
#
# pandas==0.25
# requests==2.22.0

# You might have dependencies that are used only in development. Test with Splinter is another. For example, our project
# might rely on pandas 0.25 and requests 2.22.0. However, in development, we need all of these, plus flake8 and pytest.
# The common practice is to have separate requirements file. One for production and another one for development. So
# requirements.txt is the one for production and dev-requirements.txt will be the one for development. Another issue is
# that depending on the operating system, you might need different packages. The common practice here is to specify only
# top-level dependencies and let the people decide what you need.

# def check_version(name, version_prefix):
#     mod = __import__(name)
#     version = mod.__version__
#     assert version.startswith(version_prefix), \
#         f'{name} version is {version} (wanted {version_prefix})'
#
#
# # Production packages
# check_version('flask', '1.1')
# check_version('flask_login', '0.4.1')
# check_version('numpy', '1.16.4')
#
# # Development packages
# check_version('flake8', '3.7')
# check_version('pytest', '5.1.1')
# check_version('pytest_benchmark', '3.2.2')

# # Development requirements
#
# flake8==3.7
# pytest-benchmark==3.2.2
# pytest==5.1.1

# venv:
# 	virtualenv venv
# 	./venv/bin/python -m pip install -r requirements.txt
#
# dev-venv: venv
# 	./venv/bin/python -m pip install -r dev-requirements.txt

#               What to test

#  you'll notice there are a lot of test types.
#  Integration.
#  This tests check the connection between the subsystems and connection with external systems.
#  Regression.
#  This tests check the running code over known data, returns a known solution. Fuzzing. This tests generate random data
#  and throw it at your code.
#  Linters.
#  These are static checkers that find common issues without running your tests.
#  Unit.
#  Check your code in isolation for valid output.
#  You should keep track of what bug that every kind of test find.
#  And when you get the bug report, think of the kind of test that would have caught it. After a while, you know which
#  type of tests bring the most value, and you should focus your effort on these type of tests.

# python -m pytest -v tests/tests mathlib.py:: test_sqrt           to run just a single test.

# - [Instructor] Test fixtures creates a null environment for testing. A server tests need a database with some data in
# it. You can use a fixture to create such as database and populate it before every test run or every test file run. As
# soon as you have a code to create a table in a database. We have db.py. We have the definition of the sql_schema. And
# in line 15, create_schema which will populate the database with the new schema, creating tables there. To have the
# database automatically created you can use a pytest fixture. You should use a file length conftest in the test
# directory. We input pytest and we input sqlite3 which is an impeded database that comes with the Python. In line six
# , we define a function called database. And in line five we decorate it with pytest.fixture. In line seven we create
# the connection. In line eight we yield the connection. Pytest will lose this connection. And once the test is done, it
# will continue the code from line nine and 10 to do some clean up. To use this fixture in the test, we define in line
# four def test_create_schema, which gets a parameter called database. This parameter name must match the name of the
# fixture file in conftest.py. And then we create the schema, we do our checks, and at the end when the test will be
# done, pytest will call the clean up code for us. And now we can run python -m pytest -v tests. And we see that test
# _create_schema has passed.
