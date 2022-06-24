import cx_Oracle as oracle
#from oracle_config import *

ip = "172.20.100.121"

host = "emdb1-vip.kdahit.com"

port = 1521

service_name =  "EMRAC.kdahit.com"

instance_name = "EMRAC1"

dsn_tns = oracle.makedsn(ip,port,instance_name)

ora_db = oracle.connect("appluser","appluser",dsn_tns)

cursor = ora_db.cursor()


class Ora:

    def __init__(self):
        self.ora_db = oracle.connect("appluser","appluser",dsn_tns)
        self.cursor = ora_db.cursor()

    def status_update(self):

        if self.ora_db:
            return "You have connected to the Database"

        else:
            return "Unable to connect to the database! Please contact the IT Department" 
      


    def __del__(self):
        self.cursor.close()
        self.ora_db.close()
    
    def get_label_data(self,uhid):

      
        sql_qurey = ('''
        
        Select a.PATIENT_ID, a.PATIENT_NAME,decode(sex,'F','Female','M','Male','Unknown') Sex , trunc((sysdate - a.DATE_OF_BIRTH) / 365, 0) || ' Y' as AGE,d.PRACTITIONER_NAME,e.SERV_ITEM_DESC,e.CHARGE_DATE_TIME
        from MP_Patient a , AM_PRACTITIONER d , BL_PATIENT_CHARGES_INTERFACE e --, OP_CURRENT_PATIENT c ,IP_OPEN_ENCOUNTER f
        where a.PATIENT_ID = e.PATIENT_ID and d.PRACTITIONER_ID = e.PHYSICIAN_ID ---and f.ADMIT_PRACTITIONER_ID = d.PRACTITIONER_ID
        and e.BLNG_SERV_CODE like 'NMNM%' AND E.PATIENT_ID = :uhid_get


        ''')

        self.cursor.execute(sql_qurey,{"uhid_get":uhid})
        data_for_label = self.cursor.fetchall()
        # for row in get:
        #     print(row)
        #AND A.PATIENT_ID = :uhid_get
       
        return data_for_label
        
          



#dsn_tns = cx_Oracle.makedsn(ip,port,instance_name)

#db = cx_Oracle.connect("appluser","appluser",dsn_tns)


#172.20.100.121

