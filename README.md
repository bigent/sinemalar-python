# sinemalar-python  <img src="https://travis-ci.org/bigent/sinemalar-python.svg?branch=master">
<p>A Python 2.7+ library for accessing the <a href="http://www.sinemalar.com">Sinemalar</a> API.</p>
##Installation
```cmd
pip install https://github.com/bigent/sinemalar-python
```
##Usage
```python
import sinemalar.api
```
or
```python
from sinemalar.api import *
```
###Movie
####Get about any movie
```python
>>> from sinemalar.api import Movie
>>> movie = Movie(movie_id=356, display_artists=False, display_comments=False, to_gallery=False)
>>> print(movie.orgName)
Das Leben der Anderen
```
#####movie_id
<p>The movie ID in sinemalar.com</p>
```
http://www.sinemalar.com/film/movie_id/movie_name
http://www.sinemalar.com/film/356/baskalarinin-hayati
```
#####display_artists
<p>It is providing for displaying artists in the movie.</p>

#####display_comments
<p>It is providing for displaying comment about the movie.</p>

#####to_gallery
<p>Only it is providing for displaying images about the movie.</p>

###Theatres
####Get about any theatre
```python
>>> from sinemalar.api import Theatres
>>> theatre = Theatres(theatre_id=1899).theatre
>>> print(theatre.name.encode('utf-8'))
Başakşehir Merkez Kayaşehir
```

#####theatre_id
<p>The theatre ID in sinemalar.com</p>
```
http://www.sinemalar.com/sinemasalonu/theatre_id/theatre_name
http://www.sinemalar.com/sinemasalonu/1899/basaksehir-merkez-kayasehir
```
####Learn theatres in the city
```python
>>> from sinemalar.api import Theatres
>>> theatres = Theatres(city_id=164, city_count=1000).theatres
>>> print(theatres)
[<sinemalar.api.Theatre object at 0x02F87830>, <sinemalar.api.Theatre object at 0x02F87BF0>, <sinemalar.api.Theatre object at 0x02F87C10>, <sinemalar.api.Theatre object at 0x02F874F0>, <sinemalar.api.Theatre object at 0x02F879F0>, <sinemalar.api.Theatre object at 0x02F87850>, <sinemalar.api.Theatre object at 0x02F87C50>, <sinemalar.api.Theatre object at 0x02F87530>, <sinemalar.api.Theatre object at 0x02F87670>, <sinemalar.api.Theatre object at 0x02F87610>, <sinemalar.api.Theatre object at 0x02F87770>, <sinemalar.api.Theatre object at 0x02F87AD0>, <sinemalar.api.Theatre object at 0x02F87AB0>, <sinemalar.api.Theatre object at 0x02F87B30>, <sinemalar.api.Theatre object at 0x02F879B0>, <sinemalar.api.Theatre object at 0x02F87B10>, <sinemalar.api.Theatre object at 0x02F875F0>, <sinemalar.api.Theatre object at 0x02F87630>, <sinemalar.api.Theatre object at 0x02F87650>, <sinemalar.api.Theatre object at 0x02F87710>, <sinemalar.api.Theatre object at 0x02F87790>, <sinemalar.api.Theatre object at 0x02F876D0>, <sinemalar.api.Theatre object at 0x02F877B0>, <sinemalar.api.Theatre object at 0x02F87BB0>, <sinemalar.api.Theatre object at 0x02F87910>, <sinemalar.api.Theatre object at 0x02F87CB0>, <sinemalar.api.Theatre object at 0x02F87C90>, <sinemalar.api.Theatre object at 0x02F87C70>, <sinemalar.api.Theatre object at 0x02F87390>, <sinemalar.api.Theatre object at 0x02F878F0>, <sinemalar.api.Theatre object at 0x02F878B0>, <sinemalar.api.Theatre object at 0x02F87A70>, <sinemalar.api.Theatre object at 0x02F87B50>, <sinemalar.api.Theatre object at 0x02F87990>, <sinemalar.api.Theatre object at 0x02F87970>, <sinemalar.api.Theatre object at 0x02F87A90>, <sinemalar.api.Theatre object at 0x02F87AF0>, <sinemalar.api.Theatre object at 0x02F87A50>, <sinemalar.api.Theatre object at 0x02F87A30>, <sinemalar.api.Theatre object at 0x02F879D0>, <sinemalar.api.Theatre object at 0x02F876B0>, <sinemalar.api.Theatre object at 0x02F87C30>, <sinemalar.api.Theatre object at 0x02F87950>, <sinemalar.api.Theatre object at 0x02F877F0>, <sinemalar.api.Theatre object at 0x02F87550>, <sinemalar.api.Theatre object at 0x02F877D0>, <sinemalar.api.Theatre object at 0x02F87890>, <sinemalar.api.Theatre object at 0x02F878D0>, <sinemalar.api.Theatre object at 0x02F875D0>, <sinemalar.api.Theatre object at 0x02F87BD0>, <sinemalar.api.Theatre object at 0x02F87CD0>, <sinemalar.api.Theatre object at 0x02F87D30>, <sinemalar.api.Theatre object at 0x02F87CF0>, <sinemalar.api.Theatre object at 0x02F87170>, <sinemalar.api.Theatre object at 0x02F87D50>, <sinemalar.api.Theatre object at 0x02F87D70>, <sinemalar.api.Theatre object at 0x02F87D90>, <sinemalar.api.Theatre object at 0x02F87DB0>, <sinemalar.api.Theatre object at 0x02F87DD0>, <sinemalar.api.Theatre object at 0x02F87DF0>, <sinemalar.api.Theatre object at 0x02F87E10>, <sinemalar.api.Theatre object at 0x02F87E30>, <sinemalar.api.Theatre object at 0x02F87E50>, <sinemalar.api.Theatre object at 0x02F87E70>, <sinemalar.api.Theatre object at 0x02F87E90>, <sinemalar.api.Theatre object at 0x02F87EB0>, <sinemalar.api.Theatre object at 0x02F87ED0>, <sinemalar.api.Theatre object at 0x02F87EF0>, <sinemalar.api.Theatre object at 0x02F87F10>, <sinemalar.api.Theatre object at 0x02F87F30>, <sinemalar.api.Theatre object at 0x02F87F50>, <sinemalar.api.Theatre object at 0x02F87F70>, <sinemalar.api.Theatre object at 0x02F87F90>, <sinemalar.api.Theatre object at 0x02F87FB0>, <sinemalar.api.Theatre object at 0x02F87FD0>, <sinemalar.api.Theatre object at 0x02F87FF0>, <sinemalar.api.Theatre object at 0x02F82030>, <sinemalar.api.Theatre object at 0x02F82050>, <sinemalar.api.Theatre object at 0x02F82070>]
```

#####city_id
<p>The city ID in sinemalar.com</p>
```
http://www.sinemalar.com/sinemasalonlari/city_id/city_name
http://www.sinemalar.com/sinemasalonlari/164/istanbul-avrupa
```

#####city_count
<p>A count of displaying.</p>

###Cities
####Learn this site registered cities
```python
>>> from sinemalar.api import Cities
>>> cities = Cities().cities
>>> print(cities[0].name.encode('utf-8'))
İstanbul Avrupa
```

###PlayingMovies
####Learn movies in theaters
```python
>>> from sinemalar.api import PlayingMovies
>>> movies = PlayingMovies().movies
>>> print(movies[0].director.encode('utf-8'))
Alexandre Aja
```

###PlayingMoviesRemain
####Learn other movies in theaters
```python
>>> from sinemalar.api import PlayingMoviesRemain
>>> movies = PlayingMoviesRemain().movies
>>> print(movies[0].orgName.encode('utf-8'))
Horns
```

###ComingSoon
####Learn movies coming soon
```python
>>> from sinemalar.api import ComingSoon
>>> movies = ComingSoon().movies
>>> print(movies[0].id)
174575
```

###TheatreSeance
####Learn about the movie in the city
```python
>>> from sinemalar.api import TheatreSeance
>>> movie = TheatreSeance(city_id=164, movie_id=219826)
>>> print(movie.theatres[0].name.encode('utf-8'))
Ataşehir Denizbank ONYX
```

#####city_id
<p>The city ID in sinemalar.com</p>
```
http://www.sinemalar.com/sinemasalonlari/city_id/city_name
http://www.sinemalar.com/sinemasalonlari/164/istanbul-avrupa
```
#####movie_id
<p>The movie ID in sinemalar.com</p>
```
http://www.sinemalar.com/film/movie_id/movie_name
http://www.sinemalar.com/film/356/baskalarinin-hayati
```

###ArtistGallery
####Get photos about the artist
```python
>>> from sinemalar.api import ArtistGallery
>>> artist = ArtistGallery(artist_id=26396)
>>> print(artist.gallery)
[u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-0.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-1.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-2.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-3.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-4.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-5.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-6.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-7.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-8.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-9.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-10.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-11.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-12.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-13.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-14.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-15.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-16.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-17.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-18.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-19.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-21.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-24.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-25.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-26.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-27.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-28.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-29.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-30.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-31.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-32.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-33.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-34.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-35.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-36.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-37.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-38.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-39.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-40.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-42.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-43.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-44.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-45.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-46.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-47.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-48.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-49.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-50.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-51.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-52.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-53.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-54.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-55.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-56.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-57.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-58.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-59.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-60.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-61.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-62.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-64.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-65.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-66.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-67.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-68.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/Christopher-Nolan-69.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-72.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-73.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-74.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-75.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-76.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-77.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-79.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-80.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-81.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-82.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-83.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-84.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-85.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-86.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-87.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-89.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-90.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-91.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-92.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-93.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-94.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-95.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-96.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-97.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-98.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-99.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-100.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-101.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-102.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-103.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-104.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-105.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-106.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/26396/christopher-nolan-107.jpg', u'http://img04.imgsinemalar.com/images/artist_buyuk/598229/cristopher-nolan-1.jpg']
```

#####artist_id
<p>The artist ID in sinemalar.com</p>
```
http://www.sinemalar.com/sanatci/artist_id/artist_name
http://www.sinemalar.com/sanatci/26396/christopher-nolan
```

###NearTheatre
####Learn the nearest theatres to the location
```python
>>> from sinemalar.api import NearTheatre
>>> theatres = NearTheatre(lat=41, lng=30).theatres
>>> print(theatres[0].id)
1373
```

#####lat
<p>Latitude of the location</p>

#####lng
<p>Longitude of the location</p>

###NearestSeances
####Learn the nearest theatre and seances of the theatre to the location
```python
>>> from sinemalar.api import NearestSeances
>>> seances = NearestSeances(movie_id=219826, lat=41.0, lng=30.0)
>>> print(seances.cinema.name.encode('utf-8'))
Kocaeli Dolphin
```

#####movie_id
<p>The movie ID in sinemalar.com</p>
```
http://www.sinemalar.com/film/movie_id/movie_name
http://www.sinemalar.com/film/356/baskalarinin-hayati
```

#####lat
<p>Latitude of the location</p>

#####lng
<p>Longitude of the location</p>
