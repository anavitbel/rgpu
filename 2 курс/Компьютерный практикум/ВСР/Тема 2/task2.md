### Тема 2. Разработка серверной компоненты приложения удалённого доступа к базам данных и экспериментальная проверка корректности её работы

Серверная компонента приложения может представлять собой реализацию REST API для выполнения операций CRUD в базе данных MongoDB.

Приложение реализовано с использованием Express, bodyParser, Mongoose.

Реализованы следующие операции:

`GET /products` - получение списка продуктов

`POST /products/new` - добавление нового продукта

`POST /products/update/:id` - обновление информации о продукте по ID

`POST /products/delete/:id` - удаление информации о продукте по ID

При отправке запросов для добавления и обновления продукта информация о нём передаётся в теле POST-запроса.

Сервер возвращает ответ - статус выполнения операции в формате JSON.

#### Проверка работы

Добавление данных:

```
curl -X 'POST' -d 'name=NewProduct' https://UnwieldyDoubleSets.anavitbel.repl.co/products/new
```

Ответ сервера при добавлении данных:

```json
{
	"status": "success"
}
```

Получение данных:

```
curl https://unwieldydoublesets.anavitbel.repl.co/products
```

Ответ сервера:

```json
[
  {
    "amount": {
      "number": 32,
      "unit": "kg"
    },
    "_id": "60e4268f46a5bd73485414f0",
    "name": "Apples",
    "type": "Fruits"
  },
  {
    "amount": {
      "number": 16.25,
      "unit": "kg"
    },
    "_id": "60e42ad546a5bd73485414f1",
    "name": "Bananas",
    "type": "Fruits"
  },
  {
    "amount": {
      "number": 24.5,
      "unit": "kg"
    },
    "_id": "60e42b1046a5bd73485414f2",
    "name": "Strawberries",
    "type": "Berries"
  }
]
```

