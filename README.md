![](https://storage.googleapis.com/twg-content/original_images/why-airbnb-takes-a-customer-centric-approach-to-adwords_case-studies_lg.png)

# 0x00. [AirBnB](https://www.airbnb.com) clone - The console

## Background Context
Welcome to the [AirBnB clone project](https://intranet.hbtn.io/concepts/74)! (The Holberton B&B)
Before starting, please read the AirBnB concept page and watch [this video](https://www.youtube.com/watch?v=jeJwRB33YNg&feature=youtu.be) from [Isaac Wong](https://twitter.com/KYIsaacWong), Cohort #5, showing what the Console should look like when you are complete with this project.

It is time to develop our AirBnb clone. The goal of the project is to deploy on your server a simple copy of the website. This project must be composed at the end of its development by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

See to the following picture:

<p>
<img src="https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Airbnb%20clone%20website.png" width="60%" height="60%">
</p>

AirBnb Clone is a project that consists of several stages linked together, which will be developed step by step:

* The Console
* Web Static
* MySQL storage
* Web framework - templating
* RESTful API
* Web dynamic

And today will start with The Console (a command interpreter to manage your AirBnB objects).

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration and others.

### Diagram AirBnB  clone (The Console)
![](https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Flow%20Airbnb%20clone.png)

## Create The console (manage your AirBnB objects)

* put in place a parent class (called ``BaseModel``) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (``User, State, City, Place``...) that inherit from ``BaseModel``
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine


### Files in This Repository:

| File | File Hierarchy | Description |
| :---: | :---: | :---: |
| `console.py` | [console.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/console.py) | The main console file |
| `amenity.py` | [models/amenity.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/amenity.py) | The amenity subclass |
| `base_model.py` | [models/base_model.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/base_model.py) | The base model superclass |
| `city.py` | [models/city.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/city.py) | The city subclass | 
| `place.py` | [models/place.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/place.py) | Te place subclass |
| `review.py` | [models/review.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/review.py) | Te review subclass |
| `state.py` | [models/state.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/state.py) | Te state subclass |
| `user.py` | [models/user.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/user.py) | Te user subclass |
| `file_storage.py` | [models/engine/file_storage.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/engine/file_storage.py) | The file storage class |
| `test_amenity.py` | [tests/test_amenity.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_amenity.py) | The unittest module for amenity |
| `test_base_model.py` | [tests/base_model.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_base_model.py) | The unittest module for base model |
| `test_city.py` | [tests/city.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_city.py) | The unittest module for city |
| `test_place.py` | [tests/place.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_place.py) | The unittest module for place |
| `test_review.py` | [tests/review.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_review.py) | The unittest module for review |
| `test_state.py` | [tests/state.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_state.py) | The unittest module for state |
| `test_user.py` | [tests/user.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_user.py) | The unittest module for user |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/tests/test_models/test_engine/test_file_storage.py) | The unittest module for file storage |


### Usage
### Basic usage of The Console

| Command | Usage | Example | Functionality |
| :---: | :---: | :---: | :---: |
| `help` | `help` | help | displays a list of the commands |
| `create` | `create <class>` | create BaseModel | Create a new instance |
| `show` | `show <class> <id>` | show BaseModel 787fds-fdf665-fdf843a1 | Shows a specific instance |
| `destroy` | `destroy <class> <id>` | destroy BaseModel 787fds-fdf665-fdf843a1 | Deletes a specific instance |
| `all` | `all` or `all <class>` | all BaseModel | Shows all instance or class |
| `update` | `update <class> <id> <attribute> <value>` | update BaseModel 787fds-fdf665-fdf843a1 name Maria | Update an attribute in an instance |
| `quit` | `quit` | quit | Quits the console |

### Installation:
```python
$ git clone git@github.com:mfcrespo/AirBnB_clone.git
$ ./console.py
```

## Examples:

### Interactive Mode

````python
$ ./console.py
(hbnb) all  <-- input 1
(hbnb) 
(hbnb) User.all() <-- input 2
````
#### Input 1
![](https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Airbnb%20console%20interactive.gif)

#### Input 2
![](https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Airbnb%20console%20non-interactive.gif)

### Non-interactive Mode

````python
$ echo "all User" | ./console.py
````

![](https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Airbnb%20console%20non-interactive.gif)

# Welcome to Holberton Console
[HBNHB - The Console](https://youtu.be/p00ES-5K4C8)

#### Follow us

| Authors | GitHub | Twitter | Linkedin |
| :---: | :---: | :---: | :---: |
| Maria Fernanda Crespo | [mfcrespo](https://github.com/mfcrespo) | [@mafe_crespo](https://twitter.com/mafe_crespo) | [mariafernandacrespo](https://www.linkedin.com/in/mariafernandacrespo) |
| Crispthofer Rincon | [CrispthoAlex](https://github.com/CrispthoAlex) | [CrispthoAlex](https://twitter.com/CrispthoAlex) | [carmurrain](https://www.linkedin.com/in/carmurrain) |

<p>
<img src="https://pbs.twimg.com/profile_images/962795960173846528/sl2HspUe_400x400.jpg" width="40%" height="40%">
</p>

[Crispthofer Rincon](https://twitter.com/CrispthoAlex)

<p>
<img src="https://pbs.twimg.com/profile_images/1116938743968149504/0TQ4K4r3_400x400.jpg" width="40%" height="40%">                                                       
</p>

[Maria Fernanda Crespo](https://twitter.com/mafe_crespo)

##### Holberton School - Foundations - Higher-level programming  AirBnB clone
##### June 25, 2020. Cali, Colombia