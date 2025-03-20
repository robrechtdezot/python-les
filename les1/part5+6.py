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

print(case_1())

