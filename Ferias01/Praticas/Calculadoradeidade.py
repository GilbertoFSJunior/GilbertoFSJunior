
#bibliotecas para criar a janela
from tkinter import *
from tkinter import ttk

#bibliotecas para criar e usar o calendario
from tkcalendar import Calendar, DateEntry

#bibliotecas para o calculo de datas

from dateutil.relativedelta import relativedelta

#biblioteca datetime
from datetime import date
#_______________________________________Bibliotecas______________________________________

#Criação da Janela

janela = Tk()
janela.title("Calculadora de idade")

#Configuração da janela

janela.geometry("310x400") #Tamanho da janela

#_______________________________________Janela___________________________________________
#cores

cor1="#3b3b3b" #Preto1
cor2="#333333" #Preto2
cor3="#ffffff" #Branca
cor4="#fcc058" #Laranja
cor5="#FFD700" #gold

#_______________________________________Cores_____________________________________________
#criando os frames

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief= FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=260, pady=0, padx=0, relief= FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#______________________________________Frames______________________________________________
#criando as funções de calculo da idade

def calcular():
    inicial=cal1.get()
    termino=cal2.get()

    

#Separando valores e atributos
    mes_1, dia_1, ano_1=[int(f) for f in inicial.split('/')]
    #convertendo em formato date/datetime
    data_inicial=date(ano_1, mes_1, dia_1)

    mes_2, dia_2, ano_2=[int(f) for f in termino.split('/')]
    #convertendo em formato date/datetime
    data_nascimento=date(ano_2, mes_2, dia_2)

    anos=relativedelta(data_inicial, data_nascimento).years
    meses=relativedelta(data_inicial, data_nascimento).months
    dias=relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text']=anos
    l_app_meses['text']=meses
    l_app_dias['text']=dias
    
#______________________________________Funções______________________________________________

#criação das labels do frame_cima

l_calculadora= Label(frame_cima, text="CALCULADORA", width=30, height=1, padx=3, relief=FLAT,
                      anchor= 'center', font=("Ivi 12 bold"), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade= Label(frame_cima, text="DE IDADE", width=15, height=1, padx=0, relief=FLAT,
                      anchor= 'center', font=("Arial 25 bold"), bg=cor2, fg=cor4)
l_idade.place(x=0, y=60)

l_data_inicial= Label(frame_baixo, text="Gjr_Dev", height=1, padx=3, relief=FLAT,
                      anchor= 'nw', font=("Ivi 8 italic"), bg=cor1, fg=cor5)
l_data_inicial.place(x=260, y=240)

#Criação das labels do frame_baixo


l_data_inicial= Label(frame_baixo, text="Data inicial:", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'nw', font=("Ivi 11"), bg=cor1, fg=cor3)
l_data_inicial.place(x=20, y=30)

cal1= DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2024)
cal1.place(x=170, y=30)


l_data_nascimento= Label(frame_baixo, text="Data de Nascimento:", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'nw', font=("Ivi 11"), bg=cor1, fg=cor3)
l_data_nascimento.place(x=20, y=90)

cal2= DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2024)
cal2.place(x=170, y=90)


#Label do resultado
#Anos

l_app_anos= Label(frame_baixo, text="--", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'center', font=("Ivi 25 bold"), bg=cor1, fg=cor3)
l_app_anos.place(x=66, y=135)

l_app_anos_nome= Label(frame_baixo, text="Anos", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'center', font=("Ivi 11 bold"), bg=cor1, fg=cor3)
l_app_anos_nome.place(x=67, y=170)

#Meses
l_app_meses= Label(frame_baixo, text="--", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'center', font=("Ivi 20 bold"), bg=cor1, fg=cor3)
l_app_meses.place(x=126, y=135)

l_app_meses_nome= Label(frame_baixo, text="Meses", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'center', font=("Ivi 11 bold"), bg=cor1, fg=cor3)
l_app_meses_nome.place(x=127, y=170)


#Dias
l_app_dias= Label(frame_baixo, text="--", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'center', font=("Ivi 15 bold"), bg=cor1, fg=cor3)
l_app_dias.place(x=194, y=135)

l_app_dias_nome= Label(frame_baixo, text="Dias", height=1, padx=3, pady=0, relief=FLAT,
                      anchor= 'center', font=("Ivi 11 bold"), bg=cor1, fg=cor3)
l_app_dias_nome.place(x=195, y=170)

#_________________________________________Labels_________________________________________

#criand o botão calcular

b_calcular= Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief='raised',
                      overrelief='ridge', font=("Ivi 10 bold"), bg=cor1, fg=cor3)
b_calcular.place(x=65, y=210)









janela.mainloop()