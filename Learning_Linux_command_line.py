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

#