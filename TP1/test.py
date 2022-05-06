from locale import atoi
import re
import BuildHeaderString
import BuilderMatchingString
import BuildSubstituionString
import HandleFunctionsParameters

regexHeader = r'.+?[^\{\d+],|[^,].+?$'
test_str = "Número,Nome,Curso{1,2},,Notas{2}::media,,Genero"
dados = '3162,Cândido Faísca,Teatro,Musica,1,2,Masculino'

parametrosNomeHeader = BuildHeaderString.buildHeader(regexHeader,test_str)

parametrosMatchingRegex,numParams,allArrayHeaders = BuilderMatchingString.buildMatchingString(parametrosNomeHeader)

parametrosSubstituion   = BuildSubstituionString.buildSubstituionString(parametrosNomeHeader,numParams)

print("Header",parametrosNomeHeader)
print("Regex Expression",parametrosMatchingRegex)
print("Substition Expression",parametrosSubstituion)

jsonEntry = re.sub(
    parametrosMatchingRegex,
    parametrosSubstituion,
    dados)

#Remove from json Notas: [1,]
#Transform into Notas: [1]
# Isto só acontece quando o parametro é de tamanho variavel -> Notas{1,2}
jsonEntry= jsonEntry.replace(",]","]")

# Caso apareça Notas{5}::sum então esses parametros tem de ser tratados
jsonEntry = HandleFunctionsParameters.HandleFunctions(allArrayHeaders,jsonEntry)

print("Json ->",jsonEntry)