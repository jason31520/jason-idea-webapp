#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from orm import Model, StringField, IntegerField, BooleanField, FloatField, TextField

class User(Model):
	__table__ = 'user'

	id = IntegerField(primary_key=True)
	name = StringField(ddl='varchar(50)')
	password = StringField(ddl='varchar(50)')
	email = StringField(ddl='varchar(50)')
	admin = BooleanField()
	image = StringField(ddl='varchar(500)')
	created_at = FloatField(default = time.time)

class Blog(Model):
	__table__ = 'blog'

	id = IntegerField(primary_key=True)
	user_id = IntegerField()
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	created_at = FloatField(default=time.time)

class Comment(Model):
	__table__ = 'comment'

	id = IntegerField(primary_key=True)
	blog_id = IntegerField()
	user_id = IntegerField()
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	content = TextField()
	created_at = FloatField(default=time.time)