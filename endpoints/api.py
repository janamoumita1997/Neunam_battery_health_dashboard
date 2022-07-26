import pymysql
from flask import Flask
from flask.json import jsonify
from flask import Flask, request, make_response

app = Flask(__name__)

MYSQL_DATABASE_USER= 'root'
MYSQL_DATABASE_PASSWORD= 'password'
MYSQL_DATABASE_DB= 'Li_ion_cell_info'
MYSQL_DATABASE_HOST= 'localhost'
# Database connection config
def connect_mysql():
    return pymysql.connect(
        host=MYSQL_DATABASE_HOST, user = MYSQL_DATABASE_USER, passwd = MYSQL_DATABASE_PASSWORD, database = MYSQL_DATABASE_DB,
        autocommit = True, charset = 'utf8mb4', port= 3306,
        cursorclass = pymysql.cursors.DictCursor)


conn = connect_mysql()
cursor = conn.cursor()

@app.route('/data',methods = ['POST'])
def fetch_require_data():
	try:
		req = request.json
		battery_id = req['battery_id']
		channel_id_query = "SELECT channel FROM battary_name WHERE battery_id = %s"
		cursor.execute(channel_id_query,battery_id)
		channel_no_ = cursor.fetchall()
		print("channel_no >>>",channel_no_)

		channel_no = channel_no_[0]['channel']
		chage_discharge_query = "SELECT capacity_of_charge,capacity_of_discharge FROM Cycle_67_3_1 WHERE channel = %s"
		cursor.execute(chage_discharge_query,channel_no)
		chage_discharge_info = cursor.fetchall()

		page2_Data_query = "SELECT cur,voltage, capacity,absolute_time FROM Detail_67_3_1 WHERE channel = %s"
		cursor.execute(page2_Data_query,channel_no)
		pge2_all_data = cursor.fetchall()

		temp_query = "SELECT auxiliary_channel_tu1_t FROM DetailTemp_67_3_1 WHERE channel = %s"
		cursor.execute(temp_query,channel_no)
		temp_data = cursor.fetchall()

		data = ({"chage_discharge_info":chage_discharge_info,"pge2_all_data":pge2_all_data,"temp_data":temp_data})

		return data

	except Exception as e:
		print(e)
		return "no data get"

if __name__ == '__main__':
	app.run(debug=True)

		