import os
import shutil

def get_folder_path():
    """Uživatelský input, zatím bez ošetření na chyby"""
    folder_path = input("Zadej cestu ke složce, kterou chceš roztřídit: ")
    return folder_path

def move_files(folder_path):
    """Hlavní cyklus, který projde složky a soubory, které roztřídí do složek podle přípony"""
    for folder_path, _, files in os.walk(folder_path):
        for item in files:
            file_path = os.path.join(folder_path, item)
            if os.path.isfile(file_path):
                extension = os.path.splitext(item)[1]
                new_folder_path = os.path.join(folder_path, extension.lstrip("."))

                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                new_file_path = os.path.join(new_folder_path, item)
                shutil.move(file_path, new_file_path)

if __name__ == "__main__":
    folder_path = get_folder_path()
    move_files(folder_path)
