import pandas as pd
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from googletrans import Translator
# from similarity import model_similarity

app = Flask(__name__)
Bootstrap(app)

#function to modify string with stylen transfer according  to the personality

translator=Translator()
def paraphrased(in_text):
    phrased = []
    for i in ['ko', 'ja', 'el', 'fr', 'tl', 'ar', 'ht','af', 'sq', 'am']:
        par_text = translator.translate(in_text, dest=i).text
        phrased.append(translator.translate(par_text, dest='en').text.capitalize())
    t = [i for i in phrased if i.lower() != in_text.lower()]
    return "No possible phrases" if not list(set(t)) else list(set(t))


# add a rule for the index page.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
	print("I am here!")
	if request.method == 'POST':
		text = request.form['nlg']
		altertext = get_paraphrased_text(text)
		#print(text)
	return render_template('result.html',prediction=[text,altertext])

# run the app.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
