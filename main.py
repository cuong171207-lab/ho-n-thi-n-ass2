import product_manager as pm


def print_menu():
    print("\n=========== MENU ===========")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("6. Lưu dữ liệu")
    print("0. Thoát chương trình")
    print("============================")


def main():
    print("CHÀO MỪNG ĐẾN VỚI HỆ THỐNG QUẢN LÝ POLYLAP")

    # 1. Tải dữ liệu khi khởi động
    products = pm.load_data()
    print(f"Đã tải {len(products)} sản phẩm từ hệ thống.")

    # Ánh xạ lựa chọn với hàm xử lý tương ứng
    menu_actions = {
        "1": pm.display_all_products,
        "2": pm.add_product,
        "3": pm.update_product,
        "4": pm.delete_product,
        "5": pm.search_product_by_name,
        "6": pm.save_data,
    }

    while True:
        print_menu()

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "0":
            print("Đang lưu dữ liệu trước khi thoát...")
            pm.save_data(products)
            print("Cảm ơn bạn đã sử dụng phần mềm POLYLAP. Tạm biệt!")
            break
        elif choice in menu_actions:
            # Các chức năng 2, 3, 4 có thay đổi dữ liệu nên cần cập nhật lại biến products
            if choice in ["2", "3", "4"]:
                products = menu_actions[choice](products)
            else:
                menu_actions[choice](products)
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")


if __name__ == "__main__":
    main()
