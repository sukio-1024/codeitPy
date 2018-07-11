RATE = 1.12
miran = 1100000000
price = 50000000
year = 1988
dongil = price
choice = ""
gap = 0

while (year != 2016):
    dongil *= RATE
    year += 1

if (dongil > miran):
    choice = "동일 아저씨"
    gap = dongil - miran
else:
    choice ="미란 아주머니"
    gap = miran - dongil

print("%d원 차이로 %s의 말씀이 맞습니다." %(gap, choice))