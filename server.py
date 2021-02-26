from flask import Flask, render_template, url_for, request
import database
import bussiness_logic

# constructor
app = Flask(__name__)


@app.route('/post-employee', methods=['POST'])
def post_employee():
    try:
        data = request.get_json()
        emp_id = data['emp_id']
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        metadata = data['metadata']
        print(emp_id, name, email,
              phone, address, metadata)
        database.insert_data(emp_id, name, email,
                             phone, address, metadata)
        response = {
            "data": "Updated",
            "status": 1
        }
    except:
        response = {
            "data": "not updated",
            "status": 0
        }
    return response


@app.route('/delete-employee', methods=['POST'])
def delete_employee():

    try:
        data = request.get_json()
        print(data['emp_id'])
        data_delete = database.delete_data(data['emp_id'])
        response = {
            "emp_id_deleted": data['emp_id'],
            "status": 1
        }
    except:
        response = {
            "emp_id_deleted": "failure",
            "status": 0
        }
    return response


@app.route('/select-employee', methods=['GET', 'POST'])
def select_employee():
    try:
        data = request.get_json()
        value = database.select_data(data['table'])
        jon = bussiness_logic.dictionary_conversion(value)
        print(jon)
        response = {
            "table": jon,
            "status": 1
        }

    except:
        response = {
            "table": "None",
            "status": 0
        }
    return response


@app.route('/update-data', methods=['POST'])
def update_employee():
    try:
        data = request.get_json()
        print(data['update_content'],
              data['update_content_data'], data['id'])
        database.update_data(data['update_content'],
                             data['update_content_data'], data['id'])
        response = {
            "update": "table updated",
            "status": 1
        }

    except:
        response = {
            "update": "table not updated",
            "status": 0

        }
    return response


if __name__ == "__main__":
    app.run(debug=True)
