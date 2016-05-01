import urlparse


def application(environ, start_response):
    response_body = '''
		<html>
			<head>
				<title>WSGI</title>
			</head>
			<body style="background: pink">
				<h1>Hello, World, it's simple WSGI!</h1>'''

    # parse GET parameters
    response_body += '''
				<h2>GET:</h2>
					<ul>'''
    getQuery = urlparse.parse_qs(environ['QUERY_STRING'])
    for key in getQuery.keys():
        for parameter in getQuery[key]:
            response_body += '<li>' + key + ' = ' + parameter + '</li>'
    response_body += '</ul>'

    # parse POST parameters
    response_body += '''
				<h2>POST:</h2>
					<ul>'''
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
    postQuery = urlparse.parse_qs(environ['wsgi.input'].read(request_body_size))
    for key in postQuery.keys():
        for parameter in postQuery[key]:
            response_body += '<li>' + key + ' = ' + parameter + '</li>'
    response_body += '</ul>'

    response_body += '''
			</body>
		</html>'''

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))]

    start_response('200 OK', response_headers)
    return [response_body]
