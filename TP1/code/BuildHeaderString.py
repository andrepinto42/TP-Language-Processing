import re

def buildHeader(regexExpression,headerRawString):
    parametrosNomeHeader = []
    matches = re.finditer(regexExpression, headerRawString, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        headerString = match.group(0)

        #Remover a ',' do final do match
        if headerString[len(headerString)-1] == ',':
            headerString = headerString[:-1]

        #Remover a ',' do inicio do match
        if headerString[0] == ',':
            headerString = headerString[1:]
            
        #Se o resultado não for nulo então adicionar ao array de Headers
        if (headerString != ''):
            parametrosNomeHeader.append(headerString)
    
    return parametrosNomeHeader
 