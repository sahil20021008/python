import pyqrcode

if __name__ == '__main__':
    url = input("please enter site link: ")
    qr = pyqrcode.create(url)
    qr.png("site.png")
