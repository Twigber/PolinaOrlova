
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# ===================================================================================================================

@app.route('/polina')
def polina():
    return "Polina"

@app.route('/user_info', methods=['GET'])
def user_info():
        user_name = request.args.get('name')
        user_age = request.args.get('age')
        user_list = [user_name, user_age]
        return jsonify(user_list)

@app.route('/work', methods=['POST'])
def work():
    user_name = request.form.get('name')
    user_salary = request.form.get('salary')
    user_experience_month = request.form.get('experience')
    total = int(user_salary) * int(user_experience_month)
    you_have = user_name + ' За весь период работы вы заработали ' + str(total) + '$'
    return you_have

import csv

file_path = 'C:/Users/Администратор/Desktop/Test/Python/lesson_1/'
file_name = 'users.csv'
full = file_path + file_name

# columns = ['Name', 'Age', 'Salary']
#
# with open(full, 'w') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(columns)

@app.route('/users_list_raw', methods=['POST'])
def users_list_raw():
    user_name = request.json['name']
    user_age = int(request.json['age'])
    user_salary = int(request.json['salary'])
    users_list_mini = []
    users_list_mini.append(user_name)
    users_list_mini.append(user_age)
    users_list_mini.append(user_salary)
    print('user_list_mini =', users_list_mini)

    with open(full, 'a') as f_2:
        writer = csv.writer(f_2, lineterminator='\n')
        writer.writerow(users_list_mini)
    return 'Пользователь добавлен'


# ==================================================================================================================





conn = psycopg2.connect(dbname='qa_ddldb_23_110',
                        user='user_23_110',
                        password='123',
                        host='159.69.151.133',
                        port='5056')
cursor = conn.cursor()


@app.route('/db_save', methods=['GET', 'POST'])
def db_save():
    kotik_name = request.args.get('kotik_name')
    registr = request.args.get('registr')
    cursor = conn.cursor()
    if conn:
        base_date = (kotik_name, registr)
        k_query = """insert into public.kotiki(kotik_name, registr) VALUES (%s, %s)"""
        cursor.execute(k_query, base_date)

        conn.commit()
        cursor.close()
        return 'User saved'
    else:
        return 'User doesn`t save'


@app.route('/kotik_name_registr')
def kotik_name_registr():

    result = {}
    cursor = conn.cursor()
    if conn:
        sl = cursor.execute('select kotiki.id, kotiki.kotik_name, kotiki_age.kotik_age'\
                            ' from kotiki'\
                            ' join kotiki_age on kotiki.id = kotiki_age.id ')
        sll = cursor.fetchall()
        for i in sll:
            result[str(i[0])] = {'Kotik_name': i[1], 'Age': i[2]}


        cursor.close()
        return jsonify(result)










