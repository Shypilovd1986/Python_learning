#        Level of testing
# Unit Testing - testing at the function lvl
# Component testing - testing is at the library and compiled binary level
# System testing - tests the external interfaces of a system which is a collection of systems
# Performance testing - testing done at sub - system and system levels to verify timing and resource usages are
# acceptable
#
#       Unit testing specifics
# tests individual functions
# a test should be written for each test case for a function (all positive and negative test cases).
# Groups f tests can be combined into test suites for better organization.
# Executes in the development environment rather than the production environment
# Execution of the tests should be automated

#           The unit test performs three steps.
# A setup step where it creates a test string.
# An action step where calls a production code to perform the action that is under test.
# And then an assertion step, where the test validates results of the action.
#
# This is a common structure that all of your unit test should follow.

#       To summarize, here are the keypoints on unit testing.
# Unit tests are first safety net for catching bugs in the production code.
# Unit test validate test cases for individual functions.
# They should build and run in the development environment.
# And unit test should run fast.

#       test-driven development or TDD
# TDD is a process for writing code that helps you take personal responsibility for the quality of your code.
# The process drives this by having you write the unit tests before the production code. This can seem pretty strange at
# first, but after you've used the process for a while, it becomes the norm and you'll find it hard to write code any
# other way. Even though the tests are written before the production code, that doesn't mean that all the tests are
# written first.

#       Benefits of TDD
# Gives you the confidence to change thr code
# Give you immediate feedback
# Documents what the code is doing
# Drives good object oriented design

#  The TDD work flow is broken up into three phases referred to as the red phase, green phrase, and refactor phase.
#    The first phase is the red phase. In the red phase, you write a failing unit test for the next bit of functionality
#  you want to implement in the production code.
#    Next comes the green phase, where you write just enough production code to make the failing unit test pass.
#    Last is the refactor phase, where you clean up the unit test and the production code to remove any duplication and
# make sure the code follows your team's coding standards and best practices.
#    Then you repeat the process for all the functionality you need to implement and all the positive and negative test
# cases.
#
#           These laws help ensure you're following the TDD process.
#   The first law, you may not write any production code until you have first created a failing unit test, falls along
# with the idea of writing the unit test first.
#   Seeing your new unit test fail before you've implemented the production code is a sign that the unit test has been
# implemented properly.
#   The second law, you may not write more of a unit test than is sufficient to fail, forces you to write only enough
# of a unit test for the next test case. And the next test case should always be the simplest test case.
#   The last law, you may not write more production code than is sufficient to pass the currently failing unit test,
# keeps you from writing production code without any unit test to verify it.

#  These three laws help to keep you in a small, tight loop of writing a little test that fails, then writing a little
#  production code to make it pass. Each iteration of the loop should only be a few minutes long and you're always
#  unning the unit test to verify nothing is gotten broken.

#                   virtual environment
# python3 -m venv pytest_3_venv       to create virtual environment
# source pytest_3_venv/bin/activate     to activate virtual environment
# pip3 install pytest      to install pytest
# deactivate    to deactivate pytest
#
# I'll need to setup a new configuration using net test runner to execute my unit test. First, I'll bring up the
# configuration screen by clicking on run and edit configurations. Then, I'll add a new PyTest configuration and call
# it unit test.
# next to button run , choose edit configuration
# press + in the top left corner
# choose pytest
# give the name , for example unit_test, choose root to the project
#
#       Overview of pytest
#    PyTest is a Python unit testing framework. It provides the ability to create tests, test modules, test classes, and
#  test fixtures.
#    It uses the built-in Python assert statement which makes implementing unit tests much simpler than other Python
# unit testing frameworks.
#    It also adds many useful command line arguments to help specify what tests should be run and in what order.
#    So how do you create a unit test in Python with PyTest? In PyTest, individual tests are Python functions with test
# at the beginning of the function name. The unit tests then execute production code and use the standard Python assert
# statement to perform verifications on results.
#    def test_Somefunction():
#         assert 1 == 1
#     Similar tests can be grouped together by including them in the same module or class.
#
# pytest -v      we run test from command line

#           test discovery
#     PyTest will automatically find your tests when you run it from the command line using several naming rules for the
#  test files, test classes, and test functions.
#     Test function names should begin with test.  test_function, pytest will check it,
#     Classes with tests in them should have the word Test with a capital T at the beginning of the class name. These
# classes should also have no init method. class TestClass:  pytest check it,  class myTest: don't check it
#     The file names for test modules should start with test underscore or end with underscore test.

#           An xunit-style setup and teardown
#  One key feature of all unit test frameworks is providing the ability to execute setup code before and after the test.
#  pytest provides this capability with both xUnit-style setup and teardown functions and with pytest fixtures.
#  The xUnit-style setup and teardown functions allow you to execute code before and after
#  test modules                             def setup_module():, def teardown_module(): ,
#  test functions                           def setup_function(): , def teardown_function():
#  test classes                             def setup_class(),  def teardown_class():
#  test methods in test classes             def setup_method(), def teardown_method()
#  Using these setup and teardown functions can help reduce code
#  duplication by letting you specify the setup and teardown code once at each of the different levels as necessary
#  rather than repeating the code in each individual unit test. This can help keep your code clean and manageable.

#           for example 1
# def setup_function(function):
#     if function == test1:
#         print(f'setting up {function}')
#
#
# def teardown_function(function):
#     if function == test1:
#         print(f'tearing down {function}')
#
# def test1():
#     print('test is executing')
#     assert True

# pytest -v -s        the -s argument, which tells pytest not to capture the console output, so I can see the results
# of the print statements on the console.

#  The setup class method will be executed by pytest before any of the unit tests in the class are executed. The
#  teardown class method will be executed by pytest after all of the unit tests in the class are executed. Setup method
#  will be called before each unit test in the class is executed, and the teardown method will be executed after each
#  unit test in the class has completed.

#           for example 2
# class Test_class():
#     @classmethod
#     def setup_class(cls):
#         print('setup class method')
#
#     @classmethod
#     def teardown_class(cls):
#         print('teardown class method')

#     def test1(self):
#         print('test is executing')
#         assert True

#       Test fixtures
#       Like the xUnit style of setup and teardown functions, Test Fixtures allow for re-use of code across tests by
# specifying functions that should be executed before the unit test runs.
#       Specifying that a function is a Test Fixture is done by applying the pytest.fixture decorator to the function.
#       Individual unit tests can specify they wanna use that function by specifying it in their parameter list, or by
# using the pytest.mark.usefixture decorator.
#       The fixture can also set its autouse parameter to true, which will cause all tests in the fixture scope to
# automatically execute the fixture before the test executes.
#
#       example 1
# @pytest.fixture():
# def math():
#   return Math()

# def test_Add(math):
#   assert math.add(1,1) ==2

#       example 2
# import pytest
# @pytest.fixture()
# def setup():
#     print('\nSetup')
#
# def test1(setup):
#     print('Executing test1!')
#     assert True
#
# def test2():
#     print('Executing test2!')
#     assert True

# Now I'll add setup to test1's parameter list, and rerun pytest. Now Setup is called before test1 executes, but not
# before test2 executes. So now I'll update test2 to specify that it wants the setup called before it executes by using
# the pytest.mark.usefixtures decorator. And I see that Setup is now being called before both test1, and test2.
#
#       example 3
# import pytest
# @pytest.fixture()
# def setup():
#     print('\nSetup')
#
# def test1(setup):
#     print('Executing test1!')
#     assert True
# @pytest.mark.usefixtures('setup')
# def test2():
#     print('Executing test2!')
#     assert True

#  But this can also be cumbersome for those cases where all the tests need to run the same test fixture. In this case,
#  the autouse parameter of the test fixture can be set to true, and then the fixture will automatically be executed
#  before each test that is in the fixture scope.
#               example 4
# import pytest
# @pytest.fixture(autouse=True)
# def setup():
#     print('\nSetup')
#
# def test1():
#     print('Executing test1!')
#     assert True
#
# def test2():
#     print('Executing test2!')
#     assert True

#       test fixture teardown
#       Test Fixture can specify their own teardown code that should be executed.
#       There are two methods of specifying a teardown code for a Test Fixture.
#       The yield keyword, and the request-context object's addfinalizer method.

#            example  Test Fixture Teardown - Yield
# @pytest.fixture():
# def setup():
#   print('Setup!')
#   yield
#   print('Teardown')

# The yield keyword is the simpler of the two options for teardown code. The code after the yield statement is
#   executed after the fixture goes out of scope.
# The yield keyword is a replacement for return, and any return values should be passed to it.
#
#            example  Test Fixture Teardown - Yield
# @pytest.fixture():
# def setup(request):
#     print('Setup!')
#     def teardown:
#         print('Teardown')
#     request.addfinalizer(teardown)
# The addfinalizer method of adding teardown code is a little more complicated, but also a little more capable than the
# yield statement. With the addfinalizer method, one or more finalizer functions are added via the request-context's
# addfinalizer method. One of the big differences between this method and the yield keyword is that this method allows
# for multiple finalization functions to be specified.

#           Test Fixture Scope
#  Which test a fixture applies to, and how often it is run, depends on the fixture scope.
#  Test Fixtures have four different scopes that are possible.
#   - By default, the scope is set to Function. And this specifies that the fixture should be called for all tests in
# the module.
#   - Class scope specifies that the Test Fixture should be executed once per test class.
#   - Module scope specifies that the fixture should be executed once per module.
#   - And Session scope specifies that the fixture should be executed once when pytest starts.

#           example 1
# import pytest
#
# @pytest.fixture(scope='session', autouse=True)
# def setupSession():
#     print('\n Setup Session')
#
# @pytest.fixture(scope='module', autouse=True)
# def setupModule():
#     print('\n Setup Module')
#
# @pytest.fixture(scope='function', autouse=True)
# def setupFunction():
#     print('\n Setup function')
#
# def test1():
#     print('Executing test1')
#     assert True
#
# def test2():
#     print('Executing test2')
#     assert True

#           Test Fixture Return Object and Params
# import pytest
# @pytest.fixture(params=[1,2])
# def setupData(request):
#     return request.param
#
# def test1(setupData):
#     print('print setupData')

#   Pytest fixtures allow you to optionally return data from the fixture that can be used in the test.
#   The optional params array argument in the fixture decorator can be used to specify one or more values that should be
#   passed to the test.
#   When a params argument has multiple values, the test will be called once with each value.

#           example 1
# import pytest
#
# @pytest.fixture(params=[1,2,3])
# def setupData(request):
#     retVal = request.param
#     print('\nSetup! retVal = {}'.format(retVal))
#     return retVal
#
# def test1(setupData):
#     print('\nsetup = {}'.format(setupData))
#     assert True
#
#  The params feature can be a powerful and easy way to run your unit test with various values. Care should be taken
#  with this approach, though, as you generally still want to have different test cases and separate unit tests with
#  unique names so that they can be easily identified when they fail.

#           Assert statements and exceptions
# def test_IntAssert():
#     assert 1 ==1
#
# def test_StrAssert():
#     assert 'str' == 'str'
#
# def test_floatAssert():
#     assert 1.0 == 1.0
#
# def test_arrayAssert():
#     assert [1,2,3] = [1,2,3]
#
# def test_dictAssert():
#     assert {'1':1} == {'1':1}

#       Pytests allows the use of the built in Python assert statement for performing verifications in a unit test.
#     The normal comparison operators can be used on all Python data types. Less than, greater than, less than or equal,
# greater than or equal, equal or non equal.
#     Pytests expands on the messages that are reported for assert failures to provide more context in the test results

#   Test failing!!!!!!!
# def test_BadFloatCoompare():
#     assert (0.1+0.3) == 0.3
#
#   Test Passing !!!

# from pytest import approx
# def test_GoodFloatCompare():
#     val = 0.1 +0.2
#     assert val == approx(0.3)
#     Validating floating point values can sometimes be difficult, as internally the value is stored as a series of
# binary fractions. Because of this, some comparisons that we'd expect to pass, will fail.
#     Pytests provides the approx function, which will validate the two floating point values, or approximately the same
# value, as each other, to then a default tolerance of one times e to the negative six value.
#     In some test cases, we need to verify that a function raises an exception under certain conditions.

#   Test Passing !!!
# def raiseValueException():
#     raise ValueError

#   Test failing!!!!!!!
# def test_Exception():
#     with raises(ValueError):
#         raise ValueError

#     Pytest provides the raises helper to perform this verification, using the with keyword. When the raises helper is
# used, the unit test will fail, if the specified exception is not thrown in the code block, after the raises line.

#       Command line arguments: pytest
#    By default, PyTest runs all tests that it finds in the current working directory and sub-directory using the naming
# conventions for automatic test discovery. There are several PyTest command line arguments that can be specified to try
# and be more selective about which tests will be executed.
#       You can simply pass in the module name to execute only the unit tests in that one particular module.
#       You can also simply pass in a directory path to have PyTest run only the tests in that directory.
#       You can also use the -k option to specify an evaluation string based on keywords such as the module name, the
# class name, and the function name.  pytest -v -s -k 'test2'    only test2.py will be executed,
# pytest -v -s -k 'test2' or 'test3'   only test2.py and test3.py will be executed
#       You can also use the -m option to specify that any tests that have a pytest.mark decorator that matches the
# specified expression string will be executed.
# import pytest
#
# @pytest.mark.test3
# def test3():
#     print('\nTest3!')
#     assert True
# pytest -v -s -m 'test1 or test3'   # will execute with mark test1 or test3
#       Here's some additional command line arguments that can be very useful.
#       The -v option specifies that verbose output from PyTest should be enabled. Test file from subdirectory and files
# in directory.   pytest -v -s test_file1.py   test just one file from directory ,    pytest -v -s  testSubDirectory/
# only subdirectory will test.
#       The -q option specifies the opposite. It specifies that the test should be run quietly, or with minimal output.
# This can be helpful from a performance perspective when you're running hundreds or thousands of tests.
#       The -s option specifies that PyTest should not capture the console output, allowing you to see the printouts
# from the print, from the tests.
#       The --ignore option allows you to specify a path that should be ignored during test discovery.
#       And the --maxfail option specifies that PyTest should stop after n number of test failures.

#          checkout kata overview
# A code kata is a software development exercise in which the focus is not on solving a task or problem, but on learning
# new skills and developing successful routines. For each code kata, several solutions have to be found in order to
# learn from mistakes, gain experience and develop even better solutions.

#                   TDD best practices
#      First, you should always do the next simplest test case. This allows you to gradually increase the complexity of
#  the code, refactoring as you go. This helps keep your code clean and understandable.
#      If you jump to the complex cases too quickly, you can find yourself stuck writing a lot of code for one test case
# which breaks the short feedback cycle we look for with TDD.
#      Beyond just slowing you down, this can also lead to bad design as you can miss some simple implementations that
# come from the incremental approach.

#  Always try to use descriptive test names. The code is read thousands of times more than it's written as the years go
#  by. Making the code clear and understandable should be the top priority. Unit tests are the best documentation for
#  the developers that come after you for how you intended the code to work. If they can't understand what the unit test
#  is testing, that documentation value is lost. Test suites should name the class or function that is under test and
#  the test names should describe the functionality that is being tested.

#   Using a static code analysis tool regularly on your code base is another core requirement for ensuring code quality.
#   Pylint is an excellent open source static analysis tool for Python that can be used for detecting bugs in your code.
#   It can also verify the code is formatted to the team standard, and it can even generate UML diagrams based on its
#   analysis of the code. In the last lecture I'll review what we went over in this course and where we're to go from
#   here.

#               There are many types of test doubles.
#  Dummy objects are the simplest. They are simply placeholders that are intended to be passed around but not actually
#  called or used in any real way. They'll often generate exceptions if they're called.
#  Fake objects have a different and usually simplified implementation from the production collaborator that make them
#  usable in the test code, but not suitable for production.
#  Stubs provide implementations that do expect to be called, but respond with basic canned responses.
#  Spies provide implementations that record the values that are passed into them. The tests can then use those recorded
#  values for validating the code under test.
#  Mock objects are the most sophisticated of all the test doubles. They have pre-programmed expectations about the
#  ordering of calls, the number of times functions will be called, and the values that will be passed in. Mock objects
#  will generate their own exceptions when these pre-programmed expectations are not met. Mock frameworks are libraries
#  that provide easy-to-use API's for automatically creating any of these types of test doubles at runtime. They provide
#  easy API's for specifying the Mocking expectations in your unit test.

#  Unittest.mock provides the Mock class, which is an extremely powerful class that can be used to create test objects
#  that can be used as fakes, stubs, spies, or true Mocks for other classes or functions.

#  Mock provides many built-in functions for verifying how the Mock was called, including the following assert
#  functions:
#  The assert_called function will pass if the Mock was ever called with any parameters.
#  The assert_called_once function will pass if the Mock was called exactly one time.
#  The assert_called_with function will pass if the Mock was last called with the specified parameters.
#  The assert_called_once_with function will pass if the Mock was called exactly once with the specified parameters.
#  The assert_any_call function will pass if the Mock was ever called with the specified parameters.
#  And the assert_not_called function will pass if the Mock was never called. Mock provides these additional built-in
#  attributes for verifying how it was called: the assert_has_calls function passes if the Mock was called with
#  parameters specified in each of the passed in list of Mock call objects, and optionally in the order that those call
#  objects are put into the list.

#