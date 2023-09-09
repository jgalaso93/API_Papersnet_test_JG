from fastapi import FastAPI
from utils.Locator import Locator
from utils.TowerManager import TowerManager

app = FastAPI()


@app.get("/JG-papernest-test")
def get_towers_coverage(address=None):
    """
    Main function for the API. Gets the call from the URL and process
    the data from it

    Parameters:
    -----------
    Address: (str)
        An actual address that can be located

    Return:
    -------
    In the case of an error: (str) error description
    In any other case: (dict) Operators and their coverage
    """
    try:
        location = Locator(address)
    except AttributeError as error:
        return error.args[0]

    try:
        tower_mgr = TowerManager(location)
    except AttributeError as error:
        return error.args[0]

    tower_mgr.location_coverage()

    return tower_mgr.towers_coverage