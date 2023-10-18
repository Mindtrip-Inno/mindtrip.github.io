import os

abs_path = os.path.dirname(__file__)

print(abs_path)

path = 'sdf/asd.txt'


real_path= path + abs_path

print(real_path)
