from domain import movie_search_request
from ports import i_user_input

class MovieUser:
    def __init__(self, userInputDriverPort: i_user_input.iUserInput):
        self.userInputDriverPort = userInputDriverPort

    def processInput(self, movieSearchRequest: movie_search_request.MovieSearchRequest):
        self.userInputDriverPort.handleUserInput(movieSearchRequest)