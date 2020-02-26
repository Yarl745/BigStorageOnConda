def song_decoder(song):
    return " ".join([word for word in song.split("WUB") if word])
print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
