# Basic API Project with Flask

This project is a simple demonstration of how to create and use APIs with Flask, a popular web framework for Python. It defines several endpoints that perform different operations, such as adding, subtracting, posting, getting, aborting, and returning data in JSON format. It also uses templates to render HTML pages.

## Installation

To install the required packages for this project, you need to have Python 3 and pip installed on your system. Then, you can run the following command in your terminal:

```bash
pip install flask
```

This will install Flask and requests, which are the only dependencies for this project.

## Usage

To run the project, you can use the following command in your terminal:

```bash
python app.py
```

This will start a local server on port 8000, which you can access from your browser. You can also use a tool like Postman or curl to test the API endpoints.

The available endpoints are:

- `/` : This will render the `index.html` template, which contains a simple greeting and a link to the GitHub repository of this project.
- `/add/<int:num1>/<int:num2>` : This will return the sum of `num1` and `num2` in JSON format. For example, `/add/3/5` will return `{"result": 8}`.
- `/subtract/<int:num1>/<int:num2>` : This will return the difference of `num1` and `num2` in JSON format. For example, `/subtract/10/4` will return `{"result": 6}`.
- `/post/<string:name>/<int:age>` : This will accept both GET and POST methods, and return the `name` and `age` parameters in JSON format. For example, `/post/Bob/23` will return `{"result": {"name": "Bob", "age": 23}}`.
- `/get_post/<string:name>/<int:age>` : This will accept both GET and POST methods, and return the `name` and `age` parameters in JSON format. However, if the method is GET, it will return `{"result": "GET method"}` instead. For example, `/get_post/Alice/30` will return `{"result": "GET method"}` if the method is GET, and `{"result": {"name": "Alice", "age": 30}}` if the method is POST.
- `/get_post2` : This will accept both GET and POST methods, and return the `name` and `age` parameters in JSON format. However, unlike the previous endpoint, it will get the parameters from the form data of the request, rather than the URL. For example, if you send a POST request with `name=Charlie` and `age=40` in the form data, it will return `{"result": {"name": "Charlie", "age": 40}}`.
- `/abort/<int:num>` : This will abort the request with a 404 error, unless `num` is 1, in which case it will return `Hello, world`. For example, `/abort/2` will return a 404 error, and `/abort/1` will return `Hello, world`.
- `/template` : This will render the `index.html` template, which is the same as the `/` endpoint.
- `/person/<int:id>` : This will return the details of a person with the given `id` in JSON format. The person data is stored in a dictionary inside the app. For example, `/person/1` will return `{"result": {"name": "John", "age": 25}}`.
- `/persons` : This will return the details of all the persons in the app in JSON format. The person data is stored in a list inside the app. For example, `/persons` will return `{"result": [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}, {"name": "Jack", "age": 35}]}`.
