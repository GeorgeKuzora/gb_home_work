from abc import ABC, abstractmethod

class iPrintMovieReviews(ABC):
    @abstractmethod
    def writeMovieReviews(self, movieReviewList):
      pass