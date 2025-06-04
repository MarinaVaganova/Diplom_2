class TestCode:
    SUCCESS_CODE = 200
    BAD_REQUEST_CODE = 400
    UNAUTHORIZED_CODE = 401
    FORBIDDEN_CODE = 403
    SERVER_ERROR_CODE = 500

class TestMessage:
    # Создание заказа
    # Запрос без ингредиентов - 400
    MESSAGE_CREATE_ORDER_BAD_REQUEST = "Ingredient ids must be provided"
    # Невалидный хеш ингредиента - 500
    MESSAGE_CREATE_ORDER_INTERNAL_SERVER_ERROR = "Internal Server Error"

    # Восстановление и сброс пароля
    MESSAGE_RESET_EMAIL_SENT = "Reset email sent"
    MESSAGE_PASSWORD_SUCCESSFULLY_RESET = "Password successfully reset"

    # Создание пользователя
    # Пользователь существует - 403
    MESSAGE_REGISTER_USER_ALREADY_EXISTS = "User already exists"
    # Нет одного из полей - 403
    MESSAGE_REGISTER_USER_NO_REQUIRED_FIELDS = "Email, password and name are required fields"

    # Авторизация и регистрация
    # Логин или пароль неверные, или нет одного из полей - 401
    MESSAGE_AUTH_LOGIN_UNAUTHORIZED = "email or password are incorrect"
    # Успешный выход из системы
    MESSAGE_SUCCESSFUL_LOGOUT = "Successful logout"

    # Получение и обновление информации о пользователе
    # Изменение информации без авторизации - 401
    MESSAGE_CHANGE_DATA_UNAUTHORIZED = "You should be authorised"
    # Передача почты, которая уже используется - 403
    MESSAGE_MAIL_REUSE = "User with such email already exists"

    # Получение заказов конкретного пользователя
    # Получение заказов без авторизации - 401
    MESSAGE_ORDER_NUMBERS_UNAUTHORIZED = "You should be authorised"

    # Запрос выполнен успешно - 200
    MESSAGE_SUCCESS = 'success":true'