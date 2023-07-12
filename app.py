# -*- coding: UTF-8 -*-

import customtkinter as ctk
from math import sqrt, pow

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.exp = ''
        
        self.title('Calculadora LuDani')
        self.resizable(False,False)   
        f = ('Trebuchet MS',18,'bold') 

        self.letreiro = ctk.CTkLabel(master=self,text='Calculadora LuDani',font=f)

        # Letreiro valor
        self.lb_valor = ctk.CTkLabel(master=self,text='',font=f,width=215,height=50,fg_color='#3B3B3B',corner_radius=8, anchor='e')

        # Bot�es
        self.bt_0 = ctk.CTkButton(master=self,text='0',command=lambda: press(0),width=50,height=50,font=f)
        self.bt_1 = ctk.CTkButton(master=self,text='1',command=lambda: press(1),width=50,height=50,font=f)
        self.bt_2 = ctk.CTkButton(master=self,text='2',command=lambda: press(2),width=50,height=50,font=f)
        self.bt_3 = ctk.CTkButton(master=self,text='3',command=lambda: press(3),width=50,height=50,font=f)
        self.bt_4 = ctk.CTkButton(master=self,text='4',command=lambda: press(4),width=50,height=50,font=f)
        self.bt_5 = ctk.CTkButton(master=self,text='5',command=lambda: press(5),width=50,height=50,font=f)
        self.bt_6 = ctk.CTkButton(master=self,text='6',command=lambda: press(6),width=50,height=50,font=f)
        self.bt_7 = ctk.CTkButton(master=self,text='7',command=lambda: press(7),width=50,height=50,font=f)
        self.bt_8 = ctk.CTkButton(master=self,text='8',command=lambda: press(8),width=50,height=50,font=f)
        self.bt_9 = ctk.CTkButton(master=self,text='9',command=lambda: press(9),width=50,height=50,font=f)
        
        # Operadores
        self.bt_divisao = ctk.CTkButton(master=self,text='/',command=lambda: press(' / '),width=50,height=50,font=f)
        self.bt_multiplicacao = ctk.CTkButton(master=self,text='x',command=lambda: press(' * '),width=50,height=50,font=f)
        self.bt_soma = ctk.CTkButton(master=self,text='+',command=lambda: press(' + '),width=50,height=50,font=f)
        self.bt_subtracao = ctk.CTkButton(master=self,text='-',command=lambda: press(' - '),width=50,height=50,font=f)
        self.bt_igual = ctk.CTkButton(master=self,text='=',command=lambda: resultado(),width=215,height=50,font=f)
        self.bt_apagar = ctk.CTkButton(master=self,text='<',command=lambda: apagar(),width=105,height=50,font=f)
        self.bt_ponto = ctk.CTkButton(master=self,text='.',command=lambda: press('.'),width=50,height=50,font=f)
        self.bt_exponencial = ctk.CTkButton(master=self,text='exp',command=lambda: press(' ** '),width=50,height=50,font=f)

        # GRIDs
        self.letreiro.grid(row=0,columnspan=4,padx=2.5,pady=2.5)
        self.lb_valor.grid(row=1,columnspan=4,padx=2.5,pady=2.5)
        self.bt_exponencial.grid(row=2,column=1,padx=2.5,pady=2.5)
        self.bt_apagar.grid(row=2,column=2,columnspan=4,padx=2.5,pady=2.5)
        self.bt_7.grid(row=3,column=0,padx=2.5,pady=2.5)
        self.bt_8.grid(row=3,column=1,padx=2.5,pady=2.5)
        self.bt_9.grid(row=3,column=2,padx=2.5,pady=2.5)
        self.bt_divisao.grid(row=3,column=3,padx=2.5,pady=2.5)
        self.bt_4.grid(row=4,column=0,padx=2.5,pady=2.5)
        self.bt_5.grid(row=4,column=1,padx=2.5,pady=2.5)
        self.bt_6.grid(row=4,column=2,padx=2.5,pady=2.5)
        self.bt_multiplicacao.grid(row=4,column=3,padx=2.5,pady=2.5)
        self.bt_1.grid(row=5,column=0,padx=2.5,pady=2.5)
        self.bt_2.grid(row=5,column=1,padx=2.5,pady=2.5)
        self.bt_3.grid(row=5,column=2,padx=2.5,pady=2.5)
        self.bt_subtracao.grid(row=5,column=3,padx=2.5,pady=2.5)
        self.bt_0.grid(row=6,column=1,padx=2.5,pady=2.5)
        self.bt_ponto.grid(row=6,column=2,padx=2.5,pady=2.5)
        self.bt_soma.grid(row=6,column=3,padx=2.5,pady=2.5)
        self.bt_igual.grid(row=7,columnspan=4,padx=2.5,pady=2.5)
        
        def press(v):
            global exp
            self.exp += str(v)
            #print(self.exp)
            self.lb_valor.configure(text=self.exp)

        def resultado():
            global exp
            try:
                self.lb_valor.configure(text=eval(self.exp))
                self.exp = ""
            except:
                pass


        def apagar():
            global exp
            self.exp = self.exp[:-1]
            self.lb_valor.configure(text=self.exp)
        
        

if __name__ == '__main__':
    App().mainloop()

