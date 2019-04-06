# Django graphene test

My first attempt to grasp the GraphQL concept

### Prerequisites

* Project dependencies are managed with pipenv. Please refer to [official documentation](https://pipenv.readthedocs.io/en/latest/) for installation instructions.
* App uses postgresql. The default db setup you can find in `.env` file. It is [python-dotenv](https://github.com/theskumar/python-dotenv) file so you can always override it exporting `DATABASE_URL` in your shell

### Installing

In project root directory
1. Run `pipenv install`
2. Run `pipenv shell`
3. cd into `testgraphane`

## Running the tests

Completing the steps from above, run `./manage.py runserver 0.0.0.0:808`.

Now you can access `http://0.0.0.0:8080/graphql/`. It'll show up visual GraphQL playground when you can perform queries.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Pipenv](https://pipenv.readthedocs.io/en/latest/) - Dependency Management
* [Graphene](https://graphene-python.org/) - GraphQL Library

## Contributing

Any feedback appreciated.

## Authors

* **Me** [marek2901](https://github.com/marek2901)

## License

This project is licensed under the MIT License
