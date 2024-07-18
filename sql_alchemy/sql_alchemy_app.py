from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String,
                        DECIMAL,
                        ForeignKey,
                        select)

from sqlalchemy.orm import (sessionmaker,
                            declarative_base)

# Configuração/Conexão
engine = create_engine("sqlite://")
connection = engine.connect()
Base = declarative_base()


# Definição das classes/tabelas
class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(DECIMAL)


# Criação das tabelas no DB
Base.metadata.create_all(engine)

# Criação da sessão
Session = sessionmaker(bind=engine)
session = Session()


def criar_docs():
    docs = []
    stmt_join = select(Cliente.nome, Cliente.cpf, Cliente.endereco, Conta.num, Conta.agencia).join_from(Cliente, Conta)
    results = connection.execute(stmt_join).fetchall()
    for result in results:
        doc = {
            'Nome': result[0],
            'CPF': result[1],
            'Endereço': result[2],
            'CC': result[3],
            'Agência': result[4]
        }

        docs.append(doc)

    return docs


# Fechar a sessão
session.close()
