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
    


if __name__ == "__main__":
    app.run(debug=True)
    
    