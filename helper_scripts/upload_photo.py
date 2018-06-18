#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import sys

from InstagramAPI import InstagramAPI

args 	= sys.argv

photo_path = args[1]
caption = args[2]

InstagramAPI = InstagramAPI("mir.rawr", "supersecret")
InstagramAPI.login()  # login


InstagramAPI.uploadPhoto(photo_path, caption=caption)
