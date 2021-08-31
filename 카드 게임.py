# 기계와 다른 숫자를 가지고 있는 카드 게임

# Jay와 Emily가 5장의 숫자 카드 선택
Jay = set(input("Jay가 선택한 카드 (1~9에서 5장) : ").split())
Emily = set(input("Emily가 선택한 카드 (1~9에서 5장) : ").split())

# 기계가 3장의 숫자 카드 선택
Machine = set(input("기계가 선택한 카드 (1~9에서 3장) : ").split())

# 기계에서 제시된 숫자 카드 버리기
# Jay = Jay & Machine
Jay = (Jay.difference(Machine))
# Emily = Emily & Machine
Emily = (Emily.difference(Machine))

# 더 많은 카드를 가지고 있는 사람이 승리
if len(Jay) > len(Emily) :
    print(f"Jay 대 Emily는 {len(Jay)}:{len(Emily)}로 Jay 승!" )
elif len(Jay) < len(Emily) :
    print(f"Emily 대 Jay는 {len(Emily)}:{len(Jay)}로 Emily 승!" )
else :
    print("무승부입니다!")