errors = {}
errors['000'] = 'Script inesistente'
errors['001'] = 'Parametro mancante'
errors['002'] = 'Parametro non valido'

def error(code, txt=''):
	e = {}
	e['code'] = code
	e['msg'] = errors[code]
	e['txt'] = txt
	return e

def urlMatch(url):
	url = url.lower()
	ext = ['png', 'jpg', 'jpeg', 'gif']
	goodUrl = url[:7] == 'http://'
	goodExt = url.split('.')[-1] in ext
	return goodUrl and goodExt