test_pliku = open('dyzurmaj.txt', 'r',encoding="UTF-8")
test_lini = test_pliku.readlines()
ilosc_lini = len(test_lini)	#Ilośc lini
test_pliku.close()
miesiac_centrala=""
i=1							#Pętla wywala się jeśli zaczyna się od 0 prawdopodobnie przez brak zawartosci 
							#Także dla spokoju po prostu zaczynam pętle od 1
dzien_centrala=0
for i in range(1,ilosc_lini): #Sprawdzamy każdą linie
	lina=test_lini[i]			#Przywołujemy linie i
	lina=lina.lower()
	lina=lina.replace("karol","labuda")#Jestem wpisany po nazwisku bo jest juz jeden Karol
	lina=lina.replace("styczen","jan")
	lina=lina.replace("luty","feb")
	lina=lina.replace("marzec","mar")
	lina=lina.replace("kwiecień","apr")
	lina=lina.replace("maj","may")
	lina=lina.replace("czerwiec","jun")
	lina=lina.replace("lipiec","jul")
	lina=lina.replace("sierpień","aug")
	lina=lina.replace("wrzesień","sep")
	lina=lina.replace("październik","oct")
	lina=lina.replace("listopad","nov")
	lina=lina.replace("grudzień","dec")
	lina=lina.replace(","," ")#Nie chciało mi działać z przecinkami także zamieniam je na spacje
	slowo=lina.split()		#Dzielimy slowa 
	x=len(slowo)			#Chcemy wiedzieć jak dużo jest słów w lini do pętli niżej
	for i in range(x):		#Sprawdzamy zawartość każdej lini
		#print(slowo[i])		#Wyświetlamy każde słowo z każdej lini
		slowo_x=slowo[i]
		if slowo_x in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]: #jaki miesiac
			miesiac_centrala=slowo_x
		if slowo_x in ["labuda", "krzysztof", "agnieszka", "ola", "daniel"]:#jaki konsultant
			dzien_centrala+=1
			kod_centrala=("exten = s,n,GotoIfTime(17:00-21:00,,"+str(dzien_centrala)+","+miesiac_centrala+"?konsultant_"+slowo_x+")")
			print(kod_centrala)
			
			
#TODO
#1.Wrzucanie pliku przez weba
#2.Wykrywanie który dzień 17-21 który 10-18