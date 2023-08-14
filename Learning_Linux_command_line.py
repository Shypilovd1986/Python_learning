# *****************         Intro            ****************

#   Linux is a general purpose computer operating system originally released in 1991 by Linus Torvalds. Linux is
# defined by its kernel, which is the core component of the operating system. The kernel is software which allows other
# software to communicate with a computer's hardware. Linux was inspired by MINIX, which in turn was inspired by Unix.
# And Linux is based on a philosophy that software and operating systems should be free. Both free of cost and freely
# changeable. The software license, which allows this in the case of the Linux kernel, is called the GNU General Public
# License. This emphasis on freedom, both of cost and modification, has helped Linux to become popular for many
# different applications and purposes.
#   Different groups of software and configuration choices that are maintained by individuals or groups of people are
# called distributions, or distros. Most major distributions of Linux fall into a few categories based on the original
# distribution from which they were derived. There's Arch, Debian, Red Hat, and Slackware, and many other distributions
# that we might use, or we might use distributions based on, or derived from, these particular distributions.
#    In this course, we'll focus on Ubuntu Desktop, which is based on Debian Linux. Ubuntu Desktop is user-friendly and
# it includes many tools and programs that make it a good choice for learning about Linux.
#    In practice, many companies and organizations use a distribution of Linux derived from either Debain or Red Hat.
#   --- Linuxmint, Ubuntu, Elementary OS, and Kali Linux are all derived from Debian.
#   --- CentOS, Fedora, and Red Hat Enterprise Linux are all part of the Red Hat ecosystem.
#    But as you begin working with Linux through the command line, most of what you'll do is the same across major
#    distributions. That's because the text interface, often called the command line, is a program called a shell, and
#    we'll be using the Bash shell, which is available almost everywhere. So what we explore in this course will apply
#    on any Linux distro you might find yourself using in the future.
#
#   Ctrl+Shift+'+'  make a screen a little bite more

# Comand LLine Interface :
# - allows us to interact with programs using text commands
# - command-line programs can read text inputs and output text to the screen
# - Command-line programs can read from and write to files, or use information from, or send information to other
# programs or systems.
#
#  The software will use to work with command line software, is called a shell, or command-line interpreter. And there
#  are many shells out there. Bash, the Bourne Again Shell, was first released by Brian Fox in 1989. It's still one of
#  the most widely used shells on Linux systems. And it's the one you're likely to need to become familiar with as you
#  begin your Linux command line journey. Bash extends the capabilities of earlier shells and adds newer features too.
#  Bash builds on an earlier shell created by Steven Bourne called the Bourne shell.

#  It's common to use both graphical and text-based modes of interaction at the same time. And it's common to have more
#  than one terminal window open at the same time to perform different tasks. And some programs, like software
#  development tools, include a built in terminal as well.

#  The command-line, is the general name for a text environment where we issue commands by typing. The shell is the
#  software that accepts and runs those commands. And the terminal emulator is the software the shell runs inside of.
#  Because these pieces are so closely linked, many people call the shell, the terminal and vice versa. And really there
#  isn't any harm in doing so. Generally people will know what you mean. But it's important to know that each of these
#  components are different, because their roles will become more distinct,

#  The general pattern that we'll see is command, options, and arguments. ls -lh
#  The command is the program you're running, or the action you're taking.
#  Options and arguments apply to the commands.
#  So a command is a program that takes a particular action. It's what we're asking the system to do.
#    The next part of a command line statement, the options, tell the command how to operate, changing the behavior of
#  the command, or telling it to perform different actions. In many cases, these options start with a dash or minus
#  sign, and are usually represented by one letter or number. Most commands offer more than one option. And when we need
#  to use more than one, we can list them individually.
#   For example, starting with just the ls command, I can add an option -l, which tells the ls command to show me a long
#  listing of the files in the directory rather than a shorter one. That means it shows more details about files, as
#  we'll see shortly. I can add other options too, like -a, which shows files that are normally hidden.  ls -l -a, or
# ls -lah , if we change options it will be the same
#  Some options have a longer syntax, and they start with two dashes. The options that have two dashes can't be
#  combined together. They have to go one right after the next separated by a space , for example
#  ls --group-directories-first --human-readable
#  The last portion of a statement is the argument or arguments. This is where we tell the command what thing to operate
#  on. It's usually a file or path or a set of files or directories separated by spaces. But an argument can also be a
#  string of text or something else.
#  ls -lh /usr/bin    we're telling the ls command to show us the contents of the directory usr/bin.
#  sort -u users.text   , we're telling the sort command to sort a file called users.
#  grep -i "needle" haystack     example uses a file called haystack, which is being provided to it as an argument. And
#  we're using the -i option to look for the text needle. I should point out here that strictly speaking the text needle
#  is also an argument, but it's an argument to the -i option, not directly to the grep command. Options can take
#  arguments of their own.
#
# ***********************************    Write commands in a shell at the prompt    **************************

#  The terminal application runs a shell program, which I mentioned before, the text-based interface, where we can
#  interact with a system.
# F11 to make the window full screen
#       The first thing we see here in the shell is the prompt. The prompt shows a little bit of information, in my case
#  it's my username @ my host name, which is the computer's name and the name of the folder where I'm currently working.

#  ls     to list the contents of this directory,
#  ls -l   means long listing, and that tells the LS program to show files with more detailed than just a list of names.
#        Commands need to be spelled exactly right or they won't work. Spacing and other characters that we'll use need
#  to be correct. The shell usually won't help us out if we get a command a little bit wrong or spell something a little
#  differently.
#        The commands we use are either programs installed on the system or are keywords of a shell-like bash. Most of
# what we'll use in this course are programs, the GNU core utilities or coreutils, which are the standard programs that
# come with most Linux distributions.
#   stands for the manual pages. We can think of the man pages as a technical reference book for our Linux distribution.
# If we know the name of a command, we can find out a wealth of information about what it does, what options it provides
# and what arguments it takes.

#  man ls    show information about command ls , if we press q we will quit

#  ls --help     Many commands also have an option called help, which provides a brief amount of information about them.
#  However, they usually refer you to the man pages for more detailed documentation.

# help        the help tool can act as a handy reminder for the syntax of some Bash-specific commands.

# apropos <what we are looking>     for ex apropos list    ,  Apropos searches a list of installed programs that can be
# used as commands and searches their descriptions for texts that you provide as an argument.

# ls -l De  if we press tab it will end the command , if we press ctrl + c it will cancel command

# When we press tab it must have one strong suggestion to return , if we will press tab one more time we will have
# possibilities

#       Notice that if I put a space here and press tab again, Bash will treat the second item as an argument. So auto
#  complete is showing me files and directories. It thinks I might want to pass into the A command, which doesn't do
#  anything.

# ctrl + A   , ctrl + E
#       Control A and control E moved to the beginning and the end of a line respectively. Control is represented by the
#  caret character, which is this little pointy character. Caret is spelled C-A-R-E-T, not like the vegetable.

# ctrl + left arrow         move left one word
# ctrl + right arrow        move right one word
# ctrl + U      delete from cursor to line start
# ctrl + K       delete from cursor to line end
# ctrl + shift + C      copy selected to the clipboard
# ctrl + shift + V      paste text from clipboard
# ctrl + R      search command history
# ctrl + C      cancel command


#
# df   report file system disk space usage,    df -h    report in Mb

# apropos "search for files"              in double quotes and when I run that, I see the result find, !!!!! Using the
# double quotes gave me an exact match for this phrase,

# *********************      files directory and permissions      ************************

#        Files are collections of information that represent photos, documents, source code, databases, and all kinds of
#  other things. These are the basic concept of data organization we work with in a graphical environment. And that's
#  true in the command line environment as well.

# file       determine file type
# stat       display file or file system status

#  On a Linux system everything is a file !!!!!
#  We organize files into directories which are sometimes called folders,
#  On a Linux system, files and directories are part of the file system, which defines the way the data is represented
#  on the system's storage media. Most Linux distributions follow the Filesystem Hierarchy Standard (FHS), a standard
#  which defines where certain kinds of files are stored on the file system. Having files like configurations, programs,
#  or binaries and so on in predictable locations is important to the operability of software across Linux distributions
#       The file system starts with the root represented by a slash. The file system root is the highest level of the
# organizational hierarchy of the file system. Each Linux system only has one file system and everything else
# directories, external hard drives, network shares, and so on are represented within it.
#
# ~     each user will be able to use the tilde character to represent their own personal home directory.

#  qif you hear the term root in relation to a file system path, it refers to the file system root not to the special
#  home folder.
#
# /etc      common configuration file
# /bin or /sbin    common programs or commands
# /lib   shared libraries and modules
# /mnt   or  /media standard location for mounting other file system
# /dev      The dev folder is where the system keeps references to all of the hardware it has hard drives, memory, CPU's
# and everything else.
# /proc    contains references to processes that are running on the system.
# /sys    holds files representing different kernel parameters and system information.

# *********************           path           **************************

#       There are two kinds of path called absolute and relative. An absolute path starts from the root of the file
# system, the highest level of the structure where the files are stored, which remember is represented by the slash
# character. This allows us to define a full specific location from the highest level of the file system, all the way
# down to a specific directory or file.

#       relative path, a path that isn't a complete absolute path, starting from the file system route, but one that
# starts from the current working directory as its base. The working directory is where any action we do will take place
# unless we've told a command to use files in a different path.

# ".."   In order to refer to directories higher up in the hierarchy from our working directory, we can use two dots or
# periods.

#    The tilde here is a feature of bash and many other shells and its behavior is called tilde expansion. While using
# the tilde in a path feels a little bit like using a relative path, it's really not, because the shell expands it into
# the first part of an absolute path. It's just that that part of the absolute path will be different for different
# users, but regardless it expands into a path that starts from the file system route. Regardless of our current working
# directory, the tilde will always represent our own home folder.

# *******************************      Navigating the file system       ****************************

# cd   <name directory>        change directory
# cd       return to home directory
# cd -      If I wanted to step back to the previous folder that I was using, whatever that was, I can use the shortcuts
# cd, space and a dash or a minus.
# pwd      show current directory
# . To work with file and directory names that have spaces in them, we have to tell Bash that this space is part of the
# path not a separator between two arguments or commands. There are two ways to do this. The first way is to put the
# path inside double quotes. But the more common thing we'll see is just to escape or especially mark certain characters
# to tell the Shell to treat them differently than it normally would.

#  ls -R  <departments  our directory>     I'll write ls and this time I'll use the dash capital R option to list
#  directories recursively and I'll add departments as an argument using tab completion. After I press Enter, I can see
#  what's inside all the directories inside of the department's directory
# ls --color=always     show code always in color
#
#       after exploring folder by ls -l we see some column.  The first column on the left shows whether an item is a
# directory, which will be shown with a D, a link with an L or a file represented by a dash, meaning that the attribute
# is missing or not set.
#       The next set of columns show a representation of the permissions on the file, which describes the, what kind of
# things users and members of groups are allowed to do with a file. We'll take a look at these in depth later on.
# Further to the right, we see the owner of the file and the group setting of the file.
#        Further to the right, we see the owner of the file and the group setting of the file.
#        Then we see the size of the files in bytes, which can be a little bit easier to read with a dash each option.
#        Over further to the right in the output there's the date and time that the file was modified. And finally,
# there's the name of the file or in the case of a link
#
# ********************            Create and remove directories         ************************

# mkdir <name directory>      create new directory in current folder
# mkdir <folder1/nameDirectory        create directory in folder1
# mkdir <name directory 1> <name directory 2>           create two or more directories
# mkdir -p <name directory1>/<name directory 2> This option creates any parent directories that are needed. Create
# directory 1, and then create directory two inside it
# rm <name directory>     delete directory
# rm filename?.txt    remove all files which have one character after filename , for ex filename1.txt, filename2.txt ..
# rm <name directory> -r        remove all files in select directory recursively

# ******************        Copy, move, and delete files and directories            *************

# cp <name file> <name file where copy>          The first file name argument to the CP command is the file we want to
# copy and the second file name argument is where we want to copy it to.
# cp <name file> path/where copy this file              copy file to directory
# mv <name file> path/where move this file              move file to directory
# mv <name file> <new name file>            rename file
# mv <name file> path/directory/new name file        we can move and rename file
# "."   one dot, It represents the current folder or current working directory. We can use that when working with files
# mv path/file.name .           move file from specify path to current directory
#
#  We can also move copy and delete more than one thing at a time. And one of the ways we can do that is with what are
#  called wildcards. Wildcards are characters that stand for or represent patterns in text.
#  *   star or asterisk and question mark. Star stands for any number of characters
#  ?   question mark stands for one character.
#
# mv *.txt path/where move/           move all files with extensions txt to specify directory
# mv * path/where move/           move all files  to specify directory
#
# *********************        Find files from the command line      ****************

#       To use find, I'll type find, and then provide the location or the scope of there I want to search. I'll use the
#  dot or period character for the current working directory, which is my exercise files, and then I'll type space and
#  add -name, which is the test I'm using to match files. I want to match files based on their name. There are other
#  options, like size, date and so forth but I find that I use name the most. Then I'll put a matching pattern for what
#  I'm looking for. I'll put poe* in double quotes. The asterisk wildcard will match any number of characters. This
#  should find our poems.txt file.
# find . -name "d*"     will find all files and directories which starts with a letter d in current directory
# find ~/Documents -name "d*"    will find all files and directories which starts with a letter d in Documents directory
#
# *********************         Understand user roles and sudo           ********************

#  On a multi-user system, I can have a user, you can have a user and our files are kept separate in our individual home
#  directories. We can create files that only one or another user can access. At the command line, we can switch between
#  users with the SU command, which is variously referred to as set user, switch user or substitute user. To use SU, we
#  write that command, followed by the name of the user we want to switch to, and then we'll need to provide the
#  password for that user. One of the most common uses for switching users at the command line is to do some system
#  administration tasks. There are two basic user roles on the Linux system, Normal Users and the Superuser. The
#  difference is one of privilege. A Normal User can modify and create, delete, and move their own files, but they can't
#  make system-wide configuration changes, they can't install software, they can't make changes to system files and they
#  can't change other users' files. The Superuser, which is called Root, can make changes to the system. It can install
#  software, it can start and stop services, and can perform other tasks that affect how the system overall operates.

#  So in order to allow changes to be made to the system, normal users can be granted the ability to temporarily use
#  Root's power, through a command called sudo. The command is spelled S U D O, and is commonly pronounced sudo or sudu.
#  We only want to borrow Root's power when we really need it.
# sudo ls /root      gives power of superuser to show content of root directory
# sudo -k     it's a good idea to type sudo -k to give up those privileges, meaning we'll need to type our password in
# again the next time we use the command.
# sudo -s     login  to Root shell , . And I'll need to type in my user's password. And you'll notice when we switch
# over, the prompt changes a little bit. When we were a normal user, the end of the prompt was a dollar sign, but now
# it's a pound sign or a number sign. Of course, the username over here also changed to Root, but the prompt changing
# away from the dollar sign is another visual cue to remind you that you're working as Root. To switch back to my user,
# I'll type exit.
# exit      use with command switch to normal user
# $      prompt end when we work as normal user   !!!!!!!!!!!!!!!!!!
# #      prompt end when we work as Root user  !!!!!!!!!!!!!!

# *****************        Understand file permissions         **********************

# rwxrwxrwx   file1
#  The sequence of letters, breaks down into three sections.
#  The first section represents the user designated as the owner of the file.
#  The second section of three letters represents a group, a collection of users for whom we can define specific access
#  to the file.
#  And the third section represents the access to the file for all other users who are not the files owner or who are
#  not in the group designated in the group section.
#  Each of the sections of three characters breaks down into three individual letters, which stand for read, write and
#  execute.
#  r    Read means that someone can see the contents of a file, but not modify it.
#  w    Write, means that someone can make changes to a file, but not read the contents.
#  x    execute, means that someone can run the file.

#     We can change the permissions of a file using the chmod command. This command modifies the permission mode string.
#  The string of letters we just saw. We can also change a files owner and group with two other commands, chown and
#  chgrp. The permission mode bits on a file though when we set with chmod can be modified in two ways. The first is to
#  use an octal notation like (777, 755, 644), which uses three values to represent, read, write, and execute. There's
#  another notation with another digit in front, but that's more advanced than we need to get into here. The second way
#  is called a symbolic notation, like (a = r, g+w, and o-x) which uses a shorthand for user, group, others and all.
#  An operator and a list of permissions to change.

# chmod   changes the permission mode string
# chown   change the file's owner
# chgrp   change group

#  if my user can read, write and execute, we add all those values together and come up with seven, four plus two plus
#  one. If a files group can only read and execute, that comes out to five, four plus one. So the resulting permission
#  string for this particular set of conditions would look like this, rwxr-xr-- And as the result of the command
#  chmod 754.
#               Read(4)         Write(2)            Execute(1)      Result
#   User          r                w                    x             7
#   Group         r                -                    x             5
#   Others        r                -                    -             4

#                Read(4)           Write(2)            Execute(1)         Mode
#   User(u)          +                +                    +             u+rwx
#   Group(g)         =                                                   g=r
#   Others(o)        -                                                   o-rwx
#   All(a)           =                =                    =             a=rwx
#   +   add permission
#   -   remove permission
#   =   reset permission to match new mode(removes previous mode)

#   Octal Value               Symbolic Value              Result
#       777                      a = rwx               rwxrwxrwx
#       755                 u=rwx, g = rx, o=rx        rwxr-xr-x
#       644                 u=rw, g=r, o=r             rw-r--r--
#       700                 u=rwx, g-rwx, o-rwx        rwx------

#  Symbolic Value Changes
# Original mode             Symbolic Value           Result
# rw-r--r--                      +x                 rwxr-xr-x
# rwxrwxrwx                    g=w, o=r             rwx-w-r--
# rwxr-----                    g+w, o+r             rwxrw-r--
# rwxrwxrwx                       a-x               rw-rw-rw-

# ***********************         Modify file permissions        ****************
#   ./<name file>          The period refers to the current working directory and the slash it tells the shell to look
#   inside there to find this program.

#       An executable file means the file can be run as a program on its own without having to be loaded into another
#  program first.

# ls -l <name file>     shows permission on this file
# we can check it by command stat <name file>
# chmod 644 <name file>    or  chmod a-x     remove execution for file, but we can execute it with bash
# bash <name file>        But I can still run it with another program, the Bash interpreter.
# cat <name file>         The command, cat is often used to output the contents of a file.
#  There's no single standard permission node for files in the home directory, but they're often 755, 644 or 700.
#  Depending on what the Linux distribution you're using has chosen.

# touch <name file>      create new blank file
# nano <name file>      open file in text editor nano
# ctrl+o   save file
# ctrl+x   close file
# sudo chown root <name file>      If I change the user who owns the file, my user won't be the owner anymore. So the
# first three permission bits won't apply to my user. All right, so you do chown for change ownership, root to change
# the ownership to the root user and test.sh. I have to use sudo because I need roots privileges to set something to
# root ownership.

# **********************          Create hard and symbolic links      ****************
#
#       Links are files that reference other files. And they're used to avoid having multiple copies of the same file in
#  different places. We keep one file in one location and then add a little pointer or link to other places where we
#  want the file to appear.
#    There are two kinds of links, hard links and soft or symbolic links. Hard links, point to specific data
# on the disk, and symbolic links point to a file on a disk. It's kind of a subtle difference, but it changes how
# the resulting links work.
#   ln -s <name file> <new name of file which is a link on file>       create sft link
#   I can create a symbolic link with the ln command
#   and the -s option. Then I can give it the name of the source file, the file that I want to make a link to, and then
#   the name of the link I want to create.
#  I can also tell this entry as a link because in the first column of the output, the character is an L and for normal
#  files, it's a dash or empty.
#       It's important to know that this link we created is relative. That is if we move this link somewhere else on the
#  file system, the system won't be able to reference the original file anymore. And if we move the original file, the
#  link will break as well. Because the system will be told to look at that particular path for the linked file, and it
#  won't be there anymore. We can create a symlink using an absolute path. And that solves the first problem. A symlink
#  with an absolute path can be moved anywhere in the system, and that link will continue to work. But if we move the
#  original file, even a symlink with an absolute path will break because that path will no longer be valid.
#
# ln <name file> <new name of file which is a link on file>      create hard link
#
#  A hard link appears to the user and the system to be a regular file in a file listing. But it's also just a pointer
#  to the original file, or to be more specific, it's a pointer to the actual data of a file on the disk. Every file we
#  have is a hard link to the data that makes up the file. So creating another hard link to particular data on the disk
#  doesn't duplicate that data.

# *************************           The Unix Philosophy          *****************************
#       As we start exploring command line tools, it's important to understand the principle behind many of the programs
#  we'll be looking at. That principle often called the UNIX Philosophy, says that a tool or program should do one
#  thing and do it well.
#       This philosophy suggests that we shouldn't have tools that try to do too much. We don't want one single tool or
#  program that reads files and separates the text into another file, and renames the file and compresses it into an
#  archive when it's done or one that tries to do everything anyone could possibly want to do. We want one tool to do
#  each of those tasks so we can use those specialized tools in any way we want to.

#  At the command line, we use pipes to take the output of one command and send it to another.

#       A set of commands, connected by pipes is often called a command to pipeline. The pipe character, which is
#  represented as a vertical bar, or sometimes as a vertical bar with a little break in the middle is usually the shift
#  character on the backslash key, which is found above enter or return on a US keyboard.

# echo "some text"              prints out whatever text you give it as an argument
# echo "hello" | wc    ->    1    1    6        instead of the output from echo, we see the output of the WC program,
# responding to the input from the echo command. What WC is telling me here is that there's one line of text, one word
# and six characters. The word hello is five characters long, but WC is saying there are six characters. WC is counting
# and invisible character at the end of the string called a new line, in addition to the characters that we see

# *********************         View text files with cat, head, tail, and less       *******************

# cat     it's short for concatenate. To concatenate means to stick two or more things together. And the cat command
# can do that, but it's often just used to print the contents of a file to the screen. It's also helpful to get the
# contents of a text file into a series of piped commands.

#       The head and tail commands let us see a limited number of lines from the beginning or the end of a file. They
#  work in the same way that cat does.

# head poems.txt        show first 10 lines of the text.
# tail poems.txt        show last 10 lines of the file.

# tail -n5 poems.txt      head and tail both except the -n option for a particular number of lines to show.
# cat poems.txt | cat -n | tail -n3        So there's three commands here and two pipes, the result of running that
# series of commands or that pipeline shows us that the original file has been piped into the cat -n command which
# numbered it. Then tail showed us the last five lines of that.

# cat poems.txt | less      useful for looking at longer text files and it's called less. We can use it by itself,
# passing a file name as an argument or we can pipe output to it. Less takes text input and presents it page by page or
# screen by screen and gives us some controls to move around within the text.

# ****************            Search for text in files and streams with grep                 *****************
#
#      its most basic grep returns or outputs lines of text that match a search condition called a pattern. This pattern
# can be either a specific or explicit group of characters or they can use a pattern called a regular expression. We'll
# take a look at both briefly here, but grep is a hugely powerful tool

# grep "the" poems.txt      I'll write greb and then the search term in quotes And then the name of the file that I want
# to look inside of.

# grep -n "the" poems.txt    show result of grep with numbers of lines

# grep -in "the" poems.txt     show result of grep with numbers of lines for case insensitive matching

# grep -vi "the" poems.txt       show all line without lines which has "the"
# We can also use grep to omit lines that we don't want to see. For that, we'll use the dash
# V option. I'll write grep dash VI, so we'll also use case insensitive matching our search term T, H, E and the file
# name, poems.txt. And now I can see that none of these lines have T, H, E together. There's nothing highlighted because
# grep just drops the lines that match the search term. This can be helpful if you're looking through logs, for example,
# and want to ignore all of the output from a noisy program.

#       One of the features that makes grep so flexible, is it support for regular expressions or regexes. These are
#  expressions of patterns in texts that allow us to ask more complex questions such as returning lines with only the
#  letters H, I, J and K in them, for example. Or we could search for words longer than six letters.

# grep -E "[hijk]" poems.txt      This search term is regular expression notation for the occurrence of the lowercase
# letters H, I, J or K, and I can see that the output has done what I expect. It's showing me lines with these letters
# in them.

# grep -E "\w{6,}" poems.txt        This is notation for six or more of any character, considered a word character.
#
# ***************************           Manipulate text with awk, sed, and sort           ************************

#     One of the tasks of a system administrator, a systems analyst, a scientist, or a programmer is to make use of data
#  from various logs or outputs. We've seen how to look at files and how to search within them. So now let's take a look
#  at reaching in and extracting particular data and presenting it in different ways. There's a few common tools for
#  this and which one we used is largely a matter of preference. So it's helpful to be at least a little bit familiar
#  with both. These tools are called awk and sed. Both tools are widely used in command-line operations

#       What awk is great at and is commonly used for in scripts is pulling data out of a file according to a rule. To
#  define this rule, we write an awk program either right at the command line or in a separate file if it's very complex
#  to tell awk how to get the data we want.
#       Sed is also used for modifying information from a file or stream. It's short for stream editor. And where awk is
# really helpful for extracting particular data and presenting it as the result on screen or in a pipeline, sed excels
# at changing data as it flows through a command pipeline or in place in a file. We can use either of these in a command
# pipeline or just by themselves.
#
# awk '{print $2}' simple_data.txt        Let's write a small awk program to show us just the second column of data from
# this file.
#       The single quotes contain the awk program, in this case, just print, which returns a value and an indicator of
#  the field we want the program to return, which in this case is two.
#
# awk '{print $2 "\t" $1}' simple_data.txt      returns second column, tub, first column

# awk '{print $2 "\t" $1}' simple_data.txt | sort -n     returns second column, tub, first column , using pipe line we
# sort by number

# sed s/Orange/Red simple_data.txt       The S before the slash in the expression stands for substitute. Then there's a
# slash, the string you want to replace, another slash and the string you want to replace that string with. And the
# expression terminates with a slash.

#  sort simple_data.txt      Sort, as you might expect, sorts the data passed into it in various ways. Let's take a look
#  at our simple data file again. If I just write sort, simple_data.txt, I can see that it will sort the data on the
#  first character of each row
#
# sort -k2 simple_data.text       sort has organized the rows based simply on the first character of the second field

# sort -k2 -n simple_data.txt      I'll write sort -k2 for the second column, then the -n option, and then the file name
# And now the sorting in this output makes more sense. Sort tw column by numeric.

# sort -u dupes.txt        remove all duplicates line in file, key -u stands unique
#  We can also use sort to show us unique lines of a file or remove duplicates from our output. This is useful if we're
#  looking at a log file and need to get rid of repeated entries to make the output more clear.

# rev    prints text in reverse sequence
# tac    concatenates or display files in reverse
# tr     translates or modifies individual characters according to parameters

# ******************        Edit text with Vim          *********************

#     On most Linux distributions, there's a text editor called Vim. You'll also see it referred to as vi in some places
#  for legacy reasons. The command name vi is a shortening of the word visual and vi was a popular text editor on BSD
#  Linux. The name Vim stands for vi improved. Vi or Vim takes a little bit of getting used to

# vi   or     vim        The first screen that shows up when I open the software, gives us a sense of what it's like
# to work in Vim. Instead of having a toolbar, Vim has two primary modes,
# insertion mode, where we type and make manual changes to text
# and command mode, where we issue commands like save, search and many other things.

#  I'll press i to go into insertion mode, and here I can start typing things. And if I press escape, I'll go back into
#  command mode. Keys we press in command mode, do different things than in insertion mode. So we need to be careful
#  that we're in an insertion mode, if we want to make changes to the text.
# esc   and    i     to change mode
# shift + i   remove cursor to the beginning of the line
# :w new.txt      esc to change on command mode , then :w new.txt     save file
# :wq      esc to change on command mode  then quit

# vi poems.txt     open file in vim
# In command mode, I can press Shift G to move to the bottom of the file.
# And I can type number one and capital G to move to the top of the file.
# I can move backward and forward by sentence using the left and right parentheses keys.
# And forward and backward by paragraph using the left and right curly braces.

# I    insert at beginning of line
# i    insert at cursor location
# o    insert on following line
# :q!   quit without saving
# esc   enter command mode
# esc : w    save file
# esc : wq    save and exit

# ******************           Edit text with nano          ***********************

#  Some Linux distributions include a lightweight text editor called nano. It can be installed on many other distros
#  as well. It's quite a bit simpler than Vim, so many people prefer it, though it does lack some power user features
#  that Vim enthusiasts will miss.

# nano      launch  nano editor
# nano poems.txt      open file in nano editor
# ctrl O     save the file
# ctrl x     exit file
# ctrl W      Control W is a useful feature to find texts in the document. I'll press Control W and then look for the
# word, "bright" then I'll press Enter and I'm taken to the first match. If I press Control W again, I can search for
# the same term. Pressing Enter takes me to the next match and so on.
# ctrl V    to move down a screen
# ctrl Y    to move up a screen

# ************       Working with tar and zip archives        **************

#  .tar files, short for tape archive files, are still incredibly common for distributing, sharing, and archiving files
#  on Linux systems.
#
#       TAR files often don't involve any compression, but there are ways to incorporate compression into a TAR file,
#  which we'll see as we explore different software distribution styles. Compression tries to reduce the size of a file
#  using some mathematical tricks. If we're using compression with a TAR archive, we'll often see that the file is named
#  with an extension to indicate what kind of compression is being used. For example, there's .tar.gz or .tgz, which is
#  a TAR file with gzip compression, .tar.bz2, which is a TAR file with bzip compression, and others. gzip and bzip are
#  two different methods for compressing data, and the difference between them isn't terribly important right now.

# tar -cvf myfiles.tar Exercise\ Files/
#       Let's say I wanted to make an archive of my Exercise Files. To do that, I'll go up a level in my file structure
# with cd space .. so I'm not working inside the directory I'm archiving. And then I'll write tar -cvf myfiles.tar
# Exercise Files. The c option says, create an archive. We'll use another option later to extract from an archive.
# The v tells tar to be verbose. That is, to list out each file that gets added to the archive. This can be a useful
# way to create an index of the contents of the file, or just to see what's happening. That's optional, though, if you
# don't need to see what's going on. The f option tells the tar command we want to output the archive to a file. Without
# that, the data that makes up the TAR file will be sent to the screen, to the standard output, unless we pipe it
# somewhere else. And in this case, that's not what we want. After the f option comes the file name of the archive.
# And after that, any files or directories we want included in the archive. In this case, it's just the one folder, but
# we could put more than one if we wanted to.

# tar -caf myfiles.tar.bz Exercise\ Files/
# tar -caf myfiles.tar.bz2 Exercise\ Files/
# tar -czf myfiles.tar.tgz Exercise\ Files/
# The a option tells tar to figure out what kind of compression to use based on the file extension. In this case, .gz.
# I could also specify to use gzip compression by using the option z instead of a. I can do the same thing with a bzip
# archive. I'll recall the command and change the output name to .tar.bz2. bzip can offer a little bit more compression
# for some files, but sometimes it takes quite a bit longer to run.

# mkdir unpack1
# mv myfiles.tar.bz  unpack1/
# cd unpack1/
# tar -xf myfiles.tar.bz
#  Now let's unpack them. I'll create a folder and move one of the archives into it. I'll write mkdir unpack1. And then
#  I'll move one of the files into that folder. I'll write mv myfiles.tar.bc2 space unpack1. And then I'll move into
#  that folder with cd space unpack1. Now, to extract this archive, I can write tar -xf myfiles.tar.bz2. And taking a
#  look at this directory with ls -l

# mkdir unpack2
# tar -xf myfiles.tar.bz -C unpack2
# ls unpack2
#     I'll create another folder with the command mkdir unpack2. And then I can tell tar to unarchive into that folder.
# I'll write tar -xf myfiles.tar.gz. And then I'll use the dash capital C option and provide the path to that directory,
# unpack2. The capital C option specifies a directory to change into for unarchiving. As we explore working at the
# command line, be it as a software developer, assistant administrator, or a hobbyist, we're bound to come across
# archive files as we explore new software.

#      While TAR files of various types are pretty common in the Linux world and, to some extent, in the Mac world, too,
#  the ZIP format is very widely used in large part because it's somewhat more cross-platform friendly, meaning that it
#  works well on Linux, Windows, and MacOS, allowing us to easily exchange files between these platforms.
#
# zip ziparchive.zip Exercise\ file           !!!!! create archive with empty directory
# zip -r ziparchive.zip Exercise\ file      !!!!! create archive with all files  from directory
#
# mkdir unpack2            to unzip we create directory
# mv ziparchive.zip unpack2/      move our archive to directory
# cd unpack2/   change directory
# unpack ziparchive.zip       unzip our archive

#
#        We can also tell unzip to extract files to a specific directory. To do that, I'll create another directory with
#  mkdir unpack4. And then I'll use the unzip command to extract that zip file, which is still in the unpack3 directory,
#  and I'll provide the -d option for the unpack destination of unpack4. And there's the files extracted into this
#  directory. While TAR files are a bit more Linux native, it's good to be able to work with both TAR files and ZIP
#  files in order to be flexible.
# unzip unpack2/myArchive.zip -d unpack3     unzip file myArchive.zip from directory unpack2 to directory unpack2 flag d
# stands destination

# **********************         Output redirection         ********************

#      But before we move on, it's important to understand how to get that information into a file that we can use later
#  or send to someone else. In the Bash shell, and other shells as well, there are three general pathways or streams
#  that we use to work with text, and which we can control in order to send information where we want it to go.
#   The first is the Standard Input, or stdin, which is text going into the shell or into a program, and it's usually
# keyboard input into the shell.
#   Next is the Standard Output, or stdout, which is the result of running commands that comes back to our screen when
# commands execute correctly. This is what we've been using so far when we see the output on the screen, or when we send
# it through a pipe to another program.
#   The third stream is Standard Error, which is the result that comes back from commands when they don't execute
# correctly, or when they return an error message to us.

#     Redirection :
#    Stream                     Number             Usage
# Standard input(stdin)           0             Text input
# Standard output(stdout)         1             Text output
# Standard Error(stderr)          2             Error text

# ls 1> filelist.txt   =     ls > filelist.txt   sand output of command ls to new file filelist.txt
# cat filelist.txt   show content of file

#  Redirecting the standard output is very common, so we can use a shorthand for it, getting rid of the one, and just
#  using the greater than symbol. I'll write, ls > filelist2.txt   !!!

# ls notreal 2> texterror.txt    sand text of error from stderr to file

#       We can use more than one redirection at the same time. For example, during a long copy operation, it's common to
#  redirect the standard output to a list of successfully copied files, and the standard error to a list of files that
#  failed to copy. I want to mention that the redirection operator can be a little bit dangerous. If I just type,
#  >filelist4.txt, I don't get anything back in the shell, but once I check out the file, I find that it's empty.
#  We've redirected an empty string into that file, and overwritten what was in the file before. !!!!!

# echo "some appended text" >> filelist5.txt.        We can use two greater than signs to append or stick the data on to
# the end of the existing file.

#  Like pipes, redirection is commonly used in command line scenarios. And while it's not something that we'll use with
#  every command, it does come up now and then.

# ********************         Exploring environment variables and PATH          ***************

#     The shell environment that we're using has a few variables or parameters which control different information and
# options that affect how the shell operates.

# env      show environment parameter

#     path variable is one that causes problems for people sometimes and it's important to know about. We can focus on
# it in particular using the echo command like this.

# echo $PATH          In bash and other shells path is a list of paths or directories in the file system where the shell
# is told to look for programs or executable files outside of the current working directory.

# which ls     show where command ls is located

#       Looking back at the path environment variable here, I can see that this path is represented in this variable. So
#  it's one of the places that the shell looks when we ask to run commands. Sometimes when we install new software, we
#  might want to add the path to that software, to the path variable for our environment, to make it easier to use the
#  software. Installing software with a package manager as we'll see later, generally add software to places that are
#  already in the path. So we don't have to do anything. But if we compile a tool from source or download a program and
#  put it somewhere that isn't represented in the path variable, adding that specific path to the path variable will let
#  us use it more easily. To add something to the path variable, we can edit our shell profile, which is a hidden file
#  in the home directory.

# ~/.bash_profile     edit the shell profile file

#  Files whose name begin with a period character are usually hidden from view when listing a directory.

# ls -a    show all files, normal and hidden files

#  Depending on your setup, your dot bash profile file may already exist or not.
# nano ~/.bash_profile     create file
# PATH = "$PATH:/my_custom/path"
#       I don't have one yet so I'll create one with nano tilde slash dot bash underscore profile. If you don't have a
#  bash profile doing this will create an empty shell profile in your home directory. To customize what's in the path,
#  I'll add a line that says, path equals quote dollar sign path. Which means set path to whatever path is. That by
#  itself doesn't change anything. But it does allow us to use the existing path environment variable, which is set at
#  the system level without replacing it or having to replicate it. To add more directories to my path, I'd add them
#  inside the quotes here after the existing path variable separated by colons. Then I'd save the file and close and
#  reopen my shell. I won't make a change to my path for now though, because that's getting more into shell scripting
#  than into learning how to use a shell in general. I'll close this editor and choose not to save this file. I

# ****************         Find information about your Linux distribution          ********************
#  If we find ourselves in an environment we don't know about, such as a system set up for us by someone else, the first
#  thing we need to do is understand which Linux distribution we're using. One place this information can be found is
#  in files inside the ETC folder. What the files are called specifically can vary based on which Linux distribution
#  you're using. But we can use a wildcard to match the name of these files and see what's inside them.

# ls -l /etc/*release      I have two files here. LSB release and OS release, which is a link to another file in usr/lib
# Let's see what information is in these files. First, I'll type cat etc lsb dash release. Here, I can see that I'm
# running Ubuntu

# cat /etc/*release     to show info about system which we are using

# uname -a      retrieve the system
#    Another important piece of information to know about a system is what version of the Linux kernel we're using. This
# can determine what features are available to us. We can find that information with the uname command and I'll use the
# dash a option to show all information. This shows the type of system, in this case Linux, the host name of the system,
# the version of the kernel, the architecture of the system, and so on. To just retrieve the version of the kernel, we
# can use uname dash r. This kind of information can be very helpful if you're troubleshooting something and need to ask
# for help. And it can inform whether certain software runs and what tools you have available.

# uname -r     retrieve the version of the cornel

# ******************           Find system hardware and disk information         ****************

# free -h       show information about memory in human-readable output

# cat /proc/cpuinfo       show information about central processor

# lscpu      show information about central processor   and some other information

# df -h      Let's find out how much space has taken up and how much space is available on the system's hard drive.
#  This shows the space across a few different volumes, but the most interesting one to me right now is slash or root,
#  because that's where my system files are, and also in this case where my user data is stored.

# sudo du -hd1 /         Let's take a look at how much space is taken up across my whole system. I need to use sudo here
# because my user can't see into all of the folders at the root of the file system. The du command stands for disc usage
# The -h option gives me sizes in human readable formats, and the d option tells du what level of detail to show. In
# this case, I'm giving it the value of one, meaning to show me one level deep, the first level up from the root, adding
# up everything within each of those directories. Without doing that, I get one line for every file and directory the
# tool finds.

# sudo lshw | less          We can also explore what hardware the system has with the lshw command, to list hardware.
# This provides a larger amount of information, so it's helpful to pipe it into less or redirect the output into a file
# to browse more easily. And we can use commands like lspci, and lsusb, to look at what devices are attached to the PCI
# and USB buses, if those commands are installed on our system too.

# ip a         . we may also need to find out about our systems networking information, and to do that, we can use the
# ip command with the argument, a, short for address. This will tell us the address information for each of our network
# adapters.

# ********************       Install and update software with a package manager         *********************

#       Debbian and distros like Ubuntu that are derived from it, use the APT package manager, APT stands for advanced
#  package tool.
#       Depending on the version, Red Hat and CentOS use the Yum package manager or the DNF package manager and Fedora
#  uses DNF.
#       SUSE uses YaST and Arch uses pacman.
# Generally speaking, the tools all work in a similar way. We provide the name of the package tool, and then we can use
# a command or argument to search for a particular package, to get more information about a package or install or remove
# the package. Package management tools also allow us to look for updates to existing packages and install them.

# apt search tree       this will find all of the packages whose name or description matched that term.

# apt show tree       show info about package tree

# sudo apt update        ,update all packages which I have

# sudo apt install tree     install package tree

# tree     to launch package tree

# man tree     to see manual information about package tree

#  On a Linux system, there's only one file system root. Even if we plug in other storage devices, those become part of
#  the overall file system and aren't represented as separate file systems, like we might be used to seeing on a Windows
#  system with a C and D and other drives. You can think of the file system root kind of like the my computer level on
#  a Windows system rather than the C drive. Using a desktop based file browser, we'll see other disks listed as we
#  might expect on other operating systems. Even though they're mounted or made available within the root file system,
#  usually under the mnt directory or inside of a directory called media. From the root, we move deeper into the file
#  system, and at the first level, there are a variety of directories each with a specific purpose. Some of the
#  important directories defined by the FHS include the home directory where each user's personal files are stored, and
#  bin, sbin, and usr where programs have different types are kept. Again, there's also mnt or media, which are used for
#  mounting or attaching other file systems, like you'd find on network shares and other disks. And how those are used
#  will vary based on which distribution you're using. The etc directory is where system wide configuration files are
#  stored. And var is where changeable or variable system information is kept. This is where we'll find system logs and
#  logs for other software. Some directories defined by the Filesystem Hierarchy Standard aren't real directories at
#  all. The dev, proc, and sys directories are created by the kernel to represent hardware available on the system,
#  including all the systems hardware, processes that run programs, settings in the kernel, and so on.

# sudo apt install mysql-server    to install server mysql on Linux, nce the installation is complete, the MySQL server
# should be started automatically. You can quickly check its current status via systemd:

# sudo service mysql status
# The network status of the MySQL service can also be checked by running the ss command at the terminal prompt:
# sudo ss -tap | grep mysql

# If the server is not running correctly, you can type the following command to start it:
#
# sudo service mysql restart

# A good starting point for troubleshooting problems is the systemd journal, which can be accessed at the terminal
# prompt with this command:
#
# sudo journalctl -u mysql

# Database Engines
# Whilst the default configuration of MySQL provided by the Ubuntu packages is perfectly functional and performs well
# there are things you may wish to consider before you proceed.
#
# MySQL is designed to allow data to be stored in different ways. These methods are referred to as either database or
# storage engines. There are two main engines that you’ll be interested in: InnoDB and MyISAM. Storage engines are
# transparent to the end user. MySQL will handle things differently under the surface, but regardless of which storage
# engine is in use, you will interact with the database in the same way.

# service --status-all      show all services runs
# service service_name status    show status of chosen service
# ps        show current   process stat
# ps -xa      show process stat all processes

# netstat     show Active Internet connections
# netstat -tulpen      show opened ports on server

# netstat  утилита командной строки, выводящая на дисплей состояние TCP-соединений (как входящих, так и исходящих),
# таблицы маршрутизации, число сетевых интерфейсов и сетевую статистику по протоколам. Доступна в операционных системах
# семейства UNIX и Windows. Основное назначение утилиты — поиск сетевых проблем и определение производительности сети.

# cURL — (распространяемая по лицензии MIT)[4] кроссплатформенная служебная программа командной строки, позволяющая
# взаимодействовать с множеством различных серверов по множеству различных протоколов с синтаксисом URL. Название
# расшифровывается как "client for URL".
# curl -Li http://localhost:80    returns headers

# ifconfig       to see ip addresses of mac
# sudo service apache2 stop          , stop server apache
# sudo service apache2 start          , start server apache
# sudo service --status-all          to see all running services
#
# whereis <name>       shows path of name

# /usr/sbin/apache2ctl               — bash-скрипт консольного управления сервером Apache

#   example Dockerfile for apache

# FROM ubuntu
# RUN apt-get update
# Run apt-get install apache2 -y
# EXPOSE 80
# CMD ["apache2ctl", "-D", "FOREGROUND"]

# docker run -d --name my-apache -p 80:80 -v /root/docker/files:/var/www/html my_image_apache2

# apt-get clean      , clean cash