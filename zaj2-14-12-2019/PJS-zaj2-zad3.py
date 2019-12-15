#Exercise 3. Handle the upload files for images
# Change the code to accept only image files. You can use curl to test your solution:
# !curl -F 'file=@<path>/<file>' -X POST http://127.0.0.1:5000/upload
from flask import Flask
from flask import request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


app = Flask('Upload example')
app.config['UPLOADS_DEFAULT_DEST'] = '/home/codete/workshop/'

pdfs = UploadSet('files', IMAGES)
configure_uploads(app, pdfs)
patch_request_class(app)  # set maximum file size, default is 16MB

@app.route('/upload', methods=['POST'])
def upload_file():
    filename = pdfs.save(request.files['file'])
    file_url = pdfs.url(filename)
    return "Thank you: " + str(file_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0")