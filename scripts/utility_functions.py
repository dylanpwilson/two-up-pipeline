

def read_txt_by_line(file_path):
    '''
    Return list of lines from txt file.
    txt file location determined by file_path arg.
    
    '''
    
    lines = []
    f = open(file_path, 'r')
    for line in f:
        lines.append(line)
    f.close()
    return lines