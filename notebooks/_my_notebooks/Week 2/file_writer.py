import argparse


def print_file_content(file):
    with open(file) as file_object:
        contents = file_object.read()
        print(contents)
    
def write_list_to_file(output_file,*lst):
    with open(output_file, 'w') as file_object:
        for word in lst:
            file_object.write(word)
    
def read_csv(input_file):
    list = []
    with open(input_file) as file_object:
        lines = file_object.readlines()
    for line in lines:
        strippedLine = line.strip()
        list.append(int(strippedLine))
    print(list)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    #parser.add_argument('--name', type=str, required=True)
    #parser.add_argument('path')
    parser.add_argument('--file','-file_name')
    parser.add_argument('--content')

    print_file_content('exercise.csv')

    write_list_to_file('file1.csv','Check','this','out')

    read_csv('row_list.csv')

    args = parser.parse_args()

    print_file_content(args.file)