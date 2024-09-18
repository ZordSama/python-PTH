choose = input("Mời bạn chọn chức năng \n \t 1.Đăng nhập hệ thống \n \t 2.Đăng xuất hệ thống\n \t 3.Thoát khỏi hệ thống")
match choose:
    case "1": print("Đăng nhập thành công")
    case "2": print("Đăng xuất thành công")
    case "3": print("Đã hoát khỏi hệ thống...")
    case _: print("Chức năng không tồn tại")
