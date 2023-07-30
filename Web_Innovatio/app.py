from flask import Flask, render_template, request, redirect, url_for, jsonify
from model import gen_voice, check

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def contactpage():
    if  request.method == 'POST':
        if request.form.get('name'):
            name = request.form.get('name')
            number = request.form.get('number')
            description = request.form.get('description')
            mp3_path = request.form.get('mp3_path')

            contact = f"{mp3_path}"

            print("ptint everything: ",name, number, description, mp3_path)

            return render_template('contactpage.html', name = name, contact = contact )
        
        else:
            global friend
            friend = request.form.get('friend_box')
            print("this is what you typoed into the box: ", friend)
            return render_template('ragha.html', friend = friend)


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
    if 'value' in request.form:
        global path
        if request.form['value']:
            path = request.form['value']
        # Process the value as per your requirements
        # For example, you can store it in a database, perform some calculations, etc.
        #print('Value received from client:', path)
        print("initial set: ", path)
        #gen_voice(path)

    global raksha_convo
    global ragha_convo
    if request.method == 'POST':
        if request.form.get('ragha_message'):
            ragha_message = request.form.get('ragha_message')
            #ragha_convo += "Ragha: " + ragha_message + "\n" + "\n"
            ragha_convo.append(ragha_message)
            return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)
    
    if request.method == 'GET':
        if len(raksha_convo) != 0:
            latest_message = raksha_convo[-1]
            print("final check: ",path)
            gen_voice(path, latest_message)
        return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)

    return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)



@app.route('/raksha',methods=['POST','GET'])
def raksha():
    global raksha_convo
    global ragha_convo
    if request.method == 'POST':
        if request.form.get('raksha_message'):
            raksha_message = request.form.get('raksha_message')
            raksha_convo.append(raksha_message)
            return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)
    
    if request.method == 'GET':
        return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)

    return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)



@app.route('/tryhtml', methods=['POST','GET'])
def tryhtml():    
    return render_template('try.html')



if __name__ == "__main__":
    path = ""
    friend = ""
    ragha_convo, raksha_convo = [], []
    app.run(debug=True)