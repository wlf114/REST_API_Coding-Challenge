from flask import make_response, abort
from config import db, app
from models import User, Task, UserSchema, TaskSchema

@app.route('/api/user', methods=['GET'])
def read_all_user():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    user = User.query.order_by(User.user_id).all()

    # Serialize the data for the response
    user_schema = UserSchema(many=True)
    data = user_schema.dump(user).data
    return data

"""
#Create a URL route in the application for "/api/tasks"
@app.route('/api/tasks', methods=['GET'])
def get_tasks():

    return jsonify({'tasks': [make_public_task(task) for task in tasks]})
"""

#Create a URL route in the application for "/api/tasks"
@app.route('/api/tasks', methods=['GET'])
def read_all_task():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    task = Task.query.order_by(Task.task_id).all()

    # Serialize the data for the response
    task_schema = TaskSchema(many=True)
    data = task_schema.dump(task).data
    return data