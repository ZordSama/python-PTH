def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


year = int(input("Nhập năm: "))
if year < 0:
    print("Năm không hợp lệ")
    exit()
if is_leap_year(year):
    print(f"Năm {year} nhuận có 366 ngày")
else:
    print(f"Năm {year} không nhuận có 365 ngày")
