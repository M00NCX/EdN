def palindromo(texto: str) -> str:
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

print(palindromo("ame a ema"))