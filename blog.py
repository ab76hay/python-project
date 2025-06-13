from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for blog posts
posts = []

# Template for pages
layout = '''
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; background: #f4f4f4; }}
        h1 {{ color: #333; }}
        .post {{ background: white; padding: 15px; margin-bottom: 20px; border-radius: 5px; }}
        .form-box {{ background: #fff; padding: 15px; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>📝 My Personal Blog</h1>
    <a href="{{ url_for('add_post') }}">➕ Add New Post</a>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
'''

# Home page
@app.route('/')
def home():
    return render_template_string('''
    {% extends layout %}
    {% block content %}
        {% for post in posts %}
            <div class="post">
                <h2><a href="{{ url_for('view_post', post_id=loop.index0) }}">{{ post.title }}</a></h2>
                <p>{{ post.content[:100] }}...</p>
            </div>
        {% else %}
            <p>No posts yet.</p>
        {% endfor %}
    {% endblock %}
    ''', layout=layout, posts=posts)

# View a single post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = posts[post_id]
    return render_template_string('''
    {% extends layout %}
    {% block content %}
        <div class="post">
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
            <a href="{{ url_for('home') }}">← Back</a>
        </div>
    {% endblock %}
    ''', layout=layout, post=post)

# Add new post
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('home'))

    return render_template_string('''
    {% extends layout %}
    {% block content %}
        <div class="form-box">
            <form method="POST">
                <p>Title:<br><input type="text" name="title" style="width:100%;" required></p>
                <p>Content:<br><textarea name="content" rows="5" style="width:100%;" required></textarea></p>
                <p><button type="submit">Publish</button></p>
            </form>
            <a href="{{ url_for('home') }}">← Back</a>
        </div>
    {% endblock %}
    ''', layout=layout)

if __name__ == '__main__':
    app.run(debug=True)
