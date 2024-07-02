import mysql.connector
import subprocess
import datetime
import os


class DataBase():
    def __init__(self, **kwargs):
        self.host = kwargs["host"]
        self.user = kwargs["user"]
        self.password = kwargs["password"]
        self.database = kwargs["database"]

    def connection(function):
        def internal(self, *args, **kwargs):
            try:
                self.conector = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.password
                )
                self.cursor = self.conector.cursor()

                print("Conexión iniciada")

                function(self, *args, **kwargs)
            except:
                print("ERROR: Error en la conexión")
            finally:
                self.cursor.close()
                self.conector.close()

                print("Conexión cerrada")

        return internal

    def validation_db(function):
        def internal(self, *args, **kwargs):
            self.cursor.execute(f"SHOW DATABASES LIKE '{self.database}'")

            if not self.cursor.fetchone():
                print("ERROR: Error base de datos no existe")

                return

            self.cursor.execute(f"USE {self.database};")

            return function(self, *args, **kwargs)
        return internal

    def validation_table(function):
        def internal(self, tableName, *args, **kwargs):
            self.cursor.execute(f"SHOW TABLES LIKE '{tableName}'")

            if not self.cursor.fetchone():
                print("ERROR: Error tabla no existe")

                return

            return function(self, tableName, *args, **kwargs)
        return internal

    @connection
    def get_db(self):
        self.cursor.execute("SHOW DATABASES")

        print("Listas de las bases de datos:")

        for queries in self.cursor.fetchall():
            print(f"  - {queries[0]}.")
    
    @connection
    @validation_db
    def get_table(self):
        try:
            self.cursor.execute("SHOW TABLES")

            print("Listas de las tablas:")

            for queries in self.cursor.fetchall():
                print(f"  - {queries[0]}.")
        except:
            print("ERROR: Error al obtener las tablas")

    @connection
    @validation_db
    @validation_table
    def get_column(self, tableName):
        try:
            self.cursor.execute(f"SHOW COLUMNS FROM {tableName}")

            print(f"Listas de las columnas de la tabla {tableName}:")

            for queries in self.cursor.fetchall():
                print(f"  - {queries[0]}.")
        except:
            print(f"ERROR: Error al obtener las columnas de la taba {tableName}")

    @connection
    @validation_db
    @validation_table
    def get_data(self, tableName):
        try:
            self.cursor.execute(f"SELECT * FROM {tableName}")

            print(f"Listas de los datos de la tabla {tableName}:")

            for queries in self.cursor.fetchall():
                print(f"  - {queries}.")
        except:
            print(f"ERROR: Error al obtener los datos de la tabla {tableName}")

    @connection
    @validation_db
    @validation_table
    def post_data(self, tableName, data):
        try:
            if not data:
                print("los datos están vacíos")
                return

            column_list = data.keys()
            value_list = data.values()
            column_string = ""
            value_string = ""

            for column in column_list:
                column_string += f"{column}, "
            
            for value in value_list:
                value_string += f"{value}, "

            column_string = column_string[:-2]
            value_string = value_string[:-2]

            self.cursor.execute(f"INSERT INTO {tableName}({column_string}) VALUES({value_string})")
            self.conector.commit()

            print("Datos inyectados")
        except:
            print("ERROR: No se puedo inyectar los datos")

    @connection
    @validation_db
    @validation_table
    def delete_data(self, tableName, condition):
        try:
            if not condition:
                print("los condiciones están vacíos")
                return

            self.cursor.execute(f"DELETE FROM {tableName} WHERE {condition}")
            self.conector.commit()

            print("Datos eliminados")
        except:
            print("ERROR: No se puedo eliminar los datos")

    @connection
    @validation_db
    @validation_table
    def update_data(self, tableName, data, condition):
        try:
            if not data:
                print("los datos están vacíos")
                return

            if not condition:
                print("los condiciones están vacíos")
                return

            self.cursor.execute(f"UPDATE {tableName} SET {data} WHERE {condition}")
            self.conector.commit()

            print("Datos actualizados")
        except:
            print("ERROR: No se puedo eliminar los datos")

    @connection
    @validation_db
    def backup_db(self, base_dir):
        backup_dir = os.path.join(base_dir, "backup")
        data = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        with open(f'{backup_dir}/{self.database}_{data}.sql', 'w') as out:
            subprocess.Popen(
                f'"C:\Program Files\MySQL\MySQL Workbench 8.0/"mysqldump --user={self.user} --password={self.password} --databases {self.database}',
                shell=True,
                stdout=out
            )

        print(f"Se creo la la copia de seguridad con el nombre {self.database}_{data}.sql")