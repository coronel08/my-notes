# My Notes
For [mkdocs tutorial](https://towardsdatascience.com/creating-software-documentation-in-under-10-minutes-with-mkdocs-b11f52f0fb10)

For full documentation visit [mkdocs.org](https://www.mkdocs.org).


## Helpful Links
**HTML Templates**
[HTML5up](https://html5up.net/)
[Bootstrap Templates](https://startbootstrap.com/)

**Photos and Videos**
* [Unsplash Photos](https://unsplash.com/)
* [Pexels for Photos and Videos](https://www.pexels.com/search/videos/vacation%20beach%20/)

**Emoji Markdown**
[github](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)


**Other** 
[Server Setup Linux YT](https://www.youtube.com/watch?v=ZsjK4VDopiE) showws ssh setup, create account, ufw, failban


## Commands
* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.


## Table of Contents
* [CSS Notes](css.md)
* [Django](django.md)
* [Docker](docker.md)
* [Javascript](javascript.md)
* [React](react.md)
* [Git](#git)
    * [Branches](#branches)
    * [Reversing Changes in Git](#reversing-changes-in-git)
        * [Advanced Feature, Selecting commits](#advanced-feature,-selecting-commits)
    * [Excercises](#excercises)
        * [4.1 Grabbing Just 1 Commit](#4.1-grabbing-just-1-commit)
        * [4.2 Juggling Commits](#4.2-juggling-commits)
        * [4.3 Juggling Commits #2](#4.3-juggling-commits-2)
        * [5.1 Rebasing over 9000](#5.1-rebasing-over-9000)
* [Linux](#linux)
* [Todo List](#todo-list)

---
## Git
**Resources**

* [Learning Git Interactive](https://learngitbranching.js.org/)
* [Conversational Git Blog](http://blog.anvard.org/conversational-git/)

Git commands
```
git init - To initialize git in folder

git clone [github repo]

git add [.  or folder/ or filename]

git commit -m 'message' - This is to add changes locally

git push and git pull - Push and pull remote repo

*** git pull is the same as running git fetch and git merge
 
git status - Shows what changes have been made

git log or gitk - Shows info

git describe [ref or master or branch] - Use to figure out where you are if using tags or branches
```
<br><br>

### Branches
Using merges and basic branching [Git Documentation](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

Rebasing [guide documentation](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

Rebasing best practices w/ team [Rebasing Blog](https://blog.algolia.com/master-git-rebase/)

```
git checkout -b [branch name] - This is the same as Git Branch [branch name], then Git checkout [branch name] 
git checkout [commit or HEAD^ or tag] - This detaches head

git merge [branch name] - Use merge branch [branch name], run it in master branch
git mergetool    - Tool for resolving merge conflicts

git push --set-upstream origin [branch name]   - THIS sets branch to be uploaded to Github

git branch -v   - View branches and last commit

git branch -d [branch-name] - THIS DELETES A BRANCH

git rebase master - If we are in [working branch name] this puts it on top of master linearly.
git rebase [branch name] - Run in master
git rebase [master] [branch name] - To rebase new branch into master
git rebase –abort    - IF we run into merge problems, this resets to right before

moving upwards one commit, then two ^,^^
moving upwards 3 commits ~3
Example: git checkout HEAD or [branch name]^

git branch -f master [HEAD~2 or tag or commit] - This force moves the master branch to 2 commits ago.
```
<br><br>


### Reversing changes in Git
```
git reset HEAD~1 - This reverts the branch backwards as if the commit never happened. Work for local branch.

git revert [branch name or tag] - This creates a new commit with old info under last commit. Use for remote branch
```


#### Advanced feature, selecting commits
```
git cherry-pick [commit names] - This copies the commits into master
Example: git checkout master   - Change into master branch from working branch
Example: git cherry-pick [commit] - Gets only that commit

git rebase -i HEAD~3 - This opens an interactive cherry picking gui
Example: git rebase -i HEAD~3     - This gives the option to include what commits run on working branch
Example: git branch -f master [tag or commit]   - This forces master branch to a commit 
```
<br><br>


### Excercises
From the [Learning Git Interactive](https://learngitbranching.js.org/)

#### 4.1 Grabbing Just 1 Commit
```
git checkout master;
git cherry-pick C4;
or
git rebase -i master;
git branch -f master c4;
```

#### 4.2 Juggling Commits
```
git rebase -i HEAD^^;
git checkout newImage;
git rebase caption;
git commit --amend
git rebase -i HEAD^^
git checkout caption
git rebase newImage
git branch -f master c3'';
```

#### 4.3 Juggling Commits 2
```
git checkout master
git cherry-pick c2
git commit --amend
git cherry-pick c3
```

#### 5.1 Rebasing over 9000
```
git rebase master bugfix
git rebase bugFix side
git rebase side another
git rebase another master
```
---

# Linux
[Install mergerfs](https://zackreed.me/mergerfs-another-good-option-to-pool-your-snapraid-disks/) and [setup mergerfs and snapraid](https://selfhostedhome.com/combining-different-sized-drives-with-mergerfs-and-snapraid/) and a tutorial on [snapraid only](https://www.addictivetips.com/ubuntu-linux-tips/set-up-snapraid-on-ubuntu-server/)

* Cifs(samba) Vs NFS(preffered) for filesharing mounting
---
## Todo List
* [ ] Javascript
    * [ ] Add promises section to Javascript
    * [ ] Add Javascript handle toggle at bottom of index.html in vid-site1 project
    * [ ] Add Javascript if else using Javascipt Query Selector, Classlist.conatins, and GetElementByClassname in vid-site1 project. 
* [ ] Work on react section
* [ ] Reformat and space Javascript section
* [ ] Reformat and space React Section
* [x] Make a docker page
* [ ] Fill bootstrap page
