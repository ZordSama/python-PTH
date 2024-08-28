import datetime

hoTen = input("Nhập họ tên của bạn:")
namSinh = int(input("Nhập năm sinh của bạn:"))
thisYear = datetime.date.today().year
print("Chào", hoTen, ",năm nay bạn đã ", thisYear - namSinh, " tuổi")
