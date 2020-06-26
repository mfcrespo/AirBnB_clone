![](https://storage.googleapis.com/twg-content/original_images/why-airbnb-takes-a-customer-centric-approach-to-adwords_case-studies_lg.png)

# 0x00. [AirBnB](https://www.airbnb.com) clone - The console

## Background Context
Welcome to the [AirBnB clone project](https://intranet.hbtn.io/concepts/74)! (The Holberton B&B)
Before starting, please read the AirBnB concept page and watch [this video](https://www.youtube.com/wa\
tch?v=jeJwRB33YNg&feature=youtu.be) from [Isaac Wong](https://twitter.com/KYIsaacWong), Cohort #5, sho\
wing what the Console should look like when you are complete with this project.

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first \
step is very important because you will use what you build during this project with all other followin\
g projects: HTML/CSS templating, database storage, API, front-end integration

Each task is linked and will help you to:

* put in place a parent class (called ``BaseModel``) to take care of the initialization, serializ\
ation and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string \
<-> file
* create all classes used for AirBnB (``User, State, City, Place``...) that inherit from ``BaseMo\
del``
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## Whats a command interpreter?
Do you remember the Shell? Its exactly the same but limited to a specific use-case. In our case, we wa\
nt to be able to manage the objects of our project:

   * Create a new object (ex: a new User or a new Place)
   * Retrieve an object from a file, a database etc
   * Do operations on objects (count, compute stats, etc)
   * Update attributes of an object
   * Destroy an object

## Resources
#### Read or watch:

* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Goog\
le:

### General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

# More Info
## Execution
Your shell should work like this in interactive mode:

````python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
````

But also in non-interactive mode: (like the Shell project in C)


````python
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
````

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200625%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200625T135842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=85bc284adcc13eafeba20fd002c29acb752ddde8e0bc537b49b5a26aaef2dae4)

# Welcome to Holberton Console
[HBNHB - The Console](https://youtu.be/p00ES-5K4C8)

#### Follow us
[Crispthofer Rincon](https://twitter.com/CrispthoAlex) - [Maria Fernanda Crespo](https://twitter.com/mafe_crespo)