## API Tesintg URL
https://swapi.dev/api/films

## Framework
- Python
- Pytest
- Allure report

## Goal
Please design an automation script to check:
1. How many different species appears in film-6 (Revenge of the Sith) ?
2. Please list all the film names and sort the name by episode_id.
3. Please find out all vehicles which max_atmosphering_speed is over 1000.

## Code structure
- api_objects : all the api objects
- reports : stored data for Allure report
- test_api : all the test and main 
- utils : all the utils , only api_base.py so far
- venv : setup virtual environmrnt folder here if you want to use
- exec_test.bat : batch file to run pytest and allure report. (optional)
- pytest.ini : settings for pytest
- README.md : self of this file 
- requirements.txt : all the installed components 
