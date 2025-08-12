import ast

min_vals = [999999] * 32
count = 0

with open("output.txt", "r") as f:
    for line in f:
        line = line.strip()

        # Tìm đoạn list nếu có
        if '[' in line and ']' in line:
            try:
                start = line.index('[')
                end = line.index(']', start) + 1
                list_str = line[start:end]
                nums = ast.literal_eval(list_str)

                if isinstance(nums, list) and len(nums) == 32:
                    for i in range(32):
                        min_vals[i] = min(min_vals[i], nums[i])
                    count += 1
            except Exception as e:
                continue

print(f"✅ Đã xử lý {count} list.")
secret_str = ''.join(chr(v) for v in min_vals)
print(f"🔐 Secret khôi phục được: {secret_str}")
