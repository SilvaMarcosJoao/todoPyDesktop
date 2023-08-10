import bancoDados


class Tarefa:
    banco = bancoDados.Banco()
    def __init__(self) -> None:
        self.nomeTarefa = None
        self.descTarefa = None
        self.statusTarefa = None
        self.dataTarefa = None

    def get_nomeTarefa(self) -> str:
        return self.nomeTarefa

    def set_nomeTarefa(self, nome:str) -> None:
        self.nomeTarefa = nome

    def get_descTarefa(self) -> str:
        return self.descTarefa

    def set_descTarefa(self, desc:str) -> None:
        self.descTarefa = desc
    
    def get_statusTarefa(self) -> str:
        return self.statusTarefa

    def set_statusTarefa(self, status:str) -> None:
        self.statusTarefa = status

    def get_dataTarefa(self) -> str:
        return self.dataTarefa

    def set_dataTarefa(self, data: str) -> None:
        self.dataTarefa = data

    def inserirTarefa(self, nomeTarefa:str, descTarefa:str, statusTarefa:str, dataTarefa:str) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO tarefas (nome_tarefa, descricao_tarefa, status_tarefa, data_tarefa)
                            VALUES ('{nomeTarefa}', '{descTarefa}', '{statusTarefa}', '{dataTarefa}') """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    def listarTarefas(self) -> list:
        self.banco.conectar()
        self.banco.cursor.execute('SELECT nome_tarefa, descricao_tarefa, data_tarefa, status_tarefa from tarefas')
        self.listaTaf =  self.banco.cursor.fetchall()
        return self.listaTaf