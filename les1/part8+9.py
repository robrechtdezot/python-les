def case1():
    #  Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output. 
    
    fname = input("Enter file name: ")
    fh = open(fname)
    lst = list()
    for line in fh:
        line = line.rstrip()
        line = line.split()
        for word in line:
            if word not in lst:
                lst.append(word)
    lst.sort()
    print(lst)

def case2():
    #  Use the file name mbox-short.txt as the file name   
    # 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
    # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    # You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
    # Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
    fname = input("Enter file name: ")
    fh = open(fname)
    count = 0
    for line in fh:
        line = line.rstrip()
        if line.startswith('From '):
            count = count + 1
            line = line.split()
            print(line[1])
    print("There were", count, "lines in the file with From as the first word")


