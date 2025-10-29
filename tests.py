import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #Проверить что ннельзя добавить книгу если название длиннее 40 символов
    def test_add_new_book_name_too_long_not_added(self):
        collector = BooksCollector()
        long_name = 'A' * 45
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()
    #Проверить что книге можно задать жанр
    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'
    #Проверка  что метод возвращает словарь с книгами
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        books_genre = collector.get_books_genre()

        assert books_genre['Гарри Поттер'] == 'Фантастика'
    #Проверить что возвращается книга определенного жанра
    def test_get_books_with_specific_genre_returrns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Гарри Поттер']
    #Проверить что можно вернуть книги подходящие детям
    def test_get_books_for_children_returns_only_child_friendly_books(self):
       collector = BooksCollector() 
       collector.add_new_book('Алиса в стране чудес')
       collector.add_new_book('Сияние')
       collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
       collector.set_book_genre('Сияние', 'Ужасы')
       result = collector.get_books_for_children()
       assert result == ['Алиса в стране чудес']
    #Проверить что книга добавляется в избранное
    def test_add_books_in_favorites_adds_book(self):
        collector = BooksCollector() 
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']
    #Проверить что книгу нельзя добавить в избраанное дважды
    def test_add_book_in_favorites_does_not_diplicate(self):
        collector = BooksCollector() 
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books().count('Гарри Поттер') == 1
    #проверить что книгу можно удалить из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector() 
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()
    #Тест для проверки установки жанров разным книгам
    
    @pytest.mark.parametrize(
            "book_name, genre",
        [
            ('Гарри Поттер','Фантастика'),
            ('Шерлок Холмс', 'Детективы'),
            ('Сияние', 'Ужасы'),
            ('Алиса в стране чудес', 'Мультфильмы'),
        ]
    )
    def test_set_book_genre_with_parametrize(self, book_name, genre):
        collector = BooksCollector() 
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre