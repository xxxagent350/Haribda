from datetime import datetime


def get_full_current_date() -> str:
    # Получение текущей даты и времени
    current_datetime = datetime.now()
    # Преобразование в строку
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Переводит секунды в string отображающий время
def seconds_to_time_string(time_seconds, show_only_parts = 999) -> str:
    if show_only_parts < 1:
        print("Ошибка в seconds_to_time_string(): show_only_parts не может быть менее 1")
        return ""

    days, not_days = divmod(time_seconds, 86400)
    hours, not_hours = divmod(not_days, 3600)
    minutes, not_minutes = divmod(not_hours, 60)
    seconds = not_minutes

    time_string = ""
    showed_parts = 0
    if days > 0:
        time_string += f"{int(days)}д "
        showed_parts += 1
        if showed_parts >= show_only_parts:
            return time_string
    if hours > 0:
        time_string += f"{int(hours)}ч "
        showed_parts += 1
        if showed_parts >= show_only_parts:
            return time_string
    if minutes > 0:
        time_string += f"{int(minutes)}м "
        showed_parts += 1
        if showed_parts >= show_only_parts:
            return time_string
    if seconds > 0 or time_string == "":
        time_string += f"{int(seconds)}с"
    return time_string

