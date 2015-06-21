#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core import CallObject

class Movie(CallObject):
    def __init__(self, movie_id, display_artist=False, display_comments=False):
        CallObject.__init__(self)
        self._path_name = "movie"
        self._movie_id = movie_id
        self.display_artist = display_artist
        self.display_comments = display_comments

        self.id = self.show()['id']
        self.name = self.show()['name']
        self.orgName = self.show()['orgName']
        self.image = self.show()['image']
        self.rating = self.show()['rating']
        self.type = self.show()['type']
        self.director = self.show()['director']
        self.orgName = self.show()['orgName']
        self.orgName = self.show()['orgName']

    def show(self):
        return self.GET(
                self._path_name,
                self._movie_id,
                self.is_True(self.display_artist),
                self.is_True(self.display_comments)
        )['movie']