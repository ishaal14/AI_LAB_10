TASK 01:
# Store the names of a few friends in a list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Print each person's name by accessing each element in the list
for name in names:
    print(name)
 

TASK:02
# List of people you'd like to invite to dinner
invited_guests = ["Albert Einstein", "Maya Angelou", "Leonardo da Vinci"]

# Print a personalized invitation message for each guest
for guest in invited_guests:
    print(f"Dear {guest}, I would like to invite you to dinner!")

TASK:03
# Original list of invited guests
invited_guests = ["Albert Einstein", "Maya Angelou", "Leonardo da Vinci"]

# Suppose Leonardo da Vinci can't make it, so we replace him with someone else
invited_guests[2] = "Nikola Tesla"

# Print a new set of invitation messages for each person in the updated guest list
for guest in invited_guests:
    print(f"Dear {guest}, I would like to invite you to dinner!")


TASK:04
class Employee:
    # Class variable to keep track of the total number of employees
    employee_count = 0
    
    # Constructor to initialize employee's name and salary
    def __init__(self, empName, salary):
        self.empName = empName
        self.salary = salary
        Employee.employee_count += 1  # Increment the employee count each time a new employee is created
    
    # Method to display the total number of employees
    @staticmethod
    def displayCount():
        print(f"Total number of employees: {Employee.employee_count}")
    
    # Method to display the employee's name and salary
    def displayEmployee(self):
        print(f"Employee Name: {self.empName}, Salary: ${self.salary}")

# Creating instances of the Employee class
emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)

# Displaying the count of employees
Employee.displayCount()

# Displaying details of each employee
emp1.displayEmployee()
emp2.displayEmployee()


TASK:05
import queue

# Create a LIFO Queue
lifo_queue = queue.LifoQueue()

# Adding items to the queue
lifo_queue.put(1)
lifo_queue.put(2)
lifo_queue.put(3)

# Removing and printing items from the queue (LIFO order)
print("Items in LIFO order:")
while not lifo_queue.empty():
    item = lifo_queue.get()
    print(item)



TASK:06
def find_sum(arr):
  """
  This function takes a 2D array and returns the sum of all the elements in the array.

  Args:
    arr: A 2D array of numbers.

  Returns:
    The sum of all the elements in the array.
  """
  sum = 0
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      sum += arr[i][j]
  return sum

# Create a 2D array from the input
arr = [[4], [8, 4], [8, 4, 1], [8, 7, 4, 1], [8, 7, 4, 3, 1]]

# Calculate the sum of the elements in the array
sum = find_sum(arr)

# Print the sum
print(f"The sum of all the elements in the array is: {sum}")


TASK:07
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, nbr):
        if nbr not in self.neighbors:
            self.neighbors.append(nbr)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_vertices(self, vertex_list):
        for v in vertex_list:
            self.add_vertex(v)

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))


# Create graph
g = Graph()
# Create vertices
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
# Add vertices to the graph
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
# Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'E')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
# Print graph
g.print_graph()