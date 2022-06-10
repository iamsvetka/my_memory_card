from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from PyQt5.QtGui import QFont

class Question():
    def __init__(self, question, right_answer, wrohg1, wrohg2, wrohg3):
        self.question = question
        self.right_answer = right_answer
        self.wrohg1 = wrohg1
        self.wrohg2 = wrohg2
        self.wrohg3 = wrohg3
        
def show_result():
    GB_answer.hide()
    GB_result.show()
    button.setText('Следующий вопрос')

def show_question():
    GB_answer.show()
    GB_result.hide()
    button.setText('Ответить')
    Gbuttons.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    Gbuttons.setExclusive(True)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrohg1)
    answers[2].setText(q.wrohg2)
    answers[3].setText(q.wrohg3)

    question.setText(q.question)
    txt2.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked:
            show_correct('Неверно!')

def show_correct(res):
    txt1.setText(res)
    show_result()

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)

app = QApplication([])
main_win = QWidget()
main_win.setFont(QFont('Arial', 20))
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(500, 450)
question = QLabel('В каком году канал получил золотую кнопку от YouTobe?')

GB_answer = QGroupBox('Варианты')

rbtn_1 = QRadioButton('2005')
rbtn_2 = QRadioButton('2010')
rbtn_3 = QRadioButton('2015')
rbtn_4 = QRadioButton('2020')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

Gbuttons = QButtonGroup()
Gbuttons.addButton(rbtn_1)
Gbuttons.addButton(rbtn_2)
Gbuttons.addButton(rbtn_3)
Gbuttons.addButton(rbtn_4)

V_line1 = QVBoxLayout()
V_line2 = QVBoxLayout()

H_line_GB = QHBoxLayout()

V_line1.addWidget(rbtn_1)
V_line1.addWidget(rbtn_2)

V_line2.addWidget(rbtn_3)
V_line2.addWidget(rbtn_4)

H_line_GB.addLayout(V_line1)
H_line_GB.addLayout(V_line2)

GB_answer.setLayout(H_line_GB)

layout_main = QVBoxLayout()

layout_main.addWidget(question, alignment = Qt.AlignCenter)

GB_result = QGroupBox('Результат теста')
#GB_result.hide()

v_line_gbresult = QVBoxLayout()
txt1 = QLabel('Правильно/Неправильно')
txt2 = QLabel('Правильный вариант будет тут')
  
v_line_gbresult.addWidget(txt1)
v_line_gbresult.addWidget(txt2)

GB_result.setLayout(v_line_gbresult)



button = QPushButton('ответить')

layout_main.addWidget(GB_answer)
layout_main.addWidget(GB_result)
layout_main.addWidget(button)

main_win.setLayout(layout_main)

question_list = []
question_list.append(Question('Сколько будет 2 * 2?','4','5','6','7'))

question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Русский', 'Английский', 'Итальянский'))

question_list.append(Question('В каком месяце 28 дней?', 'во всех', 'в феврале', 'в марте', 'что?'))

question_list.append(Question('Кто из президентов США написал свой собственный рассказ про Шерлока Холмса?', 'Франклин Рузвельт', 'Пушкин', 'Джон Кеннеди', 'Рональд Рейган'))

question_list.append(Question('Сколько синих полос на флаге США?', '0', '7', '13', '2'))

question_list.append(Question('Какая самая редкая группа крови?', '4', '2', '1', '3'))

question_list.append(Question('Сколько сердец у осьминога?', '3', '1', '5', '7'))

question_list.append(Question('Сколько градусов в круге?', '360', '180', '90', '125'))

question_list.append(Question('Сколько существует книг о Гарри Поттере?', '7', '2', '10', '0'))

question_list.append(Question('Какая змея самая смертоносная?', 'Черная Мамба', 'Питон', 'Уж', 'Кобра'))

main_win.cur_question = -1

next_question()

button.clicked.connect(click_ok)

main_win.show()
app.exec_()
