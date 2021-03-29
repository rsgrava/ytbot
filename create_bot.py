import random

def load_dictionary(filename):
    file = open(filename, 'r')
    dictionary = file.read().split()
    file.close()
    return dictionary

def generate_name(filename, word_number):
    dictionary = load_dictionary(filename)
    name = ""
    for i in range(0, word_number):
        name += dictionary[random.randint(0,len(dictionary))]
    name += str(random.randint(0,9999))
    return name

def save_bot(filename, email, password):
    file = open(filename, 'a')
    file.write(email + ' ' + password + '\n')
    file.close()
    return

def create_bot(infile, outfile):
    email = generate_name(infile, 1) + "@gmail.com"
    password = generate_name(infile, 1)
    save_bot(outfile, email, password)
    return

if __name__ == "__main__":
    create_bot("dictionary.txt", "bots.txt")
