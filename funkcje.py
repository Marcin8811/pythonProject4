def witaj(imie):
    print(f"Witaj {imie}!")

def idz_umyj_rece(jak_brudne):
    if jak_brudne in ['czyste', 'lekko', 'bardzo']:
        print("Idę umyć ręce!")
    if jak_brudne =='czyste':
        print('Po co przychodzisz do łazienki jak masz czyste ręce?')
    elif jak_brudne == 'lekko':
        print('Myję ręce mydłem zapachowym')
    elif jak_brudne == 'bardzo':
        print('Myję ręce pastą bhp!')
    else:
        print("Sprecyzuj jak brudne masz ręce!")

#witaj(input("Podaj swoje imie: "))

idz_umyj_rece(input("Jak brudne masz ręce? (czyste/lekko/bardzo): "))

