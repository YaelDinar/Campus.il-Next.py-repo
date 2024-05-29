#task 1.5 from chapter 1

def main():
    # 1 -> print the longest word- max length
    # using max, go through all the names and print the one with the max length
    with open('names.txt','r') as f:
        print(max(f.read().split(), key=len))

    # 2 -> print how many characters are there
    # split the string of the file so there will only be the names without spaces or \n
    # then using map and sum, count how many characters are in the file
    with open('names.txt', 'r') as f:
        print(sum(map(len, f.read().split())))

    # 3 -> print the shortest names
    # get the shortest name length by sorting the names according to their length
    # then get the length of the first name and print all the names that have the same length
    with open('names.txt', 'r') as f:
        names = f.read().split()
        #names sorted by length
        names.sort(key=len)
        #print using join the names that are the same length as the first name in the sorted names
        print(''.join(name + '\n' for name in names if len(name) == len(names[0])))

    # 4 -> creates a new file with the names' lengths in it
    # for each name, write the length and add to the string \n to drop a line
    with open('Names.txt', 'r') as f, open('name_length.txt', 'w') as out:
        out.write('\n'.join(str(len(name)) for name in f.read().split()) + '\n')

    # 5 -> gets a number from the user and prints all the names that are that length
    # print using join and drop line with \n for each name that is the same length
    length = int(input("enter a number: "))
    with open('names.txt', 'r') as f:
        print(''.join(name + '\n' for name in f.read().split() if len(name) == length))

if __name__ == "__main__":
    main()
