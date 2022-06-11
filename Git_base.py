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
# git config alias.sayhi '!echo "hello"; echo "next message"'  or  git config alias.sayhi '!git .....; git ......'
# git config -h                shows keys of config
# git help config               'git help command' shows  descriptions and settings of command
# в листалке /что искать      найдет в листалке с этими словами, q выход ,n поиск вперед ;shift n - поиск назад

# **********     git commands     *************
# git init    create git repository in /Users/learn/project/.git/
# git status    check files in working directory, index and repository
# git add file    add untracked files to index
# git add .       add all current catalog with all files to Index
# git add - A     add all files from root directory to Index
# git add -p index.html       we can choose variants of adding to Index file index.html
# git add -f .idea/project.iml(name file)      -f is the same --fource , add file from .gitignore catalog
# git commit      ,commit files from Index to Repository     первая строка заголовок не больше 50 символов
# git commit index.html      commit only index.html  from Index to Repository
# git commit -m 'Add a welcoming script'      commit and add a header to commit
# git commit -a  ,commit all tracked files from Working directory to Repository  -a is analog --all, -am is analog -a -m
# каждый комиит содержит хеш короткий идентификатор, полный идентификатор 40 symbols
# git show            shows current commit
# git show --pretty=fuller         shows full details of current commit
# git reset HEAD .idea     (or some file)   removes from Index catalog .idea

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

# ********************      branch           ***********************
# git branch         shows current branch
# git branch -v      shows current branch with information about current commit
# cat .git/refs/heads/master         shows HEAD commit on branch  master
# git branch name_branch         create new branch with name name_branch
# git checkout

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








