#!/usr/bin/env python3
"""
radiorec.py – Recording internet radio streams and Upload to SoundCloud
Copyright (C) 2017  Muhammad Taqi <taqi.official@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# import libraries
import urllib.request
from datetime import datetime


class record_radio:
    DURATION = 0

    def __init__(self, stream_url):
        self.stream_url = stream_url
        self.init()

    def __enter__(self):
        print('__enter__')

    def __exit__(self, typ, value, tb):
        print('__exit__')

    def init(self):
        h = int(datetime.utcnow().strftime("%I"))
        day = int(datetime.utcnow().strftime("%A"))
        if h == 2:
            self.DURATION = 2
        elif h == 4:
            self.DURATION = 2
        elif h == 12 and day != 'Saturday':
            self.DURATION = 3
        elif h == 19 and day != 'Saturday':
            self.DURATION = 2
        else:
            self.DURATION = 0

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def finish(self):
        print("finish")

    def record_radio(self):
        if self.DURATION != 0:
            d = datetime.now()
            filename = "recording__" + d.strftime("%b-%d-%Y__%I:%M%p")+".ogg"
            stream = urllib.request.urlopen(self.stream_url)
            start_time = datetime.now()
            dest = open(filename, 'wb')
            while (datetime.now() - start_time).seconds / 3600 <= self.DURATION:
                #print((datetime.datetime.now() - start_time).seconds / 3600)
                dest.write(stream.read(1024))
            return filename
        else:
            return None



