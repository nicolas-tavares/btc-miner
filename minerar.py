
# video base para estudo: https://www.youtube.com/watch?v=m3k4kvX6izo
# "python3 minerar.py" - no terminal (Python 3.9.6)

from hashlib import sha256
import time


def aplicar_sha256(texto):                              # sha256 - algoritmo de hash seguro de 256 bits usado para proteção criptográfica
    return sha256( texto.encode("ascii")).hexdigest()   # "encode" - codifica o texto no padrão "ascii" para ser possível fazer o hashing (retorna um objeto), hexdigest = transforma o objeto em uma string normal do python

def minerar_btc(num_bloco, transacoes, hash_anterior, qntd_zeros):
    nonce = 0

    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)

        if meu_hash.startswith("0" * qntd_zeros):
            return nonce, meu_hash
        nonce += 1

if __name__ == "__main__":

    # Exemplos de valores, para minerar verdadeiramente pegar valores reais no website "Blockchain Explorer"

    num_bloco = 15
    transacoes = """
    Nicolas -> Gustavo -> 15
    Gustavo -> Nilson -> 5
    Fulano -> Nicolas -> 12
    """
    qntd_zeros = 7
    hash_anterior = "abc"

    inicio = time.time()

    print("\n Looking for bitcoins . . .\n")
    resultado = minerar_btc(num_bloco, transacoes, hash_anterior, qntd_zeros)
    
    print(resultado)
    print("Finded in: ", time.time() - inicio , "seconds \n" )