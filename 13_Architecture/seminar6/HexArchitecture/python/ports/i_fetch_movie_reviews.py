from abc import ABC, abstractmethod

class iFetchMovieReviews(ABC):
    @abstractmethod
    def fetchMovieReviews(self, movieSearchRequest):
      pass