#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core import CallObject
from . import str2bool


class Artist(object):
    def __init__(self, artists, index):
        artist = artists[index]

        self.id = int(artist['id'])
        self.nameSurname = artist['nameSurname']
        self.characterName = str2bool(artist['characterName'], True)
        self.image = artist['image']


class Comment(object):
    def __init__(self, comments, index):
        comment = comments[index]

        self.id = int(comment['id'])
        self.username = comment['username']
        self.comment = comment['comment']
        self.addDate = comment['addDate']


class Movie(CallObject):
    def __init__(self, movie_id, display_artists=False, display_comments=False):
        CallObject.__init__(self)
        self._path_name = "movie"
        self._movie_id = movie_id
        self.display_artists = display_artists
        self.display_comments = display_comments

        #movie
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
                index = self.show()['artists'].index(i)
                self.artists.append(Artist(self.show()['artists'], index))

        #comments
        if display_comments:
            self.comments = []
            for i in self.show()['comments']:
                index = self.show()['comments'].index(i)
                self.comments.append(Comment(self.show()['comments'], index))


    def show(self):
        return self.GET(
                self._path_name,
                self._movie_id,
                self.is_True(self.display_artists),
                self.is_True(self.display_comments)
        )