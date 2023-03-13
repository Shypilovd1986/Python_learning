# discover -s  tests -p "*_test.py"
# find all test which consist with word_test.py

# in folder tests

# from unittest import TestCase, main
# from main import square
#
# class MathAction(TestCase):
#
#     def test_square_number(self):
#         self.assertEqual(square(3), 9)
#
# if __name__=="__main__":
#     main()

# where our test class must inherit from class TestCase , function main() start tests

# "coverage run -m pytest tests"


# -------------------------             pylint          -----------------
# pylint --generate-rcfile >.pylintrc      for settings pylint

#  coverage run --source=app -m pytest tests/

# ------------------ mysql  ------------------
# connect to database
# mysql -u root -p

# in config.py
# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe06,e\xc0o\xbf\x03\xeftz\x18\xc7\x03\x94\x82\xa4\x82)9'
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:19865421@localhost\ItemStorage'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# pip install mysql-connector
# pip install mysql-connector-python
# pip install mysql-connector-python-rf
# pip install pymysql
#  pip install cryptography       using in hashing password

# -------------  setuptools.py  ------------------
# """describing metadata and for installing requirements """
# from setuptools import setup, find_packages
#
# with open("README.md", "r", encoding="UTF-8") as readme_file:
#     long_description = readme_file.read()
#
# setup(
#     name="ItemStorage",
#     version="2.0.1",
#     description="ItemStorage python app",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     author="Dmitriy Shypilov",
#     author_email="shypilovd@gmail.com",
#     license="MIT",
#     packages=find_packages(),
#     include_package_data=True,
#     url="https://github.com/Shypilovd1986/items_storage",
#     install_requires=[
#         'astroid==2.15.0',
#         'attrs==22.2.0',
#         'certifi==2022.12.7',
#         'cffi==1.15.1',
#         'charset-normalizer==3.1.0',
#         'click==8.1.3',
#         'coverage==6.5.0',
#         'coveralls==3.3.1',
#         'cryptography==39.0.2',
#         'dill==0.3.6',
#         'docopt==0.6.2',
#         'exceptiongroup==1.1.0',
#         'Flask==2.2.3',
#         'Flask-SQLAlchemy==3.0.3',
#         'greenlet==2.0.2',
#         'idna==3.4',
#         'importlib-metadata==6.0.0',
#         'iniconfig==2.0.0',
#         'isort==5.12.0',
#         'itsdangerous==2.1.2',
#         'Jinja2==3.1.2',
#         'lazy-object-proxy==1.9.0',
#         'MarkupSafe==2.1.2',
#         'mccabe==0.7.0',
#         'mysql-connector==2.2.9',
#         'mysql-connector-python==8.0.32',
#         'packaging==23.0',
#         'platformdirs==3.1.1',
#         'pluggy==1.0.0',
#         'protobuf==3.20.3',
#         'pycparser==2.21',
#         'pylint==2.17.0',
#         'PyMySQL==1.0.2',
#         'pytest==7.2.2',
#         'requests==2.28.2',
#         'SQLAlchemy==2.0.5.post1',
#         'tomli==2.0.1',
#         'tomlkit==0.11.6',
#         'typing_extensions==4.5.0',
#         'urllib3==1.26.15',
#         'Werkzeug==2.2.3',
#         'wrapt==1.15.0',
#         'zipp==3.15.0'
#     ],
#     classifiers=[
#         "Development Status :: 4 - Beta",
#         "Intended Audience :: Developers",
#         "License :: MIT License",
#         "Operating System :: OS Independent",
#         "Programing language :: Python :: 3.9.6"
#     ],
#     entry_points={
#         'console_scripts': [
#             'item-storage=app.main:run_app_item_storage'
#         ],
#
#     }
# )

# python setup.py sdist    for creating distribution package
