class Cliente:
    def __init__(self, nome: str, idade: int, email: str) -> None:
        self._nome = nome
        self._idade = idade
        self._email = email
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self._nome = novo_nome
            
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 18:
            self._idade = nova_idade
            
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        if isinstance(novo_email, str) and re.fullmatch(r'^[\w\W]+@[\w]+\.[\w]+$', novo_email):
            self._email = novo_email
            
    def enviar_email(self):
        pass
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}'
    
    
