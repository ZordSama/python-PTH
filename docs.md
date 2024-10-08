# PYTHON NOTES

## 28/08/2024 Chương 1: Giới thiệu NN lập trình Python

### Q1: Nêu 3 điểm mấu chốt về quá trình hình thành và phát triển của Python

> -Nguồn gốc:
>> +Python được tạo ra bởi Guido van Rossum vào cuối những năm 1990
>> +Phiên bản 2x được phát hành vào năm 2000, và phiên bản 3x được phát hành vào năm 2008
>>
>
> -Phát triển: Qua nhiều phiên bản, Python ngày càng hoàn thiện với nhiều tính năng mới và cải tiến. Phiên bản Python 3 là phiên bản chính thức và được phát triển tích cực hiện nay.  
> -Phổ biến: Nhờ cú pháp rõ ràng, thư viện phong phú và cộng đồng lớn, Python được sử dụng rộng rãi trong nhiều lĩnh vực như khoa học dữ liệu, học máy, phát triển web,...

### Q2: Trình bày về lệnh hiển thị dữ liệu ra màn hình (CLI) trong Python
>
>-Cú pháp:
>
>````py
>print( *đối tượng )
>````
>
>-Mô tả:
>>Câu lệnh bắt đầu bằng Keyword (từ khóa) "print", phần trong ngoặc ( \*đối tượng ) có thể là string hoặc các loại đối tượng dữ liệu có thể chuyển thành string, nếu sử dụng để hiển thị nhiều đối tượng thì các đối tượng được phân cách bằng dấu ",".

### Q3: Trình bày câu lệnh nhập dữ liệu từ bàn phím (CLI) trong Python
>
>-Cú pháp:
>
>````py
>input( *đối tượng )
>````
>
>-Mô tả:  
>>Câu lệnh bắt đầu bằng Keyword "input", dữ liệu được nhập vào từ bàn phím sẽ được trả về đối tượng gọi (có thể là một hàm, một biến), \*đối tượng trong ngoặc của input() là một string hoặc các đối tượng dữ liệu có thể chuyển về string  
>
>+ VD:
>
>````py
>
>x = input("nhập vào giá trị của x:")
>str = "nhập vào y:"
>y= input(str)
>
>````
>
> //
>
### Q4: Trình bày về biến và cách sử dụng biến trong Python
>
>-Biến trong Python được khai báo và sử dụng khá trực tiếp so với các ngôn ngữ khác, nó không cần keyword khai báo, kiểu dữ liệu được tự nhận dạng và biến không chứa giá trị null.  
>-Biến trong Python chia ra làm biến cục bộ và biến toàn cục, chúng có thể được khai báo cùng tên.  
>-VD:
>
>````py
>//khai báo biến toàn cục
>x=10
>def func():
>    //khai báo biến cục bộ
>    x=20
>    print(x)
>func()
>print(x)
>````
>
> //  
>
> + 28/08/2024
>
>
> Viết CT nhập vào tt của 1 sinh viên (họ tên, giới tính, ngày sinh, email, quê quán, hệ số môn ngành) Hiển thị TT của HS đó, mỗi TT/dòng
>
>````py
> name = input("Nhập vào tên sinh viên: ")
> gender = input("Nhập vào giới tính: ")
> dob = input("Nhập vào ngày sinh: ")
> email = input("Nhập vào email: ")
> hometown = input("Nhập vào quê quán: ")
> gpa = input("Nhập vào hệ số môn ngành: ")
> print("Tên sinh viên: ", name)
> print("Giới tính: ", gender)
> print("Ngày sinh: ", dob)
> print("Email: ", email)
> print("Quê quán: ", hometown)
> print("Hệ số môn ngành: ", gpa)
> ````
>
> //  
> Viết CT nhập vào 2 số, hoán đổi chúng và hiển thị trên 1 dòng
>
> ````py
> a = int(input("Nhập vào số a: "))
> b = int(input("Nhập vào số b: "))
> a, b = b, a
> print(f"a = {a}, b = {b}")
> ````

## 18/09/2024  Kiểu dữ liệu danh sách (List)
>
> + K/n: Là tập hợp 1 hoặc nhiều phần tử có thể có các giá trị thuộc các kiểu dữ liệu khác nhau
> + Đặc điểm:
>>
>> + Các phần tử được đặt trong dấu ngoặc vuông '[]'
>> + Các phần tử phân cách với nhau bằng dấu phẩy ','
>> + Danh sách có khả năng chứa mọi giá trị, đối tượng trong Python
>> + Danh sách có thể chưa một danh sách khác như một phần tử của nó  
>
> + ví dụ:
>
> ````py
> l1 = [1, 2, 3, 4, 5]
> l2 = [1, "a", 3.14, True, [1, 2, 3]]
> l3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
> ````
>
> *Tạo danh sách
>
>> 1. Sử dụng lệnh gán
>> 2. Sử dụng hàm list()
>
> + VD:
>
> ````py
> l1 = [1, 2, 3, 4, 5]
> l2 = list((1, 2, 3, 4, 5))
> ````
>
> *Các toán tử với danh sách
>
> + Toán tử +: nối 2 danh sách lại với nhau
> + Toán tử *: lặp lại danh sách n lần
> + Toán tử in: kiểm tra 1 phần tử có trong danh sách hay không
> + Toán tử ==: so sánh 2 danh sách có bằng nhau hay không
>
> *Cách truy suất phần tử của danh sách
>
> 1. Truy suất 1 phần tử của danh sách
>    + tên_danh_sách[index]
> 2. Truy suất nhiều phần tử của danh sách
>    + tên_danh_sách[start:stop:step]
>
> *Các hàm làm việc với danh sách
>
> + len(): trả về số lượng phần tử của danh sách
> + max(): trả về phần tử lớn nhất của danh sách
> + min(): trả về phần tử nhỏ nhất của danh sách
> + sum(): trả về tổng của các phần tử của danh sách
> + sorted(): trả về danh sách đã được sắp xếp
> //
