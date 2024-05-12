# Contributing to Albee

## Basics

### Running Frontend:

Install packages
```sh
npm install
```

Run the app
```sh
npm run dev
```

### Running Backend:

Assuming you have Python installed, create and activate a Python Virtual Environment
```sh
virtualenv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

Run the app
```sh
python manage.py runserver
```
Note port 5432 is the default port for Postgres

## Contributing

### Contributing code:

1. Create a branch for your feature. This can usually be done with `git checkout -b <username>/<feature_name>`
2. _make changes._
3. Create some commits and push your changes to the origin.
4. Create a pull request and add a few reviewers. In the pull request, be sure to reference any relevant issue numbers.
5. Once the pull request has been approved, merge it into the master branch.
