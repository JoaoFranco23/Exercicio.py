#importando uma interface tkinter
from tkinter import * 
from tkinter import ttk
from tkinter import Label
from tkinter import Entry
from tkinter import Button

Login = Tk() #Variavel Responsavel por responder a aplicação
Login.title("Login") #Definee o Titulo da Janela
Login.geometry("300x200") #Define o Tamanho da Janela

Label(Login, text="Login", font=("Arial", 20)).pack() 


            
Login.mainloop() #A função é responsavel por iniciar o loop principal da interface gráfica
