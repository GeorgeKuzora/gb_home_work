package Application;

import Domain.MovieSearchRequest;
import Ports.iUserInput;

public class MovieUser {
    private iUserInput userInputDriverPort;

    public MovieUser(iUserInput userInputDriverPort) {
        this.userInputDriverPort = userInputDriverPort;
    }

    public void processInput(MovieSearchRequest movieSearchRequest)
    {
        userInputDriverPort.handleUserInput(movieSearchRequest);
    }
}
