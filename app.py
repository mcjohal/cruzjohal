from flask import Flask, render_template, abort
import os, markdown2, glob
from datetime import datetime

app = Flask(__name__)

def parse_post_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), "%B %Y")
    except ValueError:
        return datetime.min

def get_posts():
    posts = []
    for path in glob.glob("blog_posts/*.md"):
        with open(path) as f:
            lines = f.read().splitlines()
        slug = os.path.basename(path).replace(".md", "")
        title = lines[0].lstrip("# ").strip() if lines else slug
        date  = lines[1].strip() if len(lines) > 1 else ""
        excerpt = " ".join(lines[3:6]) if len(lines) > 3 else ""
        posts.append({"slug": slug, "title": title, "date": date, "excerpt": excerpt})
    posts.sort(key=lambda p: parse_post_date(p["date"]), reverse=True)
    return posts

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/teaching")
def teaching():
    return render_template("teaching.html")

@app.route("/python")
def python_page():
    return render_template("python.html")

@app.route("/python/resources")
def python_resources():
    return render_template("resources.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=get_posts())

@app.route("/blog/<slug>")
def post(slug):
    path = f"blog_posts/{slug}.md"
    if not os.path.exists(path):
        abort(404)
    with open(path) as f:
        content = markdown2.markdown(f.read(), extras=["fenced-code-blocks","tables"])
    return render_template("post.html", content=content, slug=slug)

@app.route("/claude")
def claude_page():
    return render_template("claude.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
