def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)

def sauda2(nome):
    print("Como vai, " + nome + "?")
    tchau()

def tchau():
    print("preparando para dizer tchau...")
    print("Ok, tchau!")

nome = "Maggie"
sauda(nome)