"""
    1. Phân tích thiết kế (Code Review & Architecture)
    Refactoring Plan
    1. Đặt tên biến chuẩn PEP8

    Code cũ:

    ds = []
    p = {}
    l = 5000

    Refactor:

    roster_list = []
    player = {}
    salary = 5000

    Áp dụng:

    snake_case cho biến, hàm.
    Tên thể hiện đúng ý nghĩa.
    Không dùng tên viết tắt khó hiểu.
    2. Single Responsibility Principle

    Mỗi hàm chỉ xử lý một nhiệm vụ:

    Ví dụ:

    display_roster()

    chỉ hiển thị đội hình.

    calculate_actual_pay()

    chỉ tính lương thực nhận.

    3. Docstring cho toàn bộ function

    Ví dụ:

    def calculate_actual_pay(player):
        
        Tính lương thực nhận của tuyển thủ.

        Args:
            player(dict): dữ liệu tuyển thủ

        Returns:
            float: số tiền nhận được
        
    Logging Strategy

    File log:

    roster_app.log

    Format:

    [Thời gian] - [Level] - [Message]

    Ví dụ:

    [2026-06-04 09:10:15] - [INFO] - Coach viewed the team roster.
    Phân tích hàm update_player_status()
    Input
    roster_list : list

    Danh sách tuyển thủ.

    Người dùng nhập:

    player_id
    choice update
    salary/status mới
    Output

    Cập nhật dictionary:

    Ví dụ:

    {
    "player_id":"P01",
    "salary":5500,
    "status":"Active"
    }
"""

import logging


# =====================
# LOG CONFIG
# =====================

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)



# =====================
# DATA
# =====================

roster = [

    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },

    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },

    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]



# =====================
# HELPER
# =====================


def calculate_actual_pay(player):
    """
    Tính lương thực nhận.

    Args:
        player(dict): thông tin tuyển thủ

    Returns:
        float
    """

    if player["status"] == "Benched":

        return player["salary"] * 0.5


    return player["salary"]




def find_player(roster_list, player_id):
    """
    Tìm tuyển thủ theo ID.

    Args:
        roster_list(list)
        player_id(str)

    Returns:
        dict hoặc None
    """

    for player in roster_list:

        if player["player_id"] == player_id:

            return player

    return None




# =====================
# FUNCTION 1
# =====================


def display_roster(roster_list):
    """
    Hiển thị đội hình.
    """

    logging.info(
        "Coach viewed the team roster."
    )


    if not roster_list:

        print(
            "Đội hình hiện đang trống."
        )

        return



    print(
        "\n--- ĐỘI HÌNH RIKKEI ESPORTS ---"
    )


    print(
        f"{'ID':8}| "
        f"{'Tên tuyển thủ':20}| "
        f"{'Vị trí':15}| "
        f"{'Lương':12}| "
        f"Trạng thái"
    )


    print("-"*80)



    for player in roster_list:


        try:

            name = player["name"]


            if player["status"] == "Benched":

                name += " [DỰ BỊ]"



            print(

                f"{player['player_id']:8}| "
                f"{name:20}| "
                f"{player['role']:15}| "
                f"{player['salary']:12,.1f}| "
                f"{player.get('status','Unknown')}"

            )


        except KeyError:

            print(
                "Dữ liệu tuyển thủ lỗi."
            )




# =====================
# FUNCTION 2
# =====================


def sign_player(roster_list):
    """
    Chiêu mộ tuyển thủ mới.
    """

    print(
        "\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---"
    )


    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()



    if find_player(roster_list, player_id):

        logging.warning(
            f"Failed to sign player - Duplicate player ID {player_id}"
        )


        print(
            f"Mã tuyển thủ {player_id} đã tồn tại."
        )

        return



    name = input(
        "Nhập tên tuyển thủ: "
    ).strip()


    role = input(
        "Nhập vị trí thi đấu: "
    ).strip()



    while True:

        try:

            salary = float(
                input(
                    "Nhập mức lương hàng tháng: "
                )
            )


            if salary <= 0:

                print(
                    "Lương phải là số dương."
                )

                continue


            break



        except ValueError:

            logging.warning(
                "Failed to sign player - Invalid salary input"
            )

            print(
                "Lương phải là số."
            )




    new_player = {

        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"

    }



    roster_list.append(new_player)


    logging.info(
        f"Signed new player {name} with salary {salary}"
    )


    print(
        f"Thành công: Đã chiêu mộ tuyển thủ {name}"
    )




# =====================
# FUNCTION 3
# =====================


def update_player_status(roster_list):
    """
    Cập nhật lương hoặc trạng thái.
    """


    player_id = input(
        "Nhập mã tuyển thủ cần cập nhật: "
    ).strip().upper()



    player = find_player(
        roster_list,
        player_id
    )



    if not player:


        logging.warning(
            f"Failed to update player - Player ID {player_id} not found"
        )


        print(
            "Không tìm thấy tuyển thủ."
        )

        return




    print(player)



    print(
        """
1. Cập nhật lương
2. Cập nhật trạng thái
"""
    )



    choice = input(
        "Chọn: "
    )



    try:


        if choice == "1":


            old_salary = player["salary"]


            while True:

                salary = float(
                    input(
                        "Nhập lương mới: "
                    )
                )


                if salary <= 0:

                    print(
                        "Lương phải >0"
                    )

                    continue


                break



            player["salary"] = salary



            logging.info(

                f"Updated player {player_id} salary "
                f"from {old_salary} to {salary}"

            )



        elif choice == "2":


            status = input(
                "Nhập Active/Benched: "
            )


            player["status"] = status



            logging.info(
                f"Updated player {player_id} status"
            )



    except ValueError as error:


        logging.error(error)



# =====================
# FUNCTION 4
# =====================


def generate_payroll_report(roster_list):
    """
    Tạo báo cáo quỹ lương.
    """


    total = 0



    print(
        "\n--- BÁO CÁO QUỸ LƯƠNG ---"
    )


    if not roster_list:

        print(
            "Đội hình hiện đang trống. Tổng quỹ lương: 0.0"
        )

        return



    for player in roster_list:


        try:


            actual_pay = calculate_actual_pay(
                player
            )


            total += actual_pay



            print(

                player["player_id"],
                player["name"],
                player["status"],
                player["salary"],
                actual_pay

            )



        except KeyError as error:


            logging.error(
                f"Missing key while generating payroll report: {error}"
            )

            print(
                "Lỗi: Một tuyển thủ đang bị thiếu dữ liệu."
            )




    print(
        f"Tổng quỹ lương hàng tháng: {total}"
    )


    logging.info(
        f"Generated monthly payroll report. Total: {total}"
    )





# =====================
# MENU
# =====================


def main():

    while True:


        print(
            """
===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====

1. Xem đội hình
2. Chiêu mộ tuyển thủ
3. Cập nhật lương & trạng thái
4. Báo cáo quỹ lương
5. Thoát

"""
        )


        try:


            choice = int(
                input("Chọn chức năng: ")
            )



            if choice == 1:

                display_roster(roster)


            elif choice == 2:

                sign_player(roster)


            elif choice == 3:

                update_player_status(roster)


            elif choice == 4:

                generate_payroll_report(roster)


            elif choice == 5:


                logging.info(
                    "System closed."
                )

                break


        except ValueError:


            logging.warning(
                "Invalid menu choice"
            )



if __name__ == "__main__":

    main()