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
	response.title = "Learn It"
	return dict()

