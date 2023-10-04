import pyqrcode

s = "Name: Mayank Bhardwaj\nEmail: mayankbhardwaj0085@gmail.com"
url = pyqrcode.create(s)
url.svg("mayank.svg",scale=5)

