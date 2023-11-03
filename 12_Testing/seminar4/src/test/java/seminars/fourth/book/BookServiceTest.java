package seminars.fourth.book;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;

import java.util.ArrayList;

import static org.mockito.Mockito.*;
import static org.assertj.core.api.Assertions.*;

class BookServiceTest {

  @Mock
  InMemoryBookRepository mockBookRepository;
  BookService bookService;
  Book stubBookId1 = new Book("1", "Book1", "Author1");

  @BeforeEach
  public void setUp() {
    mockBookRepository = mock(InMemoryBookRepository.class);
    bookService = new BookService(mockBookRepository);
  }

  @Test
  public void testFindBookById() {
    String bookId = "1";
    when(mockBookRepository.findById("1")).thenReturn(stubBookId1);
    assertThat(bookService.findBookById(bookId)).isEqualTo(stubBookId1);
    verify(mockBookRepository, times(1)).findById(bookId);
  }

  @Test
  public void testFindAllBooks() {
    ArrayList<Book> stubBooks = new ArrayList<Book>();
    stubBooks.add(stubBookId1);
    when(mockBookRepository.findAll()).thenReturn(stubBooks);
    assertThat(bookService.findAllBooks()).isEqualTo(stubBooks);
    verify(mockBookRepository, times(1)).findAll();
  }
}