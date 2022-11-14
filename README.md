# fun_time

To clone a repository:
``` bash
git clone <repo_url>
```

To create a branch:
``` bash
git branch <branch_name>
```

To list the branches and see the current one:
``` bash
git branch
```

To move to another branch:
``` bash
git checkout <branch_name> 
```

To pull the recent changes:
``` bash
git pull
```

To stage the changes:
``` bash
git add <filename>
# to add stage all the changes you can use .
git add .
# to add multiple files you can add multiple filenames
git add <filename_1> <filename_2>

```

To commit the changes:
```
git commit -m "your message here"
```

To push the changes:
```
# if the branch does not exist in the origin first you should set the upstream
git push --set-upstream origin dev

# The to push to the branch
git push
```

