import os
from ui import interface

# if __name__ == '__main__':
#     interface()



cur_path = os.path.dirname(__file__)
os.chdir(cur_path)
with open('test.csv', 'a', encoding='utf-8') as f:
    f.write(f"test")