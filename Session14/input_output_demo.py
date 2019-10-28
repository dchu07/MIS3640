# #writing a file
# fout = open('Session14/output.txt', 'w')
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# #when you are done writing, you should close the file.
# fout.close()
# #if you dont close the file, it gets closed for you when the program dies

#exercise 1
# def sed(pattern, replace, source, dest):
#     with open(source, 'r') as f_r:
#         with open(dest, 'w') as f_w:
#             for line in f_r:
#                 new_line = line.replace(pattern, replace)
#                 f_w.write(new_line)

# pattern = " man "
# replace = " woman "
# source = "Session14/output.txt"
# dest = "Session14/output2.txt"
# sed(pattern, replace, source, dest)

import os
cwd = os.getcwd()
#cwd stands for "current working directory"
# print(cwd)

#os.path provides other functions for working with filenames and paths
# os.path.abspath('output.txt')
# os.path.exists('output.txt')
# os.path.isdir('output.txt')
# os.path.isdir('/exercises')
# os.path.isfile('output.txt')
# os.listdir(cwd)

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """ 
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
#os.path.join takes a directory and a file name and joins them inot a complete path

def walk2(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))
