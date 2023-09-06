from modulos import *
import tarefa

class Eventos:
    objtarefa = tarefa.Tarefa()
    
    def radioToggle(self) -> None:
        """
        Captura a opção selecionada no radio button e chama a função de exibição do status.
        :return: Não há retorno.
        """
        self.radio = self.radio_var.get()
        self.exibirTarefaStatus()


    def eventCalendario(self) -> None:
        """
        Insere no entry, a data selecionada no calendário.
        :return: Não há retorno.
        """
        self.data = self.calendarioTarefa.get_date()
        if len(self.data) == 0 or len(self.data) != 0:
            self.calendarioTarefa.destroy()
        self.et_dataTarefa.delete(0, END)
        self.et_dataTarefa.insert(0, self.data)
        self.confirmData.destroy()


    def cadastroTarefa(self) -> None:
        """
        Captura os dados digitados pelo usuário nos campos de cadastro de uma nova tarefa,
        após, envia esses dados para o método da classe do objeto tarefa.
        :return: Não há retorno.
        """
        try:
            self.tarefa = self.et_nomeTarefa.get()
            self.descricao = self.textBoxDescricao.get(1.0, "end")
            self.status = self.obtStatus.get()
            self.dataTas = self.et_dataTarefa.get()

            if len(self.tarefa) == 0 or len(self.descricao) == 0 or len(self.status) == 0 or len(self.dataTas) == 0:
                messagebox.showwarning('Atenção', 'Por favor, Preencha  os campos de cadastro')
            elif len(self.tarefa) > 40:
                messagebox.showwarning('Atenção', 'Máximo de caracteres permitido é 40')
            elif len(self.descricao) > 200:
                messagebox.showwarning('Atenção', 'Máximo de caracteres permitido é 200')
            else:
               
                self.objtarefa.set_nomeTarefa(self.tarefa)
                self.objtarefa.set_descTarefa(self.descricao)
                self.objtarefa.set_statusTarefa(self.status)
                self.objtarefa.set_dataTarefa(self.dataTas)
                res = self.objtarefa.get_descTarefa()
                self.objtarefa.inserirTarefa(self.objtarefa.get_nomeTarefa(),
                                            self.objtarefa.get_descTarefa(), 
                                            self.objtarefa.get_statusTarefa(),
                                            self.objtarefa.get_dataTarefa())
                
                messagebox.showinfo('Aviso', 'Tarefa cadastrada com sucesso!')
        except Exception (ValueError, SyntaxError, SystemError, ConnectionError) as erro:
            messagebox.showerror('Erro', 'Houve erro, cadastro não finalizado', erro)
        self.limpaCampos()


    def exibirTarefas(self) -> None:
        """
        Recebe a lista de tarefas retornada pelo método de exibição da classe do objeto tarefa
        e exibe na treeview essas tarefas.
        :return: Não há retorno.
        """
        try:
            self.listaTarefa.delete(*self.listaTarefa.get_children())
            self.listaTarefas = self.objtarefa.listarTarefas()
            if len(self.listaTarefas) == 0:
                messagebox.showinfo('Alerta', 'Nenhuma Tarefa Cadastrada')
            else:
                for i in self.listaTarefas:
                    self.listaTarefa.insert('', END, values=i)
        except Exception (ValueError, SyntaxError, SystemError, ConnectionError):
            messagebox.showerror('Sistema', 'Houve um erro na listagem das tarefas')


    def exibirTarefa(self) -> None:
        """
        Recebe a  tarefa retornada pelo método de exibição da classe do objeto tarefa
        e exibe na treeview essa tarefa e suas informações.
        :return: Não há retorno.
        """
        try:
            self.buscar = self.et_buscaTarefa.get()
            self.listaTarefa.delete(*self.listaTarefa.get_children())
            self.tarefas = self.objtarefa.listarTarefa(self.buscar)
            if len(self.tarefas) == 0:
                messagebox.showinfo('Alerta', 'Tarefa Não Encontrada')
            else:
                for t in self.tarefas:
                    self.listaTarefa.insert('', END, values=t)
        except Exception (ValueError, SyntaxError, SystemError, ConnectionError):
            messagebox.showerror('Sistema', 'Houve um erro na Exibição da tarefa buscada')
    

    def exibirTarefaStatus(self) -> None:
        """
        Recebe a lista de tarefas de retornada pelo método de exibição da classe do objeto tarefa
        e exibe na treeview essas tarefas de acordo a opção de status selecionada pelo usuário.
        :return: Não há retorno.
        """
        try:
            self.listaTarefa.delete(*self.listaTarefa.get_children())
            if self.radio_var.get() == 1:
                self.setarStat = 'Concluída'
            elif self.radio_var.get() == 2:
                self.setarStat = 'Em aberto'
            self.listaTarefasStat = self.objtarefa.listarPorStatus(self.setarStat)

            for i in self.listaTarefasStat:
                self.listaTarefa.insert('', END, values=i)
        except Exception (ValueError, SyntaxError, SystemError, ConnectionError):
            messagebox.showerror('Sistema', 'Houve um erro na Exibição das tarefas')

    def encerrarTarefa(self) -> None:
        """
        Atualiza o status de uma tarefa, para concluída.
        :return: Não há retorno.
        """
        try:
            if not self.listaTarefa.selection():
                messagebox.showwarning('Atenção', 'Selecione uma tarefa para finalizá-la')
            else:
                self.selecao = self.listaTarefa.selection()
                self.itSelecionado = list(self.listaTarefa.item(self.selecao, 'values'))
                self.codigoFinal = self.itSelecionado[0]
                self.objtarefa.finalizarTarefa(self.codigoFinal)
                messagebox.showinfo('Sistema', 'Tarefa Finalizada')
        except Exception (ValueError, SyntaxError, SystemError, ConnectionError):
            messagebox.showerror('Sistema', 'Houve um erro ao finalizar a tarefa')

    def deletarTarefa(self) -> None:
        """
        Captura a tarefa selecionada pelo usuário na treeview e envia seu código para
        o método da classe do objeto tarefa que realiza o processo de deleção de uma
        tarefa.
        :return: Não há retorno.
        """
        if not self.listaTarefa.selection():
            messagebox.showwarning('Atenção', 'Selecione uma tarefa para excluí-la')
        else:
            self.selec = self.listaTarefa.selection()
            self.valuesItemSelecionado = list(self.listaTarefa.item(self.selec, 'values'))
            self.codigoTafExc = self.selec[0]

            self.objtarefa.excluirTarefa(self.codigoTafExc)
            messagebox.showinfo('Sistema', 'Tarefa excluída com sucesso!')
    
    
    def limpaCampos(self) -> None:
        """
        Remove os dados digitados nos campos.
        :return: Não há retorno.
        """
        self.et_nomeTarefa.delete(0,END)
        self.textBoxDescricao.delete('0.0', END)
        self.et_dataTarefa.delete(0, END)

    def duplo_clique_tarefa(self, event) -> None:
        """
        """
        self.limpaCampos()
        self.itemSelecionado = self.listaTarefa.selection()
        self.selecionado = list(self.listaTarefa.item(self.itemSelecionado, 'values'))
        self.codigoTaf = self.selecionado[0]
        self.et_nomeTarefa.insert(0, self.selecionado[1])
        self.textBoxDescricao.insert(1.0, self.selecionado[2])
        self.et_dataTarefa.insert(0, self.selecionado[3]) 
        self.obtStatus.set(self.selecionado[4])
        