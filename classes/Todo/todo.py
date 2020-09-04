class Todo:
	"""Making a todo list like object"""

	def __init__(self):
		"""Initialize the Todo note"""
		self.todo = {}

	def add(self, task:str, description:str)-> None:
		"""Add a new task to the todo list"""
		self.task = task
		self.description = description
		self.todo[self.task] = self.description
		

	def view(self)-> str:
		"""View the task and it's description."""
		for task, description in self.todo.items():
			print(f'Task : {task}\nDescription : {description}')

	# def __del__(self)-> None:
		# """Delete a task from the todo list"""
		# print(f'Task : "{self.task}" has been deleted')