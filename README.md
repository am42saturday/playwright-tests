## Тестовый проект с использованием Playwright

### Тестовый сценарий

1. Донор переходит на сайт
2. Кликает на кнопку “Give now”
3. Выбирает “Monthly” пожертвование
4. Вводит сумму 100 USD
5. Нажимает “Donate monthly”
6. Убирает чек-бокс покрытия комиссии “Cover transaction costs”
7. Выбирает оплату кредитной картой “Credit card”
8. Вводит карточные данные для оплаты
9. Нажимает “Continue”
10. Вводит “First name”
11. Вводит “Last name”
12. Вводит “E-mail”
13. Нажимает “Donate”

```
После этого шага форма оплаты должна вернуть пользователя 
на экран ввода карточных данных и отобразить ошибку
```

В проекте содержится 2 одинаковых теста для параллельного запуска

### Запуск тестов
#### Необходимо установить используемые пакеты:
```pip -r requirements.txt```

#### Выполнить установку браузеров для playwright:
```playwright install```

#### Выполнить установку allure, например для MacOs:
```brew install allure```

#### Запустить тесты (в терминале, находясь в папке проекта):
Для последовательного запуска тестов:

```pytest```

Для параллельного запуска тестов (в 2 потока):

```pytest -n 2```

#### Просмотр allure отчета
```allure generate report``` - если есть необходимость сохранить отчет

```allure serve report```