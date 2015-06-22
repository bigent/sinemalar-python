#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core import CallObject
from . import str2bool


class Artist(object):
    def __init__(self, artist):
        self.id = int(artist['id'])
        self.nameSurname = artist['nameSurname']
        self.characterName = str2bool(artist['characterName'], True)
        self.image = artist['image']


class Comment(object):
    def __init__(self, comment):
        self.id = int(comment['id'])
        self.username = comment['username']
        self.comment = comment['comment']
        self.addDate = comment['addDate']


class Movie(CallObject):
    def __init__(self, movie_id=None, display_artists=False, display_comments=False, movie=None, to_gallery=False):
        CallObject.__init__(self)
        self.to_gallery = to_gallery
        self._path_name = "movie"
        self.movie_id = movie_id

        if movie:
            self.id = movie['id']
            self.name = movie['name']
            self.orgName = movie['orgName']

            try:
                self.image = movie['image']
                self.rating = movie['rating']
            except:
                pass

            try:
                self.type = movie['type']
                self.seances = movie['seances']
                self.selected = int(movie['selected'])
            except:
                pass

            try:
                self.director = movie['director']
            except:
                pass

        elif not to_gallery:
            self.display_artists = display_artists
            self.display_comments = display_comments

            self.id = self.show()[self._path_name]['id']
            self.name = self.show()[self._path_name]['name']
            self.orgName = self.show()[self._path_name]['orgName']
            self.image = self.show()[self._path_name]['image']
            self.rating = self.show()[self._path_name]['rating']
            self.type = self.show()[self._path_name]['type']
            self.director = self.show()[self._path_name]['director']
            self.summary = str2bool(self.show()[self._path_name]['summary'], True)
            self.duration = str2bool(self.show()[self._path_name]['duration'], True)
            self.produceYear = self.show()[self._path_name]['produceYear']
            self.week = str2bool(self.show()[self._path_name]['week'], True)
            self.pubDate = str2bool(self.show()[self._path_name]['pubDate'], True)
            self.embedId = str2bool(self.show()[self._path_name]['embedId'], True)
            self.embedTitle = str2bool(self.show()[self._path_name]['embedTitle'], True)
            self.trailerUrl = self.show()[self._path_name]['trailerUrl']

            #artists
            if display_artists:
                self.artists = []
                for i in self.show()['artists']:
                    self.artists.append(Artist(i))

            #comments
            if display_comments:
                self.comments = []
                for i in self.show()['comments']:
                    self.comments.append(Comment(i))
        else:
            self.gallery = []
            for i in self.show():
                self.gallery.append(i)

    def show(self):
        if self.to_gallery:
            return self.GET(
                'gallery',
                self._path_name,
                self.movie_id,
            )
        else:
            return self.GET(
                    self._path_name,
                    self.movie_id,
                    self.is_True(self.display_artists),
                    self.is_True(self.display_comments)
            )


class Theatre(object):
    def __init__(self, theatre):
        self.id = int(theatre['id'])
        self.name = theatre['name']

        try:
            self.seances = theatre['seances']
            self.selected = theatre['selected']
        except:
            pass

        try:
            self.city = theatre['city']
            self.latitude = float(theatre['latitude'])
            self.longitude = float(theatre['longitude'])
            self.phone = theatre['phone']
            self.address = theatre['address']
        except:
            pass

        try:
            self.ad = theatre['ad']

            #seances
            self.movies = []
            for i in theatre['movies']:
                self.movies.append(Movie(i))
        except:
            del self.movies

        try:
            self.town = theatre['town']
            self.distance = theatre['distance']
        except:
            pass

        try:
            self.cityId = int(theatre['cityId'])
        except:
            pass


class Theatres(CallObject):
    def __init__(self, theatre_id=0, city_id=0, city_count=1000):
        CallObject.__init__(self)
        self._path_name = "theatre"
        self.theatre_id = theatre_id
        self.city_id = city_id
        self.city_count = city_count

        if city_id:
            self.theatres = []
            for i in self.show():
                self.theatres.append(Theatre(i))
        else:
            self.theatre = Theatre(self.show())

    def show(self):
        if self.city_id:
            return self.GET(
                self._path_name,
                0,
                1,
                self.city_id,
                self.city_count
            )[0]
        else:
            return self.GET(
                    self._path_name,
                    self.theatre_id,
            )[0]


class NearTheatre(CallObject):
    def __init__(self, lat=0, long=0):
        CallObject.__init__(self)
        self._path_name = "nearTheatre"
        self.latitude = lat
        self.longitude = long

        self.tenPlus = self.show()['tenPlus']

        self.theatres = []
        for i in self.show()['five']:
            self.theatres.append(Theatre(i))

    def show(self):
        return self.GET(
            "gps",
            self._path_name,
            self.latitude,
            self.longitude
        )


class City(object):
    def __init__(self, city):
        self.id = int(city['id'])
        self.name = city['name']


class Cities(CallObject):
    def __init__(self, many=0):
        CallObject.__init__(self)
        self._path_name = "cities"
        self.many = many

        #cities
        self.cities = []
        for i in self.show():
            self.cities.append(City(city=i))

    def show(self):
        return self.GET(
                self._path_name,
                self.many,
        )


class PlayingMovies(CallObject):
    def __init__(self):
        CallObject.__init__(self)
        self.api_domain = "www.sinemalar.com"

        self._path_name = "playingMovies"

        self.sections = []
        for i in self.show()['sections']:
            self.sections.append(i)

        self.movies = []
        for i in self.show()['movies']:
            for z in i:
                self.movies.append(Movie(movie=z))

    def show(self):
        return self.GET(
                self._path_name,
        )


class PlayingMoviesRemain(PlayingMovies):
    def __init__(self):
        PlayingMovies.__init__(self)
        self._path_name = "playingMoviesRemain"


class ComingSoon(PlayingMovies):
    def __init__(self):
        PlayingMovies.__init__(self)
        self._path_name = "comingSoon"


class NearestSeances(CallObject):
    def __init__(self, movie_id, lat=0, long=0):
        CallObject.__init__(self)
        self._path_name = "seance"
        self.movie_id = movie_id
        self.latitude = lat
        self.longitude = long

        self.seances = self.show()['seances']
        self.selected = self.show()['selected']
        self.cinema = Theatre(self.show()['cinema'])

    def show(self):
        return self.GET(
            "gps",
            self._path_name,
            self.latitude,
            self.longitude,
            self.movie_id
        )


class TheatreSeance(CallObject):
    def __init__(self, city_id, movie_id):
        CallObject.__init__(self)
        self._path_name = "theatreSeance"
        self.city_id = city_id
        self.movie_id = movie_id

        self.movie = Movie(movie=self.show()['movie'])

        self.theatres = []
        for i in self.show()['theatre']:
            self.theatres.append(Theatre(i))

    def show(self):
        return self.GET(
            self._path_name,
            self.city_id,
            self.movie_id
        )