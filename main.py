from time import sleep

zaman = input("süreyi girin:")

try:
    zamanInt = int(zaman)

    for i in range(zamanInt,0,-1):
        print(i)
        sleep(1)
    print("süre bitti :)")

except:
    print("sayı ile giriniz!")