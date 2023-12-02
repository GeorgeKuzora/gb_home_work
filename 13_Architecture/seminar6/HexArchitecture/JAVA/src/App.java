import Adapters.ConsolePrinter;
import Adapters.MovieReviewsRepo;
import Adapters.UserCommand;
import Application.MovieUser;
import Domain.MovieSearchRequest;
import Ports.iFetchMovieReviews;
import Ports.iPrintMovieReviews;
import Ports.iUserInput;

public class App {
    public static void main(String[] args) throws Exception {

        iFetchMovieReviews fetchMovieReviews = new MovieReviewsRepo();
        iPrintMovieReviews printMovieReviews = new ConsolePrinter();

        iUserInput userCommand = new UserCommand(fetchMovieReviews, printMovieReviews);

        MovieUser movieUser = new MovieUser(userCommand);

        MovieSearchRequest starWarsRequest = new MovieSearchRequest("StarWars");
        MovieSearchRequest starTreckRequest = new MovieSearchRequest("StarTreck");

        System.out.println("Displaying reviews for movie " + starWarsRequest.getMovieName());
        movieUser.processInput(starWarsRequest);

        System.out.println("Displaying reviews for movie " + starTreckRequest.getMovieName());
        movieUser.processInput(starTreckRequest);
       // System.out.println("Hello, World!");
    }
}
