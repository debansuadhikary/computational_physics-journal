# API = Application Programming Interface; they are third party programmable files that can perform tasks on the mode of operation like taking information from a foreign server and integrating it in my program

# This is a JSON = Java Script Object Notation; is used nowadays as Language Agnostic Centre for exchanging data between two computer 

# https://itunes.apple.com/search?entity=song&limit=1&term=weezer

# {
#  "resultCount":1,
#  "results": [
# {"wrapperType":"track", "kind":"song", "artistId":115234, "collectionId":1440878798, "trackId":1440879551, "artistName":"Weezer", "collectionName":"Weezer", "trackName":"Say It Ain't So", "collectionCensoredName":"Weezer", "trackCensoredName":"Say It Ain't So", "artistViewUrl":"https://music.apple.com/us/artist/weezer/115234?uo=4", "collectionViewUrl":"https://music.apple.com/us/album/say-it-aint-so/1440878798?i=1440879551&uo=4", "trackViewUrl":"https://music.apple.com/us/album/say-it-aint-so/1440878798?i=1440879551&uo=4", 
# "previewUrl":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/11/23/6f/11236f0d-9b5a-b780-5ebb-56c1dc512e3a/mzaf_11156035496161349512.plus.aac.p.m4a", "artworkUrl30":"https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/30x30bb.jpg", "artworkUrl60":"https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/60x60bb.jpg", "artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/100x100bb.jpg", "collectionPrice":10.99, "trackPrice":1.29, "releaseDate":"1994-05-10T12:00:00Z", "collectionExplicitness":"notExplicit", "trackExplicitness":"notExplicit", "discCount":1, "discNumber":1, "trackCount":10, "trackNumber":7, "trackTimeMillis":258853, "country":"USA", "currency":"USD", "primaryGenreName":"Rock", "isStreamable":true}]
# }

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])