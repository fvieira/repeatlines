from bottle import route, run, template, view, request, response, redirect
from StringIO import StringIO
import os

from utils import clean_text, repeat_text

error_message = None

@route('/', method='GET')
@view('upload')
def index():
    error_message = get_error_message()
    if error_message:
        return {'error_message': error_message}
    else:
        return {}


@route('/', method='POST')
def handle_upload():
    try:
        repeat_number = int(request.forms.get('repeat_number'))
    except ValueError:
        set_error_message('Repeat times must be a number.')
        redirect('/')
    if repeat_number > 10:
        set_error_message('Repeat times is too big, maximum allowed is 10.')
        redirect('/')
    upload_file = request.files.get('upload_file')
    if not upload_file:
        set_error_message('You didn\'t set the file to upload.')
        redirect('/')
    name, ext = os.path.splitext(upload_file.filename)
    if ext not in ('.txt','.text'):
        set_error_message('File extension not allowed.')
        redirect('/')

    text = upload_file.file.read()
    cleaned_text = clean_text(text)
    repeated_text = repeat_text(cleaned_text, repeat_number)
    response.content_type = 'text/plain'
    response.headers['Content-Disposition'] = 'attachment; filename="{0}_repeated{1}"'.format(name, ext)
    response.headers['Content-Length'] = str(len(repeated_text))
    return StringIO(repeated_text)

def set_error_message(msg):
    global error_message
    error_message = msg


def get_error_message():
    global error_message
    msg = error_message
    error_message = None
    return msg



def main():
    run(host='localhost', port=8005)

if __name__ == '__main__':
    main()



