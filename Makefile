help:
	@echo make env
	@echo make install
	@echo make run
	@echo make run_sicp


env:
	pipenv shell

install:
	pipenv install

run_sicp:
	python3 sicp_ex_1.6.py

run:
	python main.py
