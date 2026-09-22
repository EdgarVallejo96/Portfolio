# Portfolio

Personal portfolio site for Edgar Vallejo, built with Django. Single-page site with About, Experience, Projects,
and Contact sections, styled in a red/black theme (Oswald + Roboto).

## First-time setup

```bash
python -m venv venv
venv\Scripts\activate              # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_portfolio    # loads Experience/Project starter content
python manage.py createsuperuser   # to manage content via /admin
```

## Running the project

Once the venv exists and dependencies are installed, start the dev server with a single command
(no need to activate the venv first):

```powershell
.\venv\Scripts\python.exe manage.py runserver
```

Then visit:

- `http://127.0.0.1:8000/` - the site
- `http://127.0.0.1:8000/admin/` - manage Experience and Project entries, including uploading project screenshots

Stop the server with `Ctrl+C`.

## Project structure

- `config/` - Django project settings and root URLs.
- `portfolio/` - the app: `Experience` and `Project` models, views, admin, templates, and `i18n.py` (UI text for
  the EN/ES toggle).
- `static/` - CSS, JS, favicon/placeholder images, and the downloadable CV (`static/files/`).
- `media/projects/` - project screenshots, committed to the repo (set via the `Project.image` field/admin).

## Content

- About text, contact email, GitHub/LinkedIn links, and UI copy live in `portfolio/i18n.py` (English and Spanish)
  and `config/settings.py`.
- Experience and Project entries are stored in the database and editable via Django admin, including optional
  `*_es` fields for the Spanish translation (falls back to English if left blank). Re-run
  `python manage.py seed_portfolio` any time to reset them back to the starter content (updates existing rows by name).
- The header's EN/ES toggle switches the whole site's language (nav, bio, experience, projects, contact, and the
  downloaded CV) and is stored in the visitor's session.
