import re
import enum
from locale import atoi

class Behaviour(enum.Enum):
    NO_BEHAVIOUR = 0
    SUM = 1
    MEDIA = 2


# Variable that will store all the Special case Parameters
# Nome,Notas{2},,
# Converts to ArrayHeader(Notas,1,2)
allArrayHeaders = []

class ArrayHeader:
  def __init__(self, name, startIndex, endIndex,behaviour,paramIndex):
    self.name = name
    self.startIndex = startIndex
    self.endIndex = endIndex
    self.behaviour = behaviour
    self.paramIndex = paramIndex

def FindEntry(i):
    for specialHeader in allArrayHeaders:
        if specialHeader.startIndex is i:
            return specialHeader
    return None

def buildMatchingString(parametrosNomeHeader):
    parametrosMatchingRegex = ''
    paramNum = 0
    for j in range(0,len(parametrosNomeHeader)):
        upperBound = 1
        # Found a parameter with a { }
        if re.search(r'{.*}',parametrosNomeHeader[j]):
            # Encontrado parametro Notas{3,5}
            if matched:=re.search(r'{(\d+),(\d+)}',parametrosNomeHeader[j]):
                # lowerBound = atoi(matched.group(1))
                upperBound = atoi(matched.group(2))
            
            # Encontrado parametro Notas{5}
            elif matched:=re.search(r'{(\d+)}',parametrosNomeHeader[j]):
                upperBound = atoi(matched.group(1))
            

            #Remover {2} da string Notas{2}
            strippedParametro = re.sub(r'(.*)\{.*\}', r'\1' , parametrosNomeHeader[j])


            behaviour = Behaviour.NO_BEHAVIOUR
            # Find some special behaviour in the header Notas{5}::sum
            if behaviour_found := re.search(r'{.*}::(\w+)',parametrosNomeHeader[j]):
                name_behaviour = behaviour_found.group(1)

                if   name_behaviour.upper() == Behaviour.SUM.name:
                    behaviour = Behaviour.SUM 
                elif name_behaviour.upper() == Behaviour.MEDIA.name:
                    behaviour = Behaviour.MEDIA
                else:
                    #Some error handling here
                    print("Behaviour not determined!")
                
                #strippedParametro = Notas_sum
                strippedParametro = re.sub(r'(.*?)\{.*\}.*', rf'\1_{name_behaviour}' , parametrosNomeHeader[j])
            #Adicionar mais novos grupos de captura à string de substituição
            for num in range(0,upperBound):
                parametrosMatchingRegex += r'(.*?),'

            # Guardar numa variavel Global
            allArrayHeaders.append( ArrayHeader(strippedParametro,paramNum,paramNum+upperBound-1,behaviour,j) )
            
            # Acrescentar ao numero de parametros o numero encontrado Notas{5}
            paramNum += upperBound

        # Caso normal de um header exemplo -> Nome
        else:
            paramNum = paramNum + 1
            parametrosMatchingRegex +=  r'(.*?),'
        
        #Também é importante substituir o ultimo elemento da string de captura
        #Por uma expressao que captura tudo até o final da string
        if j+1 == len(parametrosNomeHeader):
            #Remover da string -> (.*?), -> estes são os 6 carateres finais
            parametrosMatchingRegex = parametrosMatchingRegex[:-6]
            parametrosMatchingRegex += r"(.*)"
        
    return parametrosMatchingRegex,paramNum,allArrayHeaders