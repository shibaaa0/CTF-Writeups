from bs4 import BeautifulSoup

def extract_text(svg_path):
    with open(svg_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")
    texts = soup.find_all("text")
    items = []
    for t in texts:
        x = float(t.get("x", 0))
        y = float(t.get("y", 0))
        text = t.get_text(strip=True)
        items.append((y, x, text))
    items.sort()
    return [ch for _, _, ch in items]

text0 = extract_text("1.svg")
text1 = extract_text("2.svg")

full_text = text0 + text1
code = "".join(full_text)

# Xuất thử 1000 ký tự đầu tiên
print(code[:1000])
