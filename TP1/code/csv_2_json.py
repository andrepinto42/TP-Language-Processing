#!usr/bin/env python3
from locale import atoi

import re
import BuildHeaderString
import BuilderMatchingString
import BuildSubstituionString
import HandleFunctionsParameters
import sys

# import getOPT
ENABLE_DEBUG = True
regexHeader = r'.+?[^\{\d+],|[^,].+?$'
file = None
first_line= ""
lines = []

#If there are atleast 2 arguments try to opening a file 
if (len(sys.argv) >= 2):
    file = open(sys.argv[1])
    first_line = file.readline()
else: 
    first_line =sys.stdin.readline()

parametrosNomeHeader = BuildHeaderString.buildHeader(regexHeader,first_line)

parametrosMatchingRegex,numParams,allArrayHeaders = BuilderMatchingString.buildMatchingString(parametrosNomeHeader)

parametrosSubstituion   = BuildSubstituionString.buildSubstituionString(parametrosNomeHeader,numParams)

if ENABLE_DEBUG:
    print("Header",parametrosNomeHeader)
    print("Regex Expression",parametrosMatchingRegex)
    print("Substition Expression",parametrosSubstituion)

if (len(sys.argv) >= 2):
    lines =file.readlines()
#If not then try to readlines from the standart input
else:
    lines  =sys.stdin.readlines()

numberlines = len(lines)
print("[",end="")
for index,line in enumerate(lines):
    line =line.strip()
    jsonEntry = re.sub(parametrosMatchingRegex,
                       parametrosSubstituion,
                       line)
        
    #Remove from json Notas: [1,,,]  -> Transform into Notas: [1]
    # Isto só acontece quando o parametro é de tamanho variavel -> Notas{1,3}
    jsonEntry= re.sub(r'(\[.*?)(,{1,})\]',r'\1]',jsonEntry)

    # Caso apareça Notas{5}::sum então esses parametros tem de ser tratados
    jsonEntry = HandleFunctionsParameters.HandleFunctions(allArrayHeaders,jsonEntry)

    #EOF vai aparecer na proxima iteracao   
    if (index +1 == numberlines): 
        print(jsonEntry,"]")
    else: 
        print(jsonEntry,",",end="")   

if file:
    file.close()