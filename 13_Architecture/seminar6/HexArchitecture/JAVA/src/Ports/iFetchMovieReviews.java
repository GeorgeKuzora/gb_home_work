package Ports;

import java.util.List;

import Domain.MovieReview;
import Domain.MovieSearchRequest;

public interface iFetchMovieReviews {
    public List<MovieReview> fetchMovieReviews(MovieSearchRequest movieSearchRequest);
}
