def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        print(line)

        while start < len(line):
            while line[start].isspace(): #and start < len(line):
                start = start + 1
                print("Space:")
                print(start)
            
            end = start

            if line[end].isalpha():
                while line[end].isalpha() and end < len(line):
                    end = end + 1
                    print("Bokstav:")
                    print(end)
                words.append(line[start:end].lower())
            
            elif line[end].isdigit():            
                while line[end].isdigit() and end < len(line):
                    end = end + 1
                    print("Siffra:")
                    print(end)
                words.append(line[start:end])
            if not (line[end].isdigit() or line[end].isalpha() or line[end].isspace()):
                words.append(line[end])
                

            start = end + 1
    return words    

lines = ["This is a simple sentence"]
for line in lines:
    print(len(line))