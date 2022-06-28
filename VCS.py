# can define two strategies :
# - lock-modify-unlock SCCS, Vault
# - Combined - SVN, perforce, TFS
# - copy-modify-merge , CVS, GIT, Mercurial, GNU Bazaar

# ssh-keygen -t rsa -C "shypilovd@gmail.com"     than we need to indicate file where we save ssh key , then we will
# think of password, wi will put it each time, when we are going to pull request to the server

# git clone <ssh key>       !!!!    shift + insert       insert code from RAM(random access memory)

# git gui&     call gui
# gitk&        show all history
# git ls-tree bf96    show all files in this commit
# sha1 -> hash of commit
# git checkout -- file.name      remove file from working tree
# git checkout .   remove all files from working tree
# git clean -xdf    remove all untracked files from repository
# git reset -- file.name  remove file from Index to working tree
# git reset HEAD^^ (HEAD~2)     reset to 2 commits back to working directory
# git commit --amend -m 'commit message'     is equal of reset --soft with saving changes in Index

#   after revert we need press Esc and type wq in the command prompt, we also can type q! which means don't doo
# any changes

# .gitignore
# *.log  add all files to .gitignore with extension log
# /build add all files from slash
# doc/**/*.pdf   ignoring all files with extension pdf at doc directory

# git merge --abort     cancel merge after conflict was arisen
# branch in git occupies 41 bytes
# git branch --all   show all branch wist remote

# git tag version1    we set tag on current commit and gave it a name as version1
# git tag --list show all tags
# git push --tags     push tags to the remote repository
# git checkout version1 checkout Head to commit with tag version1

# git stash save "description"    save stash as description
# git stash list   show all stashes
# git stash pop    remove from stash
# git stash apply     leave in stash
# git stash drop      clear stash


# git push           ,push data to the remote server
# git fetch
# git remote -v      shows which server we work with
# git remote show <name>
# git remote remove origin   remove server from git   !!!!
# git remote add origin <path to server > than we should do next command
# git push --set-upstream origin master

# ctrl + insert  copy from git bash
# shift + insert    ,insert to git bash

#                   branching strategies
#   Centralized strategy       small count of developers, everybody can commit, one branch
#   Feature-branch  flow      make branches of different features
#   Gitflow    when we work with specific task
#   Integration manager workflow    -   there is one blessed repository where only one manager can push data, all
# developers send all their commit to one manager, and all developers can fetch from the blessed repository
#   Dictators and Lieutenants workflow   - like previous strategy , developers send their commits to lieutenant, they
# send to dictator, he pushes  to server, everybody can fetch from the server
#   Working workflow     when we work of open source product, we send to origin developer, he commits

# git bisect
# git submodule
# git last
