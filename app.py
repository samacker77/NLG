import pandas as pd
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from googletrans import Translator
# from similarity import model_similarity

app = Flask(__name__)
Bootstrap(app)

#function to modify string with stylen transfer according  to the personality

translator=Translator()
def get_paraphrased_text(text):
    sen_ko=translator.translate(text,dest='ko')
    sen_en=translator.translate(sen_ko.text,dest='en')
    if sen_en.text.lower()==text.lower():
        #print("Greek")
        sen_greek=translator.translate(text,dest='el')
        sen_en=translator.translate(sen_greek.text,dest='en')
        if sen_en.text.lower()==text.lower():    
            #print("Spanish")
            sen_es=translator.translate(text,dest='es')
            sen_en=translator.translate(sen_es.text,dest='en')
    return sen_en.text

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
