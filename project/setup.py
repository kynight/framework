#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from framework.utils.config import LOG_PATH, REPORT_PATH

init_message = """\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

ROOT = r"{root}"
DATA_DIR = r"{data_path}"
"""

case_message = """\
[{project}]
path = {case_path}
"""

def addProject(name):
    project = os.path.split(os.path.abspath(__file__))[0]
    root = os.path.join(project, name)
    if not os.path.exists(root):
        os.makedirs(root)

    # 一些直接的数据直接在用例中写就行了，数据库中的数据则配置一个验证数据库，后续新增该功能
    # data_path = os.path.join(root, "data")
    # if not os.path.exists(data_path):
    #     os.makedirs(data_path)

    page_dir = os.path.join(root, "page")
    if not os.path.exists(page_dir):
        os.makedirs(page_dir)

    page_init_py = os.path.join(page_dir, "__init__.py")
    if not os.path.exists(page_init_py):
        with open(page_init_py, "w") as f:
            pass

    testcase_dir = os.path.join(root, "testcase")
    if not os.path.exists(testcase_dir):
        os.makedirs(testcase_dir)

    testcase_init_py = os.path.join(testcase_dir, "__init__.py")
    if not os.path.exists(testcase_init_py):
        with open(testcase_init_py, "w") as f:
            pass

    root_init_py = os.path.join(root, "__init__.py")
    if not os.path.exists(root_init_py):
        with open(root_init_py, "w") as f:
            pass

    # 所有用例直接记录在一个文件中，便于用例管理（准备平台化时再用）
    # case_ini = os.path.join(project, "case.ini")
    # with open(case_ini, "a+") as fp:
    #     fp.write(case_message.format(project=name,
    #                                  case_path=testcase_path))

if __name__ == "__main__":
    addProject("Test")
