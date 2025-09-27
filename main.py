from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt
import sys
import webbrowser
       
class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.windowTitle = "Thông Báo"
        self.icon = QMessageBox.Icon.Warning
        self.styleSheet = "background-color: #ccc; color:blue"

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/home.ui", self)
        self.msg = QMessageBox()
        cung_hoang_dao = [
            "Bạch Dương", "Kim Ngưu", "Song Tử", "Cự Giải", "Sư Tử", "Xử Nữ",
            "Thiên Bình", "Bọ Cạp", "Nhân Mã", "Ma Kết", "Bảo Bình", "Song Ngư"]

        tongiao = [
            "Phật giáo", "Thiên Chúa giáo", "Hồi giáo", "Ông Bà", " Tin Lành", "Ấn Độ giaó",
            " Do thái giáo"]
        
        self.ui.cbotongiaoNam.addItems(tongiao)
        self.ui.cbotongiaoNu.addItems(tongiao)
        self.ui.cboCungNam.addItems(cung_hoang_dao)
        self.ui.cboCungNu.addItems(cung_hoang_dao)
        # Kết nối nút với hàm xử lý sự kiện
        self.ui.btnNavHome.clicked.connect(lambda: self.handleChangePage(0))
        self.ui.btnNavSr.clicked.connect(lambda: self.handleChangePage(1))
        self.ui.btnNavMovie.clicked.connect(lambda: self.handleChangePage(2))
        self.ui.btnNavNotify.clicked.connect(lambda: self.handleChangePage(3))
        self.ui.btnLogout.clicked.connect(self.handleLogout)
        self.ui.btnclu.clicked.connect(self.handleclu)
        self.ui.btnSRR.clicked.connect(self.SRR)  # Gắn nút tìm kiếm Google

        self.ui.btnSRR_3.clicked.connect(self.SRRR)
        self.ui.btnSRR_7.clicked.connect(self.hien_thi_cung_hoang_dao)

    def handleLogout(self):
            homePage.close()
            loginPage.show()
    def handleChangePage(self, index):
            self.ui.stackedWidget.setCurrentIndex(index)

    def handleclu(self):

            cung_nam = self.ui.cboCungNam.currentText()
            cung_nu = self.ui.cboCungNu.currentText()
            ho_ten_nam = self.ui.txtnameNam.text()
            ho_ten_nu = self.ui.txtnameWomen.text()
            tuoi_nu = int(self.ui.txttuoiWomen.text())
            tuoi_nam = int(self.ui.txttuoiNam.text())
            ton_giao_nam = self.ui.cbotongiaoNam.currentText()
            ton_giao_nu = self.ui.cbotongiaoNu.currentText()
            nam_sinh_nam = int(self.ui.txtnamsinhNam.text())
            nam_sinh_nu = int(self.ui.txtnamsinhWomen.text())
            
            self.msg = QMessageBox()          
            print(cung_nam, cung_nu,ton_giao_nam, ton_giao_nu, nam_sinh_nam, nam_sinh_nu)
            
            if 2025-tuoi_nu!=nam_sinh_nu or 2025-tuoi_nam!=nam_sinh_nam:
                            self.msg.setText(" Tuổi và năm sinh không hợp lý")
                            self.msg.exec()
                            return
            elif 2025-tuoi_nu!=nam_sinh_nu and 2025-tuoi_nam!=nam_sinh_nam:
                            self.msg.setText(" Tuổi và năm sinh không hợp lý")
                            self.msg.exec()
                            return


            def tinh_so_chu_dao(nam_sinh):
                    while nam_sinh >= 10:
                        nam_sinh = sum(map(int, str(nam_sinh)))
                    return nam_sinh

                    
            def get_match_score(cung_nam, cung_nu):
                cung_hoang_dao = ["Bạch Dương", "Kim Ngưu", "Song Tử", "Cự Giải", "Sư Tử", "Xử Nữ", "Thiên Bình", "Bọ Cạp", "Nhân Mã", "Ma Kết", "Bảo Bình", "Song Ngư"]
                match_scores = [
                    [90, 75, 85, 65, 95, 70, 80, 60, 90, 65, 85, 55],
                    [75, 90, 70, 85, 65, 95, 60, 80, 70, 90, 55, 75],
                    [85, 70, 90, 60, 80, 65, 95, 75, 85, 55, 90, 70],
                    [65, 85, 60, 90, 70, 80, 55, 95, 75, 85, 65, 70],
                    [95, 65, 80, 70, 90, 75, 85, 60, 95, 55, 85, 65],
                    [70, 95, 65, 80, 75, 90, 60, 85, 70, 95, 55, 85],
                    [80, 60, 95, 55, 85, 60, 90, 75, 70, 80, 85, 65],
                    [60, 80, 75, 95, 60, 85, 75, 90, 65, 85, 70, 80],
                    [90, 70, 85, 75, 95, 70, 70, 65, 90, 85, 95, 55],
                    [65, 90, 55, 85, 55, 95, 80, 85, 85, 90, 75, 70],
                    [85, 55, 90, 65, 85, 55, 85, 70, 95, 75, 90, 80],
                    [55, 75, 70, 70, 65, 85, 65, 80, 55, 70, 80, 90]
                    ]
                    
                if cung_nam in cung_hoang_dao and cung_nu in cung_hoang_dao:
                    return match_scores[cung_hoang_dao.index(cung_nam)][cung_hoang_dao.index(cung_nu)]
                return 50

            def tinh_diem_tuong_hop(cung_nam, cung_nu, ton_giao_nam, ton_giao_nu, nam_sinh_nam, nam_sinh_nu):
                chenhlech_tuoi = abs((2025 - nam_sinh_nam) - (2025 - nam_sinh_nu))
                so_chu_dao_nam, so_chu_dao_nu = map(tinh_so_chu_dao, [nam_sinh_nam, nam_sinh_nu])
                diem = get_match_score(cung_nam, cung_nu)
                diem += 2 if ton_giao_nam == ton_giao_nu else -2
                diem += 3 if chenhlech_tuoi == 0 else 2 if chenhlech_tuoi <= 3 else 1 if chenhlech_tuoi <= 7 else -3
                diem += 4 if so_chu_dao_nam == so_chu_dao_nu else 2 if abs(so_chu_dao_nam - so_chu_dao_nu) <= 2 else -2 if abs(so_chu_dao_nam - so_chu_dao_nu) <= 5 else -4
                return max(0, min(diem, 95))

            print(f"Cặp {ho_ten_nam} {cung_nam} - {ho_ten_nu} {cung_nu} hợp nhau: {tinh_diem_tuong_hop(cung_nam, cung_nu, ton_giao_nam, ton_giao_nu, nam_sinh_nam, nam_sinh_nu)}/100")

            self.msg.setText(f"Cặp {ho_ten_nam} - {ho_ten_nu} hợp nhau: {tinh_diem_tuong_hop(cung_nam, cung_nu, ton_giao_nam, ton_giao_nu, nam_sinh_nam, nam_sinh_nu)}/100")
            self.msg.exec()         
            return     

    def SRR(self):
        query = self.ui.txtSR.text()  # Lấy nội dung tìm kiếm từ ô nhập
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)  # Mở kết quả tìm kiếm trên Google

        # Kiểm tra và hiển thị thông tin
    def hien_thi_cung_hoang_dao(self):
        # Lấy giá trị từ ComboBox
        cung_nam = self.ui.cboCungNam.currentText()
        cung_nu = self.ui.cboCungNu.currentText()

        # Dictionary chứa thông tin tôn giáo
        thong_tin_cung = {
        "Bạch Dương": "Năng động, nhiệt huyết, thích thử thách.",
        "Kim Ngưu": "Chăm chỉ, kiên nhẫn, yêu thích sự ổn định.",
        "Song Tử": "Thông minh, linh hoạt, giao tiếp tốt.",
        "Cự Giải": "Tình cảm, nhạy cảm, luôn quan tâm gia đình.",
        "Sư Tử": "Tự tin, sáng tạo, thích được chú ý.",
        "Xử Nữ": "Tỉ mỉ, thực tế, luôn tìm kiếm sự hoàn hảo.",
        "Thiên Bình": "Công bằng, yêu cái đẹp, giỏi ngoại giao.",
        "Bọ Cạp": "Mạnh mẽ, đam mê, sống nội tâm.",
        "Nhân Mã": "Tự do, phiêu lưu, yêu thích học hỏi.",
        "Ma Kết": "Trách nhiệm, kỷ luật, luôn có kế hoạch.",
        "Bảo Bình": "Độc lập, sáng tạo, suy nghĩ khác biệt.",
        "Song Ngư": "Mơ mộng, nhạy cảm, có trực giác mạnh."
    }

        # Kiểm tra và hiển thị thông tin
        if cung_nam.strip() in thong_tin_cung and cung_nu.strip() in thong_tin_cung:

            # Xây dựng nội dung hiển thị
            thong_tin = (
                f"Thông tin về hai tôn giáo:\n"
                f"- {cung_nam}: {thong_tin_cung[cung_nam]}\n"
                f"- {cung_nu}: {thong_tin_cung[cung_nu]}\n"
            )

            # Thêm lời khuyên dựa trên tình trạng tôn giáo
            if cung_nam == cung_nu:
                thong_tin += (
                    "💡 *Lời khuyên cho cặp đôi cùng tôn giáo:*\n"
                    "- Hãy cùng nhau thực hành đức tin để gắn kết tình cảm.\n"
                    "- Tận dụng các giá trị chung để thấu hiểu và đồng cảm hơn.\n"
                    "- Đừng để khác biệt quan điểm nhỏ nhặt làm ảnh hưởng tình yêu.\n"
                )
            elif cung_nam != cung_nu :
                thong_tin += (
                    "💡 *Lời khuyên cho cặp đôi khác tôn giáo:*\n"
                    "- Tôn trọng niềm tin của nhau, tránh áp đặt quan điểm cá nhân.\n"
                    "- Tìm điểm chung trong đạo đức và lối sống để xây dựng sự hòa hợp.\n"
                    "- Nếu có xung đột, hãy trò chuyện cởi mở và đặt tình yêu lên hàng đầu.\n")
 # Hiển thị thông báo
            self.msg.setText(thong_tin)
        else:
            self.msg.setText("Cung hoàng đạo không hợp lệ.")
        self.msg.exec()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key.Key_Escape:
            self.close()
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key.Key_Return:
            self.SRRR()
            self.SRR()
            self.hien_thi_cung_hoang_dao
            


    def SRRR(self):
        # Lấy giá trị từ ComboBox
        ton_giao_Nam = self.ui.cbotongiaoNam.currentText()
        ton_giao_Nu = self.ui.cbotongiaoNu.currentText()

        # Dictionary chứa thông tin tôn giáo
        thong_tin_ton_giao = {
            "Phật giáo": "Chú trọng giác ngộ, từ bi và luân hồi.",
            "Thiên Chúa giáo": "Tin vào Chúa Trời, Kinh Thánh và tình yêu thương.",
            "Hồi giáo": "Tin vào Allah, Muhammad là nhà tiên tri cuối cùng.",
            "Ông Bà": "Thờ cúng tổ tiên, truyền thống người Việt.",
            "Tin Lành": "Nhấn mạnh đức tin cá nhân và Kinh Thánh.",
            "Ấn Độ giáo": "Đa thần giáo, tin vào nghiệp báo và luân hồi.",
            "Do Thái giáo": "Dựa trên Torah, tin vào giao ước với Chúa Trời."
        }

        # Kiểm tra và hiển thị thông tin
        if ton_giao_Nam.strip() in thong_tin_ton_giao and ton_giao_Nu.strip() in thong_tin_ton_giao:

            # Xây dựng nội dung hiển thị
            thong_tin = (
                f"Thông tin về hai tôn giáo:\n"
                f"- {ton_giao_Nam}: {thong_tin_ton_giao[ton_giao_Nam]}\n"
                f"- {ton_giao_Nu}: {thong_tin_ton_giao[ton_giao_Nu]}\n\n"
            )

            # Thêm lời khuyên dựa trên tình trạng tôn giáo
            if ton_giao_Nam == ton_giao_Nu:
                thong_tin += (
                    "💡 *Lời khuyên cho cặp đôi cùng tôn giáo:*\n"
                    "- Hãy cùng nhau thực hành đức tin để gắn kết tình cảm.\n"
                    "- Tận dụng các giá trị chung để thấu hiểu và đồng cảm hơn.\n"
                    "- Đừng để khác biệt quan điểm nhỏ nhặt làm ảnh hưởng tình yêu.\n"
                )
            elif ton_giao_Nam != ton_giao_Nu :
                thong_tin += (
                    "💡 *Lời khuyên cho cặp đôi khác tôn giáo:*\n"
                    "- Tôn trọng niềm tin của nhau, tránh áp đặt quan điểm cá nhân.\n"
                    "- Tìm điểm chung trong đạo đức và lối sống để xây dựng sự hòa hợp.\n"
                    "- Nếu có xung đột, hãy trò chuyện cởi mở và đặt tình yêu lên hàng đầu.\n")
 # Hiển thị thông báo
            self.msg.setText(thong_tin)
        else:
            self.msg.setText("Tôn giáo không hợp lệ hoặc không có trong danh sách.")
        self.msg.exec()



class Register(QMainWindow):
    def __init__(self):
       super().__init__()
       self.ui=uic.loadUi("ui/register.ui",self)
       self.msg=QMessageBox()
       self.ui.btnRegister.clicked.connect(self.handleRegister)
       self.ui.btnLoo.clicked.connect(self.handleLoo)
    def handleLoo(self):
        registerPage.close()
        loginPage.show()
    
    def handleRegister(self):
        checkbox=self.ui.checkBox.checkState()
        #lấy ra thông tin email và password từ ô nhập liệu
        email=self.ui.txtEmail.text()
        password=self.ui.txtPassword.text()
        name=self.ui.txtName.text()
        print(email,password,name)
        if not name:
            self.msg.setText("Tên ko đc để trống")
            self.msg.exec()
            return
        if not email:
            self.msg.setText("Email ko đc để trống")
            self.msg.exec()
            return
        if not password:
             self.msg.setText("Password ko đc để trống")
             self.msg.exec()  
             return
        
        if not checkbox == Qt.CheckState.Checked:
             self.msg.setText("Sao mày không đồng ý???")
             self.msg.exec()  
             return
        
        if  email ==email and password==password:
            self.msg.setText(f"Chào mừng {name} đến với Heart & LoveSync,hy vọng cậu có những trải nghiệm vui vẻ nhẻ💕")
            self.msg.exec()
            homePage.show()
            self.close()
         

    def keyPressEvent(self,event):
        if event.key()==Qt.Key.Key_Escape:
            self.close()
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key.Key_Return:
            self.handleRegister()
        
class Login(QMainWindow):
    def __init__(self):
       super().__init__()
       self.ui=uic.loadUi("ui/login.ui",self)
       self.msg=QMessageBox()
        # tạo sự kiện cho nút Login
       self.ui.btnLogin.clicked.connect(self.handleLogin)
       self.ui.btnLo.clicked.connect(self.handleLo)
   
    def handleLo(self):
        loginPage.close()
        registerPage.show()

    def handleLogin(self):
        #lấy ra thông tin email và password từ ô nhập liệu
        email=self.ui.txtEmail.text()
        password=self.ui.txtPassword.text()
        checkbox=self.ui.checkBox.checkState()
        print(email,password)
        if not email:
            self.msg.setText("Email ko đc để trống")
            self.msg.exec()
            return
        if not password:
             self.msg.setText("Password ko đc để trống")
             self.msg.exec()  
             return
        
        if not checkbox == Qt.CheckState.Checked:
             self.msg.setText("Sao mày không đồng ý???")
             self.msg.exec()  
             return
    
        if  email =="trường cho đề khó thật đấy" and password=="nhưng dễ thi":
            self.msg.setText("Hello cậu, lâu rồi mới gặp  💕")
            self.msg.exec()
            homePage.show()
            self.close()
        else:
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key.Key_Escape:
            self.close()
    
    def keyPressEvent(self,event):
        if event.key()==Qt.Key.Key_Return:
            self.handleLogin()

if __name__=="__main__":
    app=QApplication(sys.argv)
    loginPage=Login()
    homePage=Home()
    registerPage=Register()
    loginPage.show()
    app.exec()