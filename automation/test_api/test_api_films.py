#Standard library imports.
import logging
import os

#Related third party imports.
import allure
import pytest

#Local application/library specific imports.  
from api_objects.films_api import *
from utils.utils import *
from test_data.test_data_from_file import *

# test 1
@allure.story("films get all success")
def test_films_get_all_success(get_session):
    film_api_obj = Films(get_session)
    film_api_obj.send("GET", None)
    assert film_api_obj.get_status_code() == 200
    logging.info("films reponse is 200 => pass")
    results = film_api_obj.response_json.get('results', [])
    for item in results:
        assert isinstance(item.get("title"), str)
        assert isinstance(item.get("episode_id"), int)
        assert isinstance(item.get("opening_crawl"), str)
        assert isinstance(item.get("director"), str)
        assert isinstance(item.get("producer"), str)
        assert validate_iso8601_date(item.get("release_date")) == True
        assert isinstance(item.get("species"), list)
        assert isinstance(item.get("starships"), list)
        assert isinstance(item.get("vehicles"), list)
        assert isinstance(item.get("characters"), list)
        assert isinstance(item.get("planets"), list)
        assert isinstance(item.get("url"), str)
        assert isinstance(item.get("created"), str)
        assert isinstance(item.get("edited"), str)
    logging.info("/film reponse schema verify => pass")


# test 2
# test 3
@allure.story("films/:id get film success")
# @pytest.mark.parametrize("data_row", get_data("film_data"))
@pytest.mark.parametrize("data_row", get_data())
def test_films_id_get_film_success(get_session, data_row):
    film_id_api_obj = Films(get_session)
    film_id = data_row['id']
    logging.info("Film id = " + film_id)
    film_id_api_obj.send("GET", film_id)
    # verify status code
    assert film_id_api_obj.get_status_code() == 200
    logging.info("/films/id reponse is 200 => pass")

    # verify data
    rsp = film_id_api_obj.response_json
    assert compare_rsp_with_data(rsp["title"], data_row['title'])
    assert compare_rsp_with_data(str(rsp["episode_id"]), data_row['episode_id'])
    opening_crawl_str = data_row['opening_crawl'].replace('\n','\r\n').strip()
    assert compare_rsp_with_data(rsp['opening_crawl'], data_row['opening_crawl'])
    assert compare_rsp_with_data(rsp["director"], data_row['director'])
    assert compare_rsp_with_data(rsp["producer"], data_row['producer'])
    assert compare_rsp_with_data(rsp["release_date"], data_row['release_date'])
    characters_string = ', '.join(rsp["characters"])
    assert compare_rsp_with_data(characters_string, data_row['characters'])
    planet_string = ', '.join(rsp["planets"])
    assert compare_rsp_with_data(planet_string, data_row['planets'])
    starships_string = ', '.join( rsp["starships"])
    assert compare_rsp_with_data(starships_string, data_row['starships'])
    vehicles_string = ', '.join( rsp["vehicles"])
    assert compare_rsp_with_data(vehicles_string ,data_row['vehicles'])
    species_string = ', '.join( rsp["species"])
    assert compare_rsp_with_data(species_string, data_row['species'])
    assert compare_rsp_with_data(rsp["created"], data_row['created'])
    assert compare_rsp_with_data(rsp["edited"], data_row['edited'])
    assert compare_rsp_with_data(rsp["url"], (data_row['url']))
    logging.info("/film/id response verify => pass")

# test 4
# test 5
# test 6
@allure.story("/films/:id send with id out of range")
@pytest.mark.parametrize('film_id', ['-1', '7', 'abc'])
def test_films_id_send_with_id_out_of_rang(get_session, film_id):
    film_id_api_obj = Films(get_session)
    logging.info("Film id = " + film_id)
    film_id_api_obj.send("GET", film_id)
    
    # verify status code
    assert film_id_api_obj.get_status_code() == 404
    logging.info("/films/id reponse is 404 => pass")

    assert film_id_api_obj.response_json["detail"] == 'Not found'
    logging.info("/films/id reponse message is 'Not found' => pass")


# test 8
# test 9
@allure.story("/films/ send_with_wrong_method")
@pytest.mark.parametrize('method', ['POST', 'PUT'])
def test_films_send_with_wrong_method(get_session, method):
    film_id_api_obj = Films(get_session)
    logging.info("API method = " + method)
    film_id_api_obj.send(method, None)
    
    # verify status code
    assert film_id_api_obj.get_status_code() == 405
    logging.info("/films/id reponse is 405 => pass")

    assert film_id_api_obj.response_json["detail"] == f"Method '{method}' not allowed."
    logging.info(f"/films/id reponse message is '{method}' => pass")

# test 9
# test 10
@allure.story("/films/:id send_with_wrong_method")
@pytest.mark.parametrize('method', ['POST', 'PUT'])
def test_films_id_send_with_wrong_method(get_session, method):
    film_id_api_obj = Films(get_session)
    logging.info("API method = " + method)
    film_id_api_obj.send(method, '1')
    
    # verify status code
    assert film_id_api_obj.get_status_code() == 405
    logging.info("/films/id reponse is 405 => pass")

    assert film_id_api_obj.response_json["detail"] == f"Method '{method}' not allowed."
    logging.info(f"/films/id reponse message is '{method}' => pass")