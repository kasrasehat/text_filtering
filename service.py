from flask import Flask, render_template, request, redirect, url_for, send_file
from text_analyzer import farsi_analyzer
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        main_text = request.form['main text']
        list_of_words = ['سلام. احوال', 'به نام ', 'مترجمین موسسه', 'خداوند الموت', 'راه‌حل مناسب']
        a,b = farsi_analyzer.find_statement(main_passage= main_text, list_of_statements= list_of_words)
        filename = b.name

        return redirect(url_for("download_file", filename=filename))
    else:
        return render_template('index.html')

@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html', value= filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = filename
    return send_file(file_path, as_attachment=True, attachment_filename='')


if __name__ == '__main__' :
    farsi_analyzer = farsi_analyzer()
    app.run(debug= True)


