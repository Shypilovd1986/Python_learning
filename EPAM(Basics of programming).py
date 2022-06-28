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

#  Big O notation is used to describe the complexity of algorithms or to predict the effectiveness of a
#  written block of code.

# The ways to look at the efficiency of an algorithm include:
# worst-case scenario
# best-case scenario
# average-case scenario
# In a worst-case scenario, an algorithm gets a data input that would take the largest possible number of actions to
# process compared to other possible inputs of the same size.
# Basic rules for calculating an algorithm's Big O Notation as follows:
# Ignore constants: we are concerned only with those elements of the function that influence the order of growth.
# For example,  gives . Certain terms "dominate" other terms (ignore low-order terms): we ignore low-order terms when
# they are dominated by high-order ones. For example,  gives ;


# Designation	Title	Description	Simple Example of Algorithms
# O(1)Constant time	Getting a collection item, for example, getting by the index in an array. Example int a = 10+5*8;
# O(log n)	Logarithmic	Divide and Conquer. The running time grows in proportion to the logarithm of the input.
# The "binary search" algorithm (described in topic 8.2) or algorithms that use if-else statements.
# O(n)	Linear time	Looping through a collection.	Finding the sum of all elements of a one-dimensional array.
# O(n logn)	Linearithmic, loglinear, quasilinear, or "n log n"	Iterations that use Divide and Conquer.
# The running time grows in proportion to n log n of the input.	The "binary search" algorithm (described in topic 8.2)
# that uses nested loops for a deep search.
# O(n2)	Quadratic	Nested loops over a collection, i.e. a loop within a loop yields f(n) = n2(a loop within a loop
# within a loop yields f(n) = n3).	Using nested loops to iterate over an array, or entering an array that is twice
# the size specified.
# O(2n)	Exponential	These algorithms grow in proportion to some factor exponentiated by the input size.	The algorithm
# for calculating the Fibonacci number recursively from top to bottom, if you do not use caching.
# O(n!)	Factorial	This class of algorithms has a run time proportional to the factorial of the input size. The
# factorial complexity is any enumeration of all possible combinations.	Any problem, for example, finding the maximum,
# which is solved by enumeration, or the output of all possible combinations of array elements will have factorial
# complexity.

# Big O is called an asymptotic function since it takes care of the performance of an algorithm at the limit, that is,
# when a lot of input data is entered into it. It should also be noted that there are other asymptotic functions.

# Function	Description
# o(n)	o tells us that we found a complexity bound that is not tight.
# O(n)	O tells us that our code will never run slower than a specific bound.
# Θ(n)	Presents the time complexity or just the complexity of our algorithm.
# Ω(n)	Ω gives us such a complexity that our program cannot be better, i.e. it gives us a lower bound for the
# complexity of our algorithm.
# ω(n)	ω tells us that a lower bound isn't tight.

# Recall that programs can use several ways to fill arrays, such as the ways provided below or by combining them.
# Assigning values to elements: the values of some arrays are known in advance. For example, the number of days in
# each of the 12 months of the year, the business results of the previous year, etc. Such arrays with the available
# data are usually initialized at the time of declaring these arrays or by using an assignment operation.
# User input: a user can fill arrays with data entered from the keyboard.
# Reading data from the files stored on a disk or from another input source: a user can also fill arrays with the data
# read from a file. Some stock information or a school report card are examples of large amounts of data that are
# difficult to enter manually each time you start a program. Therefore, it is better to store them in files and read
# them into the application as needed.

# There are several basic search algorithms in programming languages.
# - The simplest, but not the most efficient one, is a linear or sequential search. The search is carried out by full
# sequential iteration over the array elements  and by comparing its values with a given key. The speed of the
# algorithm is quite low. The time complexity of the mentioned above algorithm is O(n).
# - We can use a binary search. In this case, a search is performed in a sorted array by repeatedly dividing the
# search interval in half. In other words, let's first check the middle element of the array. If it is greater than
# the desired value, then check the middle element of the second half; otherwise, check the middle element only of the
# first half. We will repeat this procedure until the required element is found, or until there are no unchecked
# elements. On average and in the worst case,the time complexity of a binary search algorithm is O(log(n)).

# def binary_search(arr, left, right, elem):
#     while left <= right:
#         mid_index = (right + left) // 2
#         if arr[mid_index] == elem:
#             return arr[mid_index]
#         elif arr[mid_index] < elem:
#             left = mid_index+1
#         else:
#             right = mid_index-1
#     return None
#
# library_num = [108, 123, 124, 235, 285, 379, 456, 476, 756, 998]
# print("The list of the library card numbers are", library_num)
# required_num = int(input("Enter the library card number: "))
# if required_num > 0:
#     amount = binary_search(library_num, 0, len(library_num)-1, required_num)
#     if amount is None:
#         print("\nThe reader is not registered in the library.")
#     else:
#         print("The reader", amount, "is registered in the library and took book(s).")
# else:
#     print("You entered an invalid customer library card number.")
# The result:
#
# The list of the library card numbers are [108, 123, 124, 235, 285, 379, 456, 476, 756, 998]
# Enter the library card number: 456
# The reader 456 is registered in the library and took book(s).
#
# Different types of sorting algorithms have different logic and different steps but they are all based on:
# Comparison operations: sequential comparison of array elements (except radix sort).
# Permutations: the method that swaps out-of-order elements. The exchange continues until all elements are ordered.

#                                    type of sorts
# Bubble Sort is the simplest sorting algorithm. We compare pairs of adjacent elements and swap them if they are
# not in the correct order.
# You should choose the bubble sort when:
# an array is partially sorted as the bubble sort is adaptive
# an array to be sorted is relatively small
# a simple sorting implementation is desired
# there are limits on memory usage

# Insertion sort iterates through an array and moves the desired value to the beginning of the array. After the next
# position has been processed, we know that all positions preceding it are sorted, but not the positions following it.
# This sort is "stable" since identical elements will not change their order.
# def insertion_sort(arr):
#     count = 0
#     for i in range(1, len(arr)):
#         key_item = arr[i]
#         j = i-1
#         while j >= 0 and key_item < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#             count +=1
#         arr[j + 1] = key_item
#     print("The number of permutations is", count)

# Selection sort is a kind of hybrid between the bubble sort and the insertion sort. Like the bubble sort, this
# algorithm iterates over an array over and over, moving one value to the correct position. The correct position for
# the selected element is determined before moving to the next element in the array, and with each pass, the unsorted
# part of the array is decreased by one element. However, unlike the bubble sort, it selects the smallest unsorted value
# instead of the largest one. As with the insertion sort, the sorted portion of the array is at the beginning, while in
# the bubble sort it is at the end.
# Selection sort is NOT a stable sorting algorithm because equal elements are re-arranged in the final sort order
# with relation to one another.
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min = i
#         for j in range(i + 1, len(arr)):
#             if arr[min] > arr[j]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]

# an array is not partially sorted, so even if an array is partially sorted, still each element is compared and there
# is no breaking out early
# an array to be sorted is relatively small
# a simple sorting implementation is desired
# there are limits on memory usage

# Heapsort is a comparison-based sorting technique based on the binary heap data structure. This is similar to
# sorting by selection, where we first find the minimum element and place the minimum element in the beginning. However,
# in this case, the largest elements are usually placed in the nodes. We repeat the same process for the rest of the
# elements. Heapsort combines the time efficiency of merge sort and the storage efficiency of quicksort

# Heapsort is NOT a stable sorting algorithm because equal elements are rearranged in the final sort order with
# relation to one another.

#   def heapify(arr, n, i):
#       largest = i
#       left = 2 * i + 1
#       right = 2 * i + 2
#
#       if left < n and arr[i] < arr[left]:
#           largest = left
#
#       if right < n and arr[largest] < arr[right]:
#           largest = right
#
#       if largest != i:
#           arr[i], arr[largest] = arr[largest], arr[i]
#           heapify(arr, n, largest)
#
# def heap_sort(arr):
#     for i in range(len(arr)//2,-1,-1):
#         heapify(arr, len(arr), i)
#     for i in range(len(arr)-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)

# You should choose the heapsort when:
# an array is partially sorted
# an array to be sorted is relatively small
# a simple sorting implementation is desired
# there are limits on memory usage

# Merge sort is a sorting algorithm that orders lists (or other data structures whose elements can only be accessed
# sequentially, such as streams) in a specific order. To merge means to combine two (or more) sequences into one
# ordered sequence by cyclically selecting the items currently available.
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         mean = len(arr) // 2
#         left_arr = arr[:mean]
#         right_arr = arr[mean:]
#         merge_sort(left_arr)
#         merge_sort(right_arr)
#
#         i = j = k = 0
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1
#
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1

# You should choose the merge sort when:
# there is a need to implement external sorting
# an array is not partially sorted, so despite the fact that in the worst case scenario it will work faster than the
# linear one, in the best case scenario, its performance will be lower than that of the linear one
# there are no limits on memory usage

# Quicksort sort is one of the "divide and conquer" algorithms. It works by recursively repeating the following steps:
# Select a key index and split an array into two parts by it. There are many ways to do this, random or rightmost (i.e.
# the last) element, for example.
# Move all elements greater than the key to the right side of the array, and all elements less than the key to the left
# side. The key element is now in the correct position - it is larger than any element on the left and smaller than any
# element on the right.
# Repeat the first two steps until the array is completely sorted.

# Quicksort is significantly faster than other O(nlogn) algorithms, because its inner loop can be efficiently
# implemented on most data structures, and in most real-world data, it is possible to make design choices that
# minimize the probability of requiring quadratic time.

# def partition(arr,left,right):
#     i = ( left-1 )      # index of smaller element
#     key = arr[right]    # a key element
#
#     for j in range(left, right):
#         if   arr[j] < key:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
#     arr[i + 1],arr[right] = arr[right],arr[i + 1]
#     return ( i+1 )
#
# def quick_sort(arr,left,right):
#     if left < right:
#         key_index = partition(arr,left,right)
#         quick_sort(arr,left,key_index - 1)
#         quick_sort(arr,key_index + 1, right)

# You should choose the quicksort when:
# a fast sorting is desired
# there are no limits on memory usage or they are not very flexible

# Radix sort is a non-comparative sorting algorithm. It avoids comparison by creating and distributing elements into
# buckets according to their radix. The array is iterated over for several times, and the elements are rearranged
# depending on which digit is in a certain bit. After processing the bits (all or almost all), the array is ordered,
# and the bits can be processed in opposite directions - from the least significant to the most significant, or
# vice versa.

# def counting_sort(arr, place):
#     size = len(arr)
#     output = [0] * size
#     count = [0] * 10
#
#     # Determine count of elements
#     for i in range(0, size):
#         index = arr[i] // place
#         count[index % 10] += 1
#
#     # Determine cummulative count
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#
#     # Place the elements in the correct place
#     i = size - 1
#     while i >= 0:
#         index = arr[i] // place
#         output[count[index % 10] - 1] = arr[i]
#         count[index % 10] -= 1
#         i -= 1
#
#     for i in range(0, size):
#         arr[i] = output[i]
#
# def radix_sort(arr):
#     max_item = max(arr)
#     place = 1
#     while max_item // place > 0:
#         counting_sort(arr, place)
#         place *= 10

# The examples of known binary file extensions include: *.bin, *.jpg, *.mov, *.gif, *.zip, etc.
# A text file is a kind of binary file and consists of bits. Just a different data recording format. Without the
# knowledge of the code page, you won't be able to normally read a text file.
# To work with any file, the main operations that need to be done are:
#
#   Opening the file so that you can refer to it. When you open the file, some errors can occur, such as the file may
#   not exist, it may be the wrong type of the file, you may not have permission to work with the file, etc.
# You should take into account all these errors.
#   Directly processing the file data (writing, reading, searching, etc.). It should also be remembered here that we
# are not working with random access memory but with a buffered stream, which adds its own specifics.
#   Closing the file. Since the file is an external resource to the program, if it is not closed, it will continue to
# be in memory, possibly even after the program is closed (for example, you probably tried to delete an open file or
# make changes, etc.), or some data may not be written. In addition, sometimes it is necessary not to close, but to
# "reopen" the file in order, for example, to change the access mode.
#
# Do not open binary files (such as jpeg, exe, doc) in text mode as this may lead to the files being corrupted.
# File Access Type Table:
#
# File Mode	Description
# 'r'	Opens a file for reading. If the file is in read mode, the data is not deleted if the file already exists on
# the system. If there is no such file, then an error occurs. If the file is open in read mode, then writing to it is
# impossible, it cannot be written or changed.
# 'w'	Opens a file for writing. If the file exists, then its contents are lost. If the file does not exist at all,
# a new file is created. If the file is open in write mode, then data can only be written to it, it cannot be read.
# 'x'	Creates a new file for writing. If the name of an existing file is specified, an exception will be generated.
# No data loss will occur in an existing file.
# 'a'	Opens a file to write to the end of the file (append). If the file does not exist, then it is created. The prev
# iously added file content does not change.
# 'r+'	Opens a file for reading and writing from the beginning. The file must exist.
# 'w+'	Opens a file for reading and writing. If the file exists, then its contents are lost.
# 'a+'	Opens a file for reading and writing at the end of the file, appending to the file. If the file does not
# exist, then it is created.

# Combinations of the above literals can also be appended with:
#
# "t" – opens a file in text mode, can be omitted
# "b" – opens a file in binary mode
# The following access modes are possible: 'wb', 'rb', 'wb+', 'rb+', etc. If the mode is not specified, then a file is
# opened in 'rt' mode.
# After working with a file, access to it must be closed using the function close(). This method of the file object
# discards all unwritten information and closes the file object, after which no more writing can be made.
# file_object.close()

# my_file = open("My_information.txt", "w")
# print ("Name of the opened file:", my_file.name)
# my_file.close()

# The main actions while working with files are writing and reading information.
# All actions for reading and writing data to a file can be divided into three groups:
# Character-by-character input-output operations.
# Operations of line input-output.
# Input/output operations in blocks.

# Writing to a File:
# write(str): It writes a string or a sequence of bytes to a file (for binary files) and returns the number of
# characters written to the file.
# writelines(lines): It writes a list of lines without delimiters (such as line breaks) to a file.

# Reading Data from a File:
# read(size): It reads from a file the size amount of data and returns a newline as '\n'. If the size parameter is not
# specified, it reads up to the end of the file and returns the data that was read. Upon reaching the end of the file,
# with further reading we get an empty string.
# readline(): It reads a string from the specified position to the end of the string from the file object and returns
# it. It reads at most n bytes/characters if specified.
# We can read a file line-by-line using a for loop. This is both efficient and fast.

# with open("my_information.txt",'w',encoding='utf-8') as my_file:
#     my_file.write("Name is Tom Hardy.\n")
#     my_file.write("I am an English actor and producer.\n")
#     my_file.write("I am active in charity work.\n")
# with open("my_information.txt",'r',encoding='utf-8') as my_file:
#     print(my_file.readline())
#     print(my_file.readlines())

# my_file.seek(0, 0)       if we add this file will be read from the beginning

# As in C, Python has the current cursor in the file (position), and all operations with data in the file will be
# performed starting from that position. We can change the current position in the file using the seek(offset[, from])
# method. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference
# position from where the bytes are to be moved:
# SEEK_SET	0	The offset is performed from the beginning of the file. The offset should be zero or positive.
# SEEK_CUR	1	The offset is performed from the current cursor position. The offset may be negative.
# SEEK_END	2	The offset is performed from the end of the file. The offset is usually negative.
# And to find out the current position, we can use the tell() method.

# A class is an abstraction; it is a user-defined type
# A class declaration begins with the class keyword. The class declares data and functions that operate on this data
# (perform their processing). The data that can characterize an object of a class are called attributes or data members.
# Functions that can perform any action on the data (properties) of a class are called methods.

# Inheritance is described by an "Is - a" relationship. A cottage is a house, a garage can be a hangar, but a house
# will not be a hangar, and you cannot use inheritance here.

# The idea is quite simple - two objects can be related to each other, and this must be described somehow. It can
# be described as a “Has-a” relationship between classes.

# In other words, an association is a relationship between classes whose objects have an independent life cycle,
# and there is no ownership between the objects.
#                       type of association
#   one to one (Means that a person can only have one identity card, and an identity card can only be linked
# to one person.)
#   one to many (An example of a one-to-many relationship could be the relationship between a schoolmaster and children,
# where one schoolmaster teaches many children.
#   many to one (For example, one library may have many books, and each book is associated with that current library and
# cannot be a part of another library.)
# many to many (For example, a customer can buy a different product, and other customers can purchase the same product.)

#               There are two local cases of association:
#   Composition (has-a + whole-part + ownership): the life cycle of the child object coincides with the life cycle of
# the parent object. In other words, the whole explicitly controls the lifetime of its component part (the object (s)
# that make up or are contained by one object are also destroyed when that object is destroyed).
#   Aggregation (has-a + whole-part): the life cycle of the child object does not depend on the life cycle of the
# parent and can be used by other objects. In other words, although the whole contains its component part, their
# lifetime is not connected (for example, the component part is passed through the parameters of a constructor).

# class Wall:
#     def __init__(self, material, height):
#         self.material = material
#         self.height = height
#
#
#     def __str__(self):
#         return "Material is '{}', height = {} ft.".format(self.material,
#         self.height)
#
# class Furniture:
#     def __init__(self, name, cost):
#         self.name = name
#         self.cost = cost
#
#
#     def __str__(self):
#         return "name = '{}', cost = {}$".format(self.name, self.cost)
#
# class Apartment:
#     def __init__(self, street, apartment_no, material, height, furniture):
#         self.street = street
#         self.apartment_no = apartment_no
#         self.walls = Wall(material, height)
#         self.furniture = furniture
#
#     def __str__(self):
#         return "The address is '{} St' {}, walls {}, furniture=[\n{}]".format(
#         self.street,
#         self.apartment_no,
#         self.walls,
#         '\n'.join(str(element) for element in self.furniture),
#         )
#
#     def get_total_furniture_cost(self):
#         total_cost = 0
#         for element in self.furniture:
#             total_cost += element.cost
#         return total_cost
#
# if __name__ == "__main__":
#     furniture = [Furniture("bed", 150), Furniture("cupboard", 250),
#     Furniture("table", 35), Furniture("armchair", 80)]
#     flat1 = Apartment("Bronco", 3050, "brick", 23, furniture)
#     print("Information about the first apartment:", flat1)
#     print("Total furniture cost is {}$".format( flat1.get_total_furniture_cost()))