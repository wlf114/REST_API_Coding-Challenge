#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from config import db, app
from models import User, Task, UserSchema, TaskSchema


#Convert the errors to a more readable state
@app.errorhandler(404)
def not_found(error):
    """
    This function convert the 404 message to a more readable state.
    
    return: error not found 
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


#Create a URL route in the application for "/api/tasks"
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    This function print out all the current tasks
    
    return: list of tasks within the data structure
    """
    task = Task.query.order_by(Task.id).all()

    # Serialize the data for the response
    task_schema = TaskSchema(many=True)
    data = task_schema.dump(task).data
    return jsonify(data)


#Create a URL route in the application for "/api/users"
@app.route('/api/users', methods=['GET'])
def get_users():
    """
    This function print out all the current users
    
    return: list of users within the data structure
    """
    user = User.query.order_by(User.id).all()

    # Serialize the data for the response
    user_schema = UserSchema(many=True)
    data = user_schema.dump(user).data
    return jsonify(data)


#Create a URL route in the application for "/api/users/<int:user_id>"
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_tasks_by_user(user_id):
    """
    This function print out all the current tasks by the user
    
    return: list of tasks within the data structure
    """
    task = Task.query.filter(Task.user_id == user_id).all()

    # Serialize the data for the response
    task_schema = TaskSchema(many=True)
    data = task_schema.dump(task).data
    return jsonify(data)


#Create a URL route in the application for "/api/tasks/<int:task_id>"
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    This funciton returns a specific task that has been query.
    
    return: The task in query
    """
    task = Task.query.filter(Task.id == task_id)

    # Serialize the data for the response
    task_schema = TaskSchema(many=True)
    data = task_schema.dump(task).data
    return jsonify(data)


#Create a URL route in the application for "/api/tasks/archive/<archive>"
@app.route('/api/tasks/archive/<archive>', methods=['GET'])
def get_archive_task(archive):
    """
    This funciton returns all archived and active tasks
    
    return: All archived or active tasks
    """
    if (archive == 'True' or archive == 'true'):
        task = Task.query.filter(Task.archive == 1).all()
    
        # Serialize the data for the response
        task_schema = TaskSchema(many=True)
        data = task_schema.dump(task).data
        return jsonify(data)
    
    elif(archive == 'False' or archive == 'false'):
        task = Task.query.filter(Task.archive == 0).all()
    
        # Serialize the data for the response
        task_schema = TaskSchema(many=True)
        data = task_schema.dump(task).data
        return jsonify(data)
    
    else:
        abort(404)


#Create a URL route in the application for "/api/tasks/create"
@app.route('/api/tasks/create', methods=['POST'])
def create_task():
    """
    This function creates a new task and add to the data structure.
    
    return: The new task added 
    """
    task = Task(user_id = request.json['user_id'], title = request.json['title'], 
                description = request.json.get('description', ""), archive = 0)
    
    db.session.add(task)
    db.session.commit()
    
    task_schema = TaskSchema()
    data = task_schema.dump(task).data
    return jsonify(data), 201
    


#Create a URL route in the application for "/api/tasks/edit/<int:task_id>"
@app.route('/api/tasks/edit/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    This funciton finds the 
    task in query. Once found, the old task will be updated with the new
    information.
    
    return: The updated task 
    """
    task = Task.query.filter(Task.id == task_id).one_or_none()
    
    if task is not None:
        if not request.json:
            abort(400)
        if 'title' in request.json and type(request.json['title']) != str:
            abort(400)
        if 'description' in request.json and type(request.json['description']) is not str:
            abort(400)
        if 'archive' in request.json and type(request.json['archive']) is not str:
            abort(400)
            
        if 'title' in request.json:
            task.title = request.json['title']
        if 'description' in request.json:
            task.description = request.json['description']
        if 'archive' in request.json:
            if (request.json['archive'] == 'True' or request.json['archive'] == 'true'):
                task.archive = 1
            elif (request.json['archive'] == 'False' or request.json['archive'] == 'false'):
                task.archive = 0
        
        db.session.commit()
        
        task_schema = TaskSchema()
        data = task_schema.dump(task).data
        return jsonify(data), 201
    
    else:
        abort(404)
    

#Create a URL route in the application for "/api/tasks/delete/<int:task_id>"
@app.route('/api/tasks/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Identify the task and deletes the task.
    
    return: True
    """
    task = Task.query.filter(Task.id == task_id).one_or_none()
    
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        
        return jsonify({'result': True})
    
    else:
        abort(404)
        

#Run the application
if __name__ == '__main__':
    app.run(debug=True)
