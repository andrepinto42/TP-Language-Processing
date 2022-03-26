from locale import atoi
import re
import BuilderMatchingString

def HandleFunctions(allArrayHeaders,jsonEntry):
    regexDataParametros = r':\s["\[](.*?)["\]]'
    for specialHeader in allArrayHeaders:
        if specialHeader.behaviour is BuilderMatchingString.Behaviour.NO_BEHAVIOUR:
            continue
        else:
            specialHeader.paramIndex

        # Array to be initialized with numbers found of within [1,3,4,5]
        arrayNumbers = []

        matches = re.finditer(regexDataParametros, jsonEntry, re.MULTILINE)
        for index,match in enumerate(matches):
            if (index == specialHeader.paramIndex):
                arrayNumbers = match.group(1).split(',')        
                break
        
        newnumber = 0
        if specialHeader.behaviour is BuilderMatchingString.Behaviour.SUM:
            for num in arrayNumbers:
                newnumber += atoi(num)
            
        
        elif specialHeader.behaviour is BuilderMatchingString.Behaviour.MEDIA:
            count = 0
            for num in arrayNumbers:
                count +=1
                newnumber += atoi(num)
            
            newnumber = newnumber / count
        else:
            print("Not know behaviour found!")
        
        jsonEntry = re.sub(fr'"{specialHeader.name}": \[.*?\]',
                        fr'"{specialHeader.name}": {newnumber}',
                        jsonEntry)
    return jsonEntry