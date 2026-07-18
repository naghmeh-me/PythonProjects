import os

if os.path.exists('1.py'):
    os.remove('1.py')
else:
    print("the file dose not exist.")
