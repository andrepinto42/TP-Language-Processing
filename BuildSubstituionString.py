import BuilderMatchingString

# Substituion string
#"Número": "\1",
#"Nome": "\2",
#"Número": "\1",
def buildSubstituionString(parametrosNomeHeader,numParams):
    sizeHeader = len(parametrosNomeHeader)
    iterator = 0
    str_substi = '{'
    for i in range(0,sizeHeader):
        #Find a if the collum we are looking after has a special entry point
        #"Notas": [\4,\5]
        if specialHeader:= BuilderMatchingString.FindEntry(iterator):
            iterator += specialHeader.endIndex - specialHeader.startIndex
            
            #Insert the name of the parameter
            str_substi +=rf'"{specialHeader.name}": ['
            
            for k in range(specialHeader.startIndex,specialHeader.endIndex):
                str_substi += rf'\{k+1},'
            str_substi += rf'\{specialHeader.endIndex+1}]'
            
            #If currently not in the last header then add a comma ',' to separate entries
            if i != sizeHeader-1:
                str_substi += ','

        else:
            #"Número": "\1"
            str_substi += rf'"{parametrosNomeHeader[i]}": "\{iterator+1}"'
            #Adicionar uma virgula a separar os parametros
            if i+1 is not sizeHeader:
                str_substi+= ','

        #Advance the iterator
        iterator +=1
    
    str_substi += '}'
    return str_substi;