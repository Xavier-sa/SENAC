import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QCheckBox, QSpinBox, QDialogButtonBox, QLabel

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VENDAS ")

       
        layout = QVBoxLayout()

       
        self.checkboxes = []
        self.spinboxes = []

        for i in range(8):
            checkbox = QCheckBox(f" Cigarro{i + 1}")
            spinbox = QSpinBox()
            spinbox.setRange(0, 100)  
            layout.addWidget(checkbox)
            layout.addWidget(spinbox)
            self.checkboxes.append(checkbox)
            self.spinboxes.append(spinbox)

        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    if dialog.exec() == QDialog.Accepted:
        
        for checkbox, spinbox in zip(dialog.checkboxes, dialog.spinboxes):
            if checkbox.isChecked():
                print(f"{checkbox.text()}: {spinbox.value()}")
    sys.exit(app.exec())
