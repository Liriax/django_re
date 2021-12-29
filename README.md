# django_re
Recommendation engine test backend, database & frontend

## Common
- Clone the repo: `git clone https://github.com/Liriax/django_re.git`
- Open the folder: `cd django_re`
- Fast mode: `git clone https://github.com/Liriax/django_re.git && cd django_re`

## Backend & Administration
### Installation & Start
- Create virtual environment: `python -m venv venv`
- Activate virtual environment
    - macOS: `source ./venv/bin/activate`
    - Windows: `venv/Scripts/activate`
- Install requirements: `pip install -r requirements.txt`
- Start backend: `python manage.py runserver 8080`
- Create a user with: `python manage.py createsuperuser`
- Open administration: http://127.0.0.1:8080/admin
- Fast mode
    - macOS: `python -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt && python manage.py runserver 8080`
    - Windows: `python -m venv venv && venv/Scripts/activate && pip install -r requirements.txt && python manage.py runserver 8080`

### Routes
- *[GET]* Recommendations: http://127.0.0.1:8080/recommend
- *[GET]* Teams Recommendations: http://127.0.0.1:8080/recommend/1
- *[GET]* Days Recommendations: http://127.0.0.1:8080/recommend/1/22/12/2021

## Frontend
### Installation & Start
- Open the folder: `cd frontend`
- Install dependencies: `npm install`
- Start frontend: `npm start`
- Open frontend: http://127.0.0.1:3000
- Fast mode: `cd frontend && npm install && npm start`

### Storybook
- Start Storybook: `npm run storybook`

### GitHub Pages
- Override dummies: `frontend > config > > common.js > API > overrideDummies: true` 
- Deploy: `npm run deploy`
- Open frontend: https://liriax.github.io/django_re
