from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QStackedWidget, QSpinBox
from PyQt6.QtCore import QTimer
import sys

class FocusFlow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Focus Flow")
        self.setGeometry(100, 100, 400, 300)
        
        # Tạo widget chính để quản lý các trang
        self.stacked_widget = QStackedWidget()
        
        # Tạo các trang
        self.home_page = self.create_home_page()
        self.settings_page = self.create_settings_page()
        
        # Thêm các trang vào stack
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.settings_page)
        
        # Layout chính
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
        
        # Timer setup
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_left = 25 * 60  # 25 phút mặc định
        
    def create_home_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        
        self.timer_label = QLabel("25:00", self)
        self.timer_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        layout.addWidget(self.timer_label)
        
        start_button = QPushButton("Bắt đầu")
        start_button.clicked.connect(self.start_timer)
        layout.addWidget(start_button)
        
        pause_button = QPushButton("Tạm dừng")
        pause_button.clicked.connect(self.pause_timer)
        layout.addWidget(pause_button)
        
        settings_button = QPushButton("Cài đặt")
        settings_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.settings_page))
        layout.addWidget(settings_button)
        
        page.setLayout(layout)
        return page
    
    def create_settings_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        
        self.work_time_input = QSpinBox()
        self.work_time_input.setRange(1, 120)
        self.work_time_input.setValue(25)
        layout.addWidget(QLabel("Thời gian làm việc (phút):"))
        layout.addWidget(self.work_time_input)
        
        self.break_time_input = QSpinBox()
        self.break_time_input.setRange(1, 60)
        self.break_time_input.setValue(5)
        layout.addWidget(QLabel("Thời gian nghỉ (phút):"))
        layout.addWidget(self.break_time_input)
        
        save_button = QPushButton("Lưu & Quay lại")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)
        
        page.setLayout(layout)
        return page
    
    def start_timer(self):
        self.timer.start(1000)  # Mỗi giây cập nhật 1 lần
    
    def pause_timer(self):
        self.timer.stop()
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.setText(f"{minutes:02}:{seconds:02}")
        else:
            self.timer.stop()
            self.timer_label.setText("Hết giờ!")
    
    def save_settings(self):
        work_time = self.work_time_input.value()
        self.time_left = work_time * 60
        self.timer_label.setText(f"{work_time}:00")
        self.stacked_widget.setCurrentWidget(self.home_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FocusFlow()
    window.show()
    sys.exit(app.exec())