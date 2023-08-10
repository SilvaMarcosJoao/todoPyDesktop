from modulos import *
import eventos

class appTodo(eventos.Eventos):
    def __init__(self) -> None:
        self.apptodo = CTk()
        self.configTelaTodo()
        self.frameTodo()
        self.widgetsTodo()
        self.apptodo.mainloop()
        

    def configTelaTodo(self) -> None:
        self.apptodo.title('TaskPy')
        self.apptodo.configure(bg='#fff')
        self.largTela = 780
        self.altTela = 560
        self.largMonitor = self.apptodo.winfo_screenwidth()
        self.altMonitor = self.apptodo.winfo_screenheight()
        self.posX = (self.largMonitor / 2) - (self.largTela / 2)
        self.posY = (self.altMonitor / 2) - (self.altTela / 2)
        self.apptodo.geometry("%dx%d+%d+%d" % (self.largTela, self.altTela, self.posX, self.posY))
        self.apptodo.minsize(width=780, height=560)
        self.apptodo.resizable(False, False)

    def frameTodo(self) -> None:
        self.todoFrame = CTkFrame(self.apptodo, width=760, height=540, fg_color='#e4ebf0')
        self.todoFrame.place(relx=0.01, rely=0.01)

    def widgetsTodo(self) -> None:

        self.tituloTodo = CTkLabel(self.apptodo, 
                text='TasksPy', 
                font=('Ebrima', 28, 'bold'), 
                fg_color='#e4ebf0',
                bg_color='#34344e')
        self.tituloTodo.place(relx=0.43, rely=0.02)

        self.lblnomeTarefa = CTkLabel(self.apptodo, 
                text='Nome da tarefa: ', 
                font=('Ebrima', 16), 
                fg_color='#e4ebf0')
        self.lblnomeTarefa.place(relx=0.02, rely=0.08)
        self.et_nomeTarefa = CTkEntry(self.apptodo, 
                font=('Ebrima', 16),
                width=180, height=30, 
                placeholder_text='Tarefa', 
                border_width=2, 
                border_color="#34344e")
        self.et_nomeTarefa.place(relx=0.02, rely=0.13)

        self.lblDescricao = CTkLabel(self.apptodo, 
                text='Descrição: ', 
                font=('Ebrima', 16), 
                fg_color='#e4ebf0')
        self.lblDescricao.place(relx=0.02, rely=0.19)
        self.textBoxDescricao = CTkTextbox(self.apptodo,
                font=('Ebrima', 16), 
                border_width=2, 
                border_color="#34344e", 
                width=180, height=160, 
                activate_scrollbars='True')
        self.textBoxDescricao.place(relx=0.02, rely=0.24)


        self.obtStatus = StringVar()
        self.obtStatus.set('')
        self.lblStatus = CTkLabel(self.apptodo, 
                text='Status: ', 
                font=('Ebrima', 16), 
                fg_color='#e4ebf0')
        self.lblStatus.place(relx=0.02, rely=0.54)
        self.cbxStatus = CTkComboBox(self.apptodo, 
                variable=self.obtStatus,
                values=['Em aberto', 'Concluída'],  
                dropdown_fg_color='#fff',  
                border_width=2, 
                border_color='#34344e', 
                button_color='#34344e', 
                button_hover_color= '#386dbd', 
                width=180, height=30)
        self.cbxStatus.place(relx=0.02, rely=0.59)
        

        self.dataTarefa = CTkLabel(self.apptodo, 
                text='Data: ', 
                font=('Ebrima', 16), 
                fg_color='#e4ebf0')
        self.dataTarefa.place(relx=0.02, rely=0.65)
        self.et_dataTarefa = CTkEntry(self.apptodo,
                font=('Ebrima', 16),
                width=100, height=30, 
                border_width=2, 
                border_color="#34344e", 
                placeholder_text='dd/mm/yyyy')
        self.et_dataTarefa.place(relx=0.02, rely=0.7)

        self.imgBtnCal = CTkImage(dark_image=Image.open('.\imagens\\calendar.png'), size=(20,22))
        self.btnAddCalen = CTkButton(self.apptodo, 
                text='', 
                image=self.imgBtnCal, 
                fg_color='#34344e', 
                width=40, height=30, 
                command=self.aparenciaCalendario)
        self.btnAddCalen.place(relx=0.153, rely=0.7)

        self.btnAddTarefa = CTkButton(self.apptodo, 
                text='ADICIONAR', 
                font=('Ebrima', 16, 'bold'), 
                fg_color='#34344e', 
                hover_color='#386dbd', 
                width=180, height=30,
                command=self.cadastroTarefa)
        self.btnAddTarefa.place(relx=0.02, rely=0.77)

        self.btnFinTarefa = CTkButton(self.apptodo, 
                text='FINALIZAR', 
                font=('Ebrima', 16, 'bold'), 
                fg_color='#34344e', 
                hover_color='#386dbd', 
                width=180, height=30)
        self.btnFinTarefa.place(relx=0.02, rely=0.84)

        self.btnExclTarefa = CTkButton(self.apptodo, 
                text='EXCLUIR', 
                font=('Ebrima', 16, 'bold'), 
                fg_color='#34344e', 
                hover_color='#386dbd', 
                width=180, height=30)
        self.btnExclTarefa.place(relx=0.02, rely=0.91)

        self.lblbuscaTarefa = CTkLabel(self.apptodo, 
                text='Buscar Tarefa: ', 
                font=('Ebrima', 16), 
                fg_color='#e4ebf0')
        self.lblbuscaTarefa.place(relx=0.665, rely=0.08)
        self.et_buscaTarefa = CTkEntry(self.apptodo, 
                font=('Ebrima', 16),
                width=180, height=30, 
                placeholder_text='Buscar', 
                border_width=2, 
                border_color="#34344e",)
        self.et_buscaTarefa.place(relx=0.665, rely=0.13)

        self.imgBtnBusc = CTkImage(dark_image=Image.open('.\imagens\\search.png'), size=(20,22))
        self.btnbuscTarefa = CTkButton(self.apptodo, 
                text='', 
                image=self.imgBtnBusc, 
                fg_color='#34344e', 
                hover_color='#386dbd', 
                width=50, height=30)
        self.btnbuscTarefa.place(relx=0.9, rely=0.13)

        self.lblbuscaStatus = CTkLabel(self.apptodo, 
                text='Filtrar por Status: ', 
                font=('Ebrima', 16), 
                fg_color='#e4ebf0')
        self.lblbuscaStatus.place(relx=0.665, rely=0.2)

        self.radio_var = IntVar()

        self.concStatus = CTkRadioButton(self.apptodo, 
                text='Concluída', 
                value=1, 
                variable=self.radio_var, 
                command=self.radioToggle, 
                bg_color='#e4ebf0',
                border_color='#34344e')
        self.concStatus.place(relx=0.665, rely=0.25)
        self.embStatus = CTkRadioButton(self.apptodo, 
                text='Em aberto', 
                value=2, 
                variable=self.radio_var, 
                command=self.radioToggle, 
                bg_color='#e4ebf0')
        self.embStatus.place(relx=0.8, rely=0.25)

        self.btnVerTarefas = CTkButton(self.apptodo, 
                text='VER TODAS', 
                font=('Ebrima', 16, 'bold'), 
                fg_color='#34344e', 
                hover_color='#386dbd', 
                width=180, height=30,
                command=self.exibirTarefas)
        self.btnVerTarefas.place(relx=0.73, rely=0.32)

        self.listaTarefa = ttk.Treeview(self.apptodo, 
                height=4, 
                columns=('Col1', 'Col2', 'Col3', 'Col4'), 
                show='headings')

        self.listaTarefa.heading('#0', text='')
        self.listaTarefa.heading('#1', text='Tarefa')
        self.listaTarefa.heading('#2', text='Descrição')
        self.listaTarefa.heading('#3', text='Data Criação')
        self.listaTarefa.heading('#4', text='Status')

        self.listaTarefa.column('#1', width=100, anchor='center')
        self.listaTarefa.column('#2', width=240, anchor='center')
        self.listaTarefa.column('#3', width=80, anchor='center')
        self.listaTarefa.column('#4', width=100, anchor='center')

        self.listaTarefa.place(relx=0.28, rely=0.41, relwidth=0.68, relheight=0.56)

        self.scrollTarefa = CTkScrollbar(self.apptodo,  
                button_color='#34344e', 
                button_hover_color='#386dbd', 
                orientation='vertical', 
                command=self.listaTarefa.yview)
        self.scrollTarefa.place(relx=0.96, rely=0.41, relheight=0.56)


    def aparenciaCalendario(self):
        self.calendarioTarefa = Calendar(self.apptodo, 
                fg_color='#34344e', 
                font=('Ebrima', 12), 
                locale='pt_br')
        self.calendarioTarefa.place(relx=0.28, rely=0.2, width=250, height=200)

        self.confirmData = CTkButton(self.apptodo, 
                text='Confirmar',
                font=('Ebrima', 14, 'bold'),
                text_color='#fff',
                fg_color='#34344e',
                hover_color='#386dbd',
                height=20,
                command=self.eventCalendario)
        self.confirmData.place(relx=0.28, rely=0.13)
        

appTodo()
