import os
print("os.name=" ,os.name)

print("os.getenv('PATH')=" ,os.getenv('PATH'))

print("os.getcwd()=" ,os.getcwd())

os.mkdir("MyfolderDir")
print("New folder created successfully.")

print("os.getcwd()=" ,os.getcwd())

os.chdir("MyfolderDir")
print("Folder location changed.")
print("os.getcwd()=" , os.getcwd())

os.chdir("..")
os.rmdir('MyfolderDir')
print("folder deleted")