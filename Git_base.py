# ************* git configuration **************
# git config user.name 'Shypilov Dmitriy'
# git config --global user.name 'Shypilov Dmitriy'         make email global
# git config user.email shypilovd@gmail.com
# cat .git/config                 show content of folder config
# C:\Program Files\Git\etc\gitconfig or C:\ProgramData\Git\config    уровень --system
# C:\Users\<USERNAME>\.gitconfig уровень --global
# <project>/.git/config уровень --local(default)
# git config --list              show all config settings
# git config --list --global     show global config settings
# cat ~/.gitconfig     show file gitconfig where keeps settings and aliases
# git config --unset user.name                 delete user.name
# git config --remove-section user             delete section
# git config --global core.editor путь к редактору
# git config --global core.editor "'C:/Program Files (x86)/sublime text 3/subl.exe' -w"   example to make editor global
# git config --global alias.c 'config --global'
# git config --global commit.verbose true , set default state commit -v(will show diff between Index and Repository)
# git config alias.sayhi '!echo "hello"; echo "next message"'  or  git config alias.sayhi '!git .....; git ......'
# git config -h                shows keys of config
# git config --global grep.patternType perl    установит по умолчанию перл совместимый поиск для флага --grep
# git help config               'git help command' shows  descriptions and settings of command
# в листалке /что искать      найдет в листалке с этими словами, q выход ,n поиск вперед ;shift n - поиск назад

# **********     git commands     *************
# git init    create git repository in /Users/learn/project/.git/
# git status    check files in working directory, index and repository
# git add file    add untracked files to index
# git add .       add all current catalog with all files to Index
# git add -A     add all files from root directory to Index
# git add -p index.html       we can choose variants of adding to Index file index.html
# git add -f .idea/project.iml(name file)      -f is the same --fource , add file from .gitignore catalog
# git commit      ,commit files from Index to Repository     первая строка заголовок не больше 50 символов
# git commit index.html      commit only index.html  from Index to Repository
# git commit -m 'Add a welcoming script'      commit and add a header to commit
# git commit -a  ,commit all tracked files from Working directory to Repository  -a is analog --all, -am is analog -a -m
# каждый комиит содержит хеш короткий идентификатор, полный идентификатор 40 symbols
# git commit -v   , open the editor, and in it will be description between Index and Repository of HEAD, for
# familiarization of code

# *********************      delete and rename files ***********************************
# git rm -r del_directory_name      delete directory from working directory and Index  !!!! flag -r means directory
# git rm -r --cached del_directory_name       delete directory from Index and leaves in working directory and makes
# directory untracked !!!!!!!!!
# git rm file_name           delete file from working directory and Index
# git rm --cached file_name        delete directory from Index and leaves in working directory and makes file
# untracked !!!!!!!!!
# git rm -f file_name        force delete files without changes
# often after delete files we should commit fact of delete by command !!     git commit -m Cleanup
# git mv old_name  new_name      rename in git is two operations : delete and create new , then add two these files

# **********************   reset, clean   **************************
# git reset 54ac     reset HEAD on commit 54ac
# cat .git/ORIG_HEAD    show previous commit for HEAD
# git reset --hard ORIG_HEAD       reset branch on previous commit
# git reset --hard    remove files from Index , and roll back working directory on current commit, по сути чтото
# поделали, поняли что нам не подходит, и откатили состояние как было
# git reset --soft '@~'   or (54а4)reset on previous commit and keeps files in Index, по сути вернет на предыдущее сос-
# тояние перед  комитом, тоесть состояние когда в предыдущем комите наши файлы находяться в индексе но пока незакомичены
# git commit -c ORIG_HEAD    после мягкого отката при комите возьмет описание с предыдущего состояние хед,
# -с описание можно поправить,  -С описание нельзя поправить
# git commit -C ORIG_HEAD --reset-author    rewrite author during commit
# git commit --amend  its combines two commands git reset --soft '@~' and git commit -c ORIG_HEAD , can be used with
# flags --reset-author   and --no-edit which cancel calling of editor,  -m we can write Header
# git reset --mixed '@~'    average between --soft and --hard , --mixed its default state, so we can drop this flag,
# flag --mixed remove files from Index but leaves they in working directory
# git reset index.html  remove index.html from Index
# git reset HEAD .idea     (or some file)   removes from Index catalog .idea
# git clean -dxf       delete only untracked files and directory from working directory, even from the .gitignore,
# -d means that should be deleted not only files and directories too, x  -  delete also files which are ignoring by
# gitignore ,   f  - to fource this action

# ********************      branch           ***********************
# git branch         shows current branch
# git branch -v      shows current branch with information about current commit on it
# cat .git/refs/heads/master         shows HEAD commit on branch  master
# git branch name_branch         create new branch with name name_branch
# git branch -f master 54a4    carry branch master to commit 54a4 , we can write git branch -f name1_branch name2_branch
# git branch -d fix      удалит ветку если она уже обьеденена с какойто, тоесть ее комиты уже в другой ветке
# git branch -D fix      удалит ветку с ее комитами, в течение месяца можно будет ее заново создать и указать вершину
# удаленной ветки, git branch fix 2c11 , комиты передут с режима недостежимых в  доступный
# git branch fix HEAD@{6}       create branch fix on commit taken from reflog HEAD@{6}  on windows machine 'HEAD@{6}'
# git branch fix HEAD@{'2022-06-11 12:36:08 +0300'}  create branch fix which was deleted on this date
# git checkout name_branch       change current branch  to branch name_branch
# git checkout -b name_branch    create new branch and checkout on it.
# git checkout -B name_branch 54a4      create new branch and checkout on commit 54a4.
# git checkout -f HEAD      !!!!!!!!  returns to current commit without uncommitted changes , Be careful !!!
# git checkout -f index.html      !!!!!!!!  откатит как было только один файл, откатит в рабочую директорию и уберет из
# рабочей директории , аналог команды  git reset --hard, тоже удаляет из индекса и откатывает рабочую директорию
# git checkout -f name_branch      !!!!!!!!  checkout to branch without uncommitted changes , Be careful !!!
# git checkout 54a4     checkout on commit 54a4 and branch became detached HEAD state !!!!!!!!!!!
# git checkout 54a4 index.html    востановит состояние файла на момент комита 54а4 но не переключает ветки
# git checkout -         checkout on before branch
# git stash  сохраняет рабочую директорию в стеш, и возвращает в незакомиченное состояние комит, стеш можно будет приме
# нить в любой ветке и комите
# git stash pop     применяет незаконченые изменения из гит стешь к текущему комиту
# git cherry-pick 54a4     applies changes of commit 54a4 on current branch

# *******************      log,  reflog,    show
# git log     shows structure of repository from HEAD
# git log --oneline     -||- abbreviated information , same git log --pretty=oneline --abbrev-commit
# git log master --oneline   -||- abbreviated information on branch master
# git log --oneline -g     flag -g shows logs from reflog
# git log --pretty     show commits with Header and descriptions, default settings is --pretty=medium
# git log --pretty=oneline    show commits with full identifier
# git log --pretty=format:'%C(yellow)%h %C(dim green)%cd %C(reset)| %s [%an]' --date=short  settings for showing
# logs %h abbrev ident. of commit,%C(colour) приставка дает возможность отображать остаток строки в выбранном цвете
# %cd committer date, | separate symbol, %s Header of commit, %s%d Header with decorator,[%an]   author name,
# git help log  shows all list!!, [%cn]  committer name, %ad  author date, %cr relative date, shows month ,
# flag --date=short  show abbrev date, can be setting like --date=format:'%F %R' , %F  is date, %R is time
# git log --patch    or -p , add to logs, what we have done in commits
# git log database master --graph   draw graph tree for branches database and master
# git log --all --graph         draw graph tree for all branches
# git log feature ^master     shows commit of branch feature without commits of branch master, = git log feature..master
# тоесть покажет комиты с момента отхождения от ветки мастер,  git log ..master сравнит текущую ветку с мастер
# git log feature.. --boundary ,   покажет комиты на ветке feature   и той на которой сейчас HEAD
# --boundary   флаг покажет пограничный комит, тоесть тот коммит в котором ветки разделились
# git log feature...master       покажет симетрическую разность комитов, тоесть те которые есть или в одной или в
# другой ветки, но не общие для двух веток
# git log index.html     show commits where file index.html was changed
# git log -p index.html      show commits where file index.html was changed  with differences
# git log -p --follow index.html      show commits where file index.html was changed  with differences,
# с учетом изменения названия файла
# git help revisions         покажет описание команд для отображения комитов и их вариантов
# git log --grep add     find all commits where word add there is in description on current branch
# git log  --grep add master     find all commits where word add there is in description on branch master
# git log --grep add --grep list ,find all commits where word add or list there are in description on current branch
# git log --grep add --grep list --all-match ,find all commits where word add and  list there are in description
# on current branch
# git log --grep 'say(Hi|Bye)'   поиск комита в котором есть say Bye или say Hi
# git log -F   отключит регулярные выражения
# git log -Gadd  -p    покажет комиты в которых в изменениях присутствует слово add и флаг -p покажет код с изменениями
# git log -G'function SayHi \('  -p    покажет комиты в которых в изменениях присутствует обьявление функции  SayHi и
# флаг -p покажет код с изменениями
# git log -L 3,6: index.html    покажет комиты в которых вносились изменения с 3 по 6 строку в файле
# git log -'/<head>/' , '/</\head>/': index.html    покажет комиты в которых вносились изменения в блок head в файле
# git log --author=Shypilovd     finds commits where author is Shypilovd
# git log --committer=iliakan   finds commits where committer is iliakan
# git show --pretty=fuller    shows full details of current commit
# git log --before '3 month ago'     or  '2017-09-13  08:30:00 +02'  show commits which were created before 3 month ago,
# we also can use flag --after  , which shows commits which were created before 2017-09-13
# git show HEAD     show information about current commit
# git show HEAD~    show information about  commit before HEAD
# git show HEAD~~ --quiet    show information about  commit before HEAD , count of symbol ~ is count commits before
# HEAD commit, flag --quiet shows info about commit without changes
# git show HEAD~~~  = git show @~3    , 54a4~, master~,  @ means HEAD !!!!!!!!!!! on Windows machine  '@~3'
# git show 4b03b:Python_base.py       shows file Python_base.py on commit number 4b03b  git show master:Python_base.py
# git show :/range    show the most late commit with word range'
# git show --quiet    show only describing of current commit without code
# cat .git/logs/HEAD    показывает историю переключаний для вершин, в папке logs хранится вся история переключений
# git reflog   !!! is the same     git reflog HEAD        shows all history of actions for HEAD on all branches
# git reflog master      shows all history of actions for branch master
# git reflog --date=iso      shows reflog with dates
# git reflog --no-decorate    shows reflog without decorators
# git checkout '@{-3}'        вернет на предыдущих 3 переключения

# *******************      diff      ***************
# git diff commit1 commit2    same commit1..commit2, compare two commits  git diff 54as  68e3, git diff master fix
# git diff commit1...commit2  show what exactly change between two commits
# git diff HEAD     show difference between current commit and uncommited  information, between working directory
# and Repository
# git diff ,show difference between current commit and uncommited  information, between working directory and Index
# git diff --cached  or --staged ,show difference between current commit and uncommited  information, between Index
# and Repository
# git diff .     show difference of all directory
# git diff index.html      show difference of file index.html between Index and Repository
# git diff Git_base.py Python_base.py    we can write several files
# git diff master feature Git_base.py Python_base.py    show difference between branch for files
# git diff --name-only master feature       show name of files where there are differences between branches or commits
# git diff master:index.html feature:name.html   compare two files of different branches
# git diff --no-index path1 path2  сравнивает два файла независимо от гит, где они находяться и с какого проекта

# **************           merge         ***********
# git merge master fix        merge by fast-forward (перемотка) current branch master with branch fix
# git branch -f master ORIG_HEAD  вернет ветку мастер на предыдущий комит, сылка ORIG_HEAD запоминает состояние
# предыдущего комита

# **********      author's rights      ***************
# 100644     100 means its file, 644 file isn't executive, 755 is executive
# chmod +x index.html        makes index.html executive in Unix system
# chmod -x index.html        makes index.html not executive in Unix system
# git config core.fileMode false        says to system that file without executive bit,
# so system doesn't  support executive file always in 644
# git update-index --chmod=+x index.html    add file index.html executive bit in Index co file will be 755 after commit

# **********      git useful      ***************
# .gitkeep      file of 0 bytes that putts in empty repository
# .gitignore    make .ignore in root directory and add files which are don't have to be added to git
# !!!!!  gitignore always commit separately of another files
# атомарность - когда каждый коммит добавляет только одно свойство, фичу
# консистентный коммит - тоесть завершенный
# cd path     change directory
# git checkout -- master     -- означает что мастер файл , а не ветка !!!!!!!!!!!!
# git help reflog       shows describe about  command reflog or another command








