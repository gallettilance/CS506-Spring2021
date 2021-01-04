# Workflow 2:  Submitting a Pull Request

## Step 1: Fork this repo (on GitHub)

https://github.com/gallettilance/CS506-Spring2021

## Step 2: Clone your fork

Navigate to your fork on GitHub of the above repo and clone it locally. 

```bash
git clone https://github.com/<username>/CS506-Spring2021.git
```

## Step 3: `cd` into the repo

```bash
cd CS506-Spring2021
```

## Step 4: look at remotes

```bash
git remote -v
origin	https://github.com/<username>/CS506-Spring2021.git (fetch)
origin	https://github.com/<username>/CS506-Spring2021.git (push)
```

## Step 5: add an 'upstream' remote

It should point to the repository you forked

```bash
git remote add upstream https://github.com/gallettilance/CS506-Spring2021.git
```

## Step 6: look at remotes

```bash
git remote -v
origin	 https://github.com/<username>/CS506-Spring2021.git (fetch)
origin	 https://github.com/<username>/CS506-Spring2021.git (push)
upstream https://github.com/gallettilance/CS506-Spring2021.git (fetch)
upstream https://github.com/gallettilance/CS506-Spring2021.git (push)
```

## Step 7: list branches

```git
git branch
* master
```
 
## Step 8: create a working branch

`git branch practice`

## Step 9: list branches

```bash
git branch
* master
  practice
```

## Step 10: switch to working branch

`git checkout practice`

## Step 11: create a file

Create a file called `<github-username>.txt` with your name.

## Step 12: add/stage this file

`git add <github-username>.txt`

## Step 13: commit your changes

`git commit -m 'adding my txt file`
 
## Step 14: push changes to your 'working branch'

`git push origin practice`

## Step 15: submit pull request (on GitHub)

Select green button "Compare and pull request"  
<img src="../images/pull_request_button.png" align="left" height="40" width="180" >   <br> <br>

If you do not see this button, navigate to https://github.com/gallettilance/CS506-Spring2021/pulls, click on "New Pull Request", and select your username and repository in the from section.

## Step 16: actually...

Move your `<github-username>.txt` to the `00-git/` folder

## Step 17: add this change

`git add .`

## Step 18: amend your commit

`git commit --amend`

Feel free to edit your commit message in the pop up editor before closing the file.

## Step 19: force push these to your branch

`git push origin practice -f`

Notice these updates to your PR.
