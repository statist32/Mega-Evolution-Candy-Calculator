import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sys
from datetime import datetime


def change_url_language_to_english(url):
    questionmark_index = url.index("?")
    english_url = f"{url[:questionmark_index]}?hl=en"
    return english_url


def get_html(url):
    response = requests.get(url)
    if response.ok:
        return response.text


def get_wild_encounters_container(soup):
    wild_encounters_container = soup.find(
        string=["Wild encounters", "Wild Encounters", "wild encounters"]
    ).parent.parent.parent
    return wild_encounters_container


def find_all_wild_encounters(
    container,
    pokemon_grid_class="PokemonImageGridBlock__grid__pokemon",
    pokemon_name_class="PokemonImageGridBlock__grid__pokemon__caption",
):
    wild_encounters = []
    wild_encounters_html = container.findAll(class_=pokemon_grid_class)
    for wild_encounter in wild_encounters_html:
        pokemon = {}
        pokemon["name"] = (
            wild_encounter.find(class_=pokemon_name_class)
            .text.replace("^", "")
            .replace("*", "")
        )
        pokemon["imgUrl"] = wild_encounter.find("img")["src"]
        wild_encounters.append(pokemon)
    return wild_encounters


def get_pokemon_types(pokemon_name):
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().split(' ')[0]}/"
    response = requests.get(URL)
    if not response.ok:
        print(f"No types found for {pokemon_name}!\n")
        types = ["TODO", "TODO"]
    else:
        types = [type["type"]["name"].capitalize() for type in response.json()["types"]]
    return types


def combine_website_and_api_data(wild_encounters):
    pokemon_list = list()
    for wild_encounter in wild_encounters:
        pokemon = dict(wild_encounter)
        pokemon["types"] = get_pokemon_types(pokemon["name"])
        pokemon_list.append(pokemon)
    return pokemon_list


def get_colors(soup):
    background_style_container, tile_style_container = [
        container_block["style"]
        for container_block in soup.findAll(class_="ContainerBlock")
        if container_block.has_attr("style") and container_block["style"]
    ][:2]

    background_style = [
        style.strip().replace("--", "").split(":")
        for style in background_style_container.split(";")
    ]

    background_color = [
        value.strip() for prop, value in background_style if prop == "background"
    ][0]
    background_text_color = [
        value.strip() for prop, value in background_style if prop == "textColor"
    ][0]
    tile_style = [
        style.strip().replace("--", "").split(":")
        for style in tile_style_container.split(";")
    ]
    tile_background_color = [
        value.strip() for prop, value in tile_style if prop == "background"
    ][0]
    tile_text_color = [
        value.strip() for prop, value in tile_style if prop == "textColor"
    ][0]

    return {
        "backgroundColor": background_color,
        "textColor": background_text_color,
        "tileBackgroundColor": tile_background_color,
        "tileTextColor": tile_text_color,
    }


def find_event_name(soup):
    return soup.find_all(class_="ContainerBlock__headline")[0].text.strip()


def find_event_dates(soup):
    start_date_str, end_date_str = (
        soup.select_one(".ContainerBlock__body > p").text.strip().replace(".","").replace(" local time", "").split(" to ")
    )

    start_date = str(datetime.strptime(start_date_str, "%A, %B %d, %Y, at %I:%M %p")).replace(" ", "T")
    end_date = str(datetime.strptime(end_date_str, "%A, %B %d, %Y, at %I:%M %p")).replace(" ", "T")

    return start_date, end_date


def get_event(soup):
    container = get_wild_encounters_container(soup)
    wild_encounters = find_all_wild_encounters(container)
    combined_wild_encounters = combine_website_and_api_data(wild_encounters)
    colors = get_colors(soup)
    event = dict(wildEncounters=combined_wild_encounters, **colors)
    event["name"] = find_event_name(soup)
    event["startDate"],  event["endDate"] = find_event_dates(soup)
    pprint(event)


def get_go_fest(soup):
    names = [
        "Quartz Terrarium",
        "Pyrite Sands",
        "Malachite Wilderness",
        "Aquamarine Shores",
    ]
    events = []
    for name in names:
        id = name.replace(" ", "-").lower()
        print(id)
        container = soup.find(id=id)
        wild_encounters = find_all_wild_encounters(
            container,
            pokemon_grid_class="alola__pokemonGrid__pokemon",
            pokemon_name_class="alola__pokemonGrid__pokemon__label",
        )
        combined_wild_encounters = combine_website_and_api_data(wild_encounters)
        colors = {
            "backgroundColor": "rgb(169, 121, 172)",
            "textColor": "black",
            "tileBackgroundColor": "rgb(41, 104, 206)",
            "tileTextColor": "white",
        }
        event = dict(wildEncounters=combined_wild_encounters, **colors)
        event["name"] = f"Go Fest - {name}"
        event["startDate"] = "26.08.2023"
        event["endDate"] = "26.08.2023"
        events.append(event)
    pprint(events)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too few arguments. python3 downloader.py 'URL'")
        sys.exit()
    url = sys.argv[1]
    if not url.startswith("https://pokemongolive.com/post/"):
        print("URL needs to start with https://pokemongolive.com/post/")
        sys.exit()
    english_url = change_url_language_to_english(url)
    soup = BeautifulSoup(get_html(english_url), "html.parser")
    get_event(soup)
    # get_go_fest(soup)
