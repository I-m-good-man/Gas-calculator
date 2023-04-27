import os
import re


def generate_all_ui2py(path: str):
    files = os.listdir(path)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            ui_list.append(it)

    for it in ui_list:
        file_path = os.path.join(path, it)
        filename = file_path.split(os.sep)[-1]
        file_name_without_extension = filename[:-3] if filename[-3:] == '.ui' else filename
        cmd = f'pyuic6 {file_path} > {path}{os.sep}{file_name_without_extension}.py'
        os.popen(cmd)


if __name__ == '__main__':
    generate_all_ui2py(os.path.dirname((os.path.abspath(__file__))))
