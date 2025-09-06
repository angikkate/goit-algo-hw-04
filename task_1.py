# task_1.py
# Рекурсивне копіювання та сортування файлів за розширеннями

import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            # Пропускаємо приховані файли/папки
            if item.startswith('.'):
                continue

            src_path = os.path.join(src_dir, item)

            # Пропускаємо папку призначення
            if os.path.abspath(src_path) == os.path.abspath(dest_dir):
                continue

            if os.path.isdir(src_path):
                # Рекурсивний виклик для підпапок
                copy_and_sort_files(src_path, dest_dir)
            else:
                # Визначаємо розширення файлу
                ext = os.path.splitext(item)[1][1:] or "no_ext"
                target_folder = os.path.join(dest_dir, ext)
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy2(src_path, target_folder)
                print(f"Копіюю {src_path} → {target_folder}")
    except Exception as e:
        print(f"Помилка при доступі до {src_dir}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширеннями"
    )
    parser.add_argument(
        "src",
        nargs="?",
        default=".",
        help="Шлях до вихідної директорії (за замовчуванням поточна)"
    )
    parser.add_argument(
        "dest",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням dist)"
    )
    args = parser.parse_args()

    os.makedirs(args.dest, exist_ok=True)
    copy_and_sort_files(args.src, args.dest)
    print("\n Копіювання завершено!")


if __name__ == "__main__":
    main()
