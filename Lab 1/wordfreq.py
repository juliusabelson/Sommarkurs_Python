def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):

            while line[start].isspace():
                start += 1

                if start == len(line):
                    return words
            

            end = start
            if line[end].isalpha():
                while line[end].isalpha():
                    end += 1
                
                words.append(line[start:end].lower())
                    
                
            elif line[end].isdigit():
                while line[end].isdigit():
                    end += 1
                
                words.append(line[start:end].lower())
            
            else:
                words.append(line[start])
    return words


tokenize(['sweet  apple  tarts.'])

