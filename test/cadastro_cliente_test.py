import re 
import sys 
import random
from faker import Faker
sys.path.append('./../')
from Cadastro.src.cadastro import CadastroCliente
from Cadastro.src.cliente import Cliente

faker = Faker()

# Teste unitário
def test_de_cadastro_de_cliente():
    #Arrange
    cliente = Cliente("Allison", 18, "Allison@gamil.com")
    cadastro_cliente = CadastroCliente()
    
    #Act
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    
    #Assert
    assert "Cadastrado com sucesso" == resposta
    print(cliente)