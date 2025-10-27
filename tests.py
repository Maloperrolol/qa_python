from main import BooksCollector

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
        assert long_name not in collector.get_book_genre()
    #Проверить что книге можно задать жанр
    #Проверить что некорректный жанр не задается
    #Проверить что возвращаем книги с конкретным жанром
    #Проверить что можно вернуть книги подходящие детям
    #
    #Проверить что книга добавляется в избранное
    #Проверить что книгу нельзя добавить в избраанное дважды
    #проверить что книгу можно удалить из избранного
    #