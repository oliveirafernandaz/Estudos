from datetime import date
byear = int(input('Qual foi o ano de seu nascimento? '))
cyear = date.today().year
ryear = cyear - 18
#print(current_year)
if byear == ryear :
    print(f'Está na hora de você se alistar!')
elif byear < ryear :
    print(f'Você deveria ter se alistado há {cyear - byear - 18} anos.')
elif byear > ryear :
    print(f'Você ainda não está pronto para se alistar. Seu alistamento será daqui a {(cyear - byear - 18) * -1} anos')
