
def splitter(string):
    newString = string[1:-1]
    finalStr = ""
    for c in newString:
        finalStr += c + " "
    
    #Remove the last unused space
    finalStr = finalStr[:-1]
    
    return finalStr.split()