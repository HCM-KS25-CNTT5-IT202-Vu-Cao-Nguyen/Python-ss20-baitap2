# Dữ liệu từ API: (Tên, Số trận, MMR)
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),            # Thiếu MMR
    ("Optimus", 100, "N/A")   # MMR không hợp lệ
]


def calculate_bonus(matches, mmr):
    """
    Tính tiền thưởng RP.
    Bonus = (Số trận * 10) + (MMR * 0.5)
    """
    return (matches * 10) + (mmr * 0.5)


def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:

        # Debug (có thể bật khi cần)
        # print("Đang xử lý:", record)

        player_name = record[0]

        try:
            matches = record[1]
            mmr = record[2]

            mmr = int(mmr)

            bonus = calculate_bonus(matches, mmr)

            print(
                f"Tuyển thủ {player_name} nhận được {bonus} RP"
            )

        except IndexError:
            print(
                f"{player_name}: Lỗi - Hồ sơ bị thiếu thông tin!"
            )
            continue

        except ValueError:
            print(
                f"{player_name}: Lỗi - Dữ liệu MMR không hợp lệ!"
            )
            continue


# Chạy chương trình
process_bonus(player_records)