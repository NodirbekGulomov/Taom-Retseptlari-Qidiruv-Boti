from app.db.commands import add_retsept

retseptlar = [
    ("Palov", "Guruch, sabzi, go'sht, piyoz", 90, "O'rta"),
    ("Shashlik", "Go'sht, piyoz, ziravorlar", 60, "Oson"),
    ("Mastava", "Guruch, kartoshka, sabzi, go'sht", 50, "O'rta"),
    ("Lag'mon", "Xamir, go'sht, qalampir, piyoz", 80, "Qiyin"),
    ("Somsa", "Xamir, go'sht, piyoz", 70, "O'rta"),
    ("Sho'rva", "Go'sht, kartoshka, sabzi, piyoz", 45, "Oson"),
    ("Manti", "Xamir, go'sht, piyoz", 100, "Qiyin"),
    ("Qozon kabob", "Kartoshka, go'sht, piyoz", 75, "O'rta"),
    ("Tovuq kabob", "Tovuq, piyoz, ziravorlar", 50, "Oson"),
    ("Chuchvara", "Xamir, go'sht, piyoz", 90, "Qiyin"),
    ("Dimlama", "Kartoshka, sabzi, karam, go'sht", 80, "O'rta"),
    ("Achchiq chuchuk", "Pomidor, bodring, piyoz", 15, "Oson"),
    ("Oliviya", "Kartoshka, tuxum, kolbasa, mayonez", 30, "Oson"),
    ("Tuxum barak", "Xamir, tuxum, sut", 40, "O'rta"),
    ("Norin", "Xamir, go'sht", 120, "Qiyin"),
    ("Beshbarmoq", "Xamir, go'sht, piyoz", 110, "Qiyin"),
    ("Grechka", "Grechka, go'sht, piyoz", 35, "Oson"),
    ("Makaron", "Makaron, go'sht, pomidor", 25, "Oson"),
    ("Kartoshka fri", "Kartoshka, yog'", 20, "Oson"),
    ("Tovuq sho'rva", "Tovuq, kartoshka, sabzi", 40, "Oson"),
]


def add_retseptlar():
    for nomi, ingredient, vaqt, murakkablik in retseptlar:
        add_retsept(nomi, ingredient, vaqt, murakkablik)
