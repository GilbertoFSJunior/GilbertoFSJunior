#Bibliotecas necessárias

from tkinter import *
from tkinter import ttk

#variáveis
#Cores utilizadas
cor1 = "#3b3b3b" #Preta
cor2 = "#feffff" #branca
cor3 = "#38576b" #Azul
cor4 = "#ECEFF1" #Cinza
cor5 = "#FFAB40" #Laranja


#Criação da Janela

janela = Tk()
janela.title("Calc Gjr_Dev")

#Configuração da janela

janela.geometry("235x310") #Tamanho da janela
janela.config(bg=cor1)
#frame da tela da calculadora
frame_display = Frame(janela, width=235, height=50, bg=cor3)
frame_display.grid(row=0, column=0)
#frame do teclado da calculadora
frame_teclado = Frame(janela, width=235, height=268)
frame_teclado.grid(row=1, column=0)

#variavel todos valores (armazenar valores)
todos_valores = ''

#criando Labels
valor_texto = StringVar()

#função
def entrar_valores(event):

    global todos_valores
    todos_valores=todos_valores + str(event)
    

    #passando valor para a tela
    valor_texto.set(todos_valores)

#função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#função Limpa tela

def limpa_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")

    




app_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7,
                  relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2 )
app_label.place(x=0, y=0)

#criando botões Primeira linha
#clear
b_1 = Button(frame_teclado, command=limpa_tela, text= "C", width=11, height=2, bg=cor4, fg=cor1,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
#Percentual
b_2 = Button(frame_teclado, text= "%", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('%'))
b_2.place(x=118, y=0)
#Divisão
b_3 = Button(frame_teclado, text= "/", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('/'))
b_3.place(x=177, y=0)
#criando botões Segunda linha
#Botão 7
b_4 = Button(frame_teclado, text= "7", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('7'))
b_4.place(x=0, y=52)
#Botão 8
b_5 = Button(frame_teclado, text= "8", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('8'))
b_5.place(x=59, y=52)
#Botão 9
b_6 = Button(frame_teclado, text= "9", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('9'))
b_6.place(x=118, y=52)
#Multiplicação
b_7 = Button(frame_teclado, text= "*", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('*'))
b_7.place(x=177, y=52)
#criando botões Terceira linha
#Botão 4
b_8 = Button(frame_teclado, text= "4", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('4'))
b_8.place(x=0, y=104)
#Botão 5
b_9 = Button(frame_teclado, text= "5", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('5'))
b_9.place(x=59, y=104)
#Botão 
b_10 = Button(frame_teclado, text= "6", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('6'))
b_10.place(x=118, y=104)
#Subtração
b_11 = Button(frame_teclado, text= "-", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('-'))
b_11.place(x=177, y=104)
#criando botões Quarta linha
#Botão 4
b_12 = Button(frame_teclado, text= "1", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('1'))
b_12.place(x=0, y=156)
#Botão 5
b_13 = Button(frame_teclado, text= "2", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('2'))
b_13.place(x=59, y=156)
#Botão 
b_14 = Button(frame_teclado, text= "3", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('3'))
b_14.place(x=118, y=156)
#Subtração
b_15 = Button(frame_teclado, text= "+", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('+'))
b_15.place(x=177, y=156)
#criando botões Quinta linha
#zero
b_16 = Button(frame_teclado, text= "0", width=11, height=2, bg=cor4, fg=cor1,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('0'))
b_16.place(x=0, y=208)
#Ponto
b_17 = Button(frame_teclado, text= ".", width=5, height=2, bg=cor4, fg=cor1,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=  lambda: entrar_valores('.'))
b_17.place(x=118, y=208)
#Igual(executa)
b_18 = Button(frame_teclado, command=calcular, text= "=", width=5, height=2, bg=cor5, fg=cor2,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)





janela.mainloop()

