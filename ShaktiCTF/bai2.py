def hex_to_ascii_and_reverse(hex_string):
    """
    Chuyển đổi chuỗi hex thành ASCII và đảo ngược chuỗi kết quả.
    Ví dụ: '746369746b616873' -> 'tcitkahs' -> 'shaktict'
    """
    # Loại bỏ tiền tố '0x' nếu có
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]

    # Đảm bảo chuỗi hex có số lượng ký tự chẵn
    if len(hex_string) % 2 != 0:
        print(f"Cảnh báo: Chuỗi hex '{hex_string}' có độ dài lẻ. Có thể gây lỗi.")
        return ""

    ascii_chars = []
    for i in range(0, len(hex_string), 2):
        hex_pair = hex_string[i:i+2]
        try:
            # Chuyển đổi cặp hex sang số nguyên, sau đó sang ký tự ASCII
            ascii_char = chr(int(hex_pair, 16))
            ascii_chars.append(ascii_char)
        except ValueError:
            print(f"Lỗi: Không thể chuyển đổi cặp hex '{hex_pair}' thành ASCII hợp lệ.")
            return ""

    # Ghép các ký tự ASCII lại thành chuỗi
    forward_string = "".join(ascii_chars)
    # Đảo ngược chuỗi
    reversed_string = forward_string[::-1]
    return reversed_string

# Danh sách các chuỗi hex đầu vào
hex_inputs = [
    "0x746369746b616873",
    "0x58655f3368747b66",
    "0x5f64337463407274",
    "0x656974696c696240",
    "0x6873316e40765f35",
    "0x3368745f7475625f",
    "0x33725f67406c665f",
    "0x7d736e31406d"
]

# Danh sách để lưu trữ các chuỗi đã xử lý
processed_strings = []

# Xử lý từng chuỗi hex và lưu kết quả
for hex_str in hex_inputs:
    reversed_ascii = hex_to_ascii_and_reverse(hex_str)
    if reversed_ascii: # Chỉ thêm vào nếu quá trình chuyển đổi thành công
        processed_strings.append(reversed_ascii)

# Ghép tất cả các chuỗi đã xử lý lại thành một chuỗi duy nhất
final_combined_string = "".join(processed_strings)

print("---")
print("Các chuỗi sau khi chuyển đổi và đảo ngược:")
for i, s in enumerate(processed_strings):
    print(f"{i+1}. {s}")
print("---")
print("Chuỗi cuối cùng sau khi ghép nối:")
print(f"{final_combined_string}")
