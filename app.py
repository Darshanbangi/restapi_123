from flask import Flask, jsonify


app = Flask('__name__')

students = [
        {
            'id': 1,
            'student_name': 'std1',
            'age': 21,
            'email':'hello@gmail.com'
        },
        {
            'id':2,
            'student_name': 'std2',
            'age': 21,
            'email': 'hello@gmail.com'
        },
        {
            'id':3,
            'student_name': 'std3',
            'age': 21,
            'email': 'hello@gmail.com'
        },
    ]


@app.route('/students-list')
def students_list():
    return jsonify(students)


@app.route('/student/get/<int:id>')
def student_get_by_id(id):
    for std in students:
        if std['id'] == id:
            return jsonify(std)

    return "id not found"

@app.route('/students-list/restapi')
def students_list_restapi():
  import requests
  url = "https://rest-api-w214.onrender.com/students-list"
  response = requests.request("GET", url)
\

if __name__ == '__main__':
    app.run(
        
        debug=True
    )
