# Portfolio

Personal portfolio site for Edgar Vallejo, built with Django. Single-page site with About, Experience, Projects,
and Contact sections, styled in a red/black theme (Oswald + Roboto).

## Setup

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_portfolio   # loads Experience/Project starter content
python manage.py createsuperuser  # to manage content via /admin
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `http://127.0.0.1:8000/admin/` to manage Experience and Project
entries, including uploading project screenshots.

## Project structure

- `config/` - Django project settings and root URLs.
- `portfolio/` - the app: `Experience` and `Project` models, views, admin, and templates.
- `static/` - CSS, JS, favicon/placeholder images, and the downloadable CV (`static/files/`).
- `media/` - uploaded project screenshots (created at runtime, not committed).

## Content

- About text, contact email, GitHub/LinkedIn links live in `config/settings.py` and `portfolio/templates/portfolio/home.html`.
- Experience and Project entries are stored in the database and editable via Django admin. Re-run
  `python manage.py seed_portfolio` any time to reset them back to the starter content (updates existing rows by name).
