import random

BO_CAU_HOI_FILE_NAME ='bo_cau_hoi.txt'
CAU_TRA_LOI_FILE_NAME ='cau_tra_loi.txt'
PHAN_THUONG_FILE_NAME ='giai_thuong.txt'

BO_CAU_HOI = BO_CAU_HOI_FILE_NAME
CAU_TRA_LOI = CAU_TRA_LOI_FILE_NAME
PHAN_THUONG = PHAN_THUONG_FILE_NAME

with open(BO_CAU_HOI,'r',encoding='utf-8') as f:
    BO_CAU_HOI_LIST =f.readlines()

with open(CAU_TRA_LOI,'r',encoding='utf-8') as f:
    CAU_TRA_LOI_LIST =f.readlines()

with open(PHAN_THUONG,'r',encoding='utf-8') as f:
    PHAN_THUONG_LIST =f.readlines()

def ViTri():
    while True:
        x = random.randint(0, 18)
        if x not in ViTriCu:
            ViTriCu.append(x)
            break
    return x

ViTriCu = []
Help = [1]

while True:
    for i in range(0,15):
        a = ViTri()
        print(BO_CAU_HOI_LIST[a])      
        Answer = input("Nhập câu trả lời:")
        if Answer.strip().upper() == CAU_TRA_LOI_LIST[a].strip().upper():
            if i == 14:
                print(f"Chúc mừng bạn đã hoàn thành tất cả câu hỏi! Giải thưởng của bạn là {PHAN_THUONG_LIST[i]}")
            print("Chúc mừng bạn đã trả lời đúng!")        
            print("Giải thưởng hiện tại của bạn là:", PHAN_THUONG_LIST[i])
            Continue = input("Bạn có muốn đi tiếp không? (Y/N):")
            if Continue.strip().upper() == "Y":
                continue
            if Continue.strip().upper() == "N":
                print(f'Cảm ơn bạn đã tham gia trò chơi! Giải thưởng của bạn là {PHAN_THUONG_LIST[i]}')
                break
        else:
            print("Bạn đã trả lời sai!")
            if i == 0:
                print("Bạn đã sai câu hỏi đầu tiên nên không có phần thưởng!")
            else:
                print("Cảm ơn bạn đã tham gia trò chơi! Phần thưởng của bạn là 100.000đ")
            break
    break