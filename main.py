import os
import sys

line = "My phone's battery is green at 20%, red at 19%, and gone at 18% \u2014 my phone does maths like a gambler."

print(line)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)

data = line.encode("utf-8")
assert 1 <= len(data) <= 200, f"entry must be 1-200 bytes, got {len(data)}"
assert len(line.strip()) > 0
sys.exit(0)
