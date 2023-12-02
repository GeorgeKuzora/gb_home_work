package Adapters;

import java.util.List;

import Domain.MovieReview;
import Ports.iPrintMovieReviews;

public class ConsolePrinter implements iPrintMovieReviews {
    @Override
    public void writeMovieReviews(List<MovieReview> movieReviewList) {
        movieReviewList.forEach(movieReview -> {
            System.out.println(movieReview.toString());
        });
    }
}
