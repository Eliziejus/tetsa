# 1
int=5
bool=True
bytearray=bytearray(5)
bytes=b"hello"

#4

skaicius=float(4.5)

#2
name=["Petras", "Jonas", 'Jokubas']
list=[1,2,3]
tuples=1,2,3

for names in name:
    print(names)
for lists in list:
    print(lists)
for tuple in tuples:
    print(tuple)

#3
#kuriami tokiu stiliumi

manoKintamasis="hello"

#5

def my_function(data):
    for item in data:
        print(item);

print(my_function(name));

#7

# Įtaisytų tipų objektai (int, float, bool, str, tuple, unicode) yra nekintami. Įtaisytųjų tipų objektai, tokie
# kaip (sąrašas, rinkinys, diktas),
# yra keičiami. Pasirinktinės
# klasės paprastai yra keičiamos. Norint imituoti nekintamumą klasėje, reikėtų nepaisyti atributo nustatymo ir
# ištrynimo, kad būtų išimčių.


#Duomenų tipas yra pagrindinė ir labiausiai paplitusi duomenų klasifikacija. Būtent
#tokiu būdu kompiliatorius sužino formą ar informacijos rūšį, kuri bus naudojama visame kode.


# Duomenų struktūros atlieka kai kurias specialias operacijas, pavyzdžiui, įterpimą, ištrynimą ir perėjimą. Pavyzdžiui,
# turite saugoti daugelio darbuotojų duomenis, kur kiekvienas darbuotojas turi savo vardą, pavardę, darbuotojo ID ir
# mobiliojo telefono numerį.

#6

kintamasis = "IlgasSakinys"
x = kintamasis[2:5]
y = kintamasis[7:9]

x="gas"
y="ki"


#8

def printe_liste(data):
    if type(data) == dict:
        for v in data:
            print(data[v])
    elif type(data) == list:
        for v in data:
            print(v)
    else:
        for v in data:
            print(v)









