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
