class Todo:
	"""Making a todo list like object"""

	def __init__(self):
		"""Initialize the Todo note"""
		self.todo = {}

        def add(self, task:str, description:str, status=False:bool)-> None:
		"""Add a new task to the todo list"""
		self.task = task
		self.description = description
                self.status = status
		self.todo[self.task] = [self.description, self.status]

        def view(self)-> str:
		"""View the task and it's description."""
		for task, description in self.todo.items():
			print(f'Task : {task}\nDescription : {description}')

        def completed(self):
            """Set status of completed task to True"""
            self.status = True
