import random
import string
def senhaAleatoria(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

print(senhaAleatoria(24))