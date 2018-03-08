#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jason315'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio
from coreweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    print(users)
    return {
        '__template__': 'index.html',
        'users': users
}