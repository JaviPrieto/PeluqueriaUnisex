PY=python

main: app/src/main.py 
	$(PY) app/src/main.py

test: app/tests/test_cita.py
	$(PY) app/tests/test_cita.py

