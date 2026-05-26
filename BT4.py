print("--- CHƯƠNG TRÌNH VÒNG QUAY MAY MẮN - RIKKEI STORE ---")
print("Chào mừng Khách hàng VIP đến với minigame 'Đoán số may mắn'!")
print("Quy tắc: Bạn có tối đa 5 lượt để đoán chính xác 'Mã số bí ẩn'.\n")




is_won = False


for turn in range(1, 6):
    print(f"--- Lượt đoán thứ {turn}/5 ---")
    guess = int(input("Nhập số dự đoán của bạn: "))
    

    if guess == SECRET_NUMBER:
        print("Xuất sắc! Bạn đã đoán chính xác mã số bí ẩn.")
        is_won = True
        break 
    elif guess > SECRET_NUMBER:
        print("Gợi ý: Số bạn vừa nhập LỚN HƠN mã số may mắn của hệ thống.\n")
    else:
        print("Gợi ý: Số bạn vừa nhập NHỎ HƠN mã số may mắn của hệ thống.\n")


print("="*40)
print("--- KẾT QUẢ CHƯƠNG TRÌNH ---")
if is_won:
    print("CHÚC MỪNG! Bạn đã trúng thưởng phần quà đặc biệt từ Rikkei Store! 🎁")
else:
    print(f"Rất tiếc, bạn đã hết cả 5 lượt đoán. Mã số bí ẩn là: {SECRET_NUMBER}")
    print("Chúc bạn may mắn lần sau! 🍀")
print("="*40)