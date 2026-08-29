"""
MONO Cursor Pack - Interactive Busy & Cursor Tester
Allows you to trigger Windows Busy / Wait state and test all 17 custom cursors live!
"""
import sys
import os
import time
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QProgressBar, QFrame
)
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QFont, QColor, QCursor, QPixmap

class WorkerThread(QThread):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        for i in range(1, 101):
            time.sleep(0.05) # 5 second simulated heavy task
            self.progress.emit(i)
        self.finished.emit()

class CursorTesterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MONO — Live Cursor & Busy State Tester")
        self.setFixedSize(680, 520)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0E0C16;
            }
            QLabel {
                color: #F5F1FF;
                font-family: 'Segoe UI';
            }
            QPushButton {
                background-color: #1E1930;
                color: #F5F1FF;
                border: 1.5px solid #372E56;
                border-radius: 10px;
                padding: 12px 20px;
                font-family: 'Segoe UI';
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2D2548;
                border-color: #B18CFF;
            }
            QPushButton:pressed {
                background-color: #B18CFF;
                color: #0E0C16;
            }
            QComboBox {
                background-color: #1E1930;
                color: #F5F1FF;
                border: 1.5px solid #372E56;
                border-radius: 8px;
                padding: 8px 14px;
                font-family: 'Segoe UI';
                font-size: 13px;
            }
            QComboBox QAbstractItemView {
                background-color: #1E1930;
                color: #F5F1FF;
                selection-background-color: #B18CFF;
                selection-color: #0E0C16;
            }
            QProgressBar {
                background-color: #151222;
                border: 1.5px solid #2F2749;
                border-radius: 8px;
                text-align: center;
                color: #F5F1FF;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7544CC, stop:1 #B18CFF);
                border-radius: 7px;
            }
            QFrame#testArea {
                background-color: #141122;
                border: 2px dashed #3D335E;
                border-radius: 16px;
            }
        """)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(18)

        # Header
        title = QLabel("MONO Cursor Live Tester")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Simulate system Busy / Wait operations and test cursor behavior live.")
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setStyleSheet("color: #9E94BD;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        # Interactive Test Area
        self.testArea = QFrame()
        self.testArea.setObjectName("testArea")
        self.testArea.setMinimumHeight(140)
        areaLayout = QVBoxLayout(self.testArea)
        
        self.areaLabel = QLabel("Hover your mouse in this box\n(Cursor responds to selected test state)")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(QFont("Segoe UI", 13))
        self.areaLabel.setStyleSheet("color: #D5CCF2;")
        areaLayout.addWidget(self.areaLabel)
        
        layout.addWidget(self.testArea)

        # Progress bar for busy simulation
        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.setFixedHeight(22)
        self.progressBar.setTextVisible(True)
        layout.addWidget(self.progressBar)

        # Action Buttons
        btnLayout = QHBoxLayout()
        btnLayout.setSpacing(14)

        self.busyBtn = QPushButton("⏳ Simulate 5-Sec Busy State")
        self.busyBtn.clicked.connect(self.trigger_busy)
        btnLayout.addWidget(self.busyBtn)

        self.appStartingBtn = QPushButton("🔄 Test Working in Background")
        self.appStartingBtn.clicked.connect(self.trigger_app_starting)
        btnLayout.addWidget(self.appStartingBtn)

        layout.addLayout(btnLayout)

        # Dropdown to test all 17 cursors
        comboLayout = QHBoxLayout()
        comboLabel = QLabel("Manual Cursor Preview:")
        comboLabel.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.combo = QComboBox()
        
        self.cursor_files = {
            "Normal Select (Arrow)": "mono_normal_select.cur",
            "Busy / Wait": "mono_busy.cur",
            "Working in Background": "mono_working_in_background.cur",
            "Help Select": "mono_help_select.cur",
            "Precision Select (Crosshair)": "mono_precision_select.cur",
            "Text Select (IBeam)": "mono_text_select.cur",
            "Handwriting": "mono_handwriting.cur",
            "Unavailable (No)": "mono_unavailable.cur",
            "Vertical Resize": "mono_vertical_resize.cur",
            "Horizontal Resize": "mono_horizontal_resize.cur",
            "Diagonal Resize 1": "mono_diagonal_resize_1.cur",
            "Diagonal Resize 2": "mono_diagonal_resize_2.cur",
            "Move": "mono_move.cur",
            "Alternate Select": "mono_alternate_select.cur",
            "Link Select": "mono_link_select.cur",
            "Location Select (Pin)": "mono_location_select.cur",
            "Person Select": "mono_person_select.cur"
        }
        
        for name in self.cursor_files.keys():
            self.combo.addItem(name)
            
        self.combo.currentTextChanged.connect(self.on_cursor_changed)
        comboLayout.addWidget(comboLabel)
        comboLayout.addWidget(self.combo)
        layout.addLayout(comboLayout)

    def trigger_busy(self):
        """Sets the application override cursor to WaitCursor (Busy) during simulated heavy operation"""
        self.busyBtn.setEnabled(False)
        self.appStartingBtn.setEnabled(False)
        self.areaLabel.setText("BUSY: Processing heavy task...\nNotice your custom MONO Busy cursor!")
        
        # Set OS Wait Cursor
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.progressBar.setValue(0)
        
        self.worker = WorkerThread()
        self.worker.progress.connect(self.progressBar.setValue)
        self.worker.finished.connect(self.on_busy_finished)
        self.worker.start()

    def on_busy_finished(self):
        QApplication.restoreOverrideCursor()
        self.busyBtn.setEnabled(True)
        self.appStartingBtn.setEnabled(True)
        self.areaLabel.setText("Task Completed!\nCursor restored to Normal Select.")
        self.progressBar.setValue(100)

    def trigger_app_starting(self):
        """Sets the application override cursor to BusyCursor (Working in background)"""
        self.busyBtn.setEnabled(False)
        self.appStartingBtn.setEnabled(False)
        self.areaLabel.setText("WORKING IN BACKGROUND:\nNotice your custom MONO Working In Background cursor!")
        
        QApplication.setOverrideCursor(Qt.BusyCursor)
        self.progressBar.setValue(0)
        
        self.worker = WorkerThread()
        self.worker.progress.connect(self.progressBar.setValue)
        self.worker.finished.connect(self.on_busy_finished)
        self.worker.start()

    def on_cursor_changed(self, text):
        filename = self.cursor_files[text]
        cur_path = os.path.join(os.path.dirname(__file__), "dist", filename)
        if os.path.exists(cur_path):
            custom_cursor = QCursor(QPixmap(cur_path))
            self.testArea.setCursor(custom_cursor)
            self.areaLabel.setText(f"Hover here to test:\n{text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CursorTesterWindow()
    window.show()
    sys.exit(app.exec())
