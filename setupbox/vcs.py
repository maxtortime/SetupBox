import sqlite3

from db import check_table_exists
from fs import fs

class Commit:
    """
    Represents a single commit
    """
    def __init__(self, id_pointer, next_pointer, prev_pointer, msg):
        self.id_pointer = id_pointer
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer
        self.msg = msg

    def set(self, next_pointer, prev_pointer, msg):
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer
        self.msg = msg


class VCS:
    def __init__(self):
        self.commits = {}

        self.conn = sqlite3.connect(fs().vcs_db_path)

        if not check_table_exists(dbcon=self.conn, tablename="COMMITS"):
            self.conn.execute('''
            CREATE TABLE COMMITS
            (ID_POINTER CHAR(36) PRIMARY KEY NOT NULL,
            NEXT_POINTER CHAR(36) NOT NULL,
            PREV_POINTER CHAR(36) NOT NULL,
            MSG TEXT NOT NULL);
            ''')

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    def selectAll(self):
        cursor = self.conn.execute('''
        SELECT ID_POINTER, NEXT_POINTER, PREV_POINTER, MSG_POINTER FROM COMMITS;
        ''')

        commits = {}

        for row in cursor:
            commits[row[0]] = Commit(row[0], row[1], row[2], row[3])

        return commits

    def select(self, id_pointer):
        cursor = self.conn.execute('''
        SELECT ID_POINTER, NEXT_POINTER, PREV_POINTER, MSG FROM COMMITS WHERE ID_POINTER='{0}';
        '''.format(id_pointer))

        return cursor.fetchone()

    def insert(self, id_pointer, next_pointer, prev_pointer, msg):
        self.conn.execute('''
        INSERT INTO COMMITS (ID_POINTER,NEXT_POINTER,PREV_POINTER, MSG)
        VALUES ("{0}", "{1}", "{2}", "{3}");
        '''.format(id_pointer, next_pointer, prev_pointer, msg))

        self.conn.commit()

        self.commits[id_pointer] = Commit(id_pointer=id_pointer,
                                          next_pointer=next_pointer,
                                          prev_pointer=prev_pointer, msg=msg)
        return self.commits[id_pointer]

    def remove(self, id_pointer):
        self.conn.execute('''
        DELETE FROM COMMITS WHERE ID_POINTER="{0}";
        '''.format(id_pointer))

        self.conn.commit()

    def update(self, id_pointer, next_pointer):
        self.conn.execute('''
        UPDATE COMMITS SET NEXT_POINTER="{0}" WHERE ID_POINTER="{1}";
        '''.format(next_pointer, id_pointer))

        self.conn.commit()

        assert isinstance(next_pointer, str)
        self.commits[id_pointer].next_pointer = next_pointer

        return self.commits[id_pointer]

