# verifica se um número é primo
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# calcula o máximo divisor comum estendido
def mdc_extendido(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = mdc_extendido(b % a, a)
    return g, x - (b // a) * y, y

# calcula o inverso modular de e módulo phi
def inverso_modular(e, phi):
    g, x, _ = mdc_extendido(e, phi)
    if g != 1:
        raise Exception("não existe inverso modular")
    return x % phi

# gera chaves rsa com primos diferentes a cada execução
def gerar_chaves():
    from time import time
    semente = int(str(time()).replace('.', '')[-6:])
    p = 61 + (semente % 100)
    while not primo(p):
        p += 1

    q = 53 + ((semente * 2) % 100)
    while not primo(q) or q == p:
        q += 1

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverso_modular(e, phi)
    return (e, n), (d, n)

# codifica uma mensagem com a chave pública
def codificar_rsa(mensagem, chave_publica):
    e, n = chave_publica
    return [pow(ord(c), e, n) for c in mensagem]

# decodifica uma mensagem com a chave privada
def decodificar_rsa(mensagem_codificada, chave_privada):
    d, n = chave_privada
    return ''.join([chr(pow(c, d, n)) for c in mensagem_codificada])
