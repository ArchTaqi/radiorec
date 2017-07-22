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
import datetime
import urllib.request


class record_radio:

    def __init__(self, stream_url):
        self.stream_url = stream_url

    def __enter__(self):
        print('__enter__')

    def __exit__(self, typ, value, tb):
        print('__exit__')

    def init(self):
        print("init")

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def finish(self):
        print("finish")

    def record_radio(self):
        d = datetime.date.today()
        filename = "recording" + d.strftime("%Y%m%d")+".ogg"
        stream = urllib.request.urlopen(self.stream_url)
        start_time = datetime.datetime.now()
        dest = open(filename, 'wb')
        while (datetime.datetime.now() - start_time).seconds <= 30:
            print((datetime.datetime.now() - start_time).seconds)
            dest.write(stream.read(1024))
        return filename



