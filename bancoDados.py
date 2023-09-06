import modulos

class Banco:
    
    def __init__(self) -> None:
        self.conexao = None
        
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