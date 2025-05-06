class laptop:
    def __init__(self,ram,rom,size,processor,os):
        print("instance created")
        self.gb=ram
        self.ssd=rom
        self.screen=size
        self.i5=processor
        self.windows=os
    def about(self):
        return f"this is a {self.ssd} laptop of{self.gb} screen is{self.screen} pro of{self.i5} os of{self.windows}"
laptop1=laptop("dell","i5",128,"17-inch","windows")
laptop2=laptop("hp","i6", "64gb","16-inch","linux")
laptop3=laptop("apple","i9",512,"15-inch","macbook")
laptop4=laptop("acer","i8",512,"16-inch","windows")
laptop5=laptop("lenovo","i9",512,"17-inch","windows")
laptop6=laptop("lenovo","i9",512,"17-inch","windows")
laptop7=laptop("lenovo","i9",512,"17-inch","windows")
laptop8=laptop("lenovo","i9",512,"17-inch","windows")
laptop9=laptop("lenovo","i9",512,"17-inch","windows")
laptop10=laptop("lenovo","i9",512,"17-inch","windows")
print(laptop1.about())     
print(laptop2.about())
print(laptop3.about())
print(laptop4.about())
print(laptop5.about())
print(laptop6.about())
print(laptop7.about())
print(laptop8.about())
print(laptop9.about())
print(laptop10.about())


