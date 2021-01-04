# Workflow 0.2: SSH Setup (optional)

### Purpose

With SSH authentication you don't need to enter your credentials (GitHub username and password each time you push a commit to the remote).  You can skip this step for now and complete it later after the course.  

#### This is your checklist

- [ ] Set up `ssh` keys
- [ ] Add `ssh` key to GitHub
- [ ] Configure user
- [ ] Set up working directory

## Generating `ssh` keys

### Mac & Linux Users

#### Step 1:  We begin by going to our home directory (in terminal)

```bash
cd ~
pwd
/Users/gallettilance
```

#### Step 2:  Go to `.ssh` directory

```bash
pwd
/Users/gallettilance
cd .ssh
pwd
/Users/gallettilance/.ssh 
```

**Note:**  If you do not have the `.ssh` directory, you can create it

- if you are in your home directory:
	- <kbd> mkdir .ssh </kbd>  
- if you are not in your home directory:
	- <kbd> mkdir ~/.ssh </kbd>  


#### Step 3: Generate `id_rsa` keypair files if needed

- **Note:**  these `id_rsa` files contain a special password for your computer to be connect to network services (Ex:  GitHub, AWS).
- Check to see if these files exist by typing <kbd> ls -alt</kbd>
- If you do not have these two files (`id_rsa` and `id_rsa.pub`), create them by typing:  
	- <kbd> ssh-keygen</kbd>
	- Hit  <kbd> enter  </kbd> **3 times**

```bash
% pwd 
/Users/gallettilance/.ssh
% ls
% ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/gallettilance/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/gallettilance/.ssh/id_rsa.
Your public key has been saved in /Users/gallettilance/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:jmDJes1qOzDi8KynXLGQ098JMSRnbIyt0w7vSgEsr2E gallettilance@RESHAMAs-MacBook-Pro.local
The key's randomart image is:
+---[RSA 2048]----+
|   .=+           |
|.  .==           |
|.o  +o           |
|..+= oo          |
|.E.+X.  S        |
|+o=o=*oo.        |
|++.*o.+o.        |
|..*.oo           |
|o= o+o           |
+----[SHA256]-----+
% ls
total 16
-rw-------  1   1675 Dec 17 12:20 id_rsa
-rw-r--r--  1    422 Dec 17 12:20 id_rsa.pub
% 
```

#### Step 4: Copy `ssh` key

Navigate to the `.ssh` directory

<kbd> cd ~/.ssh </kbd>  

open `id_rsa.pub` using your editor of choice and copy its contents.

### Windows Users

Follow [How to Create SSH Keys with PuTTY on Windows](https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-putty/)


## Add `ssh` key to GitHub

- go to your [GitHub account](https://github.com/) (create one if you don't have one, and save your user name and password somewhere easily accessible for you.)
- click on your avatar/profile picture (upper right of screen)
- go to `Settings`
- on left of screen, select `SSH and GPG keys`
- Select <kbd> New SSH key </kbd>
- for "Title":  entitle it  "GitHub key"
- for "Key":  paste key from clipboard here
- click <kbd> Add SSH key </kbd>
- save, exit, confirm GitHub password as requested


