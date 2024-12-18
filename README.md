# Автоматизация Калькулятора

Этот проект предназначен для автоматизации работы с калькулятором Windows с использованием библиотеки `pyautogui`. Скрипт открывает калькулятор, находит кнопки и выполняет простую арифметическую операцию.

# Подготовка

Склонируйте репозиторий к себе при помощи команды: 

```bash
git clone https://github.com/FirstEncounter3/PyAutoGuiExample.git
```

Перейдите внутрь директории проекта и выполните создание и активацию виртуального окружения:

```bash
python -m venv venv
venv/Scripts/activate
```

## Зависимости

Для работы скрипта необходимо установить следующие библиотеки:

- `pyautogui`
- `pyscreeze`
- `pillow`
- `opencv-python`

Вы можете установить их с помощью pip и файла requirements.txt из проекта:

```bash
pip install -r requirements.txt
```

## Использование

1. Запустите скрипт:

```bash
python main.py
```

2. Скрипт автоматически откроет калькулятор, найдет необходимые кнопки и выполнит операцию 1 + 2 + 7.