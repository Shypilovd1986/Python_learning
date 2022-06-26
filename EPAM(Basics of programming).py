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
# flush	(Optional) A Boolean expression, which specifies if the output is flushed (True) or buffered (False — by
# default). Default: False.

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

#       life cycle of software - the stages it passes from the beginning of its creation to the end of development
# and implementation:
# *     requirement definition - Mathematical or informational formulation of a problem.
# *     analysis - The choice of numerical or other methods for solving the problem.
# *     design - The construction of an algorithm for solving the problem.
# *     coding - The choice of a programming language in order to write the constructed algorithm according to its
# rules, i.e. writing the text of the program.
# *     assurance - Debugging the program as the process of detecting, localizing, and eliminating possible errors.
# *     deployment - Program execution, i.e. obtaining the required result.
# *     maintenance - Adding new functions to the program, fixing errors detected by users.

# SDLC (software development life cycle) ;жизненный цикл програмного обеспечения !!!
# Today, we can divide the SDLC models into two large groups: "traditional" SDLC and Agile
#                           "Traditional" SLC Models:
#                                Waterfall Model
#   The Waterfall Model (or cascade) is one of the old traditional software development models which implies
# a sequential flow of stages, each of which must be fully completed before the next one starts.
# - requirements -> analysis -> design -> coding/implementation -> testing -> operation/deployment

#                                   V-Model
#    The V-Model is based on the idea of validation and verification. It inherited the structure of the Waterfall Model,
# but in addition, a detailed check and testing of the product was organized at the first stages of development.
# Already at the time when developers write the code, testers write unit tests, that is, they start testing in
# parallel with development.

#                               Incremental Model
#   The development process based on the Incremental Model combines the sequential functions of the Waterfall Model and
# consists of several development cycles (the assembly of modules). The complete system requirements are also divided
# into different iterations. New software modules are added at each iteration without any changes or minor changes to
# previously added modules. The process continues until a complete system is created. The development process can go
# either sequentially or in parallel.

#                                   Iterative Model
#   With the Iterative Model, the creation begins with the definition and implementation of a part of the functionality
# which becomes the basis for defining further requirements. This process is repeated. The version may not be ideal,
# the main thing is that it works. Since each iteration is built on the previous one, the design often remains the same.

#                                       RAD Model
#   RAD (Rapid Application Development) Model is an incremental development model. In RAD model, highly qualified teams
#   in parallel, like several mini-projects, are developing components and functions. The time frame for one cycle is
#   strictly limited. The generated modules are then assembled into one working prototype in a short time period.
#   RAD model allows to quickly show a client something working, get feedback, and introduce changes.
#
#    Rapid application development model includes the following steps:
# Business modeling:     we form a list of information flows between different departments.
# Data modeling:    based on the previously collected information, we determine the objects and other entities necessary
# for the exchange of information.
# Process modeling:     we establish links between simulated data to achieve development goals.
# Building the application: it uses auto assembly tools to convert models of computer-aided design (CAD) system to code.
# Testing:  new components and interfaces are tested.

#                                       Spiral Model
# The Spiral Model is similar to the Incremental Model but with a focus on risk assessment: the next stage builds on
# the previous one, and at the end of each round, the team or the customer decides whether to continue the project.
# This model looks like a spiral, and with each new turn, the process becomes more complicated. Each cycle usually
# includes four stages:
# The determination of requirements and constraints.
# Risk analysis and assessment of alternatives.
# Project implementation.
# Evaluation of the result and, if the quality is satisfactory, the transition to a new stage.
# Work on a project continues until the iterative process is completed in the model.

#                                       Agile Model
#   Today, more and more organizations are adopting one or another Agile approach in their IT projects. The Agile Model
# is an agility-based software development methodology that was first introduced in 1990. Agile is based on:
# *iterative development: each iteration usually takes several weeks and provides a full working version of the software
# *continuous communication and collaboration between the teams involved in the development process, including a client
# or stakeholders
# *early customer feedback
# Extreme Programming (XP) is one of the best-known uses of the Agile Model in practice.

#                                    XP (Extreme Programming) Model
#   Extreme Programming Model is an informal and progressive approach to software development based on the method of
# agile software development, where each developer is usually a professional in their field. The core ideas of the
# model are represented by a set of values, principles, and practices for the fastest possible development of
# high-quality software that provides maximum value for a client during the development process. The main thing in
# extreme programming is not to lose control of what is happening.

# Today, the most common Agile subtypes are Scrum and Kanban which are called frameworks. A framework is a more
# mature methodology with strict rules.

# In order to create a good algorithm, you need to carefully analyze the condition of a problem. Analysis is the study
# of objects or phenomena by studying their constituent elements.
#   The analysis of a problem allows you to:
#   establish what the input and output of the future algorithm are, while the input data should be explicitly described
# (the input data is determined by the imposition of constraints)
#   highlight key decisions (dependencies) between input and output data
#   highlight the modules necessary to solve the problem and determine the methods for its solution

#                               Properties of an algorithm
#   Efficiency (finiteness): an algorithm solves a problem in a finite number of steps and the prescribed solution
# is guaranteed to give a correct answer.
#   Discreteness: new data values are calculated according to certain rules from other variables with already known
#  values.
#   Certainty (determinism): each rule from the set is unambiguous, and the data themselves are unambiguously related
#  to each other.
#   Sequence of execution: the sequence of actions of an algorithm is strictly and precisely defined.
#   Massiveness: an algorithm is developed so that it can be applied to a whole class of problems, for example, an
#  algorithm for calculating certain integrals according to given accuracy.

#                   Ways to Describe Algorithms
#   There are several ways to describe algorithms. The most common ways are verbal, or pseudocode, and graphical
# description of an algorithm, or a flowchart.
#   Verbal Description of an Algorithm
#    Pseudocode specifies the steps of an algorithm using essentially natural language and through the use of the
#    following control constructs:
#
# The step (stage) of processing (calculating) data values - "=".
# The step of checking a logical condition: if (condition) is true, then perform action 1; otherwise - action 2.
# The transition (transfer of control) to a certain step (stage) .

#               Graphic Representation of an Algorithm
# The graphic representation of an algorithm (or a program flowchart) is its representation in the form of a diagram
# consisting of a sequence of blocks (geometric shapes), each of which displays the content of the next step of the
# algorithm. The action performed in this block is briefly recorded inside the figures.
# Let us consider the basic symbols for the representation of different parts of a flowchart.

#               Flowcharting guidelines:
# A flowchart should flow from top to bottom.
# If a chart becomes complex, utilize connecting blocks.
# Avoid intersecting flow lines.
# Use meaningful description in the symbol. Single keywords or short phrases will make a flowchart clearer and more
# concise.
# You can create flowcharts of programs manually, or you can use numerous special creation tools.
# When we implement loops using flowcharts, the arrow after the statements in the part "Yes" can go into the conditional
# block, or possibly into the branch leading to it.

#                                  Functions

# All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter
# refers to within a function, the change also reflects back in a function call.

# Consecutive strings are concatenated.
# Until we close the parenthesis, the expression will not end. So, we can write this:
# str = ("first line \n"
#        "second line")

#       When writing a recursive function, we are creating an infinite loop, i.e. the function calls itself ... and can
# never stop. Therefore, in recursive functions, you must use the following rules:
# At each call to a function, transfer the changed data.
# After the completion of the next call to a recursive function, some result must be returned to the calling function
# for further use.
# At some step, the further call of a recursive function must be terminated. A recursive process should step by step
# simplify the problem so that a non-recursive solution appears for it. Therefore, there are always two cases in a
# recursive function: recursive and base cases.

# single_dimension array and multi dimension array

# Arrays in Python
# Python does not have a concept of Arrays. However, Python provides another data structure called a list, which is an
# ordered collection of items that enables an easy use of a set of data that provides similar functionality as arrays
# in any other language. Also, to work with arrays in Python, you can use special libraries, like the NumPy library for
# a high-performance array implementation that aims to provide an array object that is up to 50x faster than traditional
# Python lists. The lists are covered in the topic "7.3 Lists. Stack. Queue. Binary tree".

# Structures comprise different types of data. However, Java and Python do not exactly operate with the same thing as
# a structure in C. The struct module in Python is used to convert native Python data types, such as strings and
# numbers, into a string of bytes, and vice versa.

# A structure allocates memory for every variable of it separately, while a union allocates a single shared storage
# space for all of its variables which will be the size of its biggest data member.

# Note that the lists in Java and Python and the lists as data structures are completely different lists.

#         Non-Primitive or User-Defined Data Structure Classification

#         Non-primitive:
# Build-in data type structure in Python
# -tuple, list, set, dictionary
# User-defined data structure in Python
# -Linear: stacks , queues
# Non-linear: graphs , trees

# A stack is an ordered set of elements in which the placement of new ones and the removal of existing ones occur
# at one end, called a top. A stack implements the LIFO semantics which stands for Last In First Out. When adding and
# removing from a stack, the last added item will be the first one to be removed. Stacks have a wide range of uses in
# algorithms. For example, they are used in language parsing as well as runtime memory management which relies on
# a call stack.
# There are several ways to implement a stack:
# using a one-dimensional array
# using a linked list
# using an object-oriented programming class.
# A stack needs only three operations:
# push() that adds an element to a stack
# pop() that removes an element from a stack
# top() that gives the most recent element on a stack without removing it (peek() in Java).

# A queue implements FIFO (First In First Out) semantics. !!!!!
# There are several ways to implement a queue:
# using a one-dimensional array
# using a linked list
# using an object-oriented programming class
# A queue needs a few operations:
# push_Back () that adds an item to the end of a queue
# pop_Front() that removes an item from the front of a queue

# type of queue :
# Double Ended Queue or Deque
# Priority Queue

# Binary Tree
# A tree is a data structure, that is, a tree-like structure in the form of a set of related nodes. It works in
# a similar way as graphs in mathematics.

# A real tree has a root, branches, and the ends of the branches have leaves. The tree data structure is similar to the
# structure of a regular tree and starts at the root node. Each node can branch out into child nodes. If a node has no
# children, then it is called a leaf node. Unlike real trees, they grow from top to bottom: the root node is usually
# drawn at the top and the leaves – at the bottom (in the picture above, compare the trees in life and in programming).
# There are the following types of trees depending on how many children (branches) each node can have:

#   A binary tree is a finite set of elements that is either empty or contains an element (root) associated with two
# different binary trees, called the left and right subtrees. Many trees have at most two child nodes.

#   A quadtree is a tree with four child nodes. In a quadtree that can be used to cover a grid, child nodes are usually
# named according to the direction they cover: NorthWest or NW, NorthEast or NE, SouthWest or SW, and SouthEast or SE.

# There are three ways to traverse the tree:
# Traversing the tree from top to bottom (in the direct order): A, B, C - prefix form.
# Traversing the tree in the symmetric order (from left to right): B, A, C - infix form.
# Traversing the tree in the reverse order (bottom to top): B, C, A - postfix form.

#   A binary tree works according to the rule that child nodes which are smaller than a root node keep on the left side,
# and child nodes which are greater than a root node keep on the right side. The same rule is applied for child nodes
# that are sub-trees themselves. Let us consider an example:

# grades = input("Enter the grades for the test: ").split()
#
# for grade in sorted(set(grades)):
#     print("Number of ratings {} = {}".format(grade, grades.count(grade)))
