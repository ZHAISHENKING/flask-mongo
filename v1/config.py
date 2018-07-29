import os
import sys
import pymongo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'utlib'))


ALLOWED_EXTENSIONS=dict([
            ("3gp",    "video/3gpp"),
            ("gif",    "image/gif"),
            ("jpeg",   "image/jpeg"),
            ("jpg",    "image/jpeg"),
            ("m4u",    "video/vndmpegurl"),
            ("m4v",    "video/x-m4v"),
            ("mov",    "video/quicktime"),
            ("mp4",    "video/mp4"),
            ("mpe",    "video/mpeg"),
            ("mpeg",   "video/mpeg"),
            ("mpg",    "video/mpeg"),
            ("mpg4",   "video/mp4"),
            ("png",    "image/png")
        ])

uri = 'localhost:27017'
CLIENT = pymongo.MongoClient(uri)
