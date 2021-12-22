# django_re
recommendation engine test back end &amp; database

Steps after cloning:
1. create virtual environment
2. activate virtual environment
3. pip install -r requirements.txt
4. cd mysite
5. python manage.py runserver 8080
6. cd frontend
7. npm start

Now the react frontend should be started on http://localhost:3000/ and the django backend on port 8080:http://127.0.0.1:8080/admin/
Create a superuser with python manage.py createsuperuser or use account = password = admin

URLs:
/admin/: Admin Panel, hier kann man die DB verwalten
/recommend/: zeigt alle gegebenen Recommendations (für alle Teams) an -> Spätere "Statistik"-Seite?
/recommend/n/: zeigt alle Recommendations für Team mit dem ID n an (n ist ein Integer) -> Recommendations von der Vergangenheit ausblenden
/recommend/n/2021/12/22/: zeigt alle Recommendations für Team mit dem ID n am Tag 22/12/2021 an
