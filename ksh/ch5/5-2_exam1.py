def flatten(data):
    output =[]

    for i in data:
        #print(type(i))
        if type(i) == list:
            #flatten(i)
            #output.append(flatten(i))
            output += flatten(i)
            print(output)
        else:
            #print(i)
            output.append(i)
            #print(output)
    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))