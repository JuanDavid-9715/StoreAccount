from dotenv import load_dotenv
import os

import config.database as conf_db

load_dotenv()

BASE_DIR = os.path.dirname(__file__)

db_access = {
    'host':os.getenv('HOST'),
    'user':os.getenv('USER'),
    'password':os.getenv('PASSWORD'),
    'database':os.getenv('DATABASE')
}

if __name__ == '__main__':
    db = conf_db.DataBase(**db_access)
    # db.get_db()
    # db.get_table()

    """ db.post_data(
        "diary", 
        {
            "sales": 3000000.0,
            "supplierExpenses": 3000000.0,
            "overheads": 3000000.0,
            "total": 3000000.0,
            "monthlyID": 1,
        }
    ) """

    # db.delete_data("diary", "id = 11")

    # db.update_data("diary", "sales = '2000000'", "id = 8")

    # db.get_column("diary")
    # db.get_column("monthly")
    # db.get_column("yearly")

    db.get_data("diary")
    # db.get_data("monthly")
    # db.get_data("yearly")

    # db.backup_db(BASE_DIR)