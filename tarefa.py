import bancoDados


class Tarefa:
    banco = bancoDados.Banco()
    banco.tabelaTarefa()
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
        """
        Realiza a inserção de uma tarefa no sistema.
        :param: nomeTarefa(Título da tarefa), descTarefa(Descreve a tarefa), statusTarefa(Concluída ou Em aberto), dataTarefa(Data de crição da tarefa).
        :return: Não há retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO tarefas (nome_tarefa, descricao_tarefa, status_tarefa, data_tarefa)
                            VALUES ('{nomeTarefa}', '{descTarefa}', '{statusTarefa}', '{dataTarefa}') """)
        self.banco.conexao.commit()
        self.banco.desconectar()


    def listarTarefas(self) -> list:
        """
        Listagem com todas as tarefas cadastradas.
        :return: Retorna uma lista com as tarefas.
        """
        self.banco.conectar()
        self.banco.cursor.execute("""SELECT cod_tarefa, nome_tarefa, descricao_tarefa, to_char(data_tarefa, 'DD/MM/YYYY'), status_tarefa FROM tarefas 
                                  ORDER BY cod_tarefa""")
        self.listaTaf =  self.banco.cursor.fetchall()
        self.banco.desconectar()
        return self.listaTaf
    

    def listarPorStatus(self, status: str) -> list:
        """
        Listagem das tarefas cadastradas, de acordo com o status selecionado.
        :param: status(Concluída ou Em aberto).
        :return: Retorna uma lista com as tarefas.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f"""SELECT cod_tarefa, nome_tarefa, descricao_tarefa, to_char(data_tarefa, 'DD/MM/YYYY'), status_tarefa FROM tarefas 
                                  WHERE status_tarefa = '{status}'
                                  ORDER BY cod_tarefa """)
        self.listaTafStatus = self.banco.cursor.fetchall()
        self.banco.desconectar()
        return self.listaTafStatus
    

    def listarTarefa(self, nomeTarefa:str) -> list:
        """
        Busca a tarefa solicitada pelo usuário.
        :param: nomeTarefa(Título da tarefa).
        :return: Retorna uma lista com a tarefa solicitada.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" SELECT cod_tarefa, nome_tarefa, descricao_tarefa, to_char(data_tarefa, 'DD/MM/YYYY'), status_tarefa FROM tarefas 
                                  WHERE nome_tarefa like '{nomeTarefa[0]}%' 
                                  ORDER BY cod_tarefa""")
        self.tarefa = self.banco.cursor.fetchall()
        self.banco.desconectar()
        return self.tarefa
    

    def finalizarTarefa(self, cod_tarefa:int) -> None:
        """
        Altera o status de uma tarefa para Concluída.
        :param: cod_tarefa(identificador único de cada tarefa).
        :return: Não há retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" UPDATE tarefas
                                SET status_tarefa = 'Concluída'
                                WHERE cod_tarefa = '{cod_tarefa}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()
    

    def excluirTarefa(self, cod_tarefa:int) -> None:
        """
        Exclui uma tarefa selecionada pelo usuário.
        :param: cod_tarefa(identificador único de cada tarefa).
        :return: Não há retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" DELETE FROM tarefas WHERE cod_tarefa = {cod_tarefa}""")
        self.banco.conexao.commit()
        self.banco.desconectar()