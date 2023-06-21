km = float(input('\033[35mUma distância em metros: \033[0;34;4m'))
print('''\033[0;35mA media de {:.1f}m corresponde a
{}km
{}hm
{}dam
{}dm
{}cm
{}mm'''.format(km , km/1000 , km/100 , km/10 , km*10 , km*100 , km*1000))