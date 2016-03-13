def check_table_exists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
    SELECT COUNT(*)
    FROM sqlite_master
    WHERE name = '{0}' and type='table';
    """.format(tablename.replace('\'', '\'\'')))

    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

