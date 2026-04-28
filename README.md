# Cruz Johal — Personal Teaching Website

Built with **Flask** · Deployed to **Render.com** via **GitHub**

---

## Local Development

```bash
# 1. Clone your repo
git clone https://github.com/YOUR_USERNAME/cruzjohal.git
cd cruzjohal

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run locally
python app.py
# Open http://127.0.0.1:5000
```

---

## Project Structure

```
cruzjohal/
├── app.py                  # Flask routes
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn command for Render
├── render.yaml             # Render.com config
├── .gitignore
├── README.md
│
├── templates/
│   ├── base.html           # Shared nav + footer
│   ├── index.html          # Home page
│   ├── teaching.html       # Courses + certs
│   ├── python.html         # Student resources
│   ├── blog.html           # Blog listing
│   ├── post.html           # Blog post detail
│   └── contact.html        # Contact page
│
├── static/
│   ├── css/style.css       # All styles
│   ├── img/headshot.jpg    # Your photo
│   └── resume/             # Resume download
│
└── blog_posts/             # Markdown blog posts
    ├── where-is-generative-ai-heading.md
    ├── benefits-of-learning-python-in-2026.md
    └── most-profitable-skills-by-2030.md
```

---

## Adding a Blog Post

Create a new `.md` file in `blog_posts/`. Follow this format:

```markdown
# Your Post Title
Month YYYY

One-sentence teaser shown on the blog listing page.

Your post body here in Markdown...
```

The filename becomes the URL slug: `my-post-title.md` → `/blog/my-post-title`

---

## Deploying to GitHub + Render.com

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cruzjohal.git
git push -u origin main
```

### Step 2 — Deploy on Render.com

1. Go to [render.com](https://render.com) and sign in (use GitHub OAuth)
2. Click **New → Web Service**
3. Connect your GitHub repo
4. Fill in settings:
   - **Name**: cruzjohal (or whatever you like)
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free
5. Click **Create Web Service**

Render auto-deploys every time you push to `main`. 🎉

### Step 3 — Custom Domain (optional)

In Render dashboard → Settings → Custom Domain → enter `cruzjohal.com`
Then update your DNS at your domain registrar:
- Add a CNAME record: `www` → your-render-url.onrender.com
- Add an ALIAS/ANAME at root: `@` → your-render-url.onrender.com

---

## Updating the Site

```bash
# Make your changes, then:
git add .
git commit -m "describe your change"
git push
# Render auto-deploys in ~2 minutes
```
