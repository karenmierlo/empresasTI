1. criar uma branch do release:
    git checkout -b release/1.0.x (a partir da main)
2. python manage.py collectstatic
3. git add .
4. git commit -m "nome"
5. git push (set upstream - copiar e colar)
6. git push heroku release/1.0.x:main

funcionou?

sim: fazer o merge para main e para dev
    git checkout main
    git merge release/1.0.x
    git checkout dev
    git merge main


    heroku login
    heroku git:remote -a empresas-entra21
    git remote -v
    git push heroku release/1.0.2:maingi