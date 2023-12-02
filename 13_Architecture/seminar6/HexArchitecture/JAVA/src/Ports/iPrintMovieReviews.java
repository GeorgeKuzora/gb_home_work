package Ports;

import java.util.List;

import Domain.MovieReview;

public interface iPrintMovieReviews {
    public void writeMovieReviews(List<MovieReview> movieReviewList);
}
