"""
Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, age e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a age da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
"""

class Person:
    def __init__(self, name = '', age = 0, occupation = ''):
        self._name = name
        self._age = age
        self._occupation = occupation

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @property
    def occupation(self):
        return self._occupation

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    @occupation.setter
    def occupation(self, value):
        self._occupation = value
    
person1 = Person("Gal Gadot", 40, "Actress")
print(person1._name)

person1._name = "Henry Cavill"
print(person1._name)