while True:
    try:
        ocjena = float(input("Unesite ocjenu između 0.0 i 1.0\n"))
        if 0.0<=ocjena<=1.0:
            break
        else:
            raise ValueError

    except ValueError:
        print("Izvan granica!")

if ocjena>=0.9:
    print("Ocjena: A")
elif ocjena>=0.8:
    print("Ocjena: B")
elif ocjena>=0.7:
    print("Ocjena: C")
elif ocjena>=0.6:
    print("Ocjena: D")
elif ocjena<0.6:
    print("Ocjena: F")