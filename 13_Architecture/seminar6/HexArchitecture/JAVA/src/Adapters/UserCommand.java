package Adapters;

import Application.MovieApp;
import Domain.Model;
import Domain.MovieSearchRequest;
import Ports.iFetchMovieReviews;
import Ports.iPrintMovieReviews;
import Ports.iUserInput;

public class UserCommand implements iUserInput {
    private Model model;

    public UserCommand(iFetchMovieReviews fetchMovieReviews, iPrintMovieReviews printMovieReviews) {
        MovieApp movieApp = new MovieApp(fetchMovieReviews, printMovieReviews);
        this.model = new Model(movieApp);
    }

    public void handleUserInput(Object userCommand) {
        model.Run((MovieSearchRequest)userCommand);
    }
}
