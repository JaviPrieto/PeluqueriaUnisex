PY=python

main: src/main.py 
	$(PY) src/main.py

test: tests/test_cita.py
	$(PY) tests/test_cita.py

