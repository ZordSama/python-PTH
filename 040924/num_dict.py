num_pronount = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
while True:
    num = int(input("Nhập vào số (0-9): "))
    if num >=0 and num <10:
        print(f"{num} đọc là {num_pronount[num]}")
        break
    print("Số không hợp lệ, nhập lại!")
