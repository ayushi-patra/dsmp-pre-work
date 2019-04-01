#Message Reading
file_path 

def read_file(path):
    file = open(path, 'r')
    sentence = file.read()
    return sentence

#Code starts here

sample_message = read_file(file_path) 

