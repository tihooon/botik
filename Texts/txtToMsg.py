import os
ROOT = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

with open(ROOT('Abuz1.txt'), 'r', encoding="utf-8") as txt:
    Abuz1 = txt.read()