from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def contactpage():
    if request.method == 'POST':
        #global bool1
        #bool1 = (lambda x: "CORRECT" if (request.form.get('stage1') == "Initial:a_4,Final:a_18") else "WRONG")(3)
        #return redirect(url_for('stage_1'))
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
    if request.method == 'POST':
        ragha_message = request.form.get('ragha_message')
        global ragha_convo
        ragha_convo += "Ragha: " + ragha_message + "\n" + "\n"
        return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)
    
    if request.method == 'GET':
        return render_template('ragha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)

    return render_template('ragha.html')



@app.route('/raksha',methods=['POST','GET'])
def raksha():
    if request.method == 'POST':
        raksha_message = request.form.get('raksha_message')
        global raksha_convo
        raksha_convo += "Raksha: " + raksha_message + "\n" + "\n"

        return render_template('raksha.html', raksha_convo = raksha_convo, ragha_convo = ragha_convo)
    
    if request.method == 'GET':
        return render_template('raksha.html', ragha_convo = ragha_convo, raksha_convo = raksha_convo)

    return render_template('raksha.html')
    

if __name__ == "__main__":
    ragha_convo, raksha_convo = "", ""
    app.run(debug=True)
    