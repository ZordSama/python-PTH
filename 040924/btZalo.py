# Theo quy định của nhà trường, mỗi trường hợp không đeo thẻ học sinh sẽ bị trừ a điểm thi đua của lớp, mỗi trường hợp nói chuyện trong lớp bị trừ b điểm thi đua và mỗi trường hợp đi học muộn bị trừ c điểm. Sổ đầu bài ghi nhận trong tháng có t trường hợp không đeo thẻ, n trường hợp nói chuyện riêng và m trường hợp đi học muộn. Hãy nhập các giá trị a, b, c, t, n, m từ bàn phím và tính tổng điểm bị trừ thi đua trong tháng đó.
a = int(input("nhập số điểm bị trừ với mỗi trường hợp không đeo thẻ HS: "))
b = int(input("nhập số điểm bị trừ với mỗi trường hợp nói chuyện riêng trong lớp: "))
c = int(input("nhập số điểm bị trừ với mỗi trường hợp đi học muộn: "))
t = int(input("nhập tổng số trường hợp không đeo thẻ HS trong tháng: "))
n = int(input("nhập tổng số trường hợp nói chuyện riêng trong tháng: "))
m = int(input("nhập tổng số trường hợp đi học muộn trong tháng: "))
print("tổng số điểm thi đua bị trừ trong tháng là: ", a*t + b*n + c*m)










