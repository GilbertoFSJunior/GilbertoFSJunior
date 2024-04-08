import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread

class LembreteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lembretes Diários")

        self.lembretes = []

        self.criar_interface()
        self.atualizar_lembretes()

    def criar_interface(self):
        self.label_descricao = tk.Label(self.root, text="Descrição:")
        self.label_descricao.pack(pady=5)

        self.entry_descricao = tk.Entry(self.root, width=30)
        self.entry_descricao.pack(pady=5)

        self.label_inicio = tk.Label(self.root, text="Horário de Início (HH:MM):")
        self.label_inicio.pack(pady=5)

        self.entry_inicio = tk.Entry(self.root, width=10)
        self.entry_inicio.pack(pady=5)

        self.label_fim = tk.Label(self.root, text="Horário de Fim (HH:MM):")
        self.label_fim.pack(pady=5)

        self.entry_fim = tk.Entry(self.root, width=10)
        self.entry_fim.pack(pady=5)

        self.botao_adicionar = tk.Button(self.root, text="Adicionar Lembrete", command=self.adicionar_lembrete)
        self.botao_adicionar.pack(pady=10)

    def adicionar_lembrete(self):
        descricao = self.entry_descricao.get()
        inicio = self.entry_inicio.get()
        fim = self.entry_fim.get()

        if descricao and inicio and fim:
            horario_inicio = self.converter_horario_para_segundos(inicio)
            horario_fim = self.converter_horario_para_segundos(fim)

            if horario_inicio is not None and horario_fim is not None:
                self.lembretes.append((descricao, horario_inicio, horario_fim))
                self.limpar_campos()
                self.atualizar_lembretes()

    def verificar_lembretes(self):
        while True:
            for lembrete in self.lembretes:
                descricao, horario_inicio, horario_fim = lembrete
                horario_atual = time.localtime().tm_sec + 60 * time.localtime().tm_min + 3600 * time.localtime().tm_hour

                if horario_inicio <= horario_atual <= horario_fim:
                    messagebox.showinfo("Lembrete", f"{descricao} - Agora é o horário de realizar a tarefa!")
                    self.lembretes.remove(lembrete)
                    self.atualizar




