def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    
    inner_function()
    return

# inner_function() - Выдает ошибку: NameError: name 'inner_function' is not defined. Did you mean: 'test_function'? (Вне облисти видимости)
test_function()
