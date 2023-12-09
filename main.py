import random

from PyQt5.QtWidgets import*

app = QApplication([])

window = QWidget()
window.resize(700,500)

menu_btn = QPushButton("Меню")
group_box = QGroupBox()
spin_box = QSpinBox()
pause_button = QPushButton("Відпочити")

question_lbl = QLabel("Яблуко")

answer1_btn = QRadioButton("building")
answer2_btn = QRadioButton("home")
answer3_btn = QRadioButton("application")
answer4_btn = QRadioButton("apple")

answers = [answer1_btn, answer2_btn, answer3_btn, answer4_btn]
random.shuffle(answers)

vidpovistu_btn = QPushButton("Відповісти")





main_line = QVBoxLayout()


h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addWidget(spin_box)
h1.addWidget(vidpovistu_btn)

h1.addStretch(1)
main_line.addLayout(h1)

main_line.addWidget(question_lbl)

group_line = QVBoxLayout()

group_line.addWidget(answers[0])
group_line.addWidget(answers[1])
group_line.addWidget(answers[2])
group_line.addWidget(answers[3])

group_box.setLayout(group_line)

main_line.addWidget(group_box)

window.setLayout(main_line)
window.show()

window.show()
app.exec()