import os
from os.path import join, abspath
from filecmp import cmp
from shutil import copytree, rmtree, make_archive, move
from filecmp import cmp
import sqlite3, json
import uuid

preset_dirs = set()

current_dir = abspath("./transaction_test")

preference_folder = join(current_dir, '.preference')
preset_dirs.add(preference_folder)

if os.path.lexists(preference_folder):
    preference_file_path = join(preference_folder, 'preference.json')
    preset_dirs.add(preference_file_path)

    if not os.path.lexists(preference_file_path):
        with open(preference_file_path, 'a') as f:
            f.write('{}')

    with open(preference_file_path, 'r') as f:
        preference = json.loads(f.read())

else:
    os.mkdir(preference_folder)
    preference = {}

stage_folder = join(current_dir, ".stage")
preset_dirs.add(stage_folder)
if not os.path.lexists(stage_folder):
    os.mkdir(stage_folder)

commit_folder = join(current_dir, ".commit")
preset_dirs.add(commit_folder)
if not os.path.lexists(commit_folder):
    os.mkdir(commit_folder)

head_folder = join(current_dir, ".head")
preset_dirs.add(head_folder)
if not os.path.lexists(head_folder):
    os.mkdir(head_folder)


def clear_folder(folder):
    """
    Remove all files in folder
    :param folder:
    """
    dir = join(current_dir, folder)
    l = os.listdir(dir)

    for e in l:
        filename = join(dir, e)
        rmtree(filename)


def copy_files_to(src_folder, dst_folder):
    """
    Copy files in src_folder directory to dst_folder
    :param src_folder:
    :param dst_folder:
    """
    l = os.listdir(src_folder)
    l = list(map(join, [src_folder] * len(l), l))

    map(copytree, l, list(map(join, [dst_folder] * len(l), l)))


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


class VCS:
    def __init__(self):
        self.commits = {}

        vcs_db_path = join(preference_folder, 'vcs.db')
        if not os.path.lexists(vcs_db_path):
            open(vcs_db_path, 'a').close()

        self.conn = sqlite3.connect(vcs_db_path)

        if not check_table_exists(dbcon=self.conn, tablename="COMMITS"):
            self.conn.execute('''
            CREATE TABLE COMMITS
            (ID_POINTER CHAR(36) PRIMARY KEY NOT NULL,
            NEXT_POINTER CHAR(36) NOT NULL,
            PREV_POINTER CHAR(36) NOT NULL,
            MSG TEXT NOT NULL);
            ''')

    def __del__(self):
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
        INSERT INTO COMMITS (ID_POINTER,NEXT_POINTER,PREV_POINTER)
        VALUES ("{0}", "{1}", "{2}", "{3}");
        '''.format(id_pointer, next_pointer, prev_pointer, msg))

        self.conn.commit()

        self.commits[id_pointer] = Commit(id_pointer=id_pointer,
                                          next_pointer=next_pointer,
                                          prev_pointer=prev_pointer, msg=msg)

    def remove(self, id_pointer):
        self.conn.execute('''
        DELETE FROM COMMITS WHERE ID_POINTER="{0}";
        '''.format(id_pointer))

        self.conn.commit()

    def update(self, id_pointer, next_pointer):
        self.conn.execute('''
        UPDATE COMMITS SET NEXT_POINTER={0} WHERE ID="{1}";
        '''.format(next_pointer, id_pointer))

        self.conn.commit()

        assert isinstance(next_pointer, str)
        self.commits[id_pointer].next_pointer = next_pointer


vcs = VCS()
head = None


def get_modified_files(origin, target) -> list:
    assert isinstance(origin, str)
    assert isinstance(target, str)

    ispath1dir = os.path.isdir(origin)
    ispath2dir = os.path.isdir(target)

    if ispath1dir and ispath2dir:
        ret = []

        origin_files = set(os.listdir(origin))
        target_files = set(os.listdir(target))

        common = origin_files.intersection(target_files)

        for e in common:
            origin_path = join(origin, e)
            target_path = join(target, e)

            output = get_modified_files(origin_path, target_path)

            if output is not None:
                ret += output

        files_target_only = list(target_files.difference(common))

        files_target_only = list(map(join, [target]*len(files_target_only), files_target_only))

        ret += files_target_only

        return ret

    elif (not ispath1dir) and (not ispath2dir):
        if not cmp(origin, target, False):
            return [target]
    else:
        return []


def get_new_files(origin, target) -> list:
    assert isinstance(origin, str)
    assert isinstance(target, str)

    ispath1dir = os.path.isdir(origin)
    ispath2dir = os.path.isdir(target)

    if ispath1dir and ispath2dir:
        ret = []

        origin_files = set(os.listdir(origin))
        target_files = set(os.listdir(target))

        common = origin_files.intersection(target_files)

        for e in common:
            origin_path = join(origin, e)
            target_path = join(target, e)

            output = get_modified_files(origin_path, target_path)

            if output is not None:
                ret += output

        files_target_only = list(target_files.difference(common))

        files_target_only = list(map(join, [target]*len(files_target_only), files_target_only))

        ret += files_target_only

        return ret
    else:
        return []


def get_new_files_from_head():
    return get_new_files(head, )


def add(target):
    '''
    preset folders cannot be added.
    :param target:
    :return:
    '''
    if target in preset_dirs:
        return

    copy_files_to(target, stage_folder)


def rm(target):
    if target in preset_dirs:
        return

    rmtree(join(stage_folder, target))
    rmtree(join(current_dir, target))


def reset():
    clear_folder(stage_folder)


def commit(msg):
    new_uuid = str(uuid.uuid1())

    if head is None:
        old_uuid = new_uuid
    else:
        old_uuid = head.id_pointer

    assert isinstance(old_uuid, str)
    vcs.insert(id_pointer=new_uuid,
               next_pointer=new_uuid,
               prev_pointer=old_uuid,
               msg=msg)

    vcs.update(id_pointer=old_uuid,
               next_pointer=new_uuid)

    new_commit_folder = join(commit_folder, str(new_uuid))

    if not os.path.lexists(new_commit_folder):
        os.mkdir(new_commit_folder)
    else:
        clear_folder(new_commit_folder)

    copy_files_to(stage_folder, new_commit_folder)
    clear_folder(stage_folder)
    clear_folder(head_folder)
    copy_files_to(new_commit_folder, head_folder)

