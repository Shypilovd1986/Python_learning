import os
def show_list_of_directory(name_directory):
    os.walk(name_directory)

if __name__ == '__main__':
    show_list_of_directory('Python_learning')