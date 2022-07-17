#from cpf_cnpj import Documento
#from validate_docbr import CNPJ
#from TelefonesBr import TelefonesBr
#from datetime import datetime, timedelta
#from datas_br import DatasBr

import requests

from acesso_cep import BuscaEndereco
cep = "25800320"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)