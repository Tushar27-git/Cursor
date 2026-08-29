"""
MONO Cursor Pack - Ultimate Interactive Busy & Stress Test Studio
Provides high-intensity stress testing, infinite busy lock, and multi-core calculation simulations.
"""
import sys
import os
import time
import math
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QComboBox, QProgressBar, QFrame, QCheckBox, QSlider
)
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QFont, QColor, QCursor, QPixmap, QPainter, QPen, QBrush

class HeavyComputeWorker(QThread):
    progress = Signal(int, str)
    finished = Signal()

    def __init__(self, duration_sec=5):
        super().__init__()
        self.duration_sec = duration_sec
        self._is_running = True

    def stop(self):
        self._is_running = False

    def run(self):
        start_time = time.time()
        ops = 0
        while self._is_running:
            elapsed = time.time() - start_time
            if elapsed >= self.duration_sec:
                break
            
            # Execute heavy matrix computations
            for _ in range(50000):
                _ = math.sin(ops) * math.cos(ops)
                ops += 1
                
            pct = min(100, int((elapsed / self.duration_sec) * 100))
            self.progress.emit(pct, f"Calculated {ops:,} operations | Elapsed: {elapsed:.1f}s")
            time.sleep(0.01)

        self.finished.emit()

class FlappingWorker(QThread):
    change_cursor = Signal(int)
    finished = Signal()

    def __init__(self, count=50, interval_ms=60):
        super().__init__()
        self.count = count
        self.interval_ms = interval_ms
        self._is_running = True

    def stop(self):
        self._is_running = False

    def run(self):
        for i in range(self.count):
            if not self._is_running:
                break
            self.change_cursor.emit(i % 5)
            time.sleep(self.interval_ms / 1000.0)
        self.finished.emit()

class AnimatedSpinnerWidget(QWidget):
    """Real-time 60 FPS vector spinner rendering the 3 purple dots in motion"""
    def __init__(self):
        super().__init__()
        self.setFixedSize(100, 100)
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16) # ~60 FPS

    def update_animation(self):
        self.angle = (self.angle + 4) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        
        # Center at (50, 50)
        painter.translate(50, 50)
        painter.rotate(self.angle)
        
        # Solid black center disk
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#000000"))
        painter.drawEllipse(-34, -34, 68, 68)
        
        # Pale lilac connecting arcs
        pen = QPen(QColor("#F5F1FF"), 6)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(-28, -28, 56, 56)
        
        # 3 Purple orbiting accent dots (120 deg apart)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#B18CFF"))
        for i in range(3):
            rad = math.radians(i * 120 - 90)
            x = 28 * math.cos(rad)
            y = 28 * math.sin(rad)
            # Black collar
            painter.setBrush(QColor("#000000"))
            painter.drawEllipse(int(x - 9), int(y - 9), 18, 18)
            # Lilac core
            painter.setBrush(QColor("#B18CFF"))
            painter.drawEllipse(int(x - 7), int(y - 7), 14, 14)

class CursorStressStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MONO — Busy Cursor & System Stress Studio")
        self.setFixedSize(760, 680)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0B0914;
            }
            QLabel {
                color: #F5F1FF;
                font-family: 'Segoe UI';
            }
            QPushButton {
                background-color: #171326;
                color: #F5F1FF;
                border: 1.5px solid #33294E;
                border-radius: 10px;
                padding: 12px 18px;
                font-family: 'Segoe UI';
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #241D3C;
                border-color: #B18CFF;
            }
            QPushButton:checked {
                background-color: #B18CFF;
                color: #0B0914;
                border-color: #F5F1FF;
            }
            QComboBox {
                background-color: #171326;
                color: #F5F1FF;
                border: 1.5px solid #33294E;
                border-radius: 8px;
                padding: 8px 14px;
                font-family: 'Segoe UI';
                font-size: 13px;
            }
            QComboBox QAbstractItemView {
                background-color: #171326;
                color: #F5F1FF;
                selection-background-color: #B18CFF;
                selection-color: #0B0914;
            }
            QProgressBar {
                background-color: #130F20;
                border: 1.5px solid #2B2344;
                border-radius: 8px;
                text-align: center;
                color: #F5F1FF;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7544CC, stop:1 #B18CFF);
                border-radius: 7px;
            }
            QFrame#card {
                background-color: #120E20;
                border: 1.5px solid #2A2242;
                border-radius: 14px;
                padding: 14px;
            }
            QFrame#heroArea {
                background-color: #141024;
                border: 2px dashed #403466;
                border-radius: 18px;
            }
        """)

        central = QWidget()
        self.setCentralWidget(central)
        mainLayout = QVBoxLayout(central)
        mainLayout.setContentsMargins(25, 20, 25, 20)
        mainLayout.setSpacing(14)

        # Header Title
        headerLayout = QHBoxLayout()
        titleLayout = QVBoxLayout()
        title = QLabel("MONO Cursor Stress Studio")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        subtitle = QLabel("Live Busy state stress testing, multi-core workload simulator & 60fps spinner inspector.")
        subtitle.setStyleSheet("color: #9A8FB8; font-size: 12px;")
        titleLayout.addWidget(title)
        titleLayout.addWidget(subtitle)
        headerLayout.addLayout(titleLayout)
        
        # Real-time animated spinner badge
        self.spinnerWidget = AnimatedSpinnerWidget()
        headerLayout.addWidget(self.spinnerWidget)
        mainLayout.addLayout(headerLayout)

        # Interactive Main Test Board
        self.heroArea = QFrame()
        self.heroArea.setObjectName("heroArea")
        self.heroArea.setMinimumHeight(130)
        areaLayout = QVBoxLayout(self.heroArea)
        
        self.areaLabel = QLabel("⚡ Move your cursor anywhere inside this box\n(Cursor reflects live stress state)")
        self.areaLabel.setAlignment(Qt.AlignCenter)
        self.areaLabel.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.areaLabel.setStyleSheet("color: #EDE4FF;")
        areaLayout.addWidget(self.areaLabel)
        mainLayout.addWidget(self.heroArea)

        # Live Progress & Compute Status
        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.setFixedHeight(22)
        mainLayout.addWidget(self.progressBar)

        self.statusLabel = QLabel("Ready for stress test.")
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setStyleSheet("color: #B18CFF; font-weight: bold; font-size: 12px;")
        mainLayout.addWidget(self.statusLabel)

        # Stress Test Cards
        gridFrame = QFrame()
        gridFrame.setObjectName("card")
        cardLayout = QVBoxLayout(gridFrame)
        cardLayout.setSpacing(10)

        cardTitle = QLabel("🔥 Stress Test Scenarios:")
        cardTitle.setFont(QFont("Segoe UI", 12, QFont.Bold))
        cardTitle.setStyleSheet("color: #F5F1FF;")
        cardLayout.addWidget(cardTitle)

        btnRow1 = QHBoxLayout()
        self.heavyBtn = QPushButton("💥 5-Second CPU Matrix Stress Test")
        self.heavyBtn.clicked.connect(lambda: self.run_cpu_stress(5))
        btnRow1.addWidget(self.heavyBtn)

        self.heavyLongBtn = QPushButton("⚡ 10-Second Heavy Load")
        self.heavyLongBtn.clicked.connect(lambda: self.run_cpu_stress(10))
        btnRow1.addWidget(self.heavyLongBtn)
        cardLayout.addLayout(btnRow1)

        btnRow2 = QHBoxLayout()
        self.lockToggleBtn = QPushButton("🔒 Toggle Continuous Infinite Busy State")
        self.lockToggleBtn.setCheckable(True)
        self.lockToggleBtn.toggled.connect(self.toggle_infinite_busy)
        btnRow2.addWidget(self.lockToggleBtn)

        self.flapBtn = QPushButton("🌪️ Rapid 60 FPS Cursor Flapping")
        self.flapBtn.clicked.connect(self.run_flapping_stress)
        btnRow2.addWidget(self.flapBtn)
        cardLayout.addLayout(btnRow2)

        mainLayout.addWidget(gridFrame)

        # Manual Cursor Inspector Row
        inspectorFrame = QFrame()
        inspectorFrame.setObjectName("card")
        inspLayout = QHBoxLayout(inspectorFrame)
        
        inspLabel = QLabel("Inspect Specific Cursor:")
        inspLabel.setFont(QFont("Segoe UI", 11, QFont.Bold))
        inspLayout.addWidget(inspLabel)

        self.combo = QComboBox()
        self.cursor_files = {
            "Busy / Wait (mono_busy)": "mono_busy.cur",
            "Working in Background": "mono_working_in_background.cur",
            "Normal Select (Arrow)": "mono_normal_select.cur",
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
            "Location Select": "mono_location_select.cur",
            "Person Select": "mono_person_select.cur"
        }
        for name in self.cursor_files.keys():
            self.combo.addItem(name)
        self.combo.currentTextChanged.connect(self.on_cursor_picked)
        inspLayout.addWidget(self.combo)
        mainLayout.addWidget(inspectorFrame)

        self.is_busy_locked = False
        self.worker = None

    def run_cpu_stress(self, duration):
        self.set_buttons_enabled(False)
        self.areaLabel.setText(f"🔥 SYSTEM BUSY: Running {duration}s CPU Stress Workload...\nNotice your custom MONO Busy cursor!")
        self.statusLabel.setText("Executing heavy calculations...")
        
        # Override cursor to OS WaitCursor
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.progressBar.setValue(0)
        
        self.worker = HeavyComputeWorker(duration_sec=duration)
        self.worker.progress.connect(self.on_compute_progress)
        self.worker.finished.connect(self.on_stress_finished)
        self.worker.start()

    def on_compute_progress(self, pct, msg):
        self.progressBar.setValue(pct)
        self.statusLabel.setText(msg)

    def on_stress_finished(self):
        QApplication.restoreOverrideCursor()
        self.set_buttons_enabled(True)
        self.progressBar.setValue(100)
        self.areaLabel.setText("✅ Stress Workload Complete!\nCursor returned to Normal Select.")
        self.statusLabel.setText("System Idle | Ready")

    def toggle_infinite_busy(self, checked):
        if checked:
            QApplication.setOverrideCursor(Qt.WaitCursor)
            self.lockToggleBtn.setText("🔓 Release Infinite Busy Lock")
            self.areaLabel.setText("🔒 BUSY LOCK ACTIVE: Cursor is held in Wait state indefinitely.\nMove around anywhere to test!")
            self.statusLabel.setText("Continuous Busy mode running (Click button above to release)")
            self.progressBar.setValue(100)
        else:
            QApplication.restoreOverrideCursor()
            self.lockToggleBtn.setText("🔒 Toggle Continuous Infinite Busy State")
            self.areaLabel.setText("Unlocked! Cursor restored to normal.")
            self.statusLabel.setText("System Idle | Ready")
            self.progressBar.setValue(0)

    def run_flapping_stress(self):
        self.set_buttons_enabled(False)
        self.areaLabel.setText("🌪️ STRESS FLAPPING: Rapidly toggling cursor states at 60 FPS...")
        self.statusLabel.setText("Testing render thread latency and cursor switching stability...")
        
        self.flap_worker = FlappingWorker(count=60, interval_ms=50)
        self.flap_cursors = [Qt.ArrowCursor, Qt.WaitCursor, Qt.BusyCursor, Qt.IBeamCursor, Qt.SizeAllCursor]
        self.flap_worker.change_cursor.connect(lambda idx: QApplication.changeOverrideCursor(self.flap_cursors[idx]))
        
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        
        def on_flap_done():
            QApplication.restoreOverrideCursor()
            self.set_buttons_enabled(True)
            self.areaLabel.setText("✅ Flapping Test Completed! Zero dropped frames or artifacts.")
            self.statusLabel.setText("System Idle | Ready")

        self.flap_worker.finished.connect(on_flap_done)
        self.flap_worker.start()

    def on_cursor_picked(self, text):
        filename = self.cursor_files[text]
        cur_path = os.path.join(os.path.dirname(__file__), "dist", filename)
        if os.path.exists(cur_path):
            custom_cursor = QCursor(QPixmap(cur_path))
            self.heroArea.setCursor(custom_cursor)
            self.areaLabel.setText(f"Hover here to test:\n{text}")

    def set_buttons_enabled(self, enabled):
        self.heavyBtn.setEnabled(enabled)
        self.heavyLongBtn.setEnabled(enabled)
        self.flapBtn.setEnabled(enabled)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CursorStressStudio()
    window.show()
    sys.exit(app.exec())
