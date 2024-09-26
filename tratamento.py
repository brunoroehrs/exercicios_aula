try:
    x = 10 / 2
    print(x)
except Exception as e: #as E pra usar o e como uma "variavel" para o erro usado anteriormente#
    print(f"erro {e}")
finally:#finally sempre sera executado mesmo com erro#
    print("fim")
else:#só vai executar quando ocorrer sucesso#
    print("sucesso")