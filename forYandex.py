# -*- coding: cp1251 -*-
from re import search
from types import NoneType
from yandex_music import Client

client = Client('token.txt').init()

TrackToAdd = open('My Spotify Library.txt').readlines()[::-1]

for search in TrackToAdd:

    search_result = client.search(search).best
    if search_result!=None:

        s_result = client.search(search).best.result
        s_type = client.search(search).best.type
        name = search.split(' - ')[1].replace('\n','')

        if s_type == 'track' and s_result.title == name:
            client.usersLikesTracksAdd(s_result.id)
            print(f'Трек {name} добавлен')
        else:
            print(f'Трек {name} не добавлен')
    