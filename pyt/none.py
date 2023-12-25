


def load(filename):
    return open(filename, 'r')

def wordcount(filename):


    myfile_l = filename.read().lower()
    words_in_file = myfile_l.split()
    count_dict = {}
    for i in words_in_file:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
            count = 0
    for i in count_dict:
        if count_dict[i] == 1:
            count += 1
    return count

def clear_memory(filename):
    return filename.close()













