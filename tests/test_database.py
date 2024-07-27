import pytest

from dotenv import load_dotenv
import os

from storeaccount.config.database import DataBase

load_dotenv()

BASE_DIR = os.path.dirname(__file__)

db_access = {
    'host':os.getenv('HOST'),
    'user':os.getenv('USER'),
    'password':os.getenv('PASSWORD'),
    'database':os.getenv('DATABASE')
}

class TestDatabase():
    db = DataBase(**db_access)

    @pytest.mark.parametrize(
        "table, expected",
        [
            ("diary", "200"), 
            ("monthly", "200"), 
            ("yearly", "200"), 
            ("notExist", "500"),
        ])
    def test_get_column(self, table, expected):
        self.db.get_column(table)

        assert self.db.state == expected
        if self.db.state == expected:
            assert type(self.db.result) == list
            assert self.db.result != None

    @pytest.mark.parametrize(
        "table, column, join, condition, order_by, limit, expected",
        [
            ("diary", "*", False, None, None, None, "200"), 
            ("monthly", "*", False, None, None, None, "200"), 
            ("yearly", "*", False, None, None, None, "200"),

            ("diary", "day", False, None, None, None, "200"), 
            ("monthly", "month", False, None, None, None, "200"), 
            ("yearly", "year", False, None, None, None, "200"),

            ("diary", "*", True, None, None, None, "200"), 
            ("monthly", "*", True, None, None, None, "200"),
            ("yearly", "*", True, None, None, None, "200"),

            ("diary", "*", False, "monthlyID='1'", None, None, "200"), 
            ("monthly", "*", False, "yearlyID='1'", None, None, "200"), 

            ("diary", "*", False, None, "day DESC", None, "200"), 
            ("monthly", "*", False, None, "month DESC", None, "200"), 
            ("yearly", "*", False, None, "year DESC", None, "200"),

            ("diary", "*", False, None, None, "1,10", "200"), 
            ("monthly", "*", False, None, None, "1,10", "200"), 
            ("yearly", "*", False, None, None, "1,4", "200"),

            ("diary", "day", True, None, "day DESC, month DESC, year DESC", "1,10", "200"), 
            ("monthly", "month", True, None, "month DESC, year DESC", "1,10", "200"), 
            ("yearly", "year", False, None, "year DESC", "1,4", "200"),

            ("notExistTable", "*", False, None, None, None, "500"), 
            ("diary", "notExistColumn", False, None, None, None, "500"),
            ("diary", "*", False, "notExistColumn='1'", None, None, "500"),
            ("notExistTable", "*", False, None, "notExistColumn DESC", None, "500"), 
        ])
    def test_get_data(self, table, column, join, condition, order_by, limit, expected):
        self.db.get_data(table, column=column, join=join, condition=condition, order_by=order_by, limit=limit)

        assert self.db.state == expected
        if self.db.state == expected:
            assert type(self.db.result) == list
            assert self.db.result != None

    @pytest.mark.parametrize(
        "table, data, expected",
        [
            (
                "diary", 
                {
                    "day": "test",
                    "sales": 1000000.0,
                    "supplierExpenses": 1000000.0,
                    "overheads": 1000000.0,
                    "total": 1000000.0,
                    "monthlyID": 1,
                },
                "201"
            ), 
            (
                "monthly",
                {
                    "month": "test",
                    "sales": 1000000.0,
                    "supplierExpenses": 1000000.0,
                    "overheads": 1000000.0,
                    "total": 1000000.0,
                    "yearlyID": 1,
                },
                "201"
            ), 
            (
                "yearly",
                {
                    "year": "test",
                    "sales": 1000000.0,
                    "supplierExpenses": 1000000.0,
                    "overheads": 1000000.0,
                    "total": 1000000.0,
                },
                "201"
            ),
            (
                "yearly",
                {
                    "year":"test",
                    "sales":"errorType"
                },
                "500"
            ),
            (
                "yearly",
                {
                    "year":"test",
                    "test":"test"
                },
                "500"
            ),
            ("notExist", {}, "500"),
        ])
    def test_post_data(self,table, data, expected):
        self.db.post_data(table, data)

        assert self.db.state == expected

    @pytest.mark.parametrize(
        "table, data, condition, expected",
        [
            ("diary", "sales = '2000000'", "day = 'test'", "200"), 
            ("monthly", "sales = '2000000'", "month = 'test'", "200"), 
            ("yearly", "sales = '2000000'", "year = 'test'", "200"), 
            ("yearly", "sales = 'test'", "year = 'test'", "500"), 
            ("yearly", "test = 'test'", "year = 'test'", "500"),
            ("notExist", "", "", "500"),
        ])
    def test_update_data(self, table, data, condition, expected):
        self.db.update_data(table, data, condition)

        assert self.db.state == expected

    @pytest.mark.parametrize(
        "table, condition, expected",
        [
            ("diary", "day = 'test'", "200"), 
            ("monthly", "month = 'test'", "200"), 
            ("yearly", "year = 'test'", "200"), 
            ("yearly", "test = 'test'", "500"), 
            ("notExist", "", "500"),
        ])
    def test_delete_data(self, table, condition, expected):
        self.db.delete_data(table, condition)

        assert self.db.state == expected
    
    def test_backup_db(self):
        self.db.backup_db(BASE_DIR)

        assert self.db.state == "200"