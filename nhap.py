from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import uic
import sys

class CountdownApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("timer.ui", self)
        
        # Khởi tạo timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        
        self.start_timer() # Bắt đầu đếm ngược
        
        # Thiết lập giá trị mặc định
        self.set_time(3000)  # Truyền vào 3000 giây
    
    def set_time(self, total_seconds):
        """Thiết lập thời gian từ tổng số giây"""
        self.remaining_time = total_seconds
        self.update_display()
    
    def update_display(self):
        """Cập nhật hiển thị thời gian lên UI"""
        hours = self.remaining_time // 3600
        minutes = (self.remaining_time % 3600) // 60
        seconds = self.remaining_time % 60
        
        # Hiển thị thời gian lên các label
        self.ui.hours.setText(f"{hours:02d}")
        self.ui.minutes.setText(f"{minutes:02d}")
        self.ui.seconds.setText(f"{seconds:02d}")
    
    def start_timer(self):
        """Bắt đầu đếm ngược"""
        if not self.timer.isActive():
            self.timer.start(1000)  # Cập nhật mỗi giây
        else:
            self.timer.stop()
    
    def update_timer(self):
        """Cập nhật thời gian sau mỗi giây"""
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_display()
        else:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountdownApp()
    window.show()
    sys.exit(app.exec())