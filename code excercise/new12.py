user={}
name=input("enter your name")
age=input("enter your age")
fav_movies=input("entert fav movies").split(",")
fav_songs=input("enter your fav songs").split(",")
user['name']=name
user['age']=age
user['fav-movies']=fav_movies
user['fav_songs']=fav_songs

for key,value in user.items():
    print(f"{key}:{value}")






