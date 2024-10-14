<h1 align="center">TDD_Project</h1>

Этот проект представляет собой веб-приложение для онлайн-библиотеки, созданное с использованием TDD метода (Разработка через тестирование). Сначала пишутся модульные тесты, а потом пишется приложение. 

___

<h2 align="center">Установка</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/SergeiMischenko/TDD_Project.git
    ```

2. **Перейдите в папку проекта:**
    ```bash
    cd TDD_Project
    ```

3. **Установите виртуальное окружение и активируйте его:**
    ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows
    ```

4. **Установите необходимые зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Откройте файл .env и заполнить его своими данными**
    ```env
    SECRET_KEY = 'your-secret-key'
    ```

6. **Выполните миграции базы данных:**
    ```bash
    python manage.py migrate
    ```

7. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```

8. **Доступ к тестам:**
   
    После завершения всех вышеуказанных шагов, приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
   
    Проверить что все тесты выполняются можно командой `python manage.py test`.
