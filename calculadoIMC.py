#importação 
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores

cor1 = "#282828" #preto/ fundo
cor2 = "#FF9B05" #laranja/ letra
cor3 = "#0459CF" #Azul / botão
cor4 = "#5F5D5D" #cinza escuro /caixa de entrada

#Janela
janela = Tk()
janela.geometry("390x285")
janela.config(background = cor1)
janela.resizable(width=FALSE,   height= FALSE)

#função para calcular

def calcular():

    peso = float (e_peso.get())
    altura = float (e_altura.get())

    imc = peso / altura**2


    if imc <= 18.4:
        l_resultado_texto['text'] = "O seu IMC é : magresa"
    elif imc >=25 and imc <30:
        l_resultado_texto['text'] = "O seu IMC é : sobre peso"
    elif imc >= 30:
        l_resultado_texto['text'] = "O seu IMC é : obesidade"
    else:
        l_resultado_texto['text'] = "O seu IMC é : ideal"
        
    l_resultado['text'] = "{:.{}f}".format(imc, 2)

#frames 

frame_cima =Frame(janela, width=390 , height= 60, bg =cor1, pady= 0, padx= 0, relief='flat' )
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo =Frame(janela, width=390 , height= 225, bg =cor1, pady= 0, padx= 0, relief='flat' )
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#Frame cima config

app_nome = Label(frame_cima, text="CALCULADORA DE IMC", height=1,relief='flat', anchor=CENTER, font=('Ivy 15 bold'), bg=cor1, fg=cor2)
app_nome.place(x=79, y=5)

app_linha = Label(frame_cima, text="",width=400, height=1,relief='flat', anchor=CENTER, font=('Ivy 1'), bg=cor3, fg=cor3)
app_linha.place(x=0, y=35)

#Frame baixo config

l_peso = Label(frame_baixo, text="Qual é o seu peso ?", relief='flat', anchor=CENTER, font=('Ivy 11 bold '), bg=cor1, fg=cor2)
l_peso.grid(row=0, column=0, sticky=NSEW,pady=10,padx=3 )
e_peso = Entry(frame_baixo,width=5, relief='groove',font=('Ivy 11 bold '), justify='center',highlightthickness=1 ,highlightbackground=cor2,highlightcolor=cor4,bg=cor4, fg=cor2)
e_peso.grid(row=0, column=1, sticky=NSEW,pady=10,padx=3 )

l_altura = Label(frame_baixo, text="Qual é a sua altura ?", relief='flat', anchor=CENTER, font=('Ivy 11 bold '), bg=cor1, fg=cor2)
l_altura.grid(row=1, column=0, sticky=NSEW,pady=10,padx=3 )
e_altura = Entry(frame_baixo,width=5, relief='groove',font=('Ivy 11 bold '), justify='center',highlightthickness=1 ,highlightbackground=cor2,highlightcolor=cor4,bg=cor4, fg=cor2)
e_altura.grid(row=1, column=1, sticky=NSEW,pady=10,padx=3 )

l_resultado = Label(frame_baixo, text="---",width=5, height=1, padx=6,pady=12, relief='flat', anchor=CENTER, font=('Ivy 23 bold '), bg=cor3, fg=cor2)
l_resultado.place(x=270, y=10)

l_resultado_texto = Label(frame_baixo, text="",width=28, height=5, padx=0,pady=0, relief='flat', anchor=CENTER, font=('Ivy 10 bold '), bg=cor1, fg=cor2)
l_resultado_texto.place(x=-27, y=85)

b_calcular = Button(frame_baixo,command=calcular, text="Calcular",width=37, height=1, relief='groove',  anchor=CENTER, font=('Ivy 9 bold '), bg=cor3, fg=cor2)
b_calcular.grid(row=4, column=0, sticky=NSEW,pady=60,padx=5,columnspan=3)

janela.mainloop()
