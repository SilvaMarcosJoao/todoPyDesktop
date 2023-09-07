import modulos

class Banco:
    
    def __init__(self) -> None:
        self.conexao = None
        
    def tabelaTarefa(self) -> None:
        self.conectar()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS tarefas(
	        cod_tarefa SERIAL PRIMARY KEY,
	        nome_tarefa varchar(40) not null,
	        descricao_tarefa varchar(200) not null,
	        status_tarefa varchar(8) not null,
	        data_tarefa date not null )""")
        self.conexao.commit()
        self.desconectar()

    def conectar(self):
        """
        """
        try:
            self.conexao = modulos.psycopg2.connect(
                database='tarefastodo',
                host='localhost',
                user='postgres',
                password='postgres',
                port='5432'
            )
            self.cursor = self.conexao.cursor()
        except (ConnectionError):
            print('Erro na conexão')
        else:
            return self.conexao

    def desconectar(self) -> None:
        """
        """
        try:
            self.conexao.close()
        except (ConnectionError):
            print('Erro ao tentar desconectar-se')
        else:
            print('Desconectado')

    