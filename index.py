from flask import Flask

index='''<h1>Hey there !!</h1>
  <h2><div>its Sooraj here</h2>
   <h2><div>To see the jokes navigate to below paths</div></h2>
   <h2><div><ol>
   <li>/joke-1</li>
   <li>/joke-2</li>
   <li>/joke-3</li>
   <li>/joke-4</li>
   <li>/joke-5</li>
   </ol></div></h2>
  '''


# Running the flask app
app = Flask(__name__)

#API endpoints the index page
@app.route('/',methods=['GET'])
def indexpage():
   return index


#API endpoints for question-1
@app.route('/joke-1',methods=['GET'])
def question1():
   return "<h2>What's orange and sounds like a parrot? A carrot.</h2>"

#API endpoints for question-2
@app.route('/joke-2',methods=['GET'])
def question2():
  return "<h2>What do you call a fish with no eyes? Fsh!</h2>"

#API endpoints for question-3
@app.route('/joke-3',methods=['GET'])
def question3():
  return "<h2>What do you call a bear with no teeth? A gummy bear!</h2>"

#API endpoints for question-4
@app.route('/joke-4',methods=['GET'])
def question4():
  return "<h2>Why was the math book sad? Because it had too many problems.</h2>"

#API endpoints for question-5
@app.route('/joke-5',methods=['GET'])
def question5():
  return '''<h2>Knock, knock.
Who's there?
Boo.
Boo who?
Don't cry, it's just a joke!</h2>'''

#error handling : invalid question number
@app.errorhandler(404)
def page_not_found(error):
    return 'Invalid Question Number', 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000,debug=True)