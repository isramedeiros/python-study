class Livro:
    def __init__(self, titulo = '', autor = '', paginas = 0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        print(f'{self.titulo} por {self.autor} - {self.paginas} paginas')
    
    # getter
    @property
    def titulo_autor(self):
        print(f'{self.titulo} por {self.autor}')
    
    # setter
    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade


livro1 = Livro("1984", "George Orwell", 322)

print(livro1.titulo)
print(livro1.autor)
print(livro1.paginas, "\n")