import requests
from flask import Flask, render_template, jsonify, send_from_directory, request
import os
from train import train

app = Flask(__name__)


@app.route("/")
def first():
  return render_template("home.html")


# @app.route('/')
# def index():
#     return '<html><body><form action="/upload" method="post" enctype="multipart/form-data"><input type="file" name="file"><input type="submit" value="上传"></form></body></html>'


@app.route('/upload', methods=['POST'])
def upload():
  file = request.files['file']
  if file.filename == '':
    return '文件上传失败'

  folder_name = os.path.splitext(file.filename)[0]
  folder_path = os.path.join('./models/', folder_name)

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
  file.save(os.path.join(folder_path, file.filename))
  return '文件上传成功！'


@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
  folder = '/path/to/your/folder'
  return send_from_directory(folder, filename, as_attachment=True)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
