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


<br>
✨Done! Go to GitHub to see the latest changes.