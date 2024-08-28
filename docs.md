##### 28/08/2024

# Chương 1: Giới thiệu NN lập trình Python

### Q1: Nêu 3 điểm mấu chốt về quá trình hình thành và phát triển của Python

> -Nguồn gốc: Python được tạo ra bởi Guido van Rossum vào cuối những năm 1980 với mục tiêu tạo ra một ngôn ngữ dễ học, dễ sử dụng và mạnh mẽ.  
> -Phát triển: Qua nhiều phiên bản, Python ngày càng hoàn thiện với nhiều tính năng mới và cải tiến. Phiên bản Python 3 là phiên bản chính thức và được phát triển tích cực hiện nay.  
> -Phổ biến: Nhờ cú pháp rõ ràng, thư viện phong phú và cộng đồng lớn, Python được sử dụng rộng rãi trong nhiều lĩnh vực như khoa học dữ liệu, học máy, phát triển web,...

### Q2: Trình bày về lệnh hiển thị dữ liệu ra màn hình (CLI) trong Python
>-Cú pháp:
>````py
>print( *đối tượng )
>````
>-Mô tả:
>>Câu lệnh bắt đầu bằng Keyword (từ khóa) "print", phần trong ngoặc ( \*đối tượng ) có thể là string hoặc các loại đối tượng dữ liệu có thể chuyển thành string, nếu sử dụng để hiển thị nhiều đối tượng thì các đối tượng được phân cách bằng dấu ",".

### Q3: Trình bày câu lệnh nhập dữ liệu từ bàn phím (CLI) trong Python
>-Cú pháp:
>````py
>input( *đối tượng )
>````
>-Mô tả:  
>>Câu lệnh bắt đầu bằng Keyword "input", dữ liệu được nhập vào từ bàn phím sẽ được trả về đối tượng gọi (có thể là một hàm, một biến), \*đối tượng trong ngoặc của input() là một string hoặc các đối tượng dữ liệu có thể chuyển về string  
>+ VD:
>````py
>x = input("nhập vào giá trị của x:")
>str = "nhập vào y:"
>y= input(str)
>````
> //
### Q4: Trình bày về biến và cách sử dụng biến trong Python
>-Biến trong Python được khai báo và sử dụng khá trực tiếp so với các ngôn ngữ khác, nó không cần keyword khai báo, kiểu dữ liệu được tự nhận dạng và biến không chứa giá trị null.  
>-Biến trong Python chia ra làm biến cục bộ và biến toàn cục, chúng có thể được khai báo cùng tên.  
>-VD:
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
> //

