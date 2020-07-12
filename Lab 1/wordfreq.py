def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            
            if line[start].isspace():
                while line[start].isspace():
                    start += 1
                    if start == len(line):
                        return words
            
            end = start
            if line[end].isalpha():
                while line[end].isalpha():
                    end += 1
                    if end == len(line):
                        break


                word = line[start:end].lower()
                words.append(word)
                end = end - 1

            elif line[end].isdigit():
                while line[end].isdigit():
                    end += 1
                    if end == len(line):
                        break

                word = line[start:end]
                words.append(word)
                end = end - 1
                

            else:
                word = line[end]
                words.append(word)
            
            start = end + 1
    return words



