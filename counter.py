from flask import Flask, render_template, request, redirect, session
app =Flask(__name__)
app.secret_key='keep it secret, keep it safe'


@app.route('/')
def count():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template('counter.html', count=session["count"])

@app.route('/addtwo')
def addtwo():
    session['count']+= 1
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
