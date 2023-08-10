from modulos import *
import tarefa

class Eventos:
    objtarefa = tarefa.Tarefa()
    
    def radioToggle(self) -> None:
        self.radio = self.radio_var.get()
        print(self.radio)

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
        except Exception as erro:
            messagebox.showerror('Erro', 'Houve erro, cadastro não finalizado', erro)
        self.limpaCampos()

    def exibirTarefas(self) -> None:
        self.listaTarefa.delete(*self.listaTarefa.get_children())
        self.listaTarefas = self.objtarefa.listarTarefas()

        for i in self.listaTarefas:
            self.listaTarefa.insert('', END, values=i)

    
    
    def limpaCampos(self):
        self.et_nomeTarefa.delete(0,END)
        self.textBoxDescricao.delete('0.0', END)
        self.et_dataTarefa.delete(0, END)
