import os
import re

folder_path = "C:/Users/parkn/Documents/Warcraft III/CustomMapData/ORDR1"  # 적절한 경로로 변경

print("🔍 스크립트 실행 시작...")

file_pattern = re.compile(r'ordr1_parknam5125_(\d{3})')

files = []
for filename in os.listdir(folder_path):
    match = file_pattern.match(filename)
    if match:
        files.append((filename, int(match.group(1))))


if not files:
    print("해당 폴더에 적절한 파일이 없습니다.")
    exit()

files.sort(key=lambda x: x[1], reverse=True)
latest_file = files[0][0]

print(f"📄 가장 최신 파일: {latest_file}")

found = False

with open(os.path.join(folder_path, latest_file), "r", encoding="utf-8") as file:
    for line in file:
        if "-load" in line:  
            # 정규식으로 '-load' 뒤의 값만 추출
            match = re.search(r'(-load\s+[\S]+)', line)
            if match:
                clean_text = match.group(0).rstrip('"')  # 마지막 " 제거
                print(f"✅ 찾은 값: {clean_text}")
                found = True
                break

if not found:
    print("❌ '-load'로 시작하는 라인을 찾지 못했습니다.")

input("Press Enter to exit...")