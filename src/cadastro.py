import re 
from .cliente import Cliente

class CadastroCliente():
    def __init__(self) -> None:
        self.clientes_cadastrados = [] 
        
    @staticmethod
    def cadastrar_cliente(cliente):
        if isinstance(cliente, Cliente) and re.fullmatch(r'[a-zA-Z]{3,}', cliente.nome):
            return "Cadastrado com sucesso"
        return "Não foi possível cadastrar"
