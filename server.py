from flask import Flask
import view

app = Flask(__name__)

@app.route('/')
def index():
  return view.showpage(view.litag(),'<h2>Welcome</h2>Hello Web')

@app.route('/create/')
def create():
  content="""
  <form action='/create/' method='post'>
    <p><input type='text' name='title' placeholder='title'></input></p>
    <p><textarea name='body' placeholder='body'></textarea></p>
    <input type='submit' value='create' />
  </form>
  """
  return view.showpage(view.litag(),content)
  
@app.route('/read/<int:id>/')
def read(id):
  title=''
  body=''
  for topic in view.topics:
    if id==topic['id']:
      title=topic['title']
      body=topic['body']
      break
  return view.showpage(view.litag(),f'<h2>{title}</h2>{body}')

app.run()