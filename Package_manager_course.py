# . The software that we use is generally more complex than a few lines of text, so it's delivered in two primary ways:
# as source code files, or as pre-compiled binary files.

# packages can contain source code, pre-built binaries, scripts, and metadata to tell a package management system how
# to deal with what's in the package. These scripts and metadata answer questions like, does the software need to be
# moved to a particular folder? Does it need to be compiled? Does it have any dependencies or requirements that need
# to be fulfilled by having other software available before it will run correctly? What needs to be done before or
# after compiling or copying the files to wherever they need to be? All of this information is bundled up in a package.
# Some software works all on its own, but most of the time, packages that we install will need some other components to
# make them work. These are called dependencies, because a package depends on these other packages. Commonly, packages
# will depend on a particular programming language, or tool chain, or shared library

#  The name for the process of figuring out what dependencies a package has, and whether they're available or need to
#  be installed, is dependency resolution. It's a process that can be done manually, but package management software
#  handles it for us, which is nice. There can still be problems, however, if it happens that a combination of packages
#  ends up with a circular reference, or if a required dependency conflicts with something that another package
#  requires. The software can usually figure out what's needed, but sometimes, manual intervention is required. The
#  software we use to work with packages is called package management software. Some tools can work with packages as
#  individual files that have been downloaded, and other software can go out and search repositories, or repos, for
#  software, automatically download the required packages, and then work with those files as needed. Repositories are
#  huge lists of packages that are available for download and installation

# I'll request to install it. The software will check and see if it's already installed, and if not, it'll go look
# through the list of software on the known repositories, and search for packages matching the name I've specified.
# It'll read the package information to see if there are any dependencies that it needs to download. Then, it'll
# download all of the required packages. After that, the software will either install the package, or figure out what
# needs to be installed first. During the installation, some scripts may run, some code may be compiled, and files are
# copied into locations on your computer, specified by the package creator. Then, some cleanup scripts may run. And
# you're finished. The software is installed, and ready to use.

# You can find out what the architecture of your installation is with the uname -m command. And finally, at the end
# of the file name is an extension, which for Red Hat packages is .rpm, and for Debian packages is .deb.

# On RedHat, CentOS, and Fedora, the RMP package manager, or RedHat package manager is the software that builds,
# installs, updates, and otherwise manages individual software packages on a system. These packages contain either
# pre-compiled binary files, or source code to build binaries, and metadata that describes how RPM should treat the
# files, where they should be installed in the system, how they should be compiled, and so on. We can either use RPM
# directly, if we have a .rpm file to install, or we can use yum to search respositories and interact with RPM on our
# behalf. Yum stands for Yellowdog Updater, Modified. The name Yellowdog comes from a distribution of Linux that was
# focused on IBM's power line of processors. And, incidentally, was also one of the popular versions of Linux to run
# on old, non-intel Macs in the early and mid 2000s. Yum is a re-implementation of an earlier package manager, called
# yup, or Yellowdog Updater, which was done at Duke University. Yum, sitting on top of RPM, is the default package
# management interface on RedHat Enterprise Linux, CentOS, and older versions of Fedora.

#  We can use tools yum provides to search for software and install it right from the command line. RPM keeps track of
#  software that's installed and removed in the RPM DB, and when you run certain yum commands, the yum software updates
#  a local copy of the repo data, so you can find out information about packages when you're offline. I encourage you
#  to make use of the man pages for both yum and RPM, with man yum and man RPM, respectively

#  ************************          search  by word          *******************************

#  Yum search <search-term>          The most obvious command, search, can be used to look through the names and
# descriptions of packages included in the repositories which yum knows about. These default repositories should be
# enough for us to get started and we'll take a look at adding others later on

#  Yum search tree              .Tree displays the file system a little diagram instead of a just a list of files,
#  so to search for the package here at the command line

#  Yum search all tree    You can also search the longer descriptions of packages with the search all keyword like this.

#  Yum -v search all tree    If you want to see the text that's being searched when using the all keyword you can pass
#  yum the -v flag for verbose, like this. Yum -v search all tree. But it doesn't highlight the matches there either.
#  So use that if you need it but I wouldn't recommend searching that way all the time.

#  yum provides <nmcli>     The provides command also shows you which repositories provide a given file nmcli

# ***************************      download package on computer     ********************
#       wget  <url of package>       to download package on your computer
# The provides command also shows you which repositories provide a given file

#       Control + Shift + V and Enter.   Paste into terminal on Mac

#       sudo yum install --downloadonly uuid       . I can also tell Yum to download a file for me, using the install
# command with a download only option.  But the download only option tells the install command, hey, just go look
# for and download the file, but stop there, and don't do anything else. There's a little package called UUID
# that we'll download this way.

# ******************            finding package information            ********************
# ls -lh    shows files in home folder

# cp <path>           copy file to our home folder

# clear    to clear screen

# locate uuid       shows where uuid was deployed .  Uuid generates universally unique identifiers, which can come in
# handy for a lot of things.

# sudo updatedb     update database (update location of files)

# yum info tree     to get info about package tree

# rpm -qlp uuid-1.6.2-26.el7.x86_64.rpm      If you have a file downloaded locally, you can take a look inside and see
# what files and scripts are included. We'll use rpm for this, with a dash q flag for query. Let's take a look inside
# what's in that small package we downloaded earlier, called UUID. To do that, I'll write rpm, dash q for query, l to
# list the files, and p to specify that I'm using a package file, then uuid and tab to auto-complete, and I get a list
# of files here.
#
# rpm -qlpv uuid-1.6.2-26.el7.x86_64.rpm     We can see a little more information by adding the v flag for verbose
# rpm -qlpv uuid-1.6.2-26.el7.x86_64.rpm --scripts      If we want to find out some more information about the scripts
# this package invokes, we can use the dash dash scripts option, I'll recall this previous command and add --scripts
# to the end.
#
# rpm -ql sed --scripts     (sed is name of package) We can also find out information like this about packages that are
# already installed. This works the same as checking out a package file but we just leave off the p option. So I'll
# write rpm -ql for query and list, sed, which I know is installed. These are the files that were installed when sed
# was installed. We can check out its install script too. I'll write , and up at the top here, we can see what was run
# after the software was installed, and what will be run if it's ever uninstalled.

# rpm -qf usr/bin/sed     how you can figure out which package a particular file came from, that also uses the query
# flag, but we use f and then the path to a file. For example, again with sed, and we can see it's from the sed package,
# which makes sense.

# *************************        explore checking dependencies          **********************
# yum deplist nano       can use the deplist command to see what a package's dependencies are. For example
# nano here depends on sh.  It depends on the C library, which I can get from glibc. And some other shared objects that
# it gets from ncurses-libs.

# yum list bash      And you can check to see if a package is installed already with the yum list command, followed by
# a package name. Let's take a look at bash

# rpm -qpR uuid-1.6.2-26.el7.x86_64.rpm   You can take a look at the dependencies for a package we've downloaded as well
# with rpm -q for query, p for package, and a capital R to query what the package requires. And then the name of
# the package

# rpm -qpRv uuid-1.6.2-26.el7.x86_64.rpm        And if we rerun this, with the v flag for verbose, we can see what
# requires these things. The post install and pre-uninstall steps use the ldconfig program to do some work with those
# installation stages.

# ****************************           installing package    ***************************
# sudo yum install tree       I'll install the software tree. Here I can see a listing of the repositories that yum's
# currently using.    I have a prompt here asking if this is all ok. If I press y, then yum will download the package
# and install it. If I press d, it'll just download the package but not install it. We saw that earlier with the
# download only option at the command line, and if I type N for no, which I can tell is the default because it's
# capitalized, nothing will be installed, but this session or transaction will be saved, and I can revisit it later if
# I want to

# sudo yum localinstall <package name>   If we have a package file downloaded already, we can install it with either yum
# and the local install command or with the rpm tool and the -i flag. Let's install one of the packages I have
# downloaded here. First with yum localinstall, I'll install the uuid package. I'll write sudo yum localinstall and
# the package name.

# sudo rpm -i  <package name>     same as  sudo yum localinstall <package name>

# ******************            checking what software is installed           **********************
# yum list nano    I can specify a particular package and run that to see if the package is installed.

# yum list installed      to see what installed

#  These are listed in the main page for the yum.com configuration file and you can find them if you search for color
#  dash underscore dash list. First you can see there's a difference between normal text in a package name and a
#  bolder variation.
#       The normal text, like I can see on jasper libs, jbigkit libs, and json-c here, means that the installed version
#       The bold variation, like these kbd ones, are an older version than what's available from the repositories, so
# these would be updated if I do a full update through the package manager.
#       This bold and underlined white one here, the kernel, means that it's a kernel package that matches the currently
#  running version of the kernel.
#       The yellow bold variation here on the nmap package means that the version of the package installed is newer than
# what's available from the repository.
#        The @ sign on other lines here shows that the other packages were installed through a repositories for a file
# name after the @ sign, that it was installed from a package with yum local install but installing with rpm, we just
# get installed over here on the right.
#        The other coloring that showed up for me in my installed package list, is this red one here, which means that
# there's no matching package in the repository. If I were to update that package specifically, I'd find that it's been
# replaced with python2-pyasn1 which is why the name doesn't match.
#        Blue bold text means there's an upgrade for the installed package available.
#        There's two other colors to be aware of which you'll usually only see if, instead of using yum list installed
# to see packages installed on your system, you use the yum list or yum list all commands which show everything
# available in the repositories. The first is packages colored cyan, which means there's a downgrade available for the
# installed package. And if you supply the --showduplicates argument, you'll see green with an underline which means
# that the repo version matches the installed version.

# *************************            group action           *********************
#  To work with groups we have the grouplist, groupinfo, groupinstall and groupremove commands.
#  yum grouplist      take a look at what groups are available with .
#  Environment groups are broad configurations for a system. You can think of them as roles that the server is prepared
#  to be able to fulfill. And the regular groups are tool chains or sets of software for particular tasks.

#   yum groupinfo "Basic Web Server"       you might have a system configured as a file and print server or as a basic
# web server. But also have development tools and legacy UNIX compatibility tools installed. To explore what's inside
# a group, you can use the yum groupinfo command and then the name of the group in double quotes. I can see there's an
# environment ID, which is another way of addressing the group at the command line and a brief description of what the
# group provides. Below that there's three categories of groups you might see. Mandatory, default and optional. Groups
# in the mandatory list and default list will be installed when you invoke the groupinstall command. And those on the
# optional list are skipped unless you specify to install them, either by name or with a command line argument or in the
# yum.command file if you want to change system wide behavior.

# yum groupinfo web-server      We can use the groupinfo command again to explore each of the groups listed here.
# Base here is the base installation of my distro. And core represents packages that make up the smallest possible
# installation of sent offs.Those are pretty much required for any system to work. And the web-server group is what
# we're really interested in.

# sudo yum groupinstall "Basic Web Server"       it's going to install those mandatory and default packages from the
# web server group. I'll cancel that for now. Earlier I mentioned that the optional groups won't all get installed by
# default when I ask to install the whole group.

# sudo yum --setopt=group_package_types=optional groupinstall "Basic Web Server"          If you did want to install
# all the optional packages you can use a command line flag to change how yum behaves.  Note that some groups, like
# console internet tools and scientific support are entirely composed of optional packages. So you'll need to use this
# option if you want to install them all together. Or just pick and choose ale carte. Using the command line flag makes
# the change for one invocation of yum.

# cat  /etc/yum.con file          You can add group package of types equals optional default or mandatory as a line
#  +  means that the package is not installed but can be.
#  = means that the package has been installed using the group install method.
#  An empty space means that the package is already installed, but it wasn't installed using the group install method.
#  -  dash or a minus sign means the package isn't installed and won't be installed.
# sudo yum groupinstall "Basic Web Server"  php         I do want to continue. And now after that finishes, I can check
# out the yum groupinfo command for "Basic Web Server" and I can see I have base, core, and web server installed and
# php down here is also installed.

# **********************          removing  package         *************************
# sudo yum remove nano        If you don't need a given package anymore, you can use yum or rpm to remove it. in this
# case you need to prove deletion by press Y
# sudo rpm -e nano     delete package without Y
# sudo yum groupremove "Basic Web Server"    and confirm Y. And now if I run yum grouplist, I can see that that group's
# not installed, it's only available.

# *********************           update           ***************************
# yum check-update      You can see what updates are available for your system , and if you want to upgrade all of the
# installed packages to whatever the most current version provided in the repo .
# sudo yum update     ,update all installed packages
# if you're using a remote connection, it's a good idea to run that in a screen or tmux session in case you get
# disconnected.
# sudo yum update nano    install package nano
# yum update -x packagename       exclude package from upgrade
# sudo yum install yum-plugin-versionlock       install versionlock plugin
# sudo yum versionlock packagename     other way to ensure packages aren't updated is to install the versionlock plugin for
# yum and use that to mark packages as locked, so updates from their repositories won't update them.
# sudo yum versionlock    to see what are in versionlock
# sudo yum versionlock delete 0:nano*      delete nano from versionlock
# sudo yum versionlock clear       delete all from versionlock
#
# *******************         installing from source      ***********************
#    There are a few ways of going from source code to a running binary. And while many times you'll build and compile
#  a program in an IDE, you can also download the source for software and build it with the standard tool chain at
#  the command prompt.
#    There are a few ways of going from source code to a running binary. And while many times you'll build and compile
#  a program in an IDE, you can also download the source for software and build it with the standard tool chain at
#  the command prompt.
#    tar -xf somepackage.tar.bz2        unpacking a file with the tar command,
#    cd somepackage moving into the folder created by that,
#   ./configure
#   make                          .
#   make install
#
#  yum groupinfo "Development Tools"

#  sudo yum groupinstall "Development Tools"
#   I'll go over to a website that has some source code we'll download. The software is Nmap. And even though that's
#   available through the repository, let's build it from source. Here's the link as a bzipped tarball. I'll copy the
#   link, switch to my terminal, and download it with wget.

#   wget https://nmap.org/dist//nmap-7.40.tar.bz2

#   tar -xf nmap-7.40/      to extract the archive with the name of the archive here.

#   cd nmap-7.40             That'll create a folder for me called nmap with the version number.

#  ./configure         This configure script is executable. And when we run it, it'll start looking around my
#  environment for particular tools that were installed in the Development Tools group, including the C compiler. And
#  it'll generate the make file, which we'll use in step two in order to compile the software. So, to kick off the
#  configure script, which will take a few minutes to run,
#
#  make    ,if I list the files in the directory again    by command ls , I can see I have a Makefile here. That
#  contains the instructions that the make command will follow to build and compile the software. To use it, I'll just
#  type make.  And again, this will take a few minutes. Here at the beginning, I can already see what kind of work this
#  is saving me. The software is calling G++ with all of these arguments and files.

#  ./nmap      if I take a look at the files in my home folder here again, I have nmap and some other files as well.
#  And if I run nmap with dot slash nmap, it runs just like I expect.

#  The next step is to actually install the software or copy it to somewhere on the file system where we can access it
#  easily.  There's a command called install for the make software that copies the files into place. So far we've been
#  working inside this folder and not affecting the file system outside of it. So, if you're a careful person that
#  wants to see what steps installing the software would take, you can write sudo make dash n install. The dash n option
#  just lists out the install script. So you can take a look at it and see if anything seems fishy.
# sudo make -n install

#  ls /usr/local/bin     If I list the USR local bin folder, I can see the software in there.

# which nmap    to see the path

# nmap    to see it directly

# ********************          Managing yum repositories    **********************
# yum repolist      And we can see all of the active repositories listed on the system,

# yum repolist all        we can see all of the repositories with the  disabled ones .

#  cd /etc/yum.repos.d           We can manage the repositories by working with files in the etc yum.repos.d directory.
#  Each file represents a repository or list of repositories.

# less CentOS-Base.repo       list of repo, . I'll move to the bottom of the file. Notice that this says enabled equals
# zero, that means it's disabled.

# If you need to add a new active repository, you'll need to create a .repo file here and add the appropriate
# information. Then when you run YUM update or search for a package, your system will use that repository as well.

