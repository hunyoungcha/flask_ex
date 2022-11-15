#끝나고 해볼것
#1. database 연결
#2. view에 있는 임시 데이터를 따로 파일로 저장해서 update, delete할때 실제로 변하고 없어지게 하기
#3. index페이지와 crud 페이지 다 따로 해서 관리 해보기



from flask import Flask, request, redirect
import view

app = Flask(__name__)

@app.route('/')
def index():
  return view.showpage(view.litag(),'<h2>Welcome</h2>Hello Web')

@app.route('/create/', methods=['GET','POST'])
def create():
  if request.method=='GET':
    content="""
    <form action='/create/' method='post'>
      <p><input type='text' name='title' placeholder='title'></input></p>
      <p><textarea name='body' placeholder='body'></textarea></p>
      <input type='submit' value='create' />
    </form>
    """
    return view.showpage(view.litag(),content)

  elif request.method=="POST":
    title=request.form['title']
    body=request.form['body']
    newTopic={"id":view.addTopicNum,"title":title, "body":body}
    view.topics.append(newTopic)
    url='/read/'+str(view.addTopicNum)+'/'
    view.addTopicNum+=1
    return redirect(url)

  
@app.route('/update/<int:id>/', methods=['GET','POST'])
def update(id):
  title=''
  body=''
  for topic in view.topics:
    if id==topic['id']:
      title=topic['title']
      body=topic['body']
      break
  if request.method=='GET':
    content=f"""
    <form action='/update/{id}' method='post'>
      <p><input type='text' name='title' value={title} ></input></p>
      <p><textarea name='body'>{body}</textarea></p>
      <input type='submit' value='update' />
    </form>
    """
    return view.showpage(view.litag(),content)

  elif request.method=="POST":
    title=request.form['title']
    body=request.form['body']
    view.topics[id-1]['title']=title
    view.topics[id-1]['body']=body
    url='/read/'+str(id)+'/'
    return redirect(url)


@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
  for topic in view.topics:
    if id==topic['id']:
      view.topics.remove(topic)
      break
  return redirect('/')

@app.route('/read/<int:id>/')
def read(id):
  title=''
  body=''
  for topic in view.topics:
    if id==topic['id']:
      title=topic['title']
      body=topic['body']
      break
  return view.showpage(view.litag(),f'<h2>{title}</h2>{body}',id)

app.run()