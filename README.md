 # ILoveDogs
 ### Реализация 
 Проект был написан на Python с использованием фреймфворка Django, HTML, CSS, JavaScript. Для работы со сторонним Dog API была использована библиотека requests.

 ### Инициализация
 Для инициализации вам может потребоваться Poetry так как он нужен что бы подтянуть зависимости. Скачать его можно написав в терминале     
 `pip install poetry`. После того как вы установили Poetry вам нужно будет войти в виртуальную среду в IDE,напишите комманду `poetry shell` в консоли. Последний шаг это запуск приложения, для этого в консоли напишите `python manage.py runserver`. На этом инициализация закончена.

 ### Разработка 
В самом начале я решил познакомиться с  Dog API что бы понять что он делает и как с ним работать. Разобравшись с ним я примерно понял какое приложение от меня требуют. Вторым шагом было примерный макет приложения. Я решил сделать главную страничку на которой будет список всех пород и их изображение. Кликнув на изображение вы перейдете на страницу посвященную только этой породе, где будут все изображения относящиеся к ней. Так же и присутствует функция поиска породы собак.

После того как я определился с макетом я начал делать Backend проекта и связывать его с Dog API. Так как все данные брались из стороннего API у приложения нет своей базы данных. Из за этого процесс получения данных затянулся и пришлось отказаться от идеи выводить список сразу всех пород на начальной странице и я добавил пагинацию. Для этого был добавлен query parameter page который отвечает за контент показываемый на главной странице. Это вызвало риск того что пользователь может сам вписать не правильный параметр. Поэтому при таком случае выводится ответ BadRequest с контентом Page doesn't exist

### Тестирование 
В приложение были добавлены тесты они находятся в файле /Incubator/dogs/tests.py. Они проверяют методы запросов, контент на страницах и правильность вписанной в путь породы собаки. Для запуска тестов напишите в терминале `python manage.py test dogs`.