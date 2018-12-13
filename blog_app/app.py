import json
from flask import Flask, render_template, request

app = Flask(__name__)

#### database helper method
def get_users_data(filename):
    users_result = dict()
    with open(filename, 'r') as file:
        users_result=json.load(file)
    return users_result
        
@app.route('/')
def root():
    return "this is root page Hello"
    
# as the client
# get /articles request
# application kknows to fire the method all_articles

# crud operations
# create read update destroy

articles = ['article1', 'article2','article3','article4']
    
@app.route('/articles', methods=['GET', 'POST'])
def all_articles():
    if request.method == "GET":
        # here we might make a database call to get all the articles
        return render_template('articles.html', articles=articles)
    else:
        return 'We made a POST request'
        
# create route that accepts an id
# articles/:id
# that id will be the index of a specific artilce
# then render that article string in the template

@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    article = articles[id]
    return render_template('articles.html',article=article)
    
@app.route('/users', methods=['GET'])
def get_users():
    # users = ["user1", "user2", "user3"]
    data = get_users_data("./users.json")
    users = data["users"]
    return render_template('users.html', users=users)
    
if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)