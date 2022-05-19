from dbhelper import DBHelper
import dbstr

if __name__ == "__main__":
    dbHelper = DBHelper()

    query = dbstr.get_create_query(0)
    dbHelper.drop_table("rules")
    dbHelper.execute_sql(query)