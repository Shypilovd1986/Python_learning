#                               Basics elements of a computer systems
# User interface  - the way how communication is organized between a user and a computer
# System interface - A logical interface that converts a system's input into its output that is displayed on the user
#   interface. A system's input can come from somewhere in the form of the outputs of that other system, e.g. a power
#    button, pressing buttons on the keyboard. System interfaces require physical equipment (such as a CPU, cables,
#   graphics, and memory cards), software and protocols that describe and implement methods for controlling the movement
#   of data and information between systems
# Software architecture - A set of software elements, relations among them, and properties of both elements and
#   relations. It can be represented graphically through the use of flowcharts that illustrate how the processes work
#   and how each component is related to another one.
# Component - A group of modules that perform related functions. Components can function independently and can be
#   interchanged or placed into new systems.
# Data - Information used and outputted by the system.
# Modules - Parts of one system that perform specific tasks. Each module has its own specific role which precisely
#   defines its purpose. There are hardware and software modules.


#                                   Path of solving the problems
# Problem -> Idea -> Algorithm -> Program -> Execution

# High level languages - is High level is a portable computer programming language that isn't limited by a computer,
#   designed for a specific job, and is easier to understand. It is more like a human language and less like a machine
#   language. The amount of abstractions provided defines the level of a programming language. The first high-level
#   languages were introduced in the 1950s. These include BASIC, COBOL, FORTRAN, Java, Pascal, Perl, PHP, Python,
#   Ruby, and Visual Basic.
# Low level languages - Low level is a programming language that provides little or no abstraction from programming
#   concepts and is very close to writing actual machine instructions. The main two examples of low-level languages are
#   machine learning and assembly language.

# * Machine language: The exact machine language for a program or an action can differ depending on an operating system
#   that dictates how a compiler writes a program or an action into machine language.
#       a collection of binary digits or bits that a computer reads and interprets
#       the only language a computer is capable of understanding
#       directly run on a CPU (central processing unit)
#       not portable
# *     Assembly language (e.g. Apple, Linux, Mips, Intel, etc.):
#   less error-prone
#   there is a one-to-one relationship between what it tells a computer to do, and what a computer does. Replaces 1s
#       and 0s with English instructions. Therefore, coding is easier than using a machine language
#   often one line of an assembly program contains a maximum of one instruction for a computer
# *     Imperative programming is a programming paradigm that uses statements that change a program's state. Imperative
#   programming focuses on describing how a program operates. An imperative program consists of commands for the
#   computer to perform:
#       object-oriented languages
#       procedural languages
# *     Declarative programming is a programming paradigm - a style of building the structure and elements of computer
#   programs - that expresses the logic of a computation without describing its control flow. In other words, it is a
#   language that declares what needs to be done rather than how to do it:
#       logic
#       database query
#       functional

# *  Compiled language (C, C++, Objective-C, Swift, Fortran) is a type of programming language which typically executes
# generating machine code from source code and uses the machine code to run the program.
# *  Interpreted language (Python, Javascript, Lisp, PHP, Perl) is a type of programming language for which most of its
# implementations execute instructions directly and freely, without previously compiling a program into machine-language
# instructions.

# Source code → Compiler → Bytecode (or p-code) → Interpreter → Execution

# An integrated development environment (IDE)
# a computer-assisted software environment (CASE)

# *     Text Editor A text editor is a software that is used to write computer programs. You can use any text editor
# you like. For example, a very convenient editor is Notepad++.
# *     A Compiler . A compiler is a computer program which converts a high-level language into a low-level language
# understood by a machine. In other words, we can say that it converts the source code written in a programming language
# into another computer language which the computer understands.
# *     An Interpreter . An interpreter can be used to execute the programs directly.

# Errors:
# Logical errors are divided into algorithm errors and semantic errors:
#   * Algorithm errors are the result of a discrepancy between the constructed algorithm and the course of obtaining
# the result of the task.
#   * Semantic errors occur when there is a misinterpretation of the meaning (semantics) of the operators of the
# selected programming language.
# Syntax errors occur due to a violation of the rules of program writing.

# Each of the set of values defined by one byte (from 0 to 255)

# According to the IBM encoding,
#   characters with codes from 0 to 127, which form the first half of the character generator table, are built according
# to the ASCII standard and are the same for all computers;
#   the second half of the characters (codes 128 – 255) may differ and they are usually used to locate the characters
# of the national alphabet;
#   codes 176 – 223 are reserved for pseudo-graphic characters;
#   codes 240 – 255 - for special characters.

# There are three types of operators: unary, binary, and ternary.

# A constant is a value which does not change during program execution.

# Strings are often enclosed in double quotes, while characters are enclosed in single quotes
#
# Tokens (or elementary constructions) of the language are formed from the symbols of the alphabet (the minimum
# significant units of the text in the program) and are the so-called building blocks or the basic components.

# y=a-b div 2
# What are the lexemes?
# Lexemes: {y, =, a, -, b, div, 2}

#       Keyword in Python
# False	await	else	import	pass
# None	break	except	in	raise
# True	class	finally	is	return
# and	continue	for	lambda	try
# as	def	from	nonlocal	while
# assert	del	global	not	with
# async	elif	if	or	yield

#   A lexeme is a sequence of characters in the source program that matches the pattern for a token and is identified
# by the lexical analyzer as an instance of that token. Some authors term this a "token", using "token" interchangeably
# to represent the string being tokenized, and the token data structure resulting from putting this string through the
# tokenization process.
#
#               The data type defines:
#   internal representation of data in random-access memory (RAM)
#   a set of values (range) that data of this type can receive
#   a set of operations that are allowed on such data.

#           Python data types
# Numbers: int, float, complex
# String: str
# Sequence: list, tuple, range
# Mapping: dict
# Set Types: set, frozenset
# Boolean: bool
# Binary Types: bytes, bytearray, memoryview

#       A variable is a storage unit which allocates some space in memory to hold a value and can take different values
# at different times during program execution. Before using a variable in any program, it has to be declared to allocate
# the amount of memory for the variable in accordance with its type; in this case, it can be initialized, i.e. set its
# initial value.

#                   Program data can have the following attributes:
#   Memory Class - A characteristic of the way the objects are located in memory (extern, static, and dynamic); defines
# the scope and lifetime of the variable (by default – auto).
#   Type - The type of future values of the declared objects (by default, the int type is set).
# Memory class and type are optional attributes and if one of them is missing (but not both at the same time),
# the default attributes are set.
#
#   Class names start with an uppercase letter in Java. All other identifiers start with a lowercase letter.
#   While int a = 23; is valid, writing int age = 23; would make more sense, and it would be easier to figure out what
#   it does even when you look at your code after a long time.
#
#       Operating systems have standard system streams (pipes) that are automatically opened at the beginning of program
# execution:
#       stdin — standard data input stream (stream number 0) is reserved for reading user commands or input.
#       stdout — standard data output stream (stream number 1) for programs is reserved for outputting data, usually
# (although not necessarily) a text.
#       stderr — standard error output stream (stream number 2) is reserved for outputting diagnostic and debug messages
# in a text form. If a program is unable to do everything as it should, it writes to this thread.
#
#
# keyboard: stdin(0) ->  Program -> Monitor: stdout(1), stderr(2)
#
#           The actual syntax of the print() function is:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects	the value(s) to be printed
# sep	a separator between the values (the default is a space character)
# end	printed after all values (it defaults into a new line)
# file	the object where the values are printed (default value is sys.stdout (screen))
# flush	(Optional) A Boolean expression, which specifies if the output is flushed (True) or buffered (False — by default). Default: False.

# Python also provides methods for formatting output information (for example, str.format()). When displaying
# information, curly braces {} are used as placeholders. Using %, we can also format strings just like printf() is
# used in the C programming language.

# convert to number used int(), float(), complex() if it's possible

#   Operators are symbols that help us perform certain calculations on one, two, or more operands. An operand can be
# a constant, a variable, or a function result. A specific action based on an operator is called an expression.

# According to the number of operands participating in operations, there are three types of operators:
#   unary operators that operate with a single operand
#   binary operators that operate with two operands
#   ternary (conditional) operators that operate with three operands

#   Logical Operators (|| , ! , &&)Combine two or more conditions or restrictions, and return "true" (when all
#   considered conditions are satisfied) or "false".

# Relational operators are used to compare values of the first operand with the second one. Operands can be any
# arithmetic expressions and pointers. Arithmetic operands are converted according to the same rules as for arithmetic
# operations. If the relation is true, then the value of a relational expression is '1', and if the relation is false,
# then the value of the expression is '0'.
#
# Relational Operators
# Description	Operator	Expression	Relation	Value of the Expression
# less than		a < b	false	0
# less than or equal to		a <= b	false	0
# equal to		a == b	false	0
# not equal to		a != b	true	1
# greater than		a > b	true	1
# greater than or equal to		a >= b	true	1

# a=41
# b=11
# result = a==b
# print(result)  #-> False

# using break also known as jumping out of the loop.
