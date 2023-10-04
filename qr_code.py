import pyqrcode

s = "Name: Mayank Bhardwaj\nEmail: mayankbhardwaj0085@gmail.com"
# s = "pagal"
# s = "Name - Shally Kansal\nPhone Number - +91-7417298644\nAddress - Gulaothi\nFather's Name - Mr Ghanshyam Kansal\nMother's Name - Mrs Lakshmi Kansal"
# s = image.png

url = pyqrcode.create(s)
url.svg("mayank.svg",scale=5)

