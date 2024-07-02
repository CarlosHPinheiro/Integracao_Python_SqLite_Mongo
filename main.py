from sql_alchemy_app import (session,
                             Cliente,
                             Conta,)

from mongo_app import (criar_documentos,
                       buscar_doc)

# Inserindo os dados nas tabelas no SQLite
nv_cliente_1 = Cliente(nome='Ana Beatriz', cpf='112233445', endereco='Rua dos Aymorés - 355, São Paulo - SP ')
nv_cliente_2 = Cliente(nome='Eduardo Ferreira', cpf='223344556', endereco='Rua Cinco - 55, Santa Bárbara - SP')
nv_cliente_3 = Cliente(nome='Roberto Santos', cpf='334455667', endereco='Rua São João - 601, Timões - BA')

nv_conta_cliente_1 = Conta(tipo='conta corrente', agencia='0001', num='001', id_cliente=1, saldo=200.00)
nv_conta_cliente_2 = Conta(tipo='conta corrente', agencia='0001', num='002', id_cliente=2, saldo=2000.00)
nv_conta_cliente_3 = Conta(tipo='conta corrente', agencia='0001', num='003', id_cliente=3, saldo=3500.00)

session.add(nv_cliente_1)
session.add(nv_cliente_2)
session.add(nv_cliente_3)
session.add(nv_conta_cliente_1)
session.add(nv_conta_cliente_2)
session.add(nv_conta_cliente_3)

# Commit das alterações
session.commit()

# Criando os documentos no MongoDB
criar_documentos()

# Consultar Documento
document = buscar_doc('Nome', 'Eduardo Ferreira')
print(document)
