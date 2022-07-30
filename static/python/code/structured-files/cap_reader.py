
def should_skip(line):
    return line.find(";") == -1

def should_process(line):
    return line.find(";") != -1

def process(line):
    print("Processing LINE: ", line)

if __name__=='__main__':
    with open('caps-with-header.txt', 'r') as caps:
        for line in caps:
            if should_process(line):
                process(line)
