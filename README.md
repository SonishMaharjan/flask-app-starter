Create virtual env
python3.10 -m venv venv

Run virtual env
source venv/bin/activate

// Add dev and app dependencies in requirement.in and requirement-dev.in

pip install pip-tools


pip-compile requirements/requirements.in
pip-compile requirements/requirements-dev.in

