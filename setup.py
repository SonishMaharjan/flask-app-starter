from setuptools import setup, find_packages

with open("requirements/requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="flask_starter_app",
    version="0.1.0",
    description="My Flask app starter",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.9",
)


    # install_requires=[
    #     "flask==2.3.2",
    #     "flask-jwt-extended==4.5.2",
    #     "flask-migrate==4.0.4",
    #     "flask-smorest==0.42.0",
    #     "flask-sqlalchemy==3.0.5",
    #     "passlib==1.7.4",
    #     "python-dotenv==1.0.0",
    #     "sqlalchemy==2.0.19"
    #     ],