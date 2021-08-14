from flask import jsonify, request
from app import app, db
from app.models import User
from sqlalchemy import func


@app.route('/hello', methods=['GET'])
def hello():

    return 'Hello world!', 200


@app.route('/getUsers', methods=['GET'])
def getUsers():

    users = User.query.all()
    res = jsonify([
        {
            "name": u.name,
            "phone": u.phone,
            "age": u.age
        } for u in users]
    )
    return res, 200

@app.route('/getUser', methods=['GET'])
def getUser():

    name = request.args.get('name')

    # Validate parameter
    if name is not None:
        # Filter by name lowercase
        user = User.query.filter(func.lower(User.name) == func.lower(name)).first()

        # if not response
        if user is None:
            res = jsonify({'msg': 'User not found'})

        # if response
        else:
            res = jsonify({
                "name": user.name,
                "phone": user.phone,
                "age": user.age
            })
        return res, 200

    # Parameter not found
    else:
        return {"msg": "Parameter name not found"}


## Add parameters in url
@app.route('/searchUser/<name>', methods=['GET'])
def searchUser(name):

    #name = request.args.get('name')

    # Validate parameter
    if name is not None:
        # Filter by name lowercase
        user = User.query.filter(func.lower(User.name) == func.lower(name)).first()

        # if not response
        if user is None:
            res = jsonify({'msg': 'User not found'})

        # if response
        else:
            res = jsonify({
                "name": user.name,
                "phone": user.phone,
                "age": user.age
            })
        return res, 200

    # Parameter not found
    else:
        return {"msg": "Parameter name not found"}


@app.route('/createUser', methods=['POST'])
def createUser():

    # Validate JSON format
    if request.is_json:
        data = request.get_json()
        user = User(name=data['name'], phone=data['phone'], age=data['age'])
        db.session.add(user)
        db.session.commit()
        res = jsonify({'msg': 'User created successfully'})
        return res

    # Invalid JSON format
    else:
        return {"msg": "Invalid JSON format"}


@app.route('/updateAge', methods=['PUT'])
def updateAge():

    name = request.args.get('name')
    newAge = request.args.get('newAge')

    # Validate parameter
    if name or newAge is not None:
        user = User.query.filter(func.lower(User.name) == func.lower(name)).first()

        # if not response
        if user is None:
            res = jsonify({'msg': 'User not found'})

        # if response
        else:
            user.age = newAge
            db.session.commit()
            res = jsonify({'msg': 'User updated successfully'})

        return res, 200

    # Parameter not found
    else:
        return {"msg": "Parameter name not found"}


## Add parameters in url
@app.route('/deleteUser', methods=['DELETE'])
def deletehUser():

    name = request.args.get('name')

    # Validate parameter
    if name is not None:

        # Filter by name lowercase
        user = User.query.filter(func.lower(User.name) == func.lower(name)).first()

        # if not response
        if user is None:
            res = jsonify({'msg': 'User not found'})

        # if response
        else:

            # Delete by id User
            User.query.filter(User.id == user.id).delete()
            db.session.commit()

            res = jsonify({'msg': 'User deleted'})
        return res, 200

    # Parameter not found
    else:
        return {"msg": "Parameter name not found"}
