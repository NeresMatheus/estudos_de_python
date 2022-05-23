"""
Codigo de estudo
"""

class Pessoa:
    def __init__ (self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
        #É possivel criar vairaveis ou operações dentro do criador e/ou usa-los 
        #Mas assim como em outros casos ela só existe neste escopo. 
        variavel= 'criado'
        print(variavel)
        #Assim é possivel retornar um valor ou estado durante a criação que n esteja necessariamente relaciodado
        #A classe
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return 
            
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    
    
        
        
        
