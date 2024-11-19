# Функция для записи ошибок в файл
def log_error_to_file(message):
    with open("error_log.txt", "a") as file:
        file.write(message + "\n\n\n\n\n")
