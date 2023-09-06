def display_message():
    print('Minh dang hoc ham trong chuong nay')
def favourite_book(s):
    print('Mot trong nhung cuon sach yeu thich la',s)
def make_shirt(size,ndung):
    print(f"Size ao {size}:{ndung}")
def make_shirt(size="XL",ndung="I love Python"):
    print(f"Size ao {size}:{ndung}")
def description_city(city,country="Vietnam"):
    print(city+" is in "+country)
def city_country (city,country):
    return f"{city},{country}"
def make_album (artist,title,track=None):
    album ={"artist":artist,"title":title}
    if track:
        album["track"] =track
    return album
def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album
def show_messages(messages):
    for message in messages:
        print(message)
def show_messages(messages):
    for message in messages:
        print(message)

def send_message(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"Sending: {message}")
        sent_messages.append(message)
def make_sandwich(*items):
    print("Đã đặt mua bánh mì với các thành phần sau:")
    for item in items:
        print("- " + item)

def build_profile(first_name, last_name, **user_info):
    profile = {
        "first_name": first_name,
        "last_name": last_name,
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile

def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model,
    }
    for key, value in car_info.items():
        car[key] = value
    return car



#7-1
display_message()
#7-2
favourite_book("Alice in Wonderland")
#7-3
make_shirt("XL","My Shirt")
make_shirt(size="L",ndung="Love")
#7-4
make_shirt()
make_shirt("M","Hello")
make_shirt(ndung="Python")
#7-5
description_city("Hanoi")
description_city("New York","USA")
description_city("Tokyo","Japan")
#7-6
print(city_country("Santiago","Chile"))
print(city_country("Hanoi","Vietnam"))
print(city_country("Tokyo","Japan"))
#7-7
album1=make_album("Sontung","27")
album2=make_album("Taylor","Love",10)
album3=make_album("Sheeran","I love you",15)
print(album1)
print(album2)
print(album3)
#7-8

while True:
    artist = input("Nhập tên nghệ sĩ (hoặc nhập -1 để dừng): ")
    if artist == "-1":
        break
    title = input("Nhập tiêu đề album: ")
    album = make_album(artist, title)
    print(album)
#7-9

messages = ["Message 1", "Message 2", "Message 3"]
show_messages(messages)
#7-10
messages = ["Message 1", "Message 2", "Message 3"]
sent_messages = []
send_message(messages, sent_messages)

print("\nSent Messages:")
show_messages(sent_messages)
#7-11
messages = ["Message 1", "Message 2", "Message 3"]
sent_messages = []
send_message(messages[:], sent_messages)

print("\nOriginal Messages:")
show_messages(messages)

print("\nSent Messages:")
show_messages(sent_messages)
#7-12
make_sandwich("Thịt gà", "Rau diếp", "Mayonnaise")
make_sandwich("Hamburger", "Ketchup")
make_sandwich("Phô mai", "Hành tây", "Dứa", "Salad")

#7-13

user_profile = build_profile("Huan", "Nguyen", age=20, city="Thai Binh", job="IT")
print(user_profile)

#7-14
car = make_car("Yamaha", "Outblue", color="Blue", tow_package=True)
print(car)

#7-15
from print_functions import print_models, show_completed_models

unprinted_designs = ["iphone", "robot", "laptop"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#7-16
import new_name
new_name.new_name()
from new_name import new_name
new_name()
from new_name import new_name as fn
fn()
import new_name as mn
mn.new_name()
from new_name import *
new_name()