import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(300, 150, 500, 400)

        main_layout = QVBoxLayout()

        identity_label = QLabel("Identitas")
        identity_label.setFont(QFont("Arial"))
        identity_box = QGroupBox()
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Baiq Luthfida Khairunnisa"))
        identity_layout.addWidget(QLabel("Nim  : F1D022037"))
        identity_layout.addWidget(QLabel("Kelas: C"))
        identity_box.setLayout(identity_layout)

        nav_label = QLabel("Navigation")
        nav_label.setFont(QFont("Arial"))
        nav_box = QGroupBox()
        nav_layout = QHBoxLayout()
        
        btn_style = """
            QPushButton {
                border-radius: 10px;
                background-color: #FFFFFF;
                color: black;
                font-weight: bold;
                font-family: Arial;
                padding: 8px 10px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton:pressed {
            background-color: #CCCCCC; 
            }
        """

        btn_home = QPushButton("Home")
        btn_home.setStyleSheet(btn_style)

        btn_about = QPushButton("About")
        btn_about.setStyleSheet(btn_style)

        btn_contact = QPushButton("Contact")
        btn_contact.setStyleSheet(btn_style)

        nav_layout.addWidget(btn_home)
        nav_layout.addWidget(btn_about)
        nav_layout.addWidget(btn_contact)

        nav_box.setLayout(nav_layout)

        form_label = QLabel("Registration Form")
        form_label.setFont(QFont("Arial"))
        form_box = QGroupBox()
        form_layout = QFormLayout()
        form_layout.addRow("Full Name:", QLineEdit())
        form_layout.addRow("Email:", QLineEdit())
        form_layout.addRow("Phone:", QLineEdit())

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))
        form_layout.addRow("Gender:", gender_layout)

        country_box = QComboBox()
        country_box.addItems(["Select Country", "USA", "UK", "India", "Canada"])
        form_layout.addRow("Country:", country_box)

        form_box.setLayout(form_layout)

        action_label = QLabel("Action")
        action_label.setFont(QFont("Arial"))
        action_box = QGroupBox()
        action_layout = QHBoxLayout()

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet(btn_style)

        cancel_button = QPushButton("Cancel")   
        cancel_button.setStyleSheet(btn_style)

        action_layout.addWidget(submit_button)
        action_layout.addWidget(cancel_button)

        action_box.setLayout(action_layout)

        main_layout.addWidget(identity_label)
        main_layout.addWidget(identity_box)
        main_layout.addWidget(nav_label)
        main_layout.addWidget(nav_box)
        main_layout.addWidget(form_label)
        main_layout.addWidget(form_box)
        main_layout.addWidget(action_label)
        main_layout.addWidget(action_box)

        groupbox_style = """
            QGroupBox {
                background-color: #DFDFDF;    
                border-radius: 16px;        
                padding: 10px;              
            }
        """

        for box in [identity_box, nav_box, form_box, action_box]:
            box.setStyleSheet(groupbox_style)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())