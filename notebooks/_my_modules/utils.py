
import argparse
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

def print_line_one():
    file_path = '/Users/weinell/Documents/Dev/CPH Business/4. Semester/Python/docker_notebooks/notebooks/_my_notebooks/Week 2/'
    file_names = ['file1.csv', 'exercise.csv']
    for file in os.listdir(file_path):
        file = os.path.join(file_path,file)
        if os.path.isfile(file):
            with open(file) as file_object:
                print(file_object)
        elif os.path.isdir(file):
            print('folder')
        

def print_emails(file_names):
    return

def write_headlines(md_files, out='output.txt'):
    return






if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    #parser.add_argument('--folderpath',required=True)
    args = parser.parse_args()

    #get_file_names(args.folderpath)
    #get_all_file_names('/Users/weinell/Documents/Dev/CPH Business/4. Semester/Python/docker_notebooks/notebooks/_my_notebooks/Week 2')
    #print_line_one('/Users/weinell/Documents/Dev/CPH Business/4. Semester/Python/docker_notebooks/notebooks/_my_notebooks/Week 2/exercise.csv')
    print_line_one()