import sys
import os

# print("[start] start script")

# # Dynamically add the path to the common module
# current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of main.py
# project_root = os.path.dirname(os.path.dirname(current_dir))  # Goes to /project-root
# common_module_path = os.path.join(project_root, 'common-module', 'src')  # Path to common-module/src

# # Insert the common-module/src into sys.path
# sys.path.insert(0, common_module_path)
import common_module
# from config import Consts




# for i in range(0,10):
    # print(f"{Consts.TAG} : {i}")

print("[end] end script")