from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from DBFunctions import DBFunctions


class MeterDataFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meter Data Table")
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create the table widget
        self.table_widget = QTableWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.central_widget.setLayout(layout)

        # Load data into the table
        self.load_data()

    def load_data(self):
        # Replace with your Neon DB credentials
        db_name = "neondb"
        user = "neondb_owner"
        password = "<CHANGE_ME>"
        host = "ep-late-cloud-agqu0crh-pooler.c-2.eu-central-1.aws.neon.tech"
        port = "5432"

        # Initialize the DBFunctions object
        db = DBFunctions(db_name, user, password, host, port)
        db.connect()

        # Fetch data from the meter_data table
        query = "SELECT * FROM meter_data;"
        data = db.execute_query(query)

        # Populate the table widget
        if data:
            self.table_widget.setRowCount(len(data))
            self.table_widget.setColumnCount(len(data[0]))
            self.table_widget.setHorizontalHeaderLabels(
                ["ID", "Load Value", "PV", "Grid Feed-In", "Grid Purchase", "Save Timestamp"]
            )

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        db.close_connection()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    frame = MeterDataFrame()
    frame.show()
    sys.exit(app.exec_())
