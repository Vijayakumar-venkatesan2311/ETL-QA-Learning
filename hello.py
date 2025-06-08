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

def name(rank):
    if rank==1:
        print("Rajini")
    elif rank==2:
        print("Vijay")
    else:
        print("Ajith")


name(1)
