from PySide6.QtWidgets import QApplication
from EMFrame import MeterDataFrame

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    frame = MeterDataFrame()
    frame.show()
    sys.exit(app.exec())
