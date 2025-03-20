'''loops'''
#find largest so far
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

def case_1():
    largest = None
    smallest = None
    while True:
        try: 
            num = input("Enter a number: ")
        except:
            print("Invalid input")
        else:
            if num == "done":
                break
            try:
                num = float(num)
            except:
                print("Invalid input")
            else:
                if largest is None:
                    largest = num
                elif num > largest:
                    largest = num

                if smallest is None:
                    smallest = num
                elif num < smallest:
                    smallest = num   

    print("Maximum is ", int(largest))
    print("Minimum is ", int(smallest))
# print(case_1())

def case_2():
    # find 0.8475 in text and split
    text = "X-DSPAM-Confidence:    0.8475"
    start = text.find('0.8475')
    new = text[start:].split()
    print(float(new[0]))
# print(case_2())

def case_3():
# average spam confidence
    fname = input("Enter file name: ")
    fh = open(fname)
    total_confidence = 0.0
    line_count = 0
    for line in fh:
        if line.startswith('X-DSPAM-Confidence:'):
            confidence = float(line.split(':')[1].strip())
            total_confidence += confidence
            line_count += 1
    if line_count > 0:
        line_avg = total_confidence / line_count
        print('Average spam confidence: ', line_avg)
# print(case_3())
