# The Gentle Git Guide
There is a lot to git, an aweful lot. This guide is intended to cover and demystify the most common use cases so you can get started ASAP and never fear again!

The learning curve can feel a bit daunting and no matter how experienced you are with Git you'll likely run into a bit of a pickle and git will send you into rebase hell.

Following this guide should help you get out of most pickles and allow you to gain a bit of understanding behind what you do in git and generally feel more confident.

**Note. This guide features a lot of command line git instructions. If you prefer to use git in a GUI, that is totally fine. The only thing, is that maybe this guide won't translate one-to-one although most GUI use the same terminology.**

** Other Note. This is not a guide that covers our agreed git workflow and practices such as: how to name your branch, how to format your PR etc. For this information head over to [The Ultimate Branching, Pull Request and Review Guide](https://discourse.tripactions.systems/t/the-ultimate-branching-pull-request-and-review-guide/251)

## Super Basic Stuff
### Getting a repo on your machine (Basic but painful when done badly)
In the current setup of the organisation the **best** way to get any of the repositories on your machine in a clean way is to **clone the git repo via SSH**. This allows for easy security management and not having to enter credentials and whatnot later. This requires:
- that you have generated an SSH key.
- and that that key has been added to github
- Alright, here's how you do that. Github has written really good documentation on this so follow these two links:
    - [Generating an SSH key](https://help.github.com/en/enterprise/2.15/user/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    - [Adding and SSH key to Gitub](https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account)

- If all of the above is satisfied, what you'll wanna do is **clone** a repository. Here's a toy repo you can clone. Don't worry there's no bad stuff on there. Oh also, this is a public repo so you won't have to worry about SSH and all that. By the way, the first line will make you clone the repo right in your home directory. If you have a better place just ignore that command and navigate wherever you want on your harddrive.

```
> cd ~
> git clone https://github.com/bastienboutonnet/triple_g
> cd triple_g
```
💥BOOM Nice one! If you executed the last line you're now in the the folder of your git repo you just clone. Time to get some sh**t done.

### The Trifecta
OK! So git works like this:
- First you modify or create a file (assuming you're currently in that repo you just created earlier):
```
> nano yay_my_first_file.md
```
You'll probably see something like this:
```md
  GNU nano 2.0.6                       File: yay_my_first_file.md

# Playground file.

This is the file you'll be playing with in this tutorial. Although if you don't like it feel free to
create another one.
```
- Go ahead type something in that file!
- Save your beautiful words: `Ctrl+O` to save followed by `Ctrl+X` to exit

#### Git Status
This is by far the most useful git command you'll ever use! If you want to know any any point what is happening you'll ask git to tell you what the status of the repo is.

```
> git status
```
If you followed the step above you should see something like this:
```bash
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        yay_my_first_file.md

nothing added to commit but untracked files present (use "git add" to track)
```
git will basically tell you what's up on your repo. What this says is that that you have a file or a change that is not staged (or tracked). This is often referred to as "your repo is dirty". It means you have done something new and for now git isn't really keeping track of it.
The last line often tells you what you should be doing next. This is really handy and that's why `git status` is the most useful git command you'll ever run.

#### Git Add (aka Stage)
Ok! Now, you'll wanna make sure git starts keeping track of this file. This is called "staging your changes". Most of the time you want to make git track all the changes you did so you want to stage all file, or all files currently changed in the current directory and its subfolders. This is achieved with the following:
```bash
> git add .
```
Now if you do git status again, you should see something like that:
```bash
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   yay_my_first_file.md
```
Git tells you that now, it's keeping track of the changes and that you may want to commit (essentially preserve and record your changes) to your repo.

#### Git Commit (aka Add a trace of your change)
Committing a change to one or more files means that you'll create a record that keeps track of what you did. That means, you'll now be able to refer to this change later and do stuff that we'll cover in a second.
```
> git commit -m "add my new piece of text to my first file"
```
The command is `git commit` the `-m` means that you'll write a message or note of what the change is and the rest between `" "` is a short description of what you did so that you can keep track of what happened to your repo later.

🎉 Tada! You've completed the trifecta. As a recap things go like this:
1. Make a change, check what the state of your repo is with `git status`.
2. Stage the change with `git add`.
3. Record, or commit your change with `git commit`.

### Share your changes and get other people's changes
#### Git Push
Most likely, you will be working with other people who all share a copy of the repository and most likely you will want to make sure your collaborators can also have your amazing piece of code. **This is what we call "pushing" your changes to the remote (machine)"**
And you do this as easily as that:
```bash
git push
```
If you remember, when you did `git clone` you created a local copy of a repository that is available and stored remotely. This remote repo is the one other people will clone later on to get a copy of the codebase you all are working on.

If you run `git status` again you'll see something like this now:
```bash
On branch master
Your branch is up to date with 'origin/master'.
```
👌🏻 Your collaborators will now be able to get your work on their machine too by "pulling".

#### Git Pull
This is the opposite of push. No shit!
```
> git pull
```
If you're up to date with the remote nothing really exciting will happen:
```
➜  triple_g git:(master) ✗
➜ git pull
Already up to date.'
```
If you're not up to date you'll see a summary of all the changes that have happened. In the following example a file was deleted:
```bash
➜ git pull
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (2/2), done.
From github.com:bastienboutonnet/triple_g
   127e390..5e70945  master     -> origin/master
Updating 127e390..5e70945
Fast-forward
 test | 1 -
 1 file changed, 1 deletion(-)
 delete mode 100644 test
 ```
#### That's it?
Kinda! Most of the time things go as smoothly as this. We will see later that this is a big bad thing that can happen, and git calls this **"CONFLICTS"**. A conflict arises when you and someone else have made a change to the same part of a file. This is actually not uncommon, you shouldn't panic too much.

This is basically a moment to tell git, which of the two changes you want to keep, or in what order you want to keep the changes.

**Conflict resolution is going to be different almost everytime, and it's going to be hard to explain it here. So if this happens, you should have a try or ask around for some guidance on how to resolve your first merge conflict.** We've all been there...

## The Less Basic Stuff. Isolation and Collaboration.
Ok, so now that we've covered the basic mechanics of how a change is kept track of and how this change is propagated to other collaborators. We'll complicate things a little, to allow for smooth collaboration between people on a single repo.

### Isolation Through Branching
So far, we didn't really worry about a key aspect: What happens when you push your code back to master? Well 2 pretty ugly things can happen:
 - a system that uses some of the code you just potentially affected might break, due to a bug or a breaking change.
- a user who was also working on a piece of code you may have affected might see their code break or run into conflicts.

For these two main reasons, and also to allow clear traceable development, we work using what git calls **branches**. Branches allow any one to isolate themselves from the main strand of code or **trunk** to push the tree analogy a bit further.
When you "branch out" you enter a bit of a parallel reality where all the code that happened up to the moment you branch out is available to your knowledge and use but new code won't (at least for a while) affect the main universe.

Here at TripActions, most users do not have the ability to push changes directly to master, therefore a branch-oriented worflow is actually what you'll end up doing.

To branch out, **make sure you have a recent copy of master**
```
git checkout master
git pull
```
and then create your branch. In general, you will also want to move to that branch after creating it so here is the command you should run for both of these things to happen:
```
git checkout -b <your_name>/<your_feature>
```
The `-b` takes care of running a `git branch <your_name>/<your_feature>` in the backgroun. You would replace of course the text set in `<>`. In the data team we follow the convention outlined above. For more detail over our Git conventions [head over to this discourse article](https://discourse.tripactions.systems/t/the-ultimate-branching-pull-request-and-review-guide/251)

Once you have done that you can code away, break as much stuff as you want etc. Chances are however that you won't want to stay in your pre-historical buble for ever so we'll discuss how to keep up to date with the main universe in the following section.

### Keeping up to date (Merging & Rebasing)


### Keeping Things Clean (Squashing & Fixup Workflow)