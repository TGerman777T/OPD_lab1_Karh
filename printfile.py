from contextlib import redirect_stdout
import main

with open('News.txt', 'w') as f:
    with redirect_stdout(f):
        main.parse()