def calculate_change(payment, cost):
    charge = payment - cost
    money50000 = int(charge / 50000)
    charge = charge - money50000 * 50000
    money10000 = int(charge / 10000)
    charge = charge - money10000 * 10000
    money5000 = int(charge / 5000)
    charge = charge - money5000 * 5000
    money1000 = int(charge / 1000)

    print("50000원 지폐: %d장" %(money50000))
    print("10000원 지폐: %d장" %(money10000))
    print("5000원 지폐: %d장" %(money5000))
    print("1000원 지폐: %d장" %(money1000))

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)