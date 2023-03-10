city = str(input('Em qual cidade você nasceu? ')).strip()
splcity = city.split()
fcity = splcity[0]
fcitylow = fcity.lower()
santcity = 'santo'

#print(fcity)
if fcitylow != santcity :
    print(False)
else:
    print(True)
