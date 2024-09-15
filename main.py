import random

BO_CAU_HOI_LIST = ['Có câu thành ngữ: "Đi mây về ..." gì? --- ⬥ A: Mây\t⬥ B: Núi\t⬥ C: Biển\t⬥ D: Gió\n', 'Đâu là một cách nói ví von về những trường hợp gặp vận hạn, rủi ro? --- ⬥ A: Sao quả cân\t⬥ B: Sao quả tạ\t\t⬥ C: Sao quả tấn\t⬥ D: Sao quả yến\n', 'Gỗ mun có màu gì? --- ⬥ A: Vàng\t\t⬥ B: Nâu\t⬥ C: Đen\t⬥ D: Xanh\n', 'Câu nào chỉ tình cảnh đơn độc, yếu thế không có chỗ dựa? --- ⬥ A: Thân tàn ma dại\t⬥ B: Thân cô thế cô\t⬥ C: Thân lừa ưa nặng\t\t⬥ D: Thân làm tội đời\n', 'Đâu là tên một loại đồ chơi dân gian của trẻ em? --- ⬥ A: Tò he\t\t⬥ B: Tò mò\t⬥ C: Tò vò\t⬥ D: Tến tò\n', 'Đâu là tên một bãi biển ở Quảng Bình? --- ⬥ A: Đá Lăn\t⬥ B: Đá Nhảy\t⬥ C: Đá Chạy\t⬥ D: Đá Bò\n', 'Đâu là tên một loại chợ? --- ⬥ A: Ếch\t⬥ B: Nhái\t⬥ C: Thằn lằn\t⬥ D: Cóc\n', 'Tượng đài Chiến thắng Điện Biên Phủ được dựng trên ngọn đồi nào? --- \t⬥ A: D1\t\t⬥ B: C1\t\t⬥ C: A1\t\t⬥ D: E1\n', 'Nhà văn Kim Dung (Trung Quốc) nổi tiếng với thể loại văn học gì? --- \t⬥ A: Truyện trinh thám\t\t⬥ B: Tiểu thuyết kiếm hiệp\t⬥ C: Sử thi\t⬥ D: Thơ lãng mạn\n', 'Bộ phim "Chị Dậu" được chuyển thể từ tác phẩm nào? --- \t⬥ A: Người mẹ cầm súng\t\t⬥ B: Vợ chồng A Phủ\t⬥ C: Tắt đèn\t⬥ D: Tuổi thơ dữ dội\n', 'Loại cá nào bé hơn cả? ---\t⬥ A: Voi\t⬥ B: Bống\t⬥ C: Mập\t⬥ D: Heo\n', 'Giọng khàn khàn còn được ví với gì? ---\t⬥ A: Thiên nga\t\t⬥ B: Vịt đực\t⬥ C: Ngan xiêm\t\t⬥ D: Ngỗng\n', 'Sầu riêng Cái Mơn là đặc sản của tỉnh nào? ---\t⬥ A: Tiền Giang\t\t⬥ B: Cà Mau\t⬥ C: Bến Tre\t⬥ D: Đồng Tháp\n', 'Loại củ nào sau đây có thể giúp cho vết thương mau lành và ít để lại sẹo? ---\t⬥ A: Giềng\t⬥ B: Hành tây\t\t⬥ C: Gừng\t⬥ D: Nghệ\n', 'Cướp biển còn được gọi với tên khác là gì? ---⬥ A: Đạo tặc\t⬥ B: Lâm tặc\t⬥ C: Tin tặc\t⬥ D: Hải tặc\n', 'Hoa hậu Hòa bình Quốc tế 2017 dự kiến sẽ được tổ chức tại quốc gia nào? ---\t⬥ A: Thái Lan\t⬥ B: Việt Nam\t⬥ C: Lào\t⬥ D: Campuchia\n', 'Vườn quốc gia nào hiện không nằm trong danh sách Vườn di sản ASEAN? ---\t⬥ A: Vườn quốc gia Kon Ka Kinh\t⬥ B: Vườn quốc gia Tam Đảo\t⬥ C: Vườn quốc gia Chư Mom Ray\t⬥ D: Vườn quốc gia Bái Tử Long\n', 'Nhạc sĩ nào là người phổ nhạc ca khúc "Cây đàn sinh viên"? ---\t⬥ A: Bảo Chấn\t⬥ B: Trịnh Công Sơn\t⬥ C: Quốc An\t⬥ D: Trần Tiến\n', 'Đâu không phải là một tác phẩm của họa sĩ Trần Văn Cẩn? --- ⬥ A: Đôi bạn\t⬥ B: Mẹ tôi\t⬥ C: Em Thúy\t⬥ D: Em gái tôi']
CAU_TRA_LOI_LIST = ['D\n', 'B\n', 'C\n', 'B\n', 'A\n', 'B\n', 'D\n', 'C\n', 'B\n', 'C\n', 'B\n', 'B\n', 'C\n', 'D\n', 'D\n', 'B\n', 'B\n', 'C\n', 'A']
GIAI_THUONG_LIST = ['   100.000  \n', '150.000\n', '300.000\n', '600.000\n', '1.000.000\n', '2.500.000\n', '6.000.000\n', '11.000.000\n', '22.000.000\n', '35.000.000\n', '66.000.000\n', '99.000.000\n', '120.000.000\n', '250.000.000\n', '500.000.000']


CAU_TRA_LOI_LIST_ADJUST = []
for i in CAU_TRA_LOI_LIST:
    CAU_TRA_LOI_LIST_ADJUST.append(i.strip())

GIAI_THUONG_LIST_ADJUST = []
for j in GIAI_THUONG_LIST:
    GIAI_THUONG_LIST_ADJUST.append(j.strip())

CAU_HOI_DA_RA = []
SO_THU_TU = 0
for i in range(5):
    print("Cau hoi thu {}".format(SO_THU_TU + 1))
    VI_TRI_CAU_HOI = random.randint(1, 18)

    while VI_TRI_CAU_HOI in CAU_HOI_DA_RA:
        VI_TRI_CAU_HOI = random.randint(1, 18)

    print(BO_CAU_HOI_LIST[VI_TRI_CAU_HOI])
    user_answer = input("Nhap vao cau tra loi cua ban: ")
    if user_answer.lower() == (CAU_TRA_LOI_LIST_ADJUST[VI_TRI_CAU_HOI]).lower():
        print("""
    Xin chuc mung, ban da tra loi dung!
    ---> Giai thuong cua ban luc nay la {}d !!!
                """.format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))

        if SO_THU_TU == 4:
            print("Chuc mung ban da hoan thanh tro choi voi tong giai thuong la {} dong!!!".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU]))
        else:
            SO_THU_TU += 1
            CHOI_TIEP = input("Ban co muon tiep tuc?  (Yes/No): ")
            if CHOI_TIEP.lower() == 'yes':
                CAU_HOI_DA_RA.append(VI_TRI_CAU_HOI)
                continue
            else:
                print("Chuc mung ban da hoan thanh tro choi voi tong giai thuong la {} dong!!!".format(GIAI_THUONG_LIST_ADJUST[SO_THU_TU - 1]))
                break
    else:
        if SO_THU_TU == 0:
            print("""
        That dang tiec, ban da tra loi sai cau hoi nay!
        ---> Vi sai cau hoi dau tien, ban khong nhan duoc giai thuong!
                  """)
            break
        else:
            print("""
        That dang tiec, ban da tra loi sai cau hoi nay!
        ---> Giai thuong cua ban luc nay tro ve {} dong !!!
                    """.format(GIAI_THUONG_LIST_ADJUST[0]))
            break
 