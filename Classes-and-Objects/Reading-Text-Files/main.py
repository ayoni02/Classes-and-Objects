# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from posixpath import split


def read_file_content(filename):
    # [assignment] Add your code here 
    
    with open('./story.txt', 'r') as f:
        lines = f.read()   
    return lines

x= "=============================================================================================="
print(x)
def count_words():
    text = read_file_content("./story.txt")
    splitting =  text.split()
    # [assignment] Add your code here
    count = {}
    for i in splitting:
        if i in splitting:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1

    return count

print(count_words())