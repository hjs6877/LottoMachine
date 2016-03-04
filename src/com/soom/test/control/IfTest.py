print('무얼 타고 가시겠습니까? 버스는 1, 택시는 2, 자가용은 3을 입력하세요: ')
vehicle = input()
if vehicle == "1":
    print("버스를 선택하셨습니다.")
elif vehicle == "2":
    print("택시를 선택하셨습니다.")
elif vehicle == "3":
    print("자가용을 선택하셨습니다.")
else:
    print("그냥 걸어가세요")