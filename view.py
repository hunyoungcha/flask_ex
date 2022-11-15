addTopicNum=4

topics=[
  {'id': 1, 'title':'html', 'body': 'html is ...'},
  {'id': 2, 'title':'css', 'body': 'css is ...'},
  {'id': 3, 'title':'javascript', 'body': 'javascript is ...'}
]


def litag():
  liTags=''
  for topic in topics:
    liTags+=f"<li><a href='/read/{topic['id']}/'>{topic['title']}</a></li>"
  return liTags

def showpage(contents,content, id=None):
  udpage=''
  if id !=None:
    udpage=f"""
    <a href='/update/{id}/'>update</a>
    <form action='/delete/{id}/' method='post'><input type='submit' value='delete' /></form>
    """ 
  return f"""<!doctype html>
  <html>
  <body>
    <h1><a href='/'>WEB</a></h1>
    <ol>
      {contents}
    </ol>
    {content}


    <p><a href="/create/">create</a>
    {udpage}

  </body>
  </html>
  """
