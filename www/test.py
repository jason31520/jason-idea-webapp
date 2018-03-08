#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def addUser():
	await orm.create_pool(loop=loop, user='jason', password='jason315', db='jasonidea')
	u = User(name='Emma', email='emmastong@163.com', password='000000000', image='about:blank')
	await u.save()

def findUserbyId(uesr_id):
	yield from orm.create_pool(loop=loop, user='jason', password='jason315', db='jasonidea')


loop.run_until_complete(addUser())