import uuid
from shutil import rmtree

import os
from fs import clear_folder, copy_files_to, \
    fs, is_in_preset_dirs,\
    absjoin
from os.path import join


def add(target):
    '''
    preset folders cannot be added.
    :param target:
    :return:
    '''
    if is_in_preset_dirs(target):
        return

    copy_files_to(target, fs().stage_folder)


def rm(target):
    if is_in_preset_dirs(target):
        return

    rmtree(absjoin(fs().stage_folder, target))
    rmtree(absjoin(fs().current_dir, target))


def reset():
    clear_folder(fs().stage_folder)


def commit(msg):
    global head

    new_uuid = str(uuid.uuid1())

    if head is None:
        old_uuid = new_uuid
    else:
        old_uuid = head.id_pointer

    assert isinstance(old_uuid, str)
    head = vcs.insert( id_pointer=new_uuid,
                       next_pointer=new_uuid,
                       prev_pointer=old_uuid,
                       msg=msg)

    vcs.update(id_pointer=old_uuid,
               next_pointer=new_uuid)

    new_commit_folder = join(fs().commit_folder, str(new_uuid))

    if not os.path.lexists(new_commit_folder):
        os.mkdir(new_commit_folder)
    else:
        clear_folder(new_commit_folder)

    copy_files_to(fs().stage_folder, new_commit_folder)
    clear_folder(fs().stage_folder)
    clear_folder(fs().head_folder)
    copy_files_to(new_commit_folder, fs().head_folder)


