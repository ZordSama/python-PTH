import math


# 1.Nhập từ bàn phím số nguyên n và danh sách n số nguyên
def get_n():
    n = int(input("Nhập n: "))
    if n <= 0:
        raise ValueError(
            "n phải là số nguyên lớn hơn 0"
        )  # Tạo lỗi nếu số nhập vào <= 0
    return n


def get_list(n):
    list = []
    for i in range(n):
        list.append(int(input(f"Nhập số nguyên thứ {i + 1}: ")))
    return list


# 2.Tìm ước chung lớn nhất (UCLN) và bội chung nhỏ nhất (BCNN) của tất cả các số nguyên trong dãy.
# math.gcd là hàm tìm ước chung lớn nhất trong thư viện Math của python


# hàm tìm bội nhỏ nhất
def get_lsmc(list):
    lcm = list[0]
    for i in range(1, len(list)):
        lcm = lcm * list[i] // math.gcd(lcm, list[i])
    return lcm


# hàm tìm ước lớn nhất
def get_gcd(list):
    gcd = list[0]
    for i in range(1, len(list)):
        gcd = math.gcd(gcd, list[i])
    return gcd


# 3.  Đếm xem trong dãy có bao nhiêu số chính phương, bao nhiêu số nguyên tố và hiển thị các số chính phương, số nguyên tố trong dãy.


# hàm kiểm tra số chính phương (nguyên căn bậc 2 của n bình phương lên bằng n => n là chính phương)
def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n


# hàm kiểm tra số nguyên tố (cho i từ 2 đến nguyên căn bậc 2 của n, n%i != 0  => n là snt)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


# đếm và hiển thị các số chính phương, nguyên tố trong dãy
def count_and_display(list):
    count_perfect_square = 0
    count_prime = 0
    perfect_square_list = []
    prime_list = []

    for i in list:
        if is_perfect_square(i):
            count_perfect_square += 1
            perfect_square_list.append(i)
        if is_prime(i):
            count_prime += 1
            prime_list.append(i)
    if count_perfect_square == 0:
        print("Không có số chính phương trong dãy")
    else:
        print("Số lượng số chính phương có trong dãy là: ", count_perfect_square)
        print("Danh sách các số chính phương trong dãy là: ", perfect_square_list)
    if count_prime == 0:
        print("Không có số nguyên tố trong dãy")
    else:
        print("Số lượng nguyên tố có trong dãy là: ", count_prime)
        print("Danh sách các số nguyên tố trong dãy là: ", prime_list)


# 4. Sắp xếp dãy số nguyên đã nhập theo chiều tăng dần hoặc giảm dần
def sort_list(list):
    list.sort()
    print("Danh sách số nguyên sau khi sắp xếp tăng dần: ", list)
    list.sort(reverse=True)
    print("Danh sách số nguyên sau khi sắp xếp giảm dần: ", list)


# 5.  Đếm số nguyên xuất hiện trong dãy quá một lần.
def count_occurrences(list):
    count_dict = {}
    for i in list:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for key, value in count_dict.items():
        if value > 1:
            print(f"Số {key} đã xuất hiện {value} lần trong dãy")


# 6. Tính tỉ lệ phần trăm số lượng các số lẻ trong dãy.
def calculate_odd_percentage(list):
    count_odd = 0
    for i in list:
        if i % 2 != 0:
            count_odd += 1
    percentage = (count_odd / len(list)) * 100
    print(
        f"Số lẻ đã xuất hiện {count_odd}/{len(list)} trong dãy, chiếm tổng {percentage}%"
    )


# chương trình chính

try:
    list = get_list(get_n())
    print("Danh sách số nguyên đã nhập là: ", list)
    print("UCLN của tất cả các số nguyên trong dãy là: ", get_gcd(list))
    print("BCNN của tất cả các số nguyên trong dãy là: ", get_lsmc(list))
    count_and_display(list)
    sort_list(list)
    count_occurrences(list)
    calculate_odd_percentage(list)
except Exception as error:
    print("Error: ", error)
