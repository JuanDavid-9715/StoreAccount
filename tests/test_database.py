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
        "table, column, condition, expected",
        [
            ("diary", "*", None, "200"), 
            ("monthly", "*", None, "200"), 
            ("yearly", "*", None, "200"), 
            ("diary", "day", None, "200"), 
            ("monthly", "month", None, "200"), 
            ("yearly", "year", None, "200"),
            ("diary", "*", "monthlyID='1'", "200"), 
            ("monthly", "*", "yearlyID='1'", "200"), 
            ("yearly", "*", "id='1'", "200"),
            ("diary", "day", "id='1'", "200"), 
            ("monthly", "month", "id='1'", "200"), 
            ("yearly", "year", "id='1'", "200"),
            ("notExist", "*", None, "500"), 
        ])
    def test_get_data(self, table, column, condition, expected):
        self.db.get_data(table, column=column, condition=condition)

        assert self.db.state == expected
        if self.db.state == expected:
            assert type(self.db.result) == list
            assert self.db.result != None

    @pytest.mark.parametrize(
        "table, order_by, column, condition, address, expected",
        [
            ("diary", "day", "*", None, "ASC", "200"), 
            ("monthly", "month", "*", None, "ASC", "200"), 
            ("yearly", "year", "*", None, "ASC", "200"), 
            ("diary", "day", "*", None, "DESC", "200"), 
            ("monthly", "month", "*", None, "DESC", "200"), 
            ("yearly", "year", "*", None, "DESC", "200"), 
            ("diary", "day", "*", "monthlyID='1'", "ASC", "200"), 
            ("monthly", "month", "*", "yearlyID='1'", "ASC", "200"), 
            ("diary", "day", "*", "monthlyID='1'", "DESC", "200"), 
            ("monthly", "month", "*", "yearlyID='1'", "DESC", "200"), 
            ("notExist", "", "*", None, "ASC", "500"), 
        ])
    def test_get_data_orderBy(self, table, order_by, column, condition, address, expected):
        self.db.get_data_orderBy(table, order_by, column=column, condition=condition, address=address)

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