# Implementação simples de RSA em Python

Este repositório contém uma implementação didática do algoritmo RSA em Python, focada em demonstrar os conceitos fundamentais de criptografia de chave pública de forma simples e direta.

> **Aviso:** Este código é apenas para fins de estudo e experimentação. 

#

## Funcionalidades

O arquivo `rsa.py` inclui:

- Verificação de número primo (`primo`)
- Cálculo do máximo divisor comum estendido (`mdc_extendido`)
- Cálculo de inverso modular (`inverso_modular`)
- Geração de par de chaves RSA (`gerar_chaves`)
- Codificação de mensagens com a chave pública (`codificar_rsa`)
- Decodificação de mensagens com a chave privada (`decodificar_rsa`)

A geração de chaves utiliza primos derivados de uma semente baseada no tempo de execução, garantindo pares de chaves diferentes a cada execução, mas ainda assim com foco didático, não em segurança real.

#

## Pré-requisitos

- Python 3.x instalado na máquina

Não é necessária nenhuma biblioteca externa: o código usa apenas a biblioteca padrão do Python.

#

## Como usar

1. Clone este repositório ou baixe o arquivo `rsa.py`.
2. Importe as funções no seu script Python ou use diretamente em um console interativo.

### Exemplo básico de uso

```python
from rsa import gerar_chaves, codificar_rsa, decodificar_rsa

# 1. Gerar chaves
chave_publica, chave_privada = gerar_chaves()
print("Chave pública:", chave_publica)
print("Chave privada:", chave_privada)

# 2. Mensagem original
mensagem = "Hello RSA"

# 3. Codificar com a chave pública
mensagem_codificada = codificar_rsa(mensagem, chave_publica)
print("Mensagem codificada:", mensagem_codificada)

# 4. Decodificar com a chave privada
mensagem_decodificada = decodificar_rsa(mensagem_codificada, chave_privada)
print("Mensagem decodificada:", mensagem_decodificada)
```

#

## Estrutura das funções

- `primo(n)`: retorna `True` se `n` for primo, caso contrário `False`.
- `mdc_extendido(a, b)`: implementa o algoritmo de Euclides estendido, retornando o MDC e os coeficientes da combinação linear.
- `inverso_modular(e, phi)`: calcula o inverso modular de `e` em relação a `phi`, usado no cálculo da chave privada.
- `gerar_chaves()`: gera um par de chaves `(e, n)` (pública) e `(d, n)` (privada), usando primos simples para fins didáticos.
- `codificar_rsa(mensagem, chave_publica)`: recebe uma string e devolve uma lista de inteiros representando a mensagem cifrada.
- `decodificar_rsa(mensagem_codificada, chave_privada)`: recebe a lista de inteiros cifrados e devolve a string original.

#

## Limitações (importante)

- Os valores de `p` e `q` são relativamente pequenos, o que torna o sistema inseguro para uso real.
- A geração de primos é simplificada e não segue os padrões de segurança utilizados em bibliotecas criptográficas profissionais.
- Não há tratamento de mensagens muito longas, padding seguro ou outros mecanismos necessários em implementações reais de RSA.

Este projeto deve ser usado como base de estudo para entender:
- Como o RSA é construído matematicamente
- Como a chave pública e privada se relacionam
- Como ocorre o processo de codificação e decodificação com expoentes e módulo
