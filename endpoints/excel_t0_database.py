import pymysql
import pandas as pd 



def connect_db():
    return pymysql.connect(
        host='localhost', user = 'root', passwd = 'password', database = 'Li_ion_cell_info',
        autocommit = True, charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)

cursor = connect_db().cursor()

filepath = "/home/mantech/moumita/nunam_assignment_task/5329.xlsx"
df= pd.read_excel(filepath, sheet_name = None, engine='openpyxl')
# print(df)

Cycle_67_3_1 = df['Cycle_67_3_1']
Shape = Cycle_67_3_1.shape

Statis_67_3_1 = df['Statis_67_3_1']
Shape_Statis_67_3_1 = Statis_67_3_1.shape

Detail_67_3_1 = df['Detail_67_3_1']
Shape_Detail_67_3_1 = Detail_67_3_1.shape

DetailVol_67_3_1 = df['DetailVol_67_3_1']
Shape_DetailVol_67_3_1 = DetailVol_67_3_1.shape

DetailTemp_67_3_1 = df['DetailTemp_67_3_1']
Shape_DetailTemp_67_3_1 = DetailTemp_67_3_1.shape

Cycle_67_3_1_query = "INSERT INTO Cycle_67_3_1(channel,total_of_cycle,capacity_of_charge,capacity_of_discharge,cycle_life) VALUES(%s,%s,%s,%s,%s)"


Statis_67_3_1_query = "INSERT INTO Statis_67_3_1(channel, cycle ,step ,raw_step_id,status, start_voltage, end_voltage, start_current,end_current,capacity,endure_time,relative_time,absolute_time,discharge_capacity,charge_capacity,net_engy_dchg,engy_chg,engy_dchg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


Detail_67_3_1_query = "INSERT INTO Detail_67_3_1(record_index, status, jumpto, cycle, step, cur, voltage, capacity, energy, relative_time, absolute_time,channel) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)"

DetailVol_67_3_1_query = "INSERT INTO DetailVol_67_3_1(record_id, step_name, relative_time, realtime,auxiliary_channel_tu1_u, gap_of_voltage) VALUES(%s,%s,%s,%s,%s,%s)"


DetailTemp_67_3_1_query = "INSERT INTO DetailTemp_67_3_1(record_id, step_name, relative_time, realtime,auxiliary_channel_tu1_t, gap_of_temperature,channel) VALUES(%s,%s,%s,%s,%s,%s,1)"



# my_data = []
for i, d in DetailTemp_67_3_1.iterrows():
	tupleRow = tuple(d[i] for i in range (Shape_DetailTemp_67_3_1[1]))

	# each_row=[]
	# print("tupleRow     >>>>>",tupleRow)
	# for elem in tupleRow:
	# 	#print("elem     >>>>>>>>>>>>>>>>>>>>>>",elem)
	# 	try:
	# 		date_time_obj = datetime.datetime.strptime(str(elem), '%Y-%m-%d %H:%M:%S')
	# 		#print("date_time_obj     ",date_time_obj)
	# 		each_row.append(str(elem))
	# 	except:
	# 		each_row.append(elem)

	# final_each_tuple = tuple(each_row)
	# my_data.append(final_each_tuple)

# print(my_data)
	try:
		cursor.execute(DetailTemp_67_3_1_query,tupleRow)
			#print("@@@")
	except Exception as e:
		print(">>>> ", e)

