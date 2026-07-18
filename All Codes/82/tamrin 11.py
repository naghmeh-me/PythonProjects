def reverse_details_music(details_music):
    reverse_details_music_={}
    for key in details_music:
        value_=details_music[key]
        if value_ not in reverse_details_music_:
            reverse_details_music_[value_]=[key]
        else:
            reverse_details_music_[value].append(key)
    return reverse_details_music_

details_music={"Rita ora":"Bang Bang",
               "karol g":"TQC",
               "Inna":"Hello hello",
               "Onerepublic":"Runaway",
               "Beach house":"Space song",
               "Charlie puth":"Hero",
               "Hoomaan":"Shahre moon",
               "M":"Honey",
               "Billlie ielidh":"My future",
               "Mostly autumn":"up",
               "Dua lipa":"Illusion",
               "Becky g":"Buna dia",
               "Bebe rexa":"Knees",
               "David lanz":"Nepyune dance",
               "Kovax":"My love",
               "Notd":"I wanna know",
               "Ava max":"Who's laughing now",
               "Olivia rodrigo":"Vampire"}

list_music_singer=[]

list_singer_music=[]

singer=input("enter name of the singer:")

music=input("enter the nam eof the music:")

if singer.capitalize() in details_music.keys():
    for i in details_music:
        if i==singer.capitalize():
            list_music_singer.append(details_music[i])
        else:
            continue
else:
    print("not found the singer.")

if music.capitalize() in details_music.values():
    reverse_details_music_=reverse_details_music(details_music)
    for i in reverse_details_music_:
        if i==music.capitalize():
            list_singer_music.append(reverse_details_music_[i])
        else:
            continue
else:
    print("not found.")

print(reverse_details_music(details_music))
print(f"musics of {singer}:{list_music_singer}\nsingers of {music}:{list_singer_music}")
                                     
    

