## Git Configurations

#Git configurations are settings that allow you to customize how Git works. They consist of variables and their values, and they are stored in a couple of different files. To work with Git, you must set a few configuration variables related to user settings.

```
git version
git config --global --list
git config --global user.name "shubhamchau222"
git config --global user.email "shubhamchau78@gmail.com"
git config --global init.defaultBranch main
git config --global --list

```

## Working with Local Repo

```
git init
git status
git add file1.py
git status
git commit -m "myfirst commit"
git status
git log

```

## Working with Branches
```
git branch
git branch dev
git log
git branch

#delete local branch
git branch -d <branch-name>

# delete the remote branch 
git push origin -d <branch-name>
```

## Switching the Branches

```
git switch dev
git checkout dev
# updated the source code
git add . 
git commit -m "v3"
git log
git checkout main
```

## Fast Forward merging
```
#create v4 in dev & commit to the repo
git switch main
git merge dev
```

## Git Checkouts & debugging

```
git checkout <commit-hash>
git checkout -b feature
git switch -c featurev2
```

## Remote Git Repositories

```
#create remote repo
git remote add origin <url>
git remote
git remote -v
git push origin main
git branch --all
```

## Cloning and Delete Branches
```
git clone <url> <dir-name>
git clone https://github.com/manifoldailearning/git4mlops.git my-folder
cd my-folder
git branch --all
git checkout -b unit-test
git push -u origin unit-test
git checkout main
git branch -d <branch-name> #delete local branch
git branch -d unit-test
git push origin -d unit-test
git branch --all
```

#Advance
# see the file changes in main but not in dev branch
```
git diff --name-only dev..main
git add resolved-file
git pull origin main
```

## Debugging
to got the previous commit
# You are in 'detached HEAD' state.
# if you're switching from V5 to V4
# and write $git log
# It'll show log till v4 only, and you'll fill like you have lost some v5 containts
# to see all the logs: write $git log --all
# but your head will be at V4 only

```
git log
git checkout <commit-hashcode>
```
## better practice while debuging
```
## latest commit version : v5
#0) check the log : $git log
$git log
#1) go to the commit where you want to debuge (inthis scenario v4)
$ git checkout <v4commit-hashcode>

#2: create new branch (v4 code will be copy to new branch)
$ git checkout feature_4

#3) move to the v4 hashcode again
$ git checkout <v4commit-hashcode>

#4) move to the recent changes(v5)
$ git checkout <v5commit-hashcode>

```



# to move at the recent changes:
# git checkout <commit-hashcode-latest-change>
























## Debuging Process
