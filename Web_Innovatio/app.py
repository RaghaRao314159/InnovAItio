from flask import Flask, render_template, request, redirect, url_for, send_file
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

            return render_template('contactpage.html', name = name, contact = contact)
        
        elif request.form.get('friend_box'):
            global friend
            friend = request.form.get('friend_box')
            print("this is what you typoed into the box: ", friend)
            global friend_convo
            global me_convo
            friend_convo = []
            me_convo = []
            return render_template('me.html', friend = friend, me_convo = me_convo, friend_convo = friend_convo)

    return render_template('contactpage.html')



    
@app.route('/me',methods=['POST','GET'])
def me():
    global friend
    global me_convo
    global friend_convo
    if 'value' in request.form:
        global path
        if request.form['value']:
            path = request.form['value']

        print("initial set: ", path)

    
    if request.method == 'POST':

        if request.form.get('back'):
            print("Run this ")
            return render_template('contactpage.html')
        
        if request.form.get('me_message'):
            me_message = request.form.get('me_message')
            me_convo.append(me_message)
            return render_template('me.html', me_convo = me_convo, friend_convo = friend_convo, friend = friend)

    if request.method == 'GET':
        if len(friend_convo) != 0:
            latest_message = friend_convo[-1]
            print("final check: ",path)
            #gen_voice(path, latest_message)
        return render_template('me.html', me_convo = me_convo, friend_convo = friend_convo, friend = friend)

    return render_template('me.html', friend = friend)


@app.route('/friend',methods=['POST','GET'])
def friend():
    global friend_convo
    global me_convo
    if request.method == 'POST':
        if request.form.get('friend_message'):
            friend_message = request.form.get('friend_message')
            friend_convo.append(friend_message)
            return render_template('friend.html', me_convo = me_convo, friend_convo = friend_convo)
    
    if request.method == 'GET':
        return render_template('friend.html', me_convo = me_convo, friend_convo = friend_convo)

    return render_template('friend.html', me_convo = me_convo, friend_convo = friend_convo)


@app.route('/audio')
def serve_audio():
    return send_file("Gen_voice.mp3", as_attachment=True)



if __name__ == "__main__":
    path = ""
    friend = ""
    me_convo, friend_convo = [], []
    app.run(debug=True)