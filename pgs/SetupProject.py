import time
from pgs import DefaultFiles


def create_file(path, contents=""):
    print("Creating file " + path + " ... ", end='')
    file = open(path, mode='w')
    file.write(contents)
    file.close()
    print("done.")

if __name__ == '__main__':

    setupText = r"""
   _____      _                     _____   _____  _____
  / ____|    | |                   |  __ \ / ____|/ ____|
 | (___   ___| |_ _   _ _ __       | |__) | |  __| (___
  \___ \ / _ \ __| | | | '_ \      |  ___/| | |_ |\___ \
  ____) |  __/ |_| |_| | |_) |     | |    | |__| |____) |
 |_____/ \___|\__|\__,_| .__/      |_|     \_____|_____/
                       | |
                       |_|

This utility will create a PyGameSimplified project.
It may wipe or overwrite existing project files in the directory you run this program in.
Please type the project name to confirm (no spaces or non-alpha characters), or nothing to cancel.
"""

    proj_name = input(setupText)
    if proj_name.strip() == '':
        print("Quitting setup.")
        time.sleep(1)
        quit()
    else:
        print('\n\n' + '-'*20 + " INITIALISING PGS " + '-'*20)
        print("Initialising project...")
        proj_name = ''.join(x for x in proj_name.title() if not x.isspace())
        DefaultFiles.proj_name = proj_name

        create_file("__init__.py")
        create_file("Main.pgs", contents=DefaultFiles.main())
        create_file("Color.py", contents=DefaultFiles.color())
        create_file("Window.py", contents=DefaultFiles.window())
        create_file(proj_name + "Window.pgs", contents=DefaultFiles.project_window())
        create_file(".pgsproject", contents=DefaultFiles.pgsproject())
