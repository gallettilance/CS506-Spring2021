
# Understanding Rebase and Revert


## Step 1: Create a new repository or use the one created in exercise 1

In order to get more familiar with git, we want you to initialize a new repository.
Go to GitHub and click the + beside your username. Then click "new repository".
Go ahead and name the repository and click the button to initialize it with a
README. Now select the "clone or download button". This will give you a url.
Now use the command line to navigate to where you want to initialize this
repository and run
```bash
git clone <url>
```
You now have a folder which contains only the README file. Go ahead and add a
new Python file, you can name it whatever you'd like.

## Step 2: Work on a new branch

Run the command
```bash
git checkout -b new-feature
```
to create a branch called new-feature and switch to it. Now that you are on the
new-feature branch, go ahead and add a hello world function to the Python file.
Now commit these changes by running
```bash
git add .
git commit -m "added a Hello World function"
git push origin new-feature
```

## Step 3: Update the master branch

Go to the repository on GitHub. While still on the master branch, make some
change to the README file. This is essentially a simulation of the master branch
being updated by a teammate while you were working on the new-feature branch.
Now from the command line, run
```bash
git checkout master
git pull origin master
git checkout new-feature
```
These commands updated your master branch with the change you made on GitHub
and then moved you back to the new-feature branch.
You could alternatively run
```bash
git fetch origin
git rebase origin/master
```


## Step 4: Rebase

Here is the problem: the code in the master branch has been updated since you
started working on the new-feature branch. This means that the code you are
writing is built on top of an out of date repository. There are different ways
to fix this but the one we are going to look at now is called rebase. In the
command line, run
```bash
git log
```
Notice how many commits you see. Now run
```bash
git rebase origin/master
```
This has made it so that the changes you made in the new-feature branch, effectively
were built on the up-to-date code in master. You can verify this by again running
```bash
git log
```
You should see that there is now one more commit listed. This is because the
commit which changed the README file is now included in the history of the
new-feature branch.


## Step 5: Reverting

Now let's practice undoing some mistakes. Suppose you decided that you no longer
want the change you made to the README file. Checkout the master branch and run the command
```bash
git log
```
You should see something like
```bash
commit 57a0af036f...
Author: <your name>
Date: <today's date>
Updated README.md
```

Go ahead and copy the long string after "commit". Now on the command line, run
```bash
git revert <long string you copied>
```
This should result in a text editor being opened. Go ahead and look over this
file, it's just explaining the changes that are about to happen. Close the file.
Now, if you run
```bash
git log
```
you should see a new commit which says you reverted the update README.md commit.
Go ahead and open README.md. You should see that whatever changes you made are gone.

## Step 6: Interactive Rebase

Now checkout your new-feature branch. In your python file, add a function which
takes two inputs x and y and returns x + y. Now run
```bash
git add .
git commit -m "Add function"
```
Then edit the python file to inlude a function which takes x and y and returns
x - y. Then run
```bash
git add .
git commit -m "Subtract function"
```
Now suppose you wanted to change some things about these commits. On the command
line, run
```bash
git rebase origin/master -i
```
This command should open your text editor. At the very top, you should see some
lines which begin with the word "pick". These are the commits you have made. Go
ahead and explore the various options given to you by replacing the word "pick"
with some of the options given below. Specifically, we want you to try:
"reword" which allows you to change the commit message.

"edit" which will pause the rebase when that commit is reached and allow you to
edit the files.

"squash" which will allow you to combine the add and subtract function into a
single commit.

Finally, we also want you to try adding the final two commits out of order. To
do this, simply place the first line beginning with "pick" below the second line.

Go ahead and try out these commands one at a time to see what they do. Once you
have edited the file, simply save it and then close it. You may need to use the commands
```bash
git rebase --continue
git rebase --abort
```
Once you have tried one of these options, go ahead and use the revert command to
undo what you just did and try the next command.

## Step 7: Finishing up

When you have completed all of the above, create a pull request on the repository
where your fork of this exercise is (you should have cloned it for exercise 1 and
2). This pull request should include the line "finished exercise 3" to the end of
the .txt file you pushed in the earlier exercises. This will let us know that
you have completed all of the exercises.
