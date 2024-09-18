def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}h:{minutes:02d}m:{seconds:02d}s"


s = int(input("Nhập số giây: "))
if s < 0:
    print("Số giây không hợp lệ")
    exit()
print(f"{s} giây = {seconds_to_time(s)}")
