from flask import Flask, render_template, request
import Caption_it

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def marks():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)
        caption = Caption_it.caption_this_image(path)  # You'll need to define Caption_it
        
        result_dic = {
         'image' : path,
         'caption' :caption
        }
    return render_template("index.html", your_result = result_dic)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
