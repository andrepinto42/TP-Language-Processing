#-------------------
# Lexer Code
#-------------------

import ply.lex as lex

literals = []
tokens = ['VAR', 'NUMBER']
ignore = " \t\n"
def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	print("Found a ID")
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	print(f"Illegal character {t.value[0]}") 
	t.lexer.skip(1)
	

lexer = lex.lex()

#-------------------
# Yacc Code
#-------------------

import ply.yacc as yacc

precedence = [
('left','+','-'),
('left','*','/'),
]
ts = { }
def p_grammar0(p):
	r'prog : comandos'
	


def p_grammar1(p):
	r'comandos : comando comandos'
	


def p_grammar2(p):
	r' comandos :'
	print("End of file")


def p_grammar3(p):
	r' comando : stat '
	


def p_grammar4(p):
	r'stat : VAR "=" exp'
	ts[p[1]] = p[3]


def p_grammar5(p):
	r'stat : exp'
	print(p[1])


def p_grammar6(p):
	r"exp : exp '+' exp "
	p[0] = p[1] + p[3]
	print("found a +")


def p_grammar7(p):
	r"exp : exp '-' exp "
	p[0] = p[1] - p[3]


def p_grammar8(p):
	r"exp : exp '*' exp "
	p[0] = p[1] * p[3]


def p_grammar9(p):
	r"exp : exp '/' exp "
	p[0] = p[1] / p[3]


def p_grammar10(p):
	r"exp : '(' exp ')' "
	p[0] = p[2]


def p_grammar11(p):
	r'exp : NUMBER '
	p[0] = p[1]


def p_grammar12(p):
	r'exp : VAR '
	p[0] = getval(p[1])



def getval(n):
    pass

def p_error(p):
    print("Error in",p)


parser = yacc.yacc()

