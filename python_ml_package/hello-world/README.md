# Example package

```
Hello-world/
└── hello_world/
    ├── __init__.py
    └── main.py
```

# create virtual envs

conda create  -n "name" python=3.10
pip install setuptools twine
```

## commands


```bash
## creating the build file
#installable package
#Everytime run this command once you made changes in packages
python setup.py sdist

# this will create dist file: hello_world_shubham-0.0.1.tar.gz

# now install this gz as env
pip install dist/hello_world_shubham-0.0.1.tar.gz

# pyhton now import library 
import hello_world
from hello_world import addnums
addnums(4,4) # 8
```

``` updated folder structure
.
├── Hello-world
├── dist/hello_world_shubham-0.0.1.tar.gz (generated file)
├── setup.py
└── requirement.txt/
    └── hello_world/
        ├── __init__.py
        └── main.py
```

# to upload the file (tar.gz) on python packagingindex we'll  use twin library
```bash
# https://test.pypi.org/
# username: shubhamchau77
twine upload --repository-url https://test.pypi.org/legacy/dist/hello_world_shubham-0.0.1.tar.gz

# 88 crete API token and paste on terminal
# https://test.pypi.org/project/hello-world-shubham/0.0.1/

#upladed package on pypi
pip install -i https://test.pypi.org/simple/ hello-world-shubham==0.0.1
```

