import qrcode
from PIL import Image
import pyshorteners
def code():
    link = input("Copy paste the site name=")

    location = input("give name to png file=")
    if ('http' or 'www') not in link:
        print("Invalid link")
    else:
        y = qrcode.make(link)
        file_location = 'C:/Users/gaura/PycharmProjects/generated qr/' + location + '.png'
        y.save(file_location)
        print("qrcode png location", file_location)
code()
