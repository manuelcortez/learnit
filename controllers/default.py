# -*- coding: utf-8 -*-

def user():
	if len(request.args) == 0:
		return redirect(URL("default", "index"))
	arg = request.args[0]
	if arg == "register":
		response.title = T("Register")
	elif arg == "login":
		response.title = T("Log-in")
	return dict(form=auth(), share=False)

@cache.action()
def download():
	return response.download(request, db)

def index():
	response.title = T("Learn It")
	return dict()

@auth.requires_login()
def words():
	response.title = T("My words")
	words = db(db.card.owner == auth.user).select()
	return dict(words=words)

@auth.requires_login()
def add_word():
	response.title = T("Add word")
	form = SQLFORM(db.card)
	if form.process().accepted:
		return redirect(URL("default", "words"))
	return dict(form=form)