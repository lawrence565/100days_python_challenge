from flask import Flask
from random import randint

app = Flask(__name__)
answer = randint(1, 10)

@app.route("/")
def home():
    return '<h1>"Guess a number between 0 and 9"</h1>'

@app.route("/<int:number>")
def guess(number):
    if number == 1:
        img_address = 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXUxN2M5OXhnY3hqaTl3em1vdWd2dzR3Ymc0c2xpeHYwbDl4NzZ0ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPrwk5SCKWexkLS/giphy.webp'
    elif number == 2:
        img_address = 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3ltdG01bjZ4ejlkZmwwNmdmM2w1Yzh1dzAwOHN3b2J3NjlsM3ZwayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/toKE0zZrzkjuLKBucs/giphy.webp'
    elif number == 3:
        img_address = 'https://media1.giphy.com/media/3ov9kaW3wyiefU3GGA/giphy.webp?cid=790b7611hie7m1gyo461ujrlmfsb6bg4v4x3qhntf3gm9psy&ep=v1_gifs_search&rid=giphy.webp&ct=g'
    elif number == 4:
        img_address = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDNvdnFxYjZvdWNpc3ZicTd0bWI5Z2U0bXM4bGRzaHVlNms5Zmp1aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jSEFUIq3EE4oyX2Be4/giphy.webp'
    elif number == 5:
        img_address = 'https://media0.giphy.com/media/Q5imCx8O3fOF1HihfR/giphy.webp?cid=790b761199sp82u68wcxticdxug0brdw2p3vhgkl0v8mc0m4&ep=v1_gifs_search&rid=giphy.webp&ct=g'
    elif number == 6:
        img_address = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTMxaGhvd3loOHY1OTk3ZDF4dzMybWpzM2xqMml1Y2UyMzRvYzU2ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/FwxVGlrHvRgEUaE8G5/giphy.webp'
    elif number == 7:
        img_address = 'https://media0.giphy.com/media/l378atCG9uQQa1Fy8/giphy.webp?cid=790b7611g8wi0t7kng5assp0fnx2wc4kjy8cz2ohmub0b4lz&ep=v1_gifs_search&rid=giphy.webp&ct=g'
    elif number == 8:
        img_address = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExejF0c3l6OHVsamZjejk5NHk5YjZoaGcybWZkc2gzYnYyY3NscGc0NCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/B6bnealXUbW18QjPCd/giphy.webp'
    elif number == 9:
        img_address = 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnlyeTJhd3JtaTdmMTk4eHd0amJ5MGtmMTZ3cHF5aGZkMTdrOTh6aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/6OyrnAKxd46Rfall6K/giphy.webp'
    elif number == 10:
        img_address = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTZsOTlsbHA1czB5NHRtMXhrazZoY25lY2g5aGx1NTZ2c3JnMGNseSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vD2y6a6zGBD3kpWMtA/giphy.webp'
    else:
        return "<h1>Out of range, Please try again.</h1>"

    if number < answer:
        return ("<h1 style='color: red'>Too low, Try again!</h1>"
                f"<img src={img_address}/>")
    elif number > answer:
        return ("<h1 style='color: purple'>Too high, Try again!</h1>"
                f"<img src={img_address}/>")
    elif number == answer:
        return ("<h1 style='color: green'>You found me!</h1>"
                f"<img src={img_address}/>")

if __name__ == '__main__':
    app.run()