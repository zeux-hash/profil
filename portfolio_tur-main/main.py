# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_db = request.form.get('button_db')
    button_html = request.form.get('button_html')


    email = request.form.get('email')
    text = request.form.get('text')
    

    if email is None or text is None:
        print("good boy")
    else:

        with open('feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f'Email: {email} Comment: {text}\n')

    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_db=button_db, button_html=button_html)


if __name__ == "__main__":
    app.run(debug=True)