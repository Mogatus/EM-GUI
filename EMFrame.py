from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from DBFunctions import DBFunctions


class MeterDataFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meter Data Table")
        self.setGeometry(100, 100, 1200, 800)

        # # Create the table widget
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        # Load data into the table
        self.load_data()

    def load_data(self):
        data = DBFunctions.readMeterDataFromDB()
        print (data)
        # Populate the table widget
        if data:
            self.table_widget.setRowCount(len(data))
            self.table_widget.setColumnCount(len(data[0]))
            self.table_widget.setHorizontalHeaderLabels(
                ["Load Value", "PV", "Grid Feed-In", "Grid Purchase", "Save Timestamp"]
            )

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
