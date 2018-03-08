#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def test():
	await orm.create_pool(loop=loop, user='jason', password='jason315', db='jasonidea')

	u = User(name='Jason', email='lyna318@163.com', password='123456987', image='about:blank')

	await u.save()

loop.run_until_complete(test())