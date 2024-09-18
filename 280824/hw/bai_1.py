# caculator
def cal(a, b, m):
    match m:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            return "Error"


while True:
    a = int(input("Nhập A:"))
    b = int(input("Nhập B:"))
    m = input("Nhập phép toán:")
    if cal(a, b, m) != "Error":
        print(f"Kết quả {a}{m}{b} = {cal(a, b, m)}")
        break
    print("Phép toán không hợp lệ! Vui lòng nhập lại... \n")
# end caculator
