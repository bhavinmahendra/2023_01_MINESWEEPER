# TAD gerador - operacoes basicas

def cria_gerador(b, s):
    ''' 
    int x int -> gerador
    cria um gerador, utilizando o número de bits do gerador (b) e o estado inicial (s)
    devolve o gerador
    '''
    if type(b) == int and b in (32, 64) and type(s) == int and s > 0 and s <= 2**b:
        return [b, s] # gerador e uma lista
    else:
        raise ValueError('cria_gerador: argumentos invalidos')

def cria_copia_gerador(g):
    ''' 
    gerador -> gerador
    devolve a copia do gerador g
    '''
    if type(g) == list and len(g) == 2:
        if type(g[0]) == int and g[0] in (32, 64) and type(g[1]) == int and g[1] > 0 and g[1] <= 2**g[0]:
            return [g[0], g[1]]

def obtem_estado(g):
    ''' 
    gerador -> int
    obtem o estado do gerador g
    devolve o estado
    '''
    if type(g) == list and len(g) == 2:
        if type(g[0]) == int and g[0] in (32, 64) and type(g[1]) == int and g[1] > 0 and g[1] <= 2**g[0]:
            return g[1]

def define_estado(g, s):
    ''' 
    gerador x int -> int
    altera o estado do gerador g
    devolve esse estado
    '''
    if type(g) == list and len(g) == 2:
        if type(g[0]) == int and g[0] in (32, 64) and type(g[1]) == int and g[1] > 0 and g[1] <= 2**g[0]:
            g[1] = s
            return s

def atualiza_estado(g):
    ''' 
    gerador -> int
    altera o estado do gerador utilizando o xorshift de geracao de numeros pseudoaleatorios
    devolve esse estado
    '''

    if type(g) == list and len(g) == 2:
        if type(g[0]) == int and g[0] in (32, 64) and type(g[1]) == int and g[1] > 0 and g[1] <= 2**g[0]:
            if g[0] == 32: # operacoes caso o tamanho do gerador seja 32
                g[1] ^= ( g[1] << 13 ) & 0xFFFFFFFF
                g[1] ^= ( g[1] >> 17 ) & 0xFFFFFFFF
                g[1] ^= ( g[1] << 5 ) & 0xFFFFFFFF
            else: # operacoes caso o tamanho do gerador seeja 64
                g[1] ^= ( g[1] << 13 ) & 0xFFFFFFFFFFFFFFFF
                g[1] ^= ( g[1] >> 7 ) & 0xFFFFFFFFFFFFFFFF
                g[1] ^= ( g[1] << 17 ) & 0xFFFFFFFFFFFFFFFF
            return g[1]

def eh_gerador(arg):
    '''
    universal -> booleano
    verifica se arg se trata de um gerador
    se arg for um gerador, devolve True, se nao, devolve False
    '''
    if type(arg) == list and len(arg) == 2:
        if type(arg[0]) == int and arg[0] in (32, 64) and arg[1] > 0 and type(arg[1]) == int and arg[1] <= 2**arg[0]:
            return True
    return False

def geradores_iguais(g1, g2):
    ''' 
    gerador x gerador -> booleano
    verifica se g1 e g2 são geradores iguais, caso ambos sejam geradores
    se sim , devolve True, se nao, devolve False
    '''
    if eh_gerador(g1) and eh_gerador(g2):
            return g1 == g2

def gerador_para_str(g):
    ''' 
    gerador -> str
    devolve uma cadeia de caracteres contendo o tamanho e o estado do gerador g
    '''
    if eh_gerador(g):
            return 'xorshift' + str(g[0]) + '(s=' + str(g[1]) + ')'

# TAD gerador - funcoes de alto nivel

def gera_numero_aleatorio(g, n):
    ''' 
    gerador x int -> int
    atualiza o estado do gerador utilizando o algoritmo xorshift
    devolve um numero aleatorio entre 1 e n utilizando n e o estado do gerador
    '''
    if eh_gerador(g) and n > 0 and type(n) == int:
        s = atualiza_estado(g)
        return 1 + (s % n)

def gera_carater_aleatorio(g, c):
    ''' 
    gerador x str -> str
    atualiza o estado do gerador utilizando o algoritmo xorshift
    devolve um caracter aleatorio entre 'A' e 'Z' utilizando c e o estado do gerador
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if eh_gerador(g) and type(c) == str and c in colunas:
        s = atualiza_estado(g)
        cadeia = ''
        x = ord(c) + 1
        for i in range(ord('A'), x):
            cadeia += chr(i)
        l = len(cadeia)
        return cadeia[s % l]

# TAD coordenada - operacoes basicas

def cria_coordenada(col, lin):
    ''' 
    str x int -> coordenada
    recebe uma letra maiuscula e um numero entre 1 e 99
    devolve a coordenada correspondente a essa letra e esse numero
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if type(col) == str and col in colunas and type(lin) == int and lin in range(1, 100):
        return (col, lin) # a coordenada e um tuplo
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')

def obtem_coluna(c):
    ''' 
    coordenada -> str
    devolve a coluna da coordenada c
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if type(c) == tuple and len(c) == 2:
        if type(c[0]) == str and c[0] in colunas:
            return c[0]

def obtem_linha(c):
    ''' 
    coordenada -> str
    devolve a linha da coordenada c
    '''
    if type(c) == tuple and len(c) == 2:
        if type(c[1]) == int and c[1] in range(1, 100):
            return c[1]

def eh_coordenada(arg):
    ''' 
    universal -> booleano
    devolve a coluna da coordenada c
    verifica se arg se trata de uma coordenada
    se arg for uma coordenada, devolve True, se nao, devolve False
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if type(arg) == tuple and len(arg) == 2:
        if type(arg[0]) == str and arg[0] in colunas and type(arg[1]) == int and arg[1] in range(1, 100):
            return True
    return False

def coordenadas_iguais(c1, c2):
    ''' 
    coordenada x coordenada -> booleano
    verifica se c1 e c2 são coordenadas iguais, caso ambas sejam coordenadas
    se sim, devolve True, se nao, devolve False
    '''
    if eh_coordenada(c1) and eh_coordenada(c2):
        return c1 == c2

def coordenada_para_str(c):
    ''' 
    coordenada -> str
    devolve a cadeia de caracteres correspondente a coordenada c
    '''
    if eh_coordenada(c):
        coordenada = obtem_coluna(c)
        if c[1] <= 9:
            coordenada += str(0) + str(obtem_linha(c))
        else:
            coordenada += str(obtem_linha(c))
        return coordenada

def str_para_coordenada(s):
    ''' 
    str -> coordenada
    devolve a coordenada correspondente a cadeia de caracteres s
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    col = s[0]
    lin = int(s[1:])
    if type(col) == str and col in colunas and type(lin) == int and lin in range(1, 100):
        return (col, lin)

# TAD coordenada - funcoes de alto nivel

def obtem_coordenadas_vizinhas(c):
    ''' 
    coordenada -> tuplo
    devolve um tuplo com as coordenadas vizinhas a c
    '''
    if eh_coordenada(c):
        x = obtem_coluna(c)
        y = obtem_linha(c)
        x1, y1 = chr(ord(x) - 1), y - 1 # coluna anterior, linha anterior
        x2, y2 = x, y - 1 # mesma coluna, linha anterior
        x3, y3 = chr(ord(x) + 1), y - 1 # coluna a seguir, linha anterior
        x4, y4 = chr(ord(x) + 1), y # coluna a seguir, mesma linha
        x5, y5 = chr(ord(x) + 1), y + 1 # coluna a seguir, linha a seguir
        x6, y6 = x, y + 1 # mesma coluna, linha a seguir
        x7, y7 = chr(ord(x) - 1), y + 1 # coluna anterior, linha a seguir
        x8, y8 = chr(ord(x) - 1), y # coluna anterior, mesma linha
        vis = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8)]
        visinh = ()
        for i in vis: # para verficar se sao todas coordenadas
            if eh_coordenada(i):
                visinh += (i,)
        return visinh

def obtem_coordenada_aleatoria(c, g):
    ''' 
    coordenada x gerador -> coordenada
    devolve uma coordenada aleatoria utilizando o gerador g
    '''
    if eh_gerador(g) and eh_coordenada(c):
        x = gera_carater_aleatorio(g, obtem_coluna(c)) # coluna aleatoria
        y = gera_numero_aleatorio(g, obtem_linha(c)) # linha aleatoria
        return (x, y)

# TAD parcela - operacoes basicas

def cria_parcela():
    '''
    {} -> parcela
    devolve uma parcela tapada e sem mina
    '''
    return ['tapada', 'sem mina']

def cria_copia_parcela(p):
    '''
    parcela -> parcela
    devolve a copia da parcela p
    '''
    if type(p) == list and len(p) == 2:
        return [p[0], p[1]]

def limpa_parcela(p):
    '''
    parcela -> parcela
    muda o estado da parcela p para limpa
    devolve p
    '''
    if type(p) == list and len(p) == 2:
        p[0] = 'limpa'
        return p
    
def marca_parcela(p):
    '''
    parcela -> parcela
    muda o estado da parcela p para marcada
    devolve p
    '''
    if type(p) == list and len(p) == 2:
        p[0] = 'marcada'
        return p

def desmarca_parcela(p):
    '''
    parcela -> parcela
    muda o estado da parcela p para tapada
    devolve p
    '''
    if type(p) == list and len(p) == 2:
        p[0] = 'tapada'
        return p
    
def esconde_mina(p):
    '''
    parcela -> parcela
    esconde uma mina na parcela p
    devolve p
    '''
    if type(p) == list and len(p) == 2:
        p[1] = 'com mina'
        return p

def eh_parcela(arg):
    '''
    universal -> booleano
    verifica se arg se trata de um parcela
    se arg for uma parcela, devolve True, se nao, devolve False
    '''
    if type(arg) == list and len(arg) == 2:
        if arg[0] in ('tapada', 'limpa', 'marcada') and arg[1] in ('sem mina', 'com mina'):
            return True
    return False

def eh_parcela_tapada(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela tapada
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[0] == 'tapada':
            return True
    return False

def eh_parcela_marcada(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela marcada
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[0] == 'marcada':
            return True
    return False

def eh_parcela_limpa(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela limpa
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[0] == 'limpa':
            return True
    return False

def eh_parcela_minada(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela que esconde uma mina
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[1] == 'com mina':
            return True
    return False

def parcelas_iguais(p1, p2):
    ''' 
    parcela x parcela -> booleano
    verifica se p1 e p2 são parcelas iguais, caso ambas sejam parcelas
    se sim, devolve True, se nao, devolve False
    '''
    if type(p1) == list and len(p1) == 2 and type(p2) == list and len(p2) == 2:
        if p1[0] in ('tapada', 'limpa', 'marcada') and p2[0] in ('tapada', 'limpa', 'marcada'):
            if p1[1] in ('sem mina', 'com mina') and p2[1] in ('sem mina', 'com mina'):
                return p1 == p2

def parcela_para_str(p):
    '''
    parcela -> str
    devolve a cadeia de caracteres correspondente ao estado da parcela e se contem mina ou nao
    '''
    if p[0] == 'tapada':
        return '#'
    elif p[0] == 'marcada':
        return '@'
    elif p[0] == 'limpa' and p[1] == 'sem mina':
        return '?'
    elif p[0] == 'limpa' and p[1] == 'com mina':
        return 'X'
    
# TAD parcela - funcoes de alto nivel

def alterna_bandeira(p):
    ''' 
    parcela -> booleano
    desmarca a parcela p, caso p seja uma parcela e seja marcada, devolvendo True
    marca a parcela p, caso p seja uma parcela e seja tapada, devolvendo True
    se a parcela nao for marcada nem tapada, devolve False
    '''
    if eh_parcela(p):
        if eh_parcela_marcada(p):
            desmarca_parcela(p)
            return True
        elif eh_parcela_tapada(p):
            marca_parcela(p)
            return True
    return False

# TAD campo - operacoes basicas

def cria_campo(c, l):
    ''' 
    str x int -> campo
    devolve um campo cuja a ultima coluna corresponde a c e a ultima linha corresponde a l
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if type(c) == str and c in colunas:
        if type(l) == int and l in range(1, 100):
            campo = []
            for i in range(l):
                campo.append([])
                x = ord(c) - ord('A') + 1
                for j in range(x):
                    campo[i].append(['#', cria_parcela()]) # campo e uma lista
            return campo
    raise ValueError('cria_campo: argumentos invalidos')

def cria_copia_campo(m):
    '''
    campo -> campo
    devolve a copia do campo m
    '''
    if not eh_campo(m):
        raise ValueError("cria_copia_campo: argumento invalido")
    copia = []
    for linha in m:
        nova_linha = []
        for parcela in linha:
            nova_linha.append([parcela[0], cria_copia_parcela(parcela[1])])
        copia.append(nova_linha)
    return copia

def obtem_ultima_coluna(m):
    '''
    campo -> str
    devolve a ultima coluna de m
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if chr(len(m[0]) + ord('A')) in colunas:
        if len(m) in range(1, 100):
            x = len(m[0])
            return chr(ord('A') + x - 1)

def obtem_ultima_linha(m):
    '''
    campo -> int
    devolve a ultima linha de m
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if chr(len(m[0]) + ord('A')) in colunas:
        if len(m) in range(1, 100):
            return len(m)

def obtem_parcela(m, c):
    '''
    campo x coordenada -> parcela
    devolve a parcela com coordenada c do campo m
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if chr(len(m[0]) + ord('A')) in colunas:
        if len(m) in range(1, 100):
            if eh_coordenada(c):
                col = ord(obtem_coluna(c)) - ord('A')
                lin = obtem_linha(c) - 1
                return m[lin][col][1]

def obtem_coordenadas(m, s):
    '''
    campo x str -> tuplo
    devolve um tuplo com todas as coordenadas com estado s
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if chr(len(m[0]) + ord('A')) in colunas:
        if len(m) in range(1, 100):
            tuplo = ()
            for i in range(len(m)):
                for j in range(len(m[i])): 
                    x = chr(ord('A') + j) # coluna
                    y = i + 1 # linha
                    if s == 'tapadas' and m[i][j][1][0] == 'tapada':
                        tuplo += ((x, y),)
                    elif s == 'marcadas' and m[i][j][1][0] == 'marcada':
                        tuplo += ((x, y),)
                    elif s == 'limpas' and m[i][j][1][0] == 'limpa':
                            tuplo += ((x, y),)
                    elif s == 'minadas' and m[i][j][1][1] == 'com mina':
                        tuplo += ((x, y),)
            return tuplo

def obtem_numero_minas_vizinhas(m, c):
    '''
    campo x coordenada -> int
    devolve o numero de parcelas vizinhas com minas
    '''
    colunas = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if chr(len(m[0]) + ord('A')) in colunas:
        if len(m) in range(1, 100):
            if eh_coordenada(c):
                cont = 0
                x = ord(c[0]) - ord('A') - 1 # coluna anterior
                y = ord(c[0]) - ord('A') # mesma coluna
                z = ord(c[0]) - ord('A') + 1 # coluna a seguir
                for i in (x, y, z):
                    if i >= 0 and i < len(m[0]): # i tem de ser positivo e inferior ao numero de colunas
                        for j in (c[1] - 2, c[1] - 1, c[1]): # tuplo com a linha anterior, a mesma linha e a linha a seguir
                            if j >= 0 and j < len(m) and m[j][i][1][1] == 'com mina': # j tem de ser positivo e inferior ao numero de linhas
                                cont += 1
                if m[c[1] - 1][y][1][1] == 'com mina' and cont > 0: # se c for uma parcela minada, nao conta como uma parcela vizinha minada, logo retira-se esse valor
                    cont -= 1
                return cont

def eh_campo(arg):
    '''
    universal -> booleano
    verifica se arg se trata de um campo
    se arg for uma campo, devolve True, se nao, devolve False
    '''
    if type(arg) == list and len(arg) > 0:
            for l in arg:
                if len(l) == len(arg[0]) and type(l) == list:
                    for c in l:
                        if len(c) == 2 and (c[0] in ('#', '@', '?', 'X')) and type(c[1]) == list and len(c[1]) == 2:
                            return True
    return False

def eh_coordenada_do_campo(m, c):

    '''
    campo x coordenada -> booleano
    verifica se a coordenada c pertence ao campo m
    se sim, devolve True, se nao, devolve False
    '''
    if ord(obtem_coluna(c)) <= ord(obtem_ultima_coluna(m)) and ord(obtem_coluna(c)) >= ord('A') and obtem_linha(c) != None and obtem_linha(c) > 0 and obtem_linha(c) <= obtem_ultima_linha(m):
        return True
    return False

def campos_iguais(m1, m2):
    '''
    campo x campo -> booleano
    verifica se m1 e m2 são campos iguais, caso ambas sejam campos
    se sim, devolve True, se nao, devolve False

    '''
    v_m1 = False
    v_m2 = False
    if type(m1) == list and len(m1) > 0:
        for l in m1:
            if len(l) == len(m1[0]) and type(l) == list:
                for c in l:
                    if len(c) == 2 and (c[0] in ('#', '@', '?', 'X')) and type(c[1]) == list and len(c[1]) == 2:
                        v_m1 = True
    if type(m2) == list and len(m2) > 0:
        for l in m2:
            if len(l) == len(m2[0]) and type(l) == list:
                for c in l:
                    if len(c) == 2 and (c[0] in ('#', '@', '?', 'X')) and type(c[1]) == list and len(c[1]) == 2:
                        v_m2 = True
    if v_m1 and v_m2:
            return m1 == m2
    else:
        return False

def campo_para_str(m):
    # Atualiza representação das parcelas
    for i in range(len(m)):
        for j in range(len(m[i])):
            parcela = m[i][j][1]
            if eh_parcela_tapada(parcela):
                m[i][j][0] = '#'
            elif eh_parcela_marcada(parcela):
                m[i][j][0] = '@'
            elif eh_parcela_limpa(parcela):
                if eh_parcela_minada(parcela):
                    m[i][j][0] = 'X'
                else:
                    coord = cria_coordenada(chr(ord('A')+j), i+1)
                    num = obtem_numero_minas_vizinhas(m, coord)
                    m[i][j][0] = str(num) if num > 0 else ' '

    # Construção da string
    cabecalho = '   ' + ''.join(chr(ord('A')+i) for i in range(len(m[0])))
    separador = '  +' + '-'*len(m[0]) + '+'
    linhas = []
    
    for i in range(len(m)):
        num_linha = f"{i+1:02d}"
        conteudo = ''.join(m[i][j][0] for j in range(len(m[i])))
        linhas.append(f"{num_linha}|{conteudo}|")
    
    return '\n'.join([cabecalho, separador] + linhas + [separador])

# TAD campo - funcoes de alto nivel

def coloca_minas(m, c, g, n):
    '''
    campo x coordenada x gerador x int -> campo
    coloca n minas no campo m; as coordenadas das minas sao aleatorias (utilizando um gerador) e nao coincidem com a coordenada c
    devolve o campo modificado
    '''
    if not (eh_campo(m) and eh_coordenada(c) and eh_gerador(g) and isinstance(n, int) and n >= 0):
        raise ValueError("coloca_minas: argumentos invalidos")
    
    coord_proibidas = obtem_coordenadas_vizinhas(c) + (c,)
    minas_colocadas = 0
    ultima_col = obtem_ultima_coluna(m)
    ultima_lin = obtem_ultima_linha(m)
    
    while minas_colocadas < n:
        nova_mina = obtem_coordenada_aleatoria((ultima_col, ultima_lin), g)
        if (eh_coordenada_do_campo(m, nova_mina) and 
            nova_mina not in coord_proibidas and 
            not eh_parcela_minada(obtem_parcela(m, nova_mina))):
            
            esconde_mina(obtem_parcela(m, nova_mina))
            minas_colocadas += 1
    
    return m

def limpa_campo(m, c):
    '''
    campo x coordenaada -> campo
    limpa a coordenada c
    se nao houver minas nas parcelas vizinha, limpa-as
    devolve o campo modificado
    '''
    if not (eh_campo(m) and eh_coordenada(c) and eh_coordenada_do_campo(m, c)):
        raise ValueError("limpa_campo: argumentos invalidos")
    
    parcela = obtem_parcela(m, c)
    if eh_parcela_marcada(parcela):
        return m
    
    limpa_parcela(parcela)
    
    if eh_parcela_minada(parcela):
        return m
    
    if obtem_numero_minas_vizinhas(m, c) == 0:
        for vizinha in obtem_coordenadas_vizinhas(c):
            if (eh_coordenada_do_campo(m, vizinha) and 
                eh_parcela_tapada(obtem_parcela(m, vizinha))):
                limpa_campo(m, vizinha)
    
    return m

## Funcoes adicionais

def jogo_ganho(m):
    '''
    campo -> booleano
    caso todas as parcelas sem minas estiverem limpas, devolve True; se nao devolve False
    '''
    if not eh_campo(m):
        return False
    for linha in m:
        for parcela in linha:
            if parcela[1][1] == 'sem mina' and not eh_parcela_limpa(parcela[1]):
                return False
    return True

def turno_jogador(m):
    '''
    campo -> booleano
    altera destrutivamente o campo, atraves de duas acoes, 'Limpar' e 'Marcar', numa coordenada (ambos escolhidos pelo utilizador)
    caso o utilizador tiver escolhido 'Limpar' num parcela minada devolve False; se nao devolve True
    '''
    if not eh_campo(m):
        return False
    
    while True:
        acao = input('Escolha uma ação, [L]impar ou [M]arcar:')
        try:
            if acao in ('L', 'M'):
                break
        except:
            continue
    
    while True:
        coord_str = input('Escolha uma coordenada:')
        try:
            c = str_para_coordenada(coord_str)
            if eh_coordenada_do_campo(m, c):
                break
        except:
            continue
    
    parcela = obtem_parcela(m, c)
    
    if acao == 'L':
        if eh_parcela_marcada(parcela):
            return True
        limpa_campo(m, c)
        return not eh_parcela_minada(parcela)
    else:
        alterna_bandeira(parcela)
        return True
            
def minas(c, l, n, d, s):
    '''
    str x int x int x int x int -> booleano
    utiliza-se c e l para criar um campo, n para colocar minas, d e s para um gerador
    c, ultima coluna
    l, ultima linha
    n, numero de minas
    d, tamanho do gerador
    d, estado inicial do gerador
    devolve True se o jogador ganhar; se nao devolve False
    '''
    # Validação de argumentos
    if not (isinstance(c, str) and len(c) == 1 and 'A' <= c <= 'Z' and
                isinstance(l, int) and 1 <= l <= 99 and
                isinstance(n, int) and n > 0 and
                isinstance(d, int) and d in (32, 64) and
                isinstance(s, int) and 1 <= s <= 2**d and n <= (ord(c)-ord('A')+1)*l - 9):
        raise ValueError("minas: argumentos invalidos")

    campo = cria_campo(c, l)
    marcacoes = 0 # numero de bandeiras
    print('   [Bandeiras ' + str(marcacoes) + '/6]')
    print(campo_para_str(campo))
    gerador = cria_gerador(d, s)
    coord_i = str_para_coordenada(input('Escolha uma coordenada:'))
    coloca_minas(campo, coord_i, gerador, n)
    limpa_campo(campo, coord_i)
    print('   [Bandeiras ' + str(marcacoes) + '/6]')
    print(campo_para_str(campo))
    while jogo_ganho == False:
        marcacoes = 0
        for i in campo:
            for j in i:
                if j[0] == 'X':
                    print('BOOOOOOOM!!!')
                    return False
                elif j[0] == '@':
                    marcacoes += 1
        turno_jogador(campo)
        print('   [Bandeiras ' + str(marcacoes) + '/6]')
        print(campo_para_str(campo))
    if jogo_ganho(campo):
        print('VITORIA!!!')
        return True