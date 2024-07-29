from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from student import Student

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'student_db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)

@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        new_student = Student(
            name=data['name'],
            roll_number=data['roll_number'],
            age=data['age'],
            email=data['email'],
            phone_number=data['phone_number']
        )
        new_student.save()
        return jsonify({"message": "Student added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.objects()
    return jsonify(students), 200

@app.route('/students/<string:roll_number>', methods=['PUT'])
def update_student(roll_number):
    try:
        data = request.json
        student = Student.objects(roll_number=roll_number).first()
        if student:
            student.update(
                name=data.get('name', student.name),
                age=data.get('age', student.age),
                email=data.get('email', student.email),
                phone_number=data.get('phone_number', student.phone_number)
            )
            return jsonify({"message": "Student updated successfully!"}), 200
        else:
            return jsonify({"error": "Student not found!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/students/<string:roll_number>', methods=['DELETE'])
def delete_student(roll_number):
    try:
        student = Student.objects(roll_number=roll_number).first()
        if student:
            student.delete()
            return jsonify({"message": "Student deleted successfully!"}), 200
        else:
            return jsonify({"error": "Student not found!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
