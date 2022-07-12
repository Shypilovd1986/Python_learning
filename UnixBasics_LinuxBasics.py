#   Popular Unix Shells
# sh:      Thompson shell(1971)
# sh:      Bourne shell(1977)
# csh:     C shell(1979)
# tcsh:    Tabbed C shell(1979)
# ksh:     Korn shell(1982)
# bash:    Bourne-again shell(1987)
# zsh:     Z shell(1990)
# fish:    Friendly interactive shell(2005)

# echo $SHELL    show where is located  -> /bin/zsh
# echo $0   show current shell
# sh     change to sh shell
# exit   to exit from current shell
# echo $HOME    That's the variable that Unix uses to keep track of each user's home directory.
# echo "Hello world"    output string Hello world
# echo -n "Hello world"    output string Hello world from new line
# echo $PATH       This string is a list of the directories where Unix will go looking for commands and in the order
# that it will go look for them.
# PATH=/some/path/    change path, where we have to look for commands . Be careful !!!!

#     System information commands
# date    show current time
# uptime    show time of working computer before reboot computer
# users     show all users logged to the system
# who       returns name logged users and some information like where opened in console and window, and time when logged
# uname     information about the system that we're logged
# uname -a   machine hardware name, the node name. The OS released, the OS name and the OS version.
# uname -p   the processor name.
# df      information about disc free space
# df -h      in human readable version
# du      which is for disc usage it'll tell us the size of it.
# du ~/my_project      So give it a path, I'm going to say look at the my project directory. And that's what we want it
# to tell us the disc usage for. I'll hit return and it comes up and it gives us a list of not just the my project
# directory, but every directory that's inside of it.
# du -h ~/my_project     in human readable
# du -ha ~/my_project    with all directories
# du -h -d 1 ~/my_project       Let's do -d and then a one. I'm telling it that I want it to calculate it to a depth
# of one.
# du -h -d 0 ~/my_project       If we make it a depth of zero, then it tells us just the size of that directory


#   Command-Line Shortcuts
# ctrl + a    Move cursor to start of line
# ctrl + e    Move cursor to end of line
# Up/Down arrows : Review previous commands
# Left/Right arrows: Move around the current input line

#       Changing directory
# cd ~    change directory to the home directory
# cd -     cd to previous directory

# whoami       show name of user
# who   displays a list of users who are currently logged into the computer.
# w     same who but with statistics

# pwd   show current path

# Wildcard characters
# *     zero oor more characters
# ?     any one characters
# []    any characters in the brackets
# find . -name "[fmk]name.*"    any symbol in []

#                    Creating symbolic linc
# ln -s file_name symlink_name
# references a file path, not a file
# breaks if file is moved or deleted

#                    Copy file
# cp poem.txt  myDoc/      copy file poem.txt to directory myDoc
# cp poem.txt  myDoc/poem2.txt     copy to directory and change name
# cp -R directory1 directory2      cope all content recursively from directory1 to directory2

#                Move and Rename files and directories
# mv options
# -f     force overwriting (default)
# -n     no overwriting
# -i     interactive overwriting, "ask me"

#             make  directories
# mkdir dir1     create directory in current directory
# mkdir -p dir1/dir2  create new dir2 inside new dir1
#
#           commands
# cmd +k  clear screen and scroll back
# groups     to see the groups that a user belongs to. Many of these groups are created automatically by the operating
# system and are necessary for its features to work.
# ls -l    show list of files inside current directories , first column shows permission, second - user, third group
# ls -la    show all files
# q   exit program less
# h   help menu less
# b   move back a page in less
# spacebar or f    navigate to next page in less
# which cat      show where file of command cat is located
# man cat        manual page about cat command


#       Reading files
# cat      concatenate
# more     paginated output
# less     backward scrolling, better memory use less > moore

#       Unix File Names
# Prefer underscores over spaces.
# Escape spaces with\
# Use quotes around names with spaces
# File endings (.csv , .png,  .html,  etc) not required, but helpful

#       Unix Filesystem
# /bin   Commands/programs
# /etc   Configurations
# /home User home directories
# /lib System libraries
# /tmp Temporary files
# /usr Unix system resources
# /var Variable system data files

#        permission
# chown user: group somefile.txt     change group and user for file somefile.txt
# chown user somefile.txt     set the user don't change the group for  file somefile.txt
# chown :group somefile.txt     change group for file  somefile.txt
# chown user directory1     set the user only for directory, not for file inside directory1
# chown -R user directory1      set the user  for directory and for file inside
# Alpha and Octal permission
# rwxrw-r--   =   764
# chmod (u or g or o) = rwx file
# chmod u = rwx , g = rw, o = r  file
# chmod o-r file
# chmod ug+w file
# chmod 644 file

# Sudo stands for substitute user and do
# sudo cat test.txt   show content test,txt as root user
# sudo !!       run previous command with sudo
# cat /etc/sudoers         sudo file where are keeping some information

#             Monitoring process
# ps     is short for process status, it'll return a list of the processes that are your processes, the one that are
# running that belong to you as the logged in user.
# ps -a     for all users which logged
# ps -x      We can also use ps with the -x option to look at all of the processes.
# ps -aux      or just aux     show all process with owner of process
# ps -u      to find processes that belong to a particular user.
#  PID is the process ID. Every process is given an ID number. We can see the percentage of the CPU that it's currently
#  using the percentage of the memory. This is about the virtual memory and the resident memory. We have the time that
#  it started, the amount of processor time that it's used, and the name of the command which tells us the path to the
#  file that's actually running.
# top          And it'll give us a running dashboard of the different processes. So this is updated every couple of
# seconds. It's configurable how many seconds we use for refreshing. You can see that it tells us information at the top
# about the CPU usage, about the amount of memory that it's taking up. And then it gives us those columns where it shows
# us the process ID, the command, the amount of CPU it's using, and all sorts of other information, the memory and so on
# ?     launch help option for top
#
#           Stopping processes
#       Exit:    q, ctrl+q, :q, x, ctrl+x, esc key
#       Force quit:  ctrl + c  Control C is kind of the universal way in Unix, to tell a process that it should stop.
#       Another option that many are tempted to use, is closing a window. And that may do the job but the process may
# keep running.
#       kill that process off. And especially if the process is running in the background, that may be the only option
# we have. We can't gracefully control it 'cause it's in the background, and we can't force quit in out of it, because
# it's not in our terminal window right now.
#       kill 201   or kill -9 201      (201 is PID which was taken from commands top or ps )  -9 go straight for it

#         Using the command history.
# history      it will return a list of past commands in the order that you used them
#    Dot zsh underscore history for me. And you'll see that it's just a list of commands. One per line. When we log out,
# Unix saves our current history to this file. When we log back in, Unix reads this file to restore the history to its
# memory.
# history 20     show last 20 commands
# history 1     show current command
# !34         execute command from history list
# !-5         execute command which was  command ago in history list
# !!          execute previous command
# !du     or other command , run command du with last flags and execution
# !$     run command with previous argument, for ex , first command was nano poem.txt, then I run cat !$, and I will
# read file poem.txt

#       Configure working environment
#     upon login to a Bash Shell:  ~/.bash_profile, ~/bash_login  .  Bash profile is the main one, login is really there
# mostly for legacy purposes and doesn't get used very often.
#     upon starting a new Bash sub-shell:    ~/.bashrc    . This is the file that gets run whenever bash starts up a
# new sub shell. In other words, not a login shell.
#     upon logging out of Bash shell:   ~/.bash_logout    .  it'll run any commands that are in bash_logout.
#     if [ -f ~/.bashrc ]; then source ~/.bashrc
#     fi
# write this code if you want that log writes from both shel to one file
# alias     show all aliases
# nano .bashrc       open file
# alias h='history'    add alias
# source .bashrc       reload file, need for apply changes

#       Setting the PATH variable
# nano .bashrc    open file
# export PATH='$PATH'    create variable, where take the path from existing, or we can write own path , where should
# find any command

#       Customizing the command prompt
# echo PS1    show current command prompt
# PS1 = 'What now? '    change command prompt.
#   Command prompt format code
# Bash    Zsh       Output description
# \u       %n       Username
# \s       %N       Current shell
# \w       %d       current working directory
# \W       %1d      Basename of current working
# \H       %M       Hostname
# \h       %m       Hostname up to first period
# \!       %!       History number of this command
# \d       %W       date in weekly-date format
# \A       %T       time in 24-hour format HH:MM
# \t       %*       time in 24-hour format HH:MM:SS
# \@       %t       time in 12-hour format
# \D{format} %D{format}   Use strftime format {%Y-%m-%d}
# PS1='\u | \w  '      change prompt
#
# nano .bashrc    or we can go to file
# export PS! = 'user is \u , current directory: \w '    create variable
# source .bashrc     reload file to apply changes

# command > file        directing output to file
# echo 'hello ' > banner.txt
# banner -w50 'hello '    make banner width 50
# command >>file     appending to file
# command < file     directing input from a file
# cat < file_first.txt
# sort < people.txt
# sort < people.txt  > sorted.txt
# mail -s "Subject" someone@nowhere.com < msg_file     directing input from file
# mysql -u user -p database < db_backup.sql      directing input from file
# command | command   piping output to input
# cat people.txt | sort |uniq