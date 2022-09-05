
import argparse
from genericpath import isdir
import os


def get_file_names(folderpath, out='output.txt'):
    with open(out, 'w') as file_object:
        for file in os.listdir(folderpath):
            file_object.write(file+'\n')


def get_all_file_names(folderpath, out='output.txt'):
    files = os.listdir(folderpath)
    for item in files:
        item = os.path.join(folderpath,item)
        if os.path.isfile(item):
            print(item)
        elif os.path.isdir(item):
            print(item)
            get_all_file_names(item)
        else:
            print("Unknown")

def print_line_one(file_names):
    return

def print_emails(file_names):
    return

def write_headlines(md_files, out='output.txt'):
    return






if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--folderpath',required=True)
    args = parser.parse_args()

    get_file_names(args.folderpath)
    get_all_file_names('/Users/weinell/Documents/Dev/CPH Business/4. Semester/Python/docker_notebooks/notebooks/_my_notebooks/Week 2')