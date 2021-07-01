class Stack:
    def __init__(self) -> None:
        self.__stack_list = []

    def push(self, obj) -> None:
        self.__stack_list.append(obj)
        self.remove_dupl()

    def remove_dupl(self) -> None:
        self.__stack_list = list(set(self.__stack_list))

    def pop(self) -> None:
        if len(self.__stack_list) == 0:
            return None
        return self.__stack_list.pop()

    def __str__(self) -> str:
        return '; '.join(self.__stack_list)


class TaskManager:
    def __init__(self) -> None:
        self.task = {}

    def new_task(self, task, priority) -> None:
        self.del_task(task)

        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

    def del_task(self, key) -> None:
        if key in self.task:
            del self.task[key]

    def __str__(self) -> str:
        pr_list = []
        if self.task:
            for priotiry in sorted(self.task.keys()):
                pr_list.append(f"{priotiry} {self.task[priotiry]}\n")
        return ''.join(pr_list)


manager = TaskManager()
print(manager)
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)
print(manager)
manager.del_task(2)
print(manager)

