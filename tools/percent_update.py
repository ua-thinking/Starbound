import os

# Команда для git pull
pull_command = "git pull"

# Команда для запуску percent.py в папці tools
percent_command = "python tools/percent.py"

# Команда для git push
push_command = "git push"

# Змінна для зберігання токену доступу
token = "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"

# Змінна для зберігання назви репозиторію
repository = "Starbound"

# Папка, в якій знаходиться репозиторій
repo_folder = "/path/to/repo/folder/"

# Змінна для зберігання команди для авторизації за допомогою токену доступу
auth_command = f'echo "{token}" | gh auth login --with-token'

# Команда для перевірки наявності оновлень на гітхабі
check_updates_command = f'gh repo view {repository} | grep -m 1 -oP "(?<=default_branch:\ ).*(?=\n)"'

# Команда для виконання скриптів
execute_command = f"{pull_command} && {percent_command} && {push_command}"

# Перевірка наявності оновлень на гітхабі
check_updates_output = os.popen(check_updates_command).read().strip()

# Якщо гітхаб повернув назву гілки, то виконуємо скрипт
if check_updates_output:
    # Змінна для зберігання команди для переключення на гілку з оновленнями
    checkout_command = f"git checkout {check_updates_output}"
    # Виконуємо команди в терміналі
    os.chdir(repo_folder)
    os.system(auth_command)
    os.system(checkout_command)
    os.system(execute_command)
else:
    # Якщо гітхаб не повернув назву гілки, то виводимо повідомлення
    print("Немає оновлень на гітхабі.")