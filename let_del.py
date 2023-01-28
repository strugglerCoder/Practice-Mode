def deleted(string):

    nxt = 1
    count = 0

    # for i in range(len(string)-1):
    #    if string[i]==string[i+1]:
    #        count+=1
    # return count

    for i in range(len(string)):

        if nxt == len(string):
            return count
        elif string[i] == string[nxt]:
            count += 1
        nxt += 1

print(deleted("aabccaa"))
