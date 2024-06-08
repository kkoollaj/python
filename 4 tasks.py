class TaskManager:
    def __init__(self):
        self.tasks = {
            "Невыполненные": [],
            "В работе": [],
            "Выполненные": []
        }
        self.load_tasks()

    def display_tasks(self):
        print("=== Список задач ===")
        for section, tasks in self.tasks.items():
            print(f"{section}:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            print()

    def add_task(self, section, task):
        self.tasks[section].append(task)
        print(f"Задача '{task}' добавлена в раздел '{section}'.")
        print()
        self.save_tasks()

    def remove_task(self, section, index):
        try:
            removed_task = self.tasks[section].pop(index - 1)
            print(f"Задача '{removed_task}' удалена из раздела '{section}'.")
            self.save_tasks()
        except IndexError:
            print("Неверный индекс задачи.")

    def move_task(self, from_section, to_section, index):
        try:
            task = self.tasks[from_section].pop(index - 1)
            self.tasks[to_section].append(task)
            print(f"Задача '{task}' перемещена из раздела '{from_section}' в раздел '{to_section}'.")
            self.save_tasks()
        except IndexError:
            print("Неверный индекс задачи.")

    def save_tasks(self):
        with open('4 tasks.txt', 'w', encoding='utf-8') as file:
            for section, tasks in self.tasks.items():
                file.write(f"{section}:\n")
                for task in tasks:
                    file.write(f"- {task}\n")

    def load_tasks(self):
        try:
            with open('4 tasks.txt', 'r', encoding='utf-8') as file:
                current_section = None
                for line in file:
                    line = line.strip()
                    if line.endswith(':'):
                        current_section = line[:-1]
                    elif line.startswith('- ') and current_section:
                        self.tasks[current_section].append(line[2:])
        except FileNotFoundError:
            with open('4 tasks.txt', 'w', encoding='utf-8') as file:
                pass

def main():
    task_manager = TaskManager()
    while True:
        print("1. Список задач")
        print("2. Выход")
        print()
        choice = input("Выберите действие: ")
        print()

        if choice == "1":
            task_manager.display_tasks()
            print("Функции:")
            print("1. Добавить задачу")
            print("2. Удалить задачу")
            print("3. Переместить задачу")
            print()
            sub_choice = input("Выберите функцию: ")

            if sub_choice == "1":
                section = input("Выберите раздел (Невыполненные, В работе, Выполненные): ")
                if section in task_manager.tasks:
                    task = input("Введите задачу: ")
                    task_manager.add_task(section, task)
                else:
                    print("Неверный раздел.")
            elif sub_choice == "2":
                section = input("Выберите раздел (Невыполненные, В работе, Выполненные): ")
                if section in task_manager.tasks:
                    index = int(input("Введите номер задачи для удаления: "))
                    task_manager.remove_task(section, index)
                else:
                    print("Неверный раздел.")
            elif sub_choice == "3":
                from_section = input("Выберите исходный раздел (Невыполненные, В работе, Выполненные): ")
                to_section = input("Выберите целевой раздел (Невыполненные, В работе, Выполненные): ")
                if from_section in task_manager.tasks and to_section in task_manager.tasks:
                    index = int(input("Введите номер задачи для перемещения: "))
                    task_manager.move_task(from_section, to_section, index)
                else:
                    print("Неверный раздел.")
            else:
                print("Неверный выбор.")
        elif choice == "2":
            print("Пока.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
