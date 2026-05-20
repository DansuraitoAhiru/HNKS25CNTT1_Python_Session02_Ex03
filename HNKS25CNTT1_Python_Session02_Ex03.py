# input
patient_name = input("Nhập họ và tên bệnh nhân: ")     # nhập tên bệnh nhân
age = int(input("Nhập tuổi của bệnh nhân: "))          # nhập tuổi bênh nhân

# dùng if lồng để kiểm tra điều kiện
if patient_name == "" or patient_name == " ":                 # ktra xem tên có rỗng ko  
    print("Lỗi: Tên ko hợp lệ!")       #output
elif age<0 or age>150:                 # ktra xem tuổi có âm hoặc > 150 ko
    print("Lỗi: Tuổi nằm ngoài phạm vi con người(0-150)!")     #ouput
else:   # ko dính bẫy thì mới bắt đầu kiểm tra tuổi và in phiếu
    #phân luồng bệnh nhân
    if age<6:
        classification = print("ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi.")
    elif age>=80:
        classification = print("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.")
    else:
        classification = print("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.")
    
    # in phiếu
    print("--- Phiếu Phiếu khám bệnh điện tử ---") 
    print(f"Tên bệnh nhân: {patient_name}")
    print(f"Tuổi bệnh nhân: {age}")
    print(f"Kết quả phân luồng: {classification}")
