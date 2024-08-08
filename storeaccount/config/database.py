import mysql.connector
import subprocess
import datetime
import os


class DataBase():
    def __init__(self, **kwargs):
        self.__host = kwargs["host"]
        self.__user = kwargs["user"]
        self.__password = kwargs["password"]
        self.__database = kwargs["database"]

    def connection(function):
        def internal(self, *args, **kwargs):
            try:
                self.conector = mysql.connector.connect(
                    host = self.__host,
                    user = self.__user,
                    password = self.__password
                )
                self.cursor = self.conector.cursor()

                print("Conexión iniciada")

                self.result=[]
                self.state=""
                self.message=""
                self.information=""
                function(self, *args, **kwargs)
            except Exception as e:
                self.state = "500"
                self.message = "Internal Server Error"
                self.information="ERROR: Error connecting database"
                print("ERROR: Error connecting database")
                print(e)
            finally:
                self.cursor.close()
                self.conector.close()

                print("Conexión cerrada")
            return self.result
        return internal

    def validation_db(function):
        def internal(self, *args, **kwargs):
            self.cursor.execute(f"SHOW DATABASES LIKE '{self.__database}'")

            if not self.cursor.fetchone():
                self.state = "500"
                self.message = "Internal Server Error"
                self.information="ERROR: Database does not exist"
                print("ERROR: Database does not exist")

                return

            self.cursor.execute(f"USE {self.__database};")

            return function(self, *args, **kwargs)
        return internal

    def validation_table(function):
        def internal(self, table, *args, **kwargs):
            self.cursor.execute(f"SHOW TABLES LIKE '{table}'")

            if not self.cursor.fetchone():
                self.state = "500"
                self.message = "Internal Server Error"
                self.information="ERROR: Table does not exist"
                print("ERROR: Table does not exist")

                return

            return function(self, table, *args, **kwargs)
        return internal

    @connection
    @validation_db
    @validation_table
    def get_column(self, table):
        try:
            self.cursor.execute(f"SHOW COLUMNS FROM {table}")

            self.state = "200"
            self.message = "Ok"
            print(f"Lists of columns from table {table}:")

            for column in self.cursor.fetchall():
                self.result.append(column)
                print(f"  - {column[0]}.")
        except mysql.connector.Error as e:
            self.state = "500"
            self.message = "Internal Server Error"
            self.information=f"ERROR: Error getting columns from table {table}"
            print(f"ERROR: Error getting columns from table {table}")
            print(f"ERROR_TYPE: {e}")

    @connection
    @validation_db
    @validation_table
    def get_length(self, table):
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {table}")

            self.state = "200"
            self.message = "Ok"
            print(f"The length of table {table} is:")
            
            for column in self.cursor.fetchall():
                self.result.append(column)
                print(f"  - {column[0]}.")
        except mysql.connector.Error as e:
            self.state = "500"
            self.message = "Internal Server Error"
            self.information=f"ERROR: Error getting length from table {table}"
            print(f"ERROR: Error getting length from table {table}")
            print(f"ERROR_TYPE: {e}")

    @connection
    @validation_db
    @validation_table
    def get_data(self, table, column='*', join=False, condition=None, order_by=None, limit=None):
        try:
            query = f"SELECT {column} FROM {table}"

            if join and table != "yearly":
                if table == "diary":
                    query += " JOIN monthly ON diary.monthlyID=monthly.id"

                query += " JOIN yearly ON monthly.yearlyID=yearly.id"
            if condition:
                query += f" WHERE {condition}"
            if order_by:
                query += f" ORDER BY {order_by}"
            if limit:
                query += f" LIMIT {limit}"
            
            self.cursor.execute(query)

            self.state = "200"
            self.message = "Ok"
            print(f"Lists of data from table {table}:")
            for data in self.cursor.fetchall():
                self.result.append(data)
                print(f"  - {data}.")
            
        except mysql.connector.Error as e:
            self.state = "500"
            self.message = "Internal Server Error" 
            self.information=f"ERROR: Error getting data from table {table}"
            print(f"ERROR: Error getting data from table {table}")
            print(f"ERROR_TYPE: {e}")
    
    @connection
    @validation_db
    @validation_table
    def post_data(self, table, data):
        try:
            if not data:
                print("los datos están vacíos")
                return

            columns = ", ".join(data.keys())
            values = ", ".join(f"'{v}'" for v in data.values())

            self.cursor.execute(f"INSERT INTO {table}({columns}) VALUES({values})")
            self.conector.commit()

            self.state = "201"
            self.message = "Created"
            print("Injected data")
        except mysql.connector.Error as e:
            self.state = "500"
            self.message = "Internal Server Error"
            self.information=f"ERROR: Could not inject data into table {table}"
            print(f"ERROR: Could not inject data into table {table}")
            print(f"ERROR_TYPE: {e}")

    @connection
    @validation_db
    @validation_table
    def delete_data(self, table, condition):
        try:
            if not condition:
                print("los condiciones están vacíos")
                return

            self.cursor.execute(f"DELETE FROM {table} WHERE {condition}")
            self.conector.commit()

            self.state = "200"
            self.message = "Ok"
            print("Delete data")
        except mysql.connector.Error as e:
            self.state = "500"
            self.message = "Internal Server Error"
            self.information=f"ERROR: Could not delete data in table {table}"
            print(f"ERROR: Could not delete data in table {table}")
            print(f"ERROR_TYPE: {e}")

    @connection
    @validation_db
    @validation_table
    def update_data(self, table, data, condition):
        try:
            print("entro")
            if not data:
                print("los datos están vacíos")
                return

            if not condition:
                print("los condiciones están vacíos")
                return
            print("verificaciones hecha")
            update_data = ", ".join(f"{column}='{value}'" for column, value in data.items())
            print(f"update_data = {update_data}")
            print(f"condition = {condition}")

            self.cursor.execute(f"UPDATE {table} SET {update_data}WHERE {condition}")
            self.conector.commit()

            self.state = "200"
            self.message = "Ok"
            print("Update data")
        except Exception as e:
            self.state = "500"
            self.message = "Internal Server Error"
            self.information=f"ERROR: Could not update data in table {table}"
            print(f"ERROR: Could not update data in table {table}")
            print(f"ERROR_TYPE: {e}")

    @connection
    @validation_db
    def backup_db(self, base_dir):
        try:
            backup_dir = os.path.join(base_dir, "backup")
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            backup_file = f"{self.__database}_{date_str}.sql"
            backup_path = os.path.join(backup_dir, backup_file)

            with open(backup_path, 'w') as out:
                subprocess.Popen(
                    f'"C:\Program Files\MySQL\MySQL Workbench 8.0/"mysqldump --user={self.__user} --password={self.__password} --databases {self.__database}',
                    shell=True,
                    stdout=out
                )
                
            self.state = "200"
            self.message = "Ok"
            print(f"The backup was created with the name {backup_file}")
        except Exception as e:
            self.state = "500"
            self.message = "Internal Server Error"
            self.information=f"ERROR: Could not create backup"
            print(f"ERROR: Could not create backup")
            print(f"ERROR_TYPE: {e}")