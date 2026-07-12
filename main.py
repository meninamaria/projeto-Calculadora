from pathlib import Path
from PyQt5 import uic, QtWidgets

buffer = 0
temporary = 0
dis = ""
calc = []

def add():
    global buffer,dis

    # buffer = num1+num2
    # return num1+num2
    dis+='+'
    calculadora.display.setText(dis)

def sub(num1, num2):
    global buffer
    buffer = num1-num2
    return num1-num2

def mult(num1,num2):
    global buffer
    buffer = num1*num2
    return num1*num2

def div(num1,num2):
    global buffer
    buffer = num1/num2
    return num1/num2

def button_clicked(button):
    global buffer,dis,clicks, calc, temporary
    if button=="1":
        calc.append(str(1))
        dis+='1'
        calculadora.display.setText(dis)

    elif button=='2':
        calc.append(str(2))        
        dis+='2'
        calculadora.display.setText(dis)

    elif button=='3':
        calc.append(str(3))        
        dis+='3'
        calculadora.display.setText(dis)

    elif button=='4':
        calc.append(str(4))        
        dis+='4'
        calculadora.display.setText(dis)

    elif button=='5':
        calc.append(str(5))        
        dis+='5'
        calculadora.display.setText(dis)

    elif button=='6':
        calc.append(str(6))
        dis+='6'
        calculadora.display.setText(dis)

    elif button=='7':
        calc.append(str(7))        
        dis+='7'
        calculadora.display.setText(dis)

    elif button=='8':
        calc.append(str(8))        
        dis+='8'
        calculadora.display.setText(dis)

    elif button=='9':
        calc.append(str(9))        
        dis+='9'
        calculadora.display.setText(dis)

    elif button=='0':
        calc.append(str(0))
        dis+='0'
        calculadora.display.setText(dis)

    elif button=='+':
        calc.append(str('+'))        
        dis+='+'
        calculadora.display.setText(dis)

    elif button=='-':
        calc.append(str('-'))
        dis+='-'
        calculadora.display.setText(dis)

    elif button=='*':
        calc.append(str('*'))        
        dis+='×'
        calculadora.display.setText(dis)

    elif button=='/':
        calc.append(str('/'))        
        dis+='÷'
        calculadora.display.setText(dis)  

    elif button=='del':
        buffer = 0
        dis = ''
        calculadora.display.setText(dis)   

    elif button=='x':
        print("APAGAR O ULTIMO ELEMENTO")
        # eu acho que tem ser lista
    else:
        calculadora.display.setText(buffer)   


def verificar_calc():
    global calc
    # aqui é pra verificar se o último elemento é operador ou não
    concat = ''
    for i in range(0, len(calc)): 
        # [1 , 1 , 1 , +]
        if calc[-1]=='+' or calc[-1]=='-' or calc[-1]=='*' or calc[-1]=='/':
            break
        concat += str(calc[i])
    
    number = int(concat)
    temporary = number


app = QtWidgets.QApplication([])

ui_path1 = Path(__file__).with_name("telaCalculadora.ui")
calculadora = uic.loadUi(str(ui_path1))

# botoes das operações
calculadora.button_add.clicked.connect(lambda: button_clicked("+"))
calculadora.button_sub.clicked.connect(lambda: button_clicked("-"))
calculadora.button_mult.clicked.connect(lambda: button_clicked("*"))
calculadora.button_div.clicked.connect(lambda: button_clicked("/"))


# botoes dos numeros
calculadora.button_1.clicked.connect(lambda: button_clicked("1"))
calculadora.button_2.clicked.connect(lambda: button_clicked("2"))
calculadora.button_3.clicked.connect(lambda: button_clicked("3"))
calculadora.button_4.clicked.connect(lambda: button_clicked("4"))
calculadora.button_5.clicked.connect(lambda: button_clicked("5"))
calculadora.button_6.clicked.connect(lambda: button_clicked("6"))
calculadora.button_7.clicked.connect(lambda: button_clicked("7"))
calculadora.button_8.clicked.connect(lambda: button_clicked("8"))
calculadora.button_9.clicked.connect(lambda: button_clicked("9"))
calculadora.button_0.clicked.connect(lambda: button_clicked("0"))

# botoes de execucao
calculadora.button_DEL.clicked.connect(lambda: button_clicked("del"))
calculadora.button_Apagar.clicked.connect(lambda: button_clicked("x"))
calculadora.button_equal.clicked.connect(lambda: button_clicked("="))


calculadora.show()
app.exec()



