import json
from filecmp import cmp
from shutil import copy2, copytree, rmtree

import os
from os.path import join, abspath


def absjoin(path1, path2):
    return abspath(join(path1, path2)) if not os.path.isabs(path2) else path2

class vcsfilesystem:
    def __init__(self, current_dir):
        self.preset_dirs = set()

        self.current_dir = abspath(current_dir)

        self.preference_folder = abspath(join(current_dir, '.preference'))
        self.preset_dirs.add(self.preference_folder)

        if os.path.lexists(self.preference_folder):
            self.preference_file_path = abspath(join(self.preference_folder, 'preference.json'))
            self.preset_dirs.add(self.preference_file_path)

            if not os.path.lexists(self.preference_file_path):
                with open(self.preference_file_path, 'a') as f:
                    f.write('{}')

            with open(self.preference_file_path, 'r') as f:
                self.preference = json.loads(f.read())

        else:
            os.mkdir(self.preference_folder)
            self.preference = {}

        self.stage_folder = abspath(join(self.current_dir, ".stage"))
        self.preset_dirs.add(self.stage_folder)
        if not os.path.lexists(self.stage_folder):
            os.mkdir(self.stage_folder)

        self.commit_folder = abspath(join(self.current_dir, ".commit"))
        self.preset_dirs.add(self.commit_folder)
        if not os.path.lexists(self.commit_folder):
            os.mkdir(self.commit_folder)

        self.head_folder = abspath(join(self.current_dir, ".head"))
        self.preset_dirs.add(self.head_folder)
        if not os.path.lexists(self.head_folder):
            os.mkdir(self.head_folder)

        self.vcs_db_path = abspath(join(self.preference_folder, 'vcs.db'))
        if not os.path.lexists(self.vcs_db_path):
            open(self.vcs_db_path, 'a').close()

    def __del__(self):
        pass



def fs():
    global fs_instance
    assert isinstance(fs_instance, vcsfilesystem)
    return fs_instance


def initfs(current_dir):
    global fs_instance
    fs_instance = vcsfilesystem(current_dir=current_dir)


def is_in_preset_dirs(path):
    p = absjoin(fs().current_dir, path)
    return p in fs().preset_dirs


def clear_folder(folder):
    """
    Remove all files in folder
    :param folder: MUST put the relative folder
    """
    dir = abspath(join(fs().current_dir, folder))
    l = os.listdir(dir)

    for e in l:
        if absjoin(fs().current_dir, e) in fs().preset_dirs:
            continue

        filename = absjoin(dir, e)

        if os.path.isdir(filename):
            rmtree(filename)
        else:
            os.remove(filename)


def copy_files_to(src_dir, dst_dir):
    """
    Copy files in src_folder directory to dst_folder
    :param src_folder:
    :param dst_folder:
    """
    src_dir = absjoin(fs().current_dir, src_dir)
    dst_dir = absjoin(fs().current_dir, dst_dir)

    l = os.listdir(src_dir)
    target = []

    for e in l:
        p = absjoin(src_dir, e)

        if p in fs().preset_dirs:
            continue

        target.append(e)

    src_folder = list(map(absjoin, [src_dir] * len(target), target))
    dst_folder = list(map(absjoin, [dst_dir] * len(target), target))

    for idx in range(len(src_folder)):
        if os.path.isdir(src_folder[idx]):
            copytree(src_folder[idx], dst_folder[idx]);
        else:
            copy2(src_folder[idx], dst_folder[idx])


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
            origin_path = absjoin(origin, e)
            target_path = absjoin(target, e)

            output = get_modified_files(origin_path, target_path)

            if output is not None:
                ret += output

        files_target_only = list(target_files.difference(common))

        files_target_only = list(map(absjoin, [target]*len(files_target_only), files_target_only))

        ret += files_target_only

        return ret

    elif (not ispath1dir) and (not ispath2dir):
        if not cmp(origin, target, False):
            return [target]
    else:
        return []


def get_new_files(cur, path1, path2) -> list:
    ispath1dir = os.path.isdir(path1)
    ispath2dir = os.path.isdir(path2)

    if ispath1dir and ispath2dir:
        ret = []

        origin_files = set(os.listdir(path1))
        target_files = set(os.listdir(path2))

        common = origin_files.intersection(target_files)

        for e in common:
            origin_path = absjoin(path1, e)
            target_path = absjoin(path2, e)

            output = get_new_files(absjoin(cur, e), origin_path, target_path)

            if output is not None:
                ret += output

        files_target_only = list(target_files.difference(common))

        files_target_only = list(map(absjoin, [cur]*len(files_target_only), files_target_only))

        ret += files_target_only

        return ret
    else:
        return []
