wyp1 = ['Proszę zwrócić uwagę, że', 'I tak mam trzy razy mniej czasu, więc pozwolić powiedzieć:', 'Ja nie potrzebowałem edukacji seksualnej, żeby wiedzieć, że', 'No niestety:', 'Gdzie leży przyczyna problemu? Ja państwu powiem:', 'Państwo chyba nie widzą, że', 'Oświadczam kategorycznie:', 'Powtarzam:', 'Powiedzmy to z całą mocą', 'W polsce dzisiaj', 'Państwo sobie nie zdają sprawy, że', 'To ja przepraszam bardzo:', 'Otóż nie wiem, czy pan wie, że', 'Yyyyy...', 'Ja chcę powiedzieć jedną rzecz:', 'Trzeba powiedzieć jasno:', 'Jak powiedział wybitny krakowianin Stanisław Lem,', 'Proszę mnie dobrze zrozumieć:', 'Ja chciałem państwu przypomnieć, że', 'Niech państwo nie mają złudzeń:', 'Powiedzmy to wyraźnie:']

wyp2 = ['własciciele niewolników', 'związkowcy', 'trockiści', 'tak zwane dzieci kwiaty', 'rozmaici urzędnicy', 'federaści', 'etatyści', 'ci durnie i zlodzieje', 'ludzie wybrani głosami meneli spod budki z piwem', 'socjaliści pobożni', 'socjaliści bezbożni', 'komuniści z krzyżem w zębach', 'agenci obcych służb', 'członkowie Bandy Czworga', 'pseudo-masoni z Wielkiego Wschodu Francji', 'przedstawiciele czerwonej hołoty', 'ci wszyscy *tfu* geje', 'funkcjonariusze reżimowej telewizji', 'tak zwani ekolodzy', 'ci wszyscy *tfu* demokraci', 'agenci bezpieki', 'feminazistki']

wyp3 = ['po przeczytaniu Manifestu komunistycznego', 'którymi się brzydzę', 'których nienawidzę', 'z okolic "Gazety Wyborczej"', 'czyli taka żydokomuna', 'odkąd zniesiono karę śmierci', 'którymi pogardzam', 'których miejsce w normalnym kraju jest w więzieniu', 'na polecenie Brukseli', 'posłusznie', 'bezmyślnie', 'z nieprawdopodobną pogardą dla człowieka', 'za pieniądze podatników', 'zgodnie z ideologią LGBTQZ', 'za wszelką cenę', 'zupełnie bezkarnie', 'całkowicie bezczelnie', 'o poglądach na lewo od komunizmu', 'celowo i świadomie', 'z premedytacją', 'od czasów Okrągłego Stołu', 'w ramach postępu']

wyp4 = ['udają homoseksualistów', 'niszczą rodzinę', 'idą do polityki', 'zakazują góralom robienia oscypków', 'organizują paraolimpiady', 'wprowadzją ustrój, w którym raz na cztery lata można wybrać sobie pana', 'ustawiają fotoradary', 'wprowadzają dotacje', 'wydzielają buspasy', 'podnoszą wiek emerytalny', 'rżną głupa', 'odbierają dzieci rodzicom', 'wprowadzają absurdalne przepisy', 'umieszczają dzieci w szkołach koedukacyjnych', 'wprowadzają parytety', 'nawołują do podniesienia podatków', 'próbują wyrzucić kierowców z miast', 'próbują skłocić Polskę z Rosją', 'głoszą brednie o globalnym ociepleniu', 'zakazują posiadania broni', 'nie dopuszczają prawicy do władzy', 'uczą dzieci homoseksualizmu']

wyp5 = ['żeby poddawać wszystkich tresurze', 'bo taka jest ich natura', 'bo chcą wszystko kontrolować', 'bo nie rozumieją, że socjalizm nie działa', 'żeby wreszcie zapanował socjalizm', 'dokładnie tak jak tow. Janosik', 'zamiast pozwolić ludziom zarabiać', 'żeby wyrwać kobiety z domu', 'bo to jest w interesie tak zwanych ludzi pracy', 'zamiast pozwolić decydować konsumentowi', 'żeby nie opłacalo się mieć dzieci', 'zamiast obniżyć podatki', 'bo nie rozumieją, że selekcja naturalna jest czymś dobrym', 'żeby mężczyźni przestali być agresywni', 'bo dzięki temu mogą brać łapówki', 'bo dzięki temu mogą kraść', 'bo dostają za to pieniądze', 'bo tak się uczy w państwowej szkole', 'bo bez tego *tfu* d*mokracja nie może istnieć', 'bo głupich jest więcej niż mądrych', 'bo chcą tworzyć raj na ziemi', 'bo chcą niszczyć cywilizację białego człowieka']

wyp6 = ['co ma zresztą tyle samo sensu, co zawody w szachach dla debili.', 'co zostało dokładnie zaplanowane w Magdalence przez śp. generała Kiszczaka.', 'i trzeba być idiotą, żeby ten system popierać.', 'ale nawet ja jeszcze dożyję normalnych czasów.', 'co dowodzi, że wyskrobano nie tych, co trzeba.', 'a zwykłym ludziom wmawiają, że coś im "dzadzą".', '- cóż: chcieliście *tfu* d*mokracji, to macie.', 'dlatego trzeba zlikwidować koryto, a nie zmieniać świnie.', 'a wystarczyłoby przestać wypłacać zasiłki.', 'podczas gdy normalni ludzie uważani są za dziwaków.', 'co w wieku XIX po prostu by wyśmiano.', '- dlatego w społeczeństwie jest równość, a powinno być rozwarstwienie.', 'co prowadzi Polskę do katastrofy.', '- dlatego trzeba przywrócić normalność.', 'ale w wolnej Polsce pójdą siedzieć.', 'przez kolejne kadencje.', 'o czym się nie mówi.', 'i właśnie dlatego Europa umiera.', 'ale przyjdą muzułmanie i zrobią porządek', '- tak samo zresztą jak za Hitlera', '- proszę zobaczyć, co się dzieje na Zachodzie, jeśli mi państwo nie wierzą.', 'co lat temu sto nikomu nie przyszłoby do głowy.']

from tkinter import *
import random


def get_text():
    x = [random.choice(wyp1), random.choice(wyp2), random.choice(wyp3), random.choice(wyp4), random.choice(wyp5), random.choice(wyp6)]
    return ' '.join(x)

def new_text():
    wypowiedz.configure(text=get_text())

def change():
    global count
    if count != 4:
        count +=1
    else:
        count = 0

    my_pic = PhotoImage(file=f'krul/{count}.gif')
    label.image = my_pic
    label.configure(image=my_pic)
    label.place(x=15, y=15)
    gora.configure(text="Oto Twoja losowa wypowiedź Krula:")
    gora.place(x=250, y=15)
    wypowiedz.place(x=250, y=45)
    guzik.place(x=250, y=230)


    root.after(100, change)



root = Tk()
root.title('KORWIN KORWIN KORWIN KORWIN KORWIN KORWIN')
root.geometry('500x275')
count = 0
root.iconbitmap('krul/krul.ico')


my_pic = PhotoImage(f'krul/{count}.gif')



label = Label(root)
label.place(x=200, y=500)
label.pack()
gora = Label(root, text=get_text(), font="Calibri 10")
gora.pack()
wypowiedz = Label(root, wraplength=200, text=get_text(), font="Calibri 11", justify="center")
wypowiedz.pack()
guzik = Button(root, text="Wygeneruj nową wypowiedź", command=new_text, width=30)
guzik.pack()
root.after(100, change)
root.mainloop()