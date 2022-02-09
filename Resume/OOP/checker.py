with open('file1.txt') as file1:

    with open('file2.txt') as file2:

        file1 = [x.strip() for x in file1]
        file2 = [x.strip() for x in file2]

        diffs = (set(file1) ^ set(file2))
        
        print (diffs)