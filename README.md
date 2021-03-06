# REST_API_Coding-Challenge
A REST API created for the Thirdfort coding challenge

## How to run the API
To run the API, multiple python dependencies are needed and you can install all the required dependencies by the running the following command:
```
pip install Flask Flask-SQLAlchemy flask-marshmallow marshmallow-sqlalchemy marshmallow
```
1.  **Flask** install the flask micro-framework to python.
2.  **Flask-SQLAlchemy** adds SQLAlchemy for database creation.
3.  **flask-marshmallow** adds the flask part of mashmallow.
4.  **marshmallow-sqlalchemy** allow programs to serialize and deserialize Python objects generated by SQLAlchemy.
5.  **marshmallow** adds the Marshmallow functionality.

Once all the dependencies have been installed, the following command can be runned to initialise the server:
```
python app.py
```
This should initialise a server at `http://localhost:5000`, since no `.html` have been created to support the API. To run the function located in the `app.py`, we have to invoke `curl` within the terminal to gain access to these funtions.

## The Data Structure
The models of the database can be found within the `models.py` file. Two models have been defined and they are `User` and `Task`, where `Task` is a child of `User`.

The model `Task` contains:
* id - An value assigned to the node, an integer
* title - The title of the task, a string
* description - Some description of the task itself and be left blanked, a string
* archive - The current state of the task, a bool
* user_id - The id of the user this task belongs to, an integer

## The functions
All functions are associated with the `http://localhost:5000/api` URI and they can be invoked by calling the correct `curl` commands.

### Creating a new node
```
curl -i -H "Content-Type: application/json" -X POST -d "{""user_id"":1, ""title"":""Do work"", ""description"":""REST API""}" http://localhost:5000/api/tasks/create
```
This will create a new node within the database for `user_id:1` by invoking the `POST` method.

### Update a previously saved note
```
C:\Users\William Fung>curl -i -H "Content-Type: application/json" -X PUT -d "{""title"":""Watch movie""}" http://localhost:5000/api/tasks/edit/2
```
This edits the title of `task_id:2` by invoking the `PUT` method.

### Delete a saved note
```
curl -X DELETE http://localhost:5000/api/tasks/delete/1
```
This deletes a node with `task_id:1` by invoking the `DELETE` method.

### Archive a note
```
curl -i -H "Content-Type: application/json" -X PUT -d "{""archive"":""true""}" http://localhost:5000/api/tasks/edit/2
```
This updates the `archive` variable within `task_id:2` to `true` by using the `PUT` method. 

### Unarchive a previously archived note
```
curl -i -H "Content-Type: application/json" -X PUT -d "{""archive"":""false""}" http://localhost:5000/api/tasks/edit/2
```
The change the state of the archive value back to false.

### List saved notes that aren't archived
```
curl -i http://localhost:5000/api/tasks/archive/false
```
Lists all the nodes that are active.

### List notes that are archived
```
curl -i http://localhost:5000/api/tasks/archive/true
```
List all the nodes that have been archived.

## Software chosen for the build
The programming language python was chosen due to the extensive number of dependencies that are avaiable to create a REST API. The dependencies chosen were Flask, SQLAlchemy and Marshmallow. Together they allowed the creation of the current build.

The Flask micro-framewok allows for the initialisation of local server with little to no setup and allows for the delivery of HTTP methods. It also supports a JSON-based data-interchange format.

SQLAlchemy provides an Object Relational Model (ORM), which stores Python objects to a database representation and allows for a multi-user environment. It also has tie-in with the Flask framework, hence no addtional setups are required.

Marshmallow provides functionality to serialise and deserialise Python objects as they flow out of and into the JSON-based REST API.

## Possible alternatives
There are many alternatives to the software chosen for the build. For example, Java could have been used to setup the API and instead of using SQLite from SQLAlchemy, one could have used PostgreSQL. However, using PostgreSQL would require additional setup.

## Further improvments
The web service is currently open to any clients, meaning an unauthorised person can write a new client that can access and edit the data. Although a `User` model has been setup, it currently does not act as an authentication to the API. Therefore, a login form should be created.

