from typing import Dict, List

import psycopg2


def insert(table: str, column_values: Dict):
    conn = psycopg2.connect(dbname='midis_schedule_db', user='postgres',
                            password='SECRET', host='localhost')
    cursor = conn.cursor()
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys())).replace('?', '%s')
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def fetchall(table: str, columns: List[str]) -> List[Dict]:
    conn = psycopg2.connect(dbname='aio', user='postgres',
                            password='docker', host='pg-docker')
    cursor = conn.cursor()
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def fetch(table: str, columns: List[str], conditions: dict) -> List[Dict]:
    conn = psycopg2.connect(dbname='aio', user='postgres',
                            password='docker', host='pg-docker')
    cursor = conn.cursor()
    statements = []
    for statement in conditions.keys():
        statements.append(f"{statement} = '{conditions[statement]}'")
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} "
                   f"FROM {table} "
                   f"WHERE " + " and ".join(statements))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, conditions: dict) -> None:
    conn = psycopg2.connect(dbname='aio', user='postgres',
                            password='docker', host='pg-docker')
    cursor = conn.cursor()
    statements = []
    for statement in conditions.keys():
        statements.append(f"{statement} = {conditions[statement]}")
    cursor.execute(f"delete from {table} where " + " and ".join(statements))
    conn.commit()


def update(table: str, column_values: dict, conditions: Dict):
    conn = psycopg2.connect(dbname='aio', user='postgres',
                            password='docker', host='pg-docker')
    cursor = conn.cursor()
    setter = []
    for item in column_values.keys():
        setter.append(f"{item} = '{column_values[item]}'")
    statements = []
    for statement in conditions.keys():
        statements.append(f"{statement} = '{conditions[statement]}'")
    cursor.execute(f"UPDATE {table} "
                   f"SET {', '.join(setter)} "
                   f"WHERE {' and '.join(statements)}")
    conn.commit()


def get_cursor():
    conn = psycopg2.connect(dbname='aio', user='postgres',
                            password='docker', host='pg-docker')
    cursor = conn.cursor()
    return cursor


def _init_db():
    """Инициализирует БД"""
    print("Бд не найдена. Создаем новую!")
    with open("db_create.sql", "r") as f:
        sql = f.read()
    conn = psycopg2.connect(dbname='aio', user='postgres',
                            password='docker', host='pg-docker')
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    conn = psycopg2.connect(dbname='midis_schedule_db', user='postgres',
                            password='SECRET', host='localhost')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='Users'")
    table_exists = cursor.fetchall()
    if table_exists:
        print("Бд найдена!")
        return
    _init_db()