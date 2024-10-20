# Common modules

The intent of this repository is to expose a common functionality used by 
multiple projects.

Adding new functionality **must** be done only with test which verify its 
correctness.

Import modules from this repo into others projects should be done by this 
way:
```
1. Define common-modules/setup.py
2. pip install -e /path/to/common-module
3. Import packages from the common-module (e.g. from common_module.storage.pydantic_models import Inventory2024DTO)
```

Be careful name of packages shared across projects -- it should me unique across a whole project. This way it is proposed under src directory defined a package name which will maintained unique across a whole project and the rest packages will be stored under it, e.g. <module-name>/src/<unique-package-name>

The issue is the compiler search for an import path from paths defines in sys.path. The first which matches will be used, the equivalent paths would be left and never reached, so uniqueness of paths should be carefully maintained by a developer. 

# Others options

```
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../common_modules')))

# Now you can import your common modules
from module1 import common_function1
from module2 import common_function2

common_function1()
common_function2()
```

Export ```PYTHONPATH``` globally is not recommended. 
```
export PYTHONPATH="/path/to/your_project/common_modules:$PYTHONPATH"
```

In future consider migration into the wheel packaged installed over pip
```
from setuptools import setup, find_packages

setup(
    name='common_modules',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # List any dependencies here
)

pip install .
``` 