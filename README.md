Create virtual env
python3.10 -m venv venv

Run virtual env
source venv/bin/activate

// Add dev and app dependencies in requirement.in and requirement-dev.in

pip install pip-tools

// Generate requirement.txt
pip-compile requirements/requirements.in
pip-compile requirements/requirements-dev.in


//install dependencies.
pip install -r requirements/requirements.txt
pip install -r requirements/requirements-dev.txt


