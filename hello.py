def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')


"""
1. git add hello.py - this means already file is staged 

Ans -- now how to unstage it --> git reset hello.py

2. Staged file – How to do changes in the code, Even if a file is staged (git add done), 

Ans -- You can still open and modify it. If you do:-
-- You’ll see the same file listed twice:
-- Once in staged
-- Once in unstaged

3. git commit -am "Updated message" 

-- Stage the changes
-- Commit it in one command
-- But this only works for tracked files (files already committed before).

3. git config --global core.autocrlf true 

-- This tells Git:
👉 “I’m on Windows. Please automatically convert line endings as needed.”


4. del .git\index.lock - manually delete the lock file
"""

def vote_eligibility(age):
    if age <= 18:
        print(f"not eligible for voting his/her age is {age}")
    else:
        print((f"eligible for voting his/her age is {age}"))

vote_eligibility(23)

# Step	                                                 Action
# git stash	                                  Save current work temporarily
# git checkout main	                          Switch to another branch
# git checkout feature_changes_Jun_8	      Come back to your feature
# git stash pop	                              Restore your work
# git add, git commit, git push	              Save and upload

def name(rank):
    if rank==1:
        print("Rajini")
    elif rank==2:
        print("Vijay")
    else:
        print("Ajith")


name(1)

