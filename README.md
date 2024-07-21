# There was a task:
# Тестовое задание Python **Developer**

Сделать web приложение, оно же сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время.

 - *Вывод данных (прогноза погоды) должен быть в удобно читаемом формате. 

 - Веб фреймворк можно использовать любой.

 - api для погоды:* https://open-meteo.com/ *(можно использовать какое-нибудь другое, если вам удобнее)*

будет плюсом если:
1. написаны тесты
2. app докеризирован
3. сделаны автодополнение (подсказки) при вводе города
4. при повторном посещении сайта будет предложено посмотреть погоду в городе, в котором пользователь уже смотрел ранее
5. будет сохраняться история поиска для каждого пользователя, и будет API, показывающее сколько раз вводили какой город


# Solution

# Weather Forecast App

## Overview

The Weather Forecast App is a Django-based web application that provides users with weather forecasts for various cities. Users can search for cities, view weather data, and manage their accounts.

## Features

- User authentication (login, logout, signup)
- Search for weather forecasts by city name
- Display of weather data including max and min temperatures
- Autocomplete functionality for city search
- User-friendly interface with Bootstrap styling

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vsirotkin/Python_Meteo_Project.git
   cd weather-forecast-app
   ```

2. **Set up a virtual environment using Pipenv:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set up the database:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

2. **User Registration:**
   - Click on the "Sign Up" link to create a new account.
   - Fill in the required information and submit the form.

3. **User Login:**
   - Use the "Log In" link to access your account.
   - Enter your credentials and click "Log In".

4. **Viewing Weather Data:**
   - After logging in, you can search for cities using the search bar.
   - The application will display weather data for the selected city.

5. **Logging Out:**
   - Click on the "Log Out" link to end your session.

## Testing

To run the test suite, use the following command:
```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [yourname@example.com](mailto:yourname@example.com).



# Docker
To start your Docker container, apply migrations, and set up a superuser, follow these steps:

1. **Start the Docker container**:
   Open a terminal and navigate to the directory containing your `compose.yml` file. Then run the following command to start your Docker containers:

   ```bash
   docker compose up -d
   ```

   The `-d` flag runs the containers in detached mode, meaning they will run in the background.

2. **Apply migrations**:
   Once the containers are up and running, you can apply the database migrations using the following command:

   ```bash
   docker compose exec web python manage.py makemigrations
   docker compose exec web python manage.py migrate
   ```

3. **Create a superuser**:
   To create a superuser for your Django application, run the following command:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

   Follow the prompts to set up the username, email, and password for the superuser.

Here's a summary of the commands you need to run:

```bash
# Start the Docker containers
docker-compose up -d

# Apply migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser
```

After completing these steps, your Docker container should be running with the necessary migrations applied, and you should have a superuser account set up for your Django application. You can access your application by navigating to `http://localhost:8000` in your web browser.
