import re

def case1():
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"

    handle = open(name)
    hour_counts = {}

    for line in handle:
        if line.startswith("From "):
            words = line.split()
            time_part = words[5]  # Extract the time (HH:MM:SS)
            hour = time_part.split(":")[0]  # Extract the hour (HH)
            hour_counts[hour] = hour_counts.get(hour, 0) + 1  # Update count

    # Sort by hour and print
    for hour, count in sorted(hour_counts.items()):
        print(hour, count)

def case2():
    
    '''regular expression'''
    name = input("Enter file:")
    if len(name) < 1:
        name = "texttoread.txt"
    handle = open(name)
    total = 0

    for line in handle:
            numbers = re.findall(r'\d+', line)  # Find all numbers in the line
            total += sum(map(int, numbers))  # Convert to integers and sum them up

    print("Sum:", total)   

def case3():