wage = 5
exchange_rate = 1142.16

print("%d 시간에 %d%s 벌었습니다." % (1, wage * 1, "달러"))
print("%d 시간에 %d%s 벌었습니다." % (5, wage * 5, "달러"))
print("%d 시간에 %.1f%s 벌었습니다." % (1, wage * exchange_rate, "원"))
print("%d 시간에 %.1f%s 벌었습니다." % (5, wage * exchange_rate * 5, "원"))
