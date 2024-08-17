from flask import Flask
import random

liste = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
         "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
         "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
         "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

yazitura=["yazı çıktı.Tura dediysen kaybettin","tura çıktı.Yazı dediysen kaybettin."]

character = ["a","b","c","d","e","f","g","h","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



app = Flask(__name__)

@app.route("/")
def hello_world():
    return   '<a href="/ikinci">Rastgele bir gerçeği görüntüle!</a>' '<p></p>' '<a href="/yazitura">Yazı tura(basmadan önce tahmininizi söyleyin)</a>' '<p></p>' '<a href="/isimsehirharfsecici">İsim Şehir Harf Secici</a>' '<p></p>' 

@app.route("/ikinci")
def ikinci():
    return f'<p>{random.choice(liste)}</p>' '<a href="/">ANASAYFA!</a>'

@app.route("/yazitura")
def oyun1():
    return f'<p>{random.choice(yazitura)}</p>'  '<a href="/">ANASAYFA!</a>'
    

@app.route("/isimsehirharfsecici")
def oyun2():
    return f'<p>{random.choice(character)}</p>' '<a href="/">ANASAYFA!</a>'

app.run(debug=True)