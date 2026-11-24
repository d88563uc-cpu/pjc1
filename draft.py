import csv

data = [
    ["họ và tên", "điểm số"],
    ["Nguyễn Văn A",8.5],
    ["Nguyễn Văn B", 9],
    ["Phạm Thị Ngọc A",7.5],
    ["Phạm Thị Ngọc B",8],
    ["Rách Khang",1],
]

with open("students.csv",mode='w',encoding= "utf-8-sig",newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

def record_score(score):
    class InvalidScoreError:
     pass
    if not (0 <= score <= 100):
     raise InvalidScoreError(f"{score} is not between 0 and 100")
    return score