temperatura = int(input("Podaj temperaturę: "))

HOT_TEMPERATURA = 30
WARM_TEMPERATURA = 25
MILD_TEMPERATURA = 20

if (temperatura >= HOT_TEMPERATURA):
    print("Jest gorąco")

elif (temperatura >= WARM_TEMPERATURA):
    print("Jest ciepło")

elif (temperatura >= MILD_TEMPERATURA):
    print("Ani ciepło ani zimno")

else:
    print("Jest zimno")
