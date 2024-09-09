# Practice-Git
A dummy repo to practice git. Feel free to do anything with it 😄.    

Choose either the vscode or CLI approach. The vscode approach is more beginner friendly.

As time passes I'll add more git actions here. For now just focus on these basic steps:
## To stage, commit a file
In VSCode:
1. Add, delete, or change the fruits.
2. Go to left side bar -> Source control
3. Click on "+" for files that you changed. Your files are now staged. 
4. Add commit message: eg. "Add pear" 
5. Click on Commit. Your commits are now made to your local repo.

In CLI:
```
git add .            //stage all files
git commit -m "Add pear"
```

## To push your local changes to the remote repo
Rationale: Your local commits are only present in your local repo.    
Hence we need to push the changes to the remote repo so that everyone else can see it.  
The remote repo is called ***origin***.

In VSCode:      
1. Click on Sync changes. 

In CLI:
```
git push origin main
```
This means that you're pushing your main branch to the origin (remote branch). 
**main** can be replaced by **master** depending on the name of your local branch. 



## Branching
Allows developers to work on different features without affecting the main branch. This ensures main branch is not affected.   

In CLI:
```
# Check which branch you're on
git branch

# On main branch, create a new branch
git checkout -b branch-red-fruits

#...make changes to the code

# Commit and push from branch-red-fruits 
git add .
git commit -m "Update red fruits"
git push origin branch-red-fruits 
```
Now check if your changes in branch-red-fruits are pushed to github.


## Merging branch to main branch
When you are done with your new feature in branch-red-fruits, you're ready to merge your code into the main branch, so that everyone else can see (and pull) it.

Merge own branch to main branch.   
In CLI:   
```
git checkout main  # go to main branch
git merge branch-red-fruits # merge main branch with yr_branch
git commit -m "Merge branch-red-fruits branch into main"
git push origin main # push main branch to remote repo
```
Now check if you successfully merged yr branch in Github. 

# Dealing with Merge conflicts
Merge conflicts arises when there are changes made in your branch and the main branch, and git do not know which one to keep.   

So, first make sure you update your branch with the latest changes in the main branch.
```
1. Git checkout main
2. Git pull
3. Git checkout branch-red-fruits
4. Git merge main
5. Resolve conflicts manually in vscode
6. Git push origin branch-red-fruits
7. Check Github
```
Resolve conflicts in Vscode -> choose which code changes to keep and discard. 

# Updating your branch with the main branch
```
1. Git checkout main
2. Git pull
3. Git checkout yr_branch
4. Git merge main
5. Resolve conflicts manually in vscode (if any)
6. Git push origin yr_branch
7. Check github
```

# Merging branch to main
After making edits in your branch,
```
1. stage, commit, git push origin yr_branch
2. Go to github > yr_branch 
3. Select Contribute > create pull request
```

<br>
✨Done! Go to GitHub to see the latest changes.