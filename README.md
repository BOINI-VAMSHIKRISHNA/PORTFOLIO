# Running the Flask version

## Run it locally

```
cd portfolio-flask
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:3000` in your browser. Stop it with Ctrl+C.

(If `python` isn't recognized on Windows, try `py app.py` instead — some installs only register the `py` launcher.)

## Deploy to Render

1. Push this folder's contents to a GitHub repo, keeping the structure:
   ```
   app.py
   requirements.txt
   render.yaml
   templates/index.html
   ```
2. On render.com: **New +** → **Web Service** → connect the repo.
3. Render should pick up settings from `render.yaml` automatically. If not, set manually:
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Deploy — you'll get a URL like `https://vamshi-krishna-portfolio.onrender.com`.

## Keep it awake with UptimeRobot

Same as before: add an HTTP(s) monitor pointed at `your-render-url.onrender.com/health`, interval set to 5 minutes (the free-plan minimum).

## Editing content

All the page content lives in `templates/index.html` — same file as the Node version, just served by Flask's `render_template` instead of Express's static middleware.
