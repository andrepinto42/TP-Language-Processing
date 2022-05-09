#-------------------
# Lexer Code
#-------------------

import ply.lex as lex

literals = ['+', '-', '/', '*', '=', '(', ')']
ignore = " \t\n"
tokens = ['VAR', 'NUMBER']
def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	print("Found a ID")
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	error(f"Illegal character {t.value[0]}")
	t.lexer.skip(1)
	return t

print("done")
print("another string")


lexer = lex.lex()

#-------------------
# Yacc Code
#-------------------

import ply.yacc as yacc

precedence = [
('left','+','-'),
('left','*','/'),
('right','UMINUS'),
]
ts = { }
def p_grammar0(p):
	r"stat : VAR "=" exp"
	ts[p[1]] = p[3]

def p_grammar1(p):
	r"stat : exp"
	print(p[1])

def p_grammar2(p):
	r"exp : exp '+' exp "
	t[0] = t[1] + t[3]

def p_grammar3(p):
	r"exp : exp '-' exp "
	t[0] = t[1] - t[3]

def p_grammar4(p):
	r"exp : exp '*' exp "
	t[0] = t[1] * t[3]

def p_grammar5(p):
	r"exp : exp '/' exp "
	t[0] = t[1] / t[3]

def p_grammar6(p):
	r"exp : '-' exp %prec UMINUS "
	t[0] = -t[2]

def p_grammar7(p):
	r"exp : '(' exp ')' "
	t[0] = t[2]

def p_grammar8(p):
	r"exp : NUMBER "
	t[0] = t[1]

def p_grammar9(p):
	r"exp : VAR "
	t[0] = getval(t[1])


parser = yacc.yacc()
parser.parse("5+5")

