# ****************************         some   terminology          *******************************

# Package     bundle of software in a file
# Patch       set of changes to modify files
# Pattern     Group of packages or template for a role
# Product     Group of packages that makes up a product
#  Most of what you'll use in day to day operation are packages. Bundles of software that represent a library or tool
#  or something like that. A patch is a set of changes that fixes or patches software. A pattern is a group of packages,
#  kind of like a template that lets you work with multiple packages that are related in some way, like to install a
#  role, like a web server or file server, or capability, like a desktop environment, or a suite of technical writing
#  tools. And a product is the highest level of package organization, referring to the group of packages that make up
#  a given product, like a distro. So, let's get started learning about Zypper.

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxx      Manage Packages with RPM and YUM      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#
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
# sudo yum versionlock packagename     other way to ensure packages aren't updated is to install the versionlock plugin
# for yum and use that to mark packages as locked, so updates from their repositories won't update them.
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


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxx      Manage Packages dpkg and APT      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#

# The packages manager for Debian and distros derived from Debian, like Ubuntu, is called dpkg or Debian package. As a
# user, we can interact with it directly, or we can use another higher level program that gives us a few more features.
# Dpkg by itself manages packages and can install from downloaded package files. Other tools like the apt suite of tools
# and aptitude can search online repositories for packages and download package files and then hand them off to dpkg to
# install or manage. The apt software acts as a front end to the apt-get and apt-cache tools, which can search,
# download, and modify the list of packages installed on the system and can search predefined or user defined
# repositories to find additional software. And there's aptitude, which offers a text mode interface. Using apt-get
# directly is very common and it's how I tend to work with packages on Ubuntu. But I encourage you to check out aptitude
# as well to see how you like it. Be sure to explore the man pages for
#       five manual
# man dpkg
# man apt-get
# man apt-cache
# man apt
# man aptitude
# to find out more.

#   dpkg : works directly with package files
#   apt : advanced package tool : suite of tools for managing packages and dependencies apt-get, apt-cache, etc
#   aptitude : offers a text interface as well as CLI

#  Two primary ways of installing  in order to enable different functionality or to add features we need are downloading
#  a package from a project or maintainer's site, and using the search capacity of the package manager to go look in
#  software repositories.

# ****************     searching for a package       **************************

# apt search <name package>          search  a package or some text that I want to search for if I don't know the
# particular package name.  Apt search searches the whole package description, so if the string nano appears anywhere
# in the text that describes a package,

# apt-cache search  <name package>  to search the repository information cache, I get a bit more of a compact listing
# of the same information, the package name and a brief summary of what it does. But if we scroll up and take a look at
# the output from apt search up here, here's nano, and I can see that it's installed. But if I look at the output from
# apt cache, that nano application doesn't show up, so that's one of the reasons that I prefer using apt search. It
# shows me all of the matches, not just things that aren't installed.

# ****************     downloading from the web       **************************

#  Often, software isn't available in the repository will be offered for download on our website, but you can also
#  browse the repositories for your distro on the web. I'm going to visit packages.ubuntu.com. If you're using debian,
#  you can visit packages.debian.org.

#  search for a little utility called uuid, that we'll install manually later in the chapter, and I'll make sure to
#  choose mydistro, there it is, and I can see that it depends on two different libraries. Libc, which is already
#  included in my installation, and libossp/uuid16, which we'll need to download also if we want to be able to
#  successfully install uuid later on. I'll open that up in a new tab, and we'll download that in a moment. For uuid,
#  I'll click the link for my architecture, which is amd64, and I'll copy the link from one of these repository mirrors.
#  Then I'll go back to my terminal, and I'll download that with wget.

#  apt-get download nano       download package nano but will not install it, can be useful when we want to install
#  on offline machine

# *************************       finding package information      ***********************

# apt show nano           show information about package , package name, the version that's currently available and the
# section of the repository that it's in. In this case, editors. I can also see some information about where the package
# is from and it's maintainers and where to find information about bugs for this package. I can see the installed size
# is 700 kilobytes and then I can see what this package provides.

# dpkg --info uuid_1.6.2-1.5build2_amd64.deb      If we have a local package like we downloaded earlier, we can take a
# look at the information

# dpkg -c uuid_1.6.2-1.5build2_amd64.deb      listing of all of the files this package would install, where they go and
# the ownership and permission information.

# dpkg -S /usr/bin/nmcli     If there's a file already installed in the system and you want to see which package is
# responsible for it .

# *************************       installing package       ***********************

# apt install packagename       Using apt or apt-get the software will go out and find any dependencies that a package
# requires and download them
# and apt-get install packagename

# dpkg -i package       to install a local package file. In addition to the package that's requested. Then it will
# follow the installation scripts in the packages and put everything in place.

# sudo apt update        If you're working on a clean install, or you haven't done anything with packages in a while,
# it's a good idea to run an apt update before installing software to make sure that you have an up to date copy of the
# software lists from their repositories.

# sudo apt install nmap       install package nmap

# dpkg --info uuid_1.6.2-1.5build2_amd64.deb         If you recall, we know that this uuid package has a dependency.
# Show dependent package of uuid

# if there is some problem dependency use
# sudo dpkg -i uuid_1.6.2-1.5build2_amd64.deb  <dependency problem library name>     And now it installs both packages.

# *************************       checking what software is installed      ***********************

# apt list --installed       shows all packages already installed.
# And here's the list, I can see the package name and then after the slash, the repositories where the package is from,
# the installed version

# dpkg -L nano       And if you're curious exactly what a package installed on your system. For example nano

# dpkg -s nano       or       apt list nano     If you're curious about whether a particular package is installed, you
# can find that out too using either apt list and the package name. And then seeing whether it's listed as installed or
# upgradeable, or you can use dpkg -s and the package name, let's use that to find out about the nano editor.

# *************************        exploring aptitude       ***********************

# The Aptitude software, while it's newer than APT and is becoming recommended for use across various distributions, is
# not installed by default on Ubuntu. Let's install it and have a look around.

# sudo apt install aptitude         install aptitude

#  Aptitude includes many of the commands that we've already seen for working with packages, including search, install,
#  and as we'll see in a little bit, remove. So it can replace APT for most purposes if you choose to use it instead.

#  One major difference from APT and T package is that Aptitude offers a different type of interface. It's still text,
#  but you can navigate it with arrow keys and keyboard shortcuts.

#  sudo aptitude      invoke the aptitude
#  Here at the very top we can see some menu items. The next line has reminders about some keyboard shortcuts. C-T up
#  here stands for control T, and that invokes the menu. We'll look through that in a moment. The question mark key
#  brings up a help listing. And "q" quits out of whatever you're doing. If you're at the main screen here, it'll offer
#  to quit out of Aptitude back to the command line. "u" updates information from the repository. And "g" takes you to
#  the preview window where you can see changes that would take place on the next upgrade, and decide whether to apply
#  or skip them. I'll press "q" to go back to the main screen. I'll hit control-T to toggle the menus here, and that
#  puts us in the Actions menu. This menu has reminders of keyboard commands too, which is helpful. We could go to that,
#  install and remove packages screen, or we could update the packages from here too. And there's a couple other options
#  here. Along with an option to play Minesweeper, which is helpful if you're in the middle of working on a server and
#  decide you need just a little more stress in your day. There's an option near the bottom here labeled "Become root",
#  which if you haven't started on Aptitude with sudo, is required to do much other than search for packages and browse
#  around. And then there's "Quit" at the bottom. Pressing the right arrow takes me to undo, which is control-U. And the
#  Package menu here lists some options for when you're navigating the list of packages. Perhaps more importantly here,
#  "+" to install a package and "-" to remove a package. This "Purge" option here has a shortcut key of underscore or
#  shift minus on the US keyboard. The Resolver, the next menu, provides shortcut keys for conflict resolution and
#  dependency reconciliation. If Aptitude detects a conflict in packages you've selected, it'll try to give you some
#  options to resolve that conflict. The Search menu gives us the ability to search within lists when once displayed,
#  and shows us that the shortcut for "Find" is slash. And to search backwards it's backslash. There are some other
#  options as well. To find again with "n" and so on. Options and Views have some areas worth exploring as well. And
#  here's "Help".  I'll press escape to exit these menus.

#   /nmap      Let's search for nmap here and see what it shows.

#  Here's the nmap package, and I see there's some letters in the column to the left. There's actually three columns
#  for letters here, and in the first one for nmap and some of the others, I see a lowercase "i". That means the package
#  on that line is installed. A "p" here would mean that the package is not installed, and a "c" means that it has been
#  installed but was deleted and some configuration files remain on the system. A "v" means that the package is virtual.
#  The second column, which is blank right now, as you can see here, shows what action is going to be taken on the
#  package on this line. If I were to press "minus" here to delete the package, I can see a "d" for delete. I'll undo
#  that with control-U. If I were installing a package with "+", the second column would show the letter "i". And if you
#  see the letter "p" it means the package and its configuration will be removed or purged. I can toggle purge with
#  underscore. If I were to press "+" to try to add this package back, I'd get a capital "B" here in the second column.
#  That indicates that this package is broken, and I see a new interface here at the bottom of the screen. As well as an
#  indication that there's one broken package up here near the top. This interface at the bottom is the resolver, and
#  it's going to suggest some steps for me to un-break this package. I can see here that it suggests one removal, and I
#  can press the "e" key to examine the suggestion it's giving me.

#   Notice here on the third line, I have two tabs. You can move between these tabs with F6 to move left and F7 to go
#   right. You can also click the tabs with a mouse. In fact you can click on any item on the screen, but you still have
#   to press escape to get out of menus. Back here on the resolver, this recommends that I remove the nmap package, as
#   I was doing before. And leaves the recommendation unresolved. That's fine, so I can press the exclamation mark, as
#   it shows down here at the bottom, to apply this recommendation. If there were more than one option to resolve this
#   dependency, I could move between them by pressing period or comma. Now that I've accepted that recommendation, I'm
#   taken back to the packages screen. Moving up and down with the arrow keys, I can see the description of the selected
#   package shows down here at the bottom. To navigate this tray of packages, I can use the carrot or circumflex. The
#   point to character which is shift-6 on the US keyboard, to move to the parent item. Here it's main, and I can
#   collapse or expand it with enter. Okay, I've marked the nmap package for removal, and I can see up here that it'll
#   free up about 20 megabytes of space. So to make this happen I'll press "g". That takes me to the preview window
#   where I can see what's going to be done. Nmap is going to be deleted due to unsatisfied dependencies, which I caused
#   to happen by my actions in the dependency resolver. And Aptitude has determined that these other packages aren't
#   needed anymore, so it'll delete them as well. I'll press "g" again to take these actions, and when it's done I'll
#   press return to go back to Aptitude. Take a moment to look around these various sections, and then when you're done
#   press "q" to quit. And you can select yes with the arrow key or you can press "y".

# *************************        removing a package        ***********************

# we have a few options to remove a package. Overall, there's removing a package, and purging a package.
# Removing a package deletes the software, and purge removes any configuration files related to the software
# If you reinstall the package, chances are it'll work as you configured it. But if you purge the package, custom
# configuration goes away.

# sudo apt remove uuid      or      sudo dpkg -r uuid          ,remove uuid package
# sudo apr autoremove      ,to clean up after ourselves here. This will remove those packages that are no longer needed.
#
# *************************        Upgrading a package        ***********************

# sudo apt update          before you upgrade or install anything if you haven't done so in a while to allow the package
# manager to get the latest information from the repositories. And then, if I write sudo apt upgrade, I can see that
# amongst all of these many, many things that it wants to update, right in the middle here is nano, but I don't want to
# upgrade all of these things right now. I just want Nano to be brought up to date.

# sudo apt install nano       can be use to update to new version just one package

#  Let's take a look at doing a bulk update of all the installed software. What this does is compare the cache of
#  packages available from the repository for your distro with what's installed and figures out what's needed to bring
#  your system up to date. Typically, this updates anything that's available, unless you indicate that you want to keep
#  a particular package from being updated. This is called keeping it back and you can mark a package as kept back with
#  the apt mark tool

# sudo dpkg -r nano       show old version of nano
# sudo dpkg -i nano       show current version of nano

# sudo apt-mark hold nano       to hold it back. I'll use the apt mark tool to indicate that this older version of Nano
# is to be kept back or skipped when everything else updates.

# sudo apt upgrade         Now, if I run sudo apt upgrade, I'll see everything that would be updated, but Nano is no
# longer on the list. As I can see up here at the top, it's been kept back. The process of updating can take a while
# with this many packages.

# sudo apt-mark unhold nano     if we decided we wanted to upgrade Nano after all, we could un-mark it with apt mark.
# and now if I run sudo apt upgrade again, now Nano is fair game to be updated. And there we go.

# *************************            Installing from source            ********************

# sudo apt install build-essential        The tools that are required for this to work here on ubuntu come in a meta
# package called build-essential. You can find out more about that with appshow build-essential, and you can install it.

#  Now I'll go over to a website that has some code that we'll downland. The website is for nmap, and even though nmap
#  is available through the repository, let's build it from source. Here's the link as bzipped tarball, so I'll copy
#  that location, move back to my terminal and download that with wget and then I'll use the tar command -xf and the
#  name of the package to unpack it, and then I'll move into the folder that created.

# head configure      to explore configure (shows its consist)
# ./configure    to run execute file configure

#  if I list the files in the directory again I can see that I have a make file here. That contains the instructions
#  that the make command will follow to build and compile the software. To use it I'll just type make. And again this
#  will take a few minutes. Here at the beginning I can already see what kind of work this is saving me. This software
#  is calling g++ with all of these arguments and files. That would be quite a bit of work to write myself. Now if I
#  take a look at the files in my folder here again. I have nmap and some of the other tools that were compiled. And if
#  I try to run nmap with ./nmap, it runs.

#  pwd     The next step is to actually install the software or copy it somewhere on the file system where we can access
#  it easily. Right now the software is inside this folder in my home folder, which isn't a great place to store a
#  program that I plan to use often. There's a command called install for the make software that copies files into place

# sudo make -n install           if you're a careful kind of person that wants to see what steps installing the software
# would take.The -n option just lists out the install script. So you can take a look at it and see if anything looks
# fishy.  We need sudo to install because it's going to install the software into a privileged location on the desk,
# inside the usr folder. So, now let's run this command for real, with sudo make install, and the software's installed.

# sudo make install
# ls /usr/local/bin/               Now I can see that my software's on the path.
# nmap
#
# *************************            Managing APT repositories            ********************

# cd /etc/apt
# ls -l
# Most of the time we can get along just fine using the repositories provided by the distro but we can modify the list
# of repositories too, if we need to make changes to the versions we're using or if we need to add third-party sources
# for software that isn't part of the main repos. Apt keeps it's list of repositories in two places

# ls sources.list.d
# Apt keeps it's list of repositories in two places In the sources.list file inside /etc/apt/ and in other files inside
# the sources.list.d directory. Sources.list is usually reserved for the distro repositories and other software, or
# users, can put entries in sources.list.d. But you can work in sources.list too, if you like. It all depends on how
# modular you want your configuration to be.
#
# nano /etc/apt/sources.list            Let's take a look at sources.list. Here we see a few entries, starting with deb
# and deb-src. Deb refers to Debian packages and deb-src denotes a source code repository. After that comes the address
# where the repository can be found.

#  We can add other repositories here setting the type, the address, and whatever other information is needed. You can
#  comment out an entry if you don't need it all the time. Once the list of repositories has been edited we'll need to
#  run apt update so the system goes out and gets information from the new repos.

# sudo apt update

#  apt-key list
#  Some repositories are signed with cryptographic keys in order to allow a system to verify the authenticity of the
#  packages. You can manage these keys with apt-key to keep them up to date. And you can view them with apt-key list.
#  While most people won't need to edit the repository settings they are customizable and on distributions using apt
#  and D package the settings are centrally managed.

# After updating a list of repositories, you should run apt update


# xxxxxxxxxxxxxxxxxxx    the Zypper Package Manager    xxxxxxxxxxxxxxxxxxxxxxxxxxx


# -  used at the command line oon SUSE systems
# -  Zypper is a front end for ZYpp
# -  Zypper manages packages and repositories
# -  Zypper uses RPM packages
# -  Uses long or short commands (install or in)

# On systems running SUSE and openSUSE, the package management software we'll use at the command line is called Zypper.
# Zypper gives us an easy way to work with and search software repositories, resolve dependencies, and install, update,
# and remove software. Generally speaking, there are two ways to install and manage packages on a system. We can install
# software manually from package files we download, or we can use the package management software to search repositories
# of packages and download them and install them that way. The packages that Zypper works with are RPM files, so I won't
# spend time here going over those again. The basic operation of Zypper is pretty similar to the other package managers
# we've seen. Commands that Zypper offers come in two types, long and short. For the most part here,

# You can see both sets of commands by typing zypper by itself with the command line. Doing that shows a quick reference
# to commands you can use, and what they do. For example, here's the long version removelock and the short version rl of
# this command which removes a package lock.

# man zypper      More detailed information is provided in the Zypper man page. At man zypper. We'll focus on working
# at the command line and then finish up with a look at managing software with a YaST graphical configuration tool.
# As we work with Zypper, we'll come across terms like package, patch, pattern, and product. And these are different
# levels of working with software. Most of what you'll use in day to day operation are packages.

# ***************        Searching for a package          ***********************
#
# To begin working with packages we need to know what we're looking for. Sometimes we know the package name, or we know
# something about what we plan to install.

# sudo zypper refresh   So the software will be requesting the latest version, instead of an older one.

# zypper search <package name or some key from information about package >      to search package,     to search the
# repositories for information that matches. But before we do this, it's important to make sure we have an updated copy,
# of what's available on the repositories. Brand new packages show up occasionally. So it's useful to make sure we have
# information, about the latest versions that are available.

#   First column here on the left is the status. Which will show whether something is installed, i means install
#   seconds column shows the name of the item.
#   The patch, package, product or pattern. Most of what we'll see when we're working with zypper, is a package, as we
# see here in the right most column. But you may see the others, here and there, as you  work.
#   The third column from the left here, shows a brief description of each item. All of these results match our search
# term
#
# zypper info <name package>     info about package,  Here we can see more detailed information about this item. It
# shows which repository this package comes from, the version, architectures, venture, and other helpful information,
# like the installed size, whether it's installed, and more.

# nslookup example.com     But sometimes we need to use a command or tool, that's part of a larger package. And it can
# be unclear where to find the right package. As an example of this, I like to use the nslookup command. It's really
# useful for showing name servers for domain names.

# cnf <package name >      imagine you're working as an administrator, and you discover you need to use the nslookup
# command. But it's not available on the system you're using. It's easy to say, okay I'll go install that. We can look
# for the nslookup package in the repositories. But that package isn't found. So how do we get it? On SuSE and openSUSE
# there an handler called cnf. Short for, command not found. And it can tell us what package a missing command, might be
# available as part of. I'll write cnf nslookup, and aha, I can see that the nslookup tool, is part of the bind-utils
# package. Now if I go look for bind-utils, there's something I can install. So if you know you need to use a command,
# and it's not available as a package itself, keep cnf in mind to give you a hint,

# zypper search -t pattern.          Here's a list of patterns that are available for the repositories. As I mentioned,
# these are things like roles, such as a gateway server or mail server, and desktop environments are included here too,
# making them a lot easier to install. Just like with packages, we can explore these with zypper info, to find out what
# packages are included.

# zypper install -t pattern mate         where mate is name of the pattern. That's a lot of packages,

# ***********************       Installing a package        ************************************

# sudo zypper install <name package>            to install package,
#       I can see the status column has changed for packages I've installed. The GCC package which I as the user
# requested to be installed is listed with i+, which means that it was installed by user request.
#       Other packages here just have the i, which means they were installed by the resolver as dependencies to a user
# installed packaged.
#       And sometimes you may see V which indicates that a different version than it's listed in the repository metadata
# is installed.

# sudo zypper install --download-only <package name>                  to download file but nt install
#  Once the download finishes, the packages aren't installed, but they're stored over in the /var/cache/zypp packages
#  directory inside subdirectories named by the repository and the architecture respectively. Let's take a look inside
#  those folders.
#  ls -Rlh /var/cache/zypp  Scrolling down here, I can see that the packages that were downloaded by the package manager
#  are spread across a few folders. Some came from the update repository, some came from the OSS repository, and some
#  have no architecture associated with them, so they're in a different folder. These are stored in the cache right now,
#  so if you install from these files, Zypper will delete the dependency RPMs. So don't install from your original copy
#  of the files, copy them to a system and then install from that copy, or install them from a read only file system.

# curl dash 0 https://nmap.org/dist/namp-7.80-1.x86_64.rpm               We can also download RPM packages directly
# through curl or some other method after finding the package somewhere on the internet.
# after downloading we can install by the       sudo zypper install namp-7.80-1.x86_64.rpm     Once we have an RPM file,
# we can install it with Zypper install and the name of the file. For packages to download from a webpage, you may run
# into signing issues. I'm going to ignore the issue here, but if you want to be more cautious, you can import the
# signing key manually. And now we have that package installed without using the repository. Depending on your
# environment, you can choose which method to use to install packages.
#
# ******************           Finding out what's installed             *******************

# zypper search --installed-only               It can be helpful to find out what's installed on the system.
# zypper se -i          it's shortened notation

# zypper search -t product -i       to search what products were installed
# zypper search -t pattern -i       to search what patterns were installed
# zypper search -t package -i       to search what packages were installed
# zypper search -t patch -i       to search what patches were installed

# **********************           Package versions and updates           *****************************

#  In addition to installing software, we can use Zypper to upgrade it or downgrade it as well. Upgrades or updates,
#  come along when there's new features or bug fixes, either for user-facing software or for system software.  And
#  sometimes we need to rollback software to a previous version, if there's a bug or compatibility issues with newer
#  versions.

#  zypper search -s nmap     Let's take a look at all the versions of Nmap that are available in the repository

#  sudo zypper install -f 'nmap=7.70 -lp151.2.5'      to install old version , -f means fource

#  When we're working with specific versions of things, it's useful to tell the system, "No, don't update this, if
#  there's a newer version. "I want this one." That's called adding a lock, and we can lock and unlock packages here
#  from the command line. A lock doesn't prevent people from using the software or anything like that, it just prevents
#  the package manager from doing anything with that package until the lock is removed. Let's lock Nmap and then check
#  for updates.

# sudo zypper al <name package>        add lock to tge package
# sudo zypper ll      to show list of locked
# sudo zypper update     to update all what we have installed except locked
# sudo reboot     ,to reboot system
# sudo zypper remove lock <name package>        or rl     remove lock from the package
# sudo zypper dist-upgrade      Another option we have, is to upgrade to a new distro when it's available.

# !!!!!!    sudo zypper ll^C        using ^C  code will not execute

#  Managing versions of packages and installing updates, especially security updates, is a critical part of system
#  administration.

# *********************             Removing a package              ***********************

# sudo zypper remove <name package>        or rm      This removes the package, but can leave other packages that were
# dependencies of the package still installed. To avoid this, we can use the -u option, which removes those packages
# that won't be needed after removing a given package.

# sudo zypper remove -u <name package>    to remove package with its dependencies

#  sudo zypper packages --unneeded      to show unneeded packages

# *********************          Managing Zypper repositories        *****************************

# zypper repos     or    zypper rl            We can take a look at the repositories that Zypper knows about .
#  This gives us a table showing numbered rows, one for each repo. We can see the alias and the name of the repo,
#  whether it's enabled, whether it uses cryptographic verification, and whether it's included in the list of
#  repositories to refresh when the zypper refresh command is used to update the local copy of repository information.
#  Notice that some of the repositories are disabled. This was a selection that was made during installation. There's a
#  fixed set of repositories the system knows about, but for most people these four are enabled and the others aren't.
#  So if we need them we can enable them, or even add new ones.

#  sudo zypper modifyrepo -e <number from the table of name repo >      To enable a repository
#  sudo zypper modifyrepo -d <number from the table of name repo >      To disable a repository

# lets us export the list of repositories, and import a list as well. This can be useful as a backup before a
# possibly breaking action, or as a quick way to share a list of repositories with another system.

#  zypper repos --export Zypper    <file name>         To export the list, a filename.
#  sudo zypper addrepo <file name>      to import Although  We can also add external repositories using the same addrepo
#  command. There's a list of third-party repositories on the distro site, so let's find one there and add it.

#  sudo zypper addrepo help               let's take a look at what addrepo options mean. . And here, I can see that
#  the -c option checks to see if the URI exists, the -f option adds to the refresh list, and the -p option sets the
#  priority.

# sudo zypper ar -cfp 90 http://ftp.gwdg.de/pub/linux/misc/packman/suse/openSuse_Leap_15.1/ packman      I can see that
# the repository was added, using the nickname packman.
# sud zypper refresh        to download the information from this repository. Because it's new, I have a new key, and I
# can choose whether or not to accept it.

#  Then I can search for a package that I know appears in that repository, but not in the others. I'll write zypper
#  search sweep. Here are packages from that repository, and we can check that by typing zypper info sweep and seeing
#  that it comes from the packman repository. If we're done using a third-party repo, we can remove it fairly easily.

#  Once again, let's take a look at our repositories. The one I just added is number two, so let's remove that one.
#  I'll write zypper removerepo and the number two. Then taking a look at the list again, I can see it's been removed.

# ****************           Managing packages with YaST          *********************
# But I'd like to take a moment to show you how to work with packages in the GUI as well. Using the YaST configuration
# software that SUSE and openSUSE use. I'll click on my menu here, and go to applications and settings. Here's YaST.
# Here in the software section, I see an option for Software Repositories, I'll click that. Here, we can take a look at
# the repositories and edit them as needed. I'll cancel out of here. Here in the Online Update section, we can see if
# there are any patches that need to be installed. And we can browse the other pages of the interface like the patterns
# View, which shows patterns that are installed and what their components are. Over on the search tab, we can search
# for packages both on the system and in their repositories. We can search and look through a list of matches, exploring
# the information for each package. I'll install this one, it sounds fun. I'll click the little box next to the package.
# Clicking it once changes the icon to a plus, which means that it's marked to install. Once the package is installed
# we'll have other options. And we'll see those in a moment. So that's marked to install. I'll accept these changes by
# clicking the accept button. And then I can watch the progress as the software is installed. Okay, that's installed.
# Let's open it up. That's pretty neat. I'll close the software for now. The Software Management area gives me another
# view into these tabs that I can use to manage the software. I'll search again, and here's the package I just
# installed. Notice how when I click the box here, other icons appear. This one with an upward pointing arrow means
# update. And this one with a horizontal line means remove. Let's remove the software that was just installed. To do
# that I'll click accept, and there we go.