from flask import Flask, render_template, request, redirect, url_for
import random
import sched, time

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def contactpage():
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')
        description = request.form.get('description')
        mp3_path = request.form.get('mp3_path')

        contact = f"{mp3_path}"

        print(name, number, description, mp3_path)

        return render_template('contactpage.html', name = name, contact = contact )
    
    if request.form.get('chat'):
        return redirect(url_for('chatpage'))

    return render_template('contactpage.html')


@app.route('/chatpage',methods=['POST','GET'])
def chatpage():
    if request.form.get('sender'):
        sender = request.form.get('sender')
        return render_template('chatpage.html', sender = sender)
    
    if request.form.get('back'):
        redirect(url_for('contactpage'))

    return render_template('chatpage.html')

    
@app.route('/ragha',methods=['POST','GET'])
def ragha():
    global raksha_convo
    global ragha_convo
    if request.method == 'POST':
        ragha_message = request.form.get('ragha_message')
        #ragha_convo += "Ragha: " + ragha_message + "\n" + "\n"
        ragha_convo.append(ragha_message)
        return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)
    
    if request.method == 'GET':
        return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)

    return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)



@app.route('/raksha',methods=['POST','GET'])
def raksha():
    global raksha_convo
    global ragha_convo
    if request.method == 'POST':
        raksha_message = request.form.get('raksha_message')
        raksha_convo.append(raksha_message)
        return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)
    
    if request.method == 'GET':
        return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)

    return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)


if __name__ == "__main__":
    ragha_convo, raksha_convo = [], []
    app.run(debug=True)