celcius = input("masukkan suhu celcius : ")
try:
    valinput = float(celcius)
    print('suhu celcius adalah', round(valinput, 2))
    reamur = (4/5) * valinput
    print('reamurnya adalah : ', round(reamur, 2))
    fahrenheit = (9/5) * valinput + 32
    print('fahrenheit adalah : ', round(fahrenheit, 2))
    kelvin = valinput + 273
    print('kelvinnya adalah : ', round(kelvin, 2))
except ValueError:
    print ("Input harus berupa angka")