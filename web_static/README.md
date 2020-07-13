![](https://storage.googleapis.com/twg-content/original_images/why-airbnb-takes-a-customer-centric-approach-to-adwords_case-studies_lg.png)

# 0x01. [AirBnB](https://www.airbnb.com) clone - Web static

## Background Context

### Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static pages
Style guide
Fake contents
No Javascript
No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

AirBnb Clone is a project that consists of several stages linked together, which will be developed step by step:

* The Console
* Web Static
* MySQL storage
* Web framework - templating
* RESTful API
* Web dynamic


### Diagram AirBnB  clone (Web static)
![](https://github.com/mfcrespo/AirBnB_clone/blob/master/images/Flow%20Airbnb%20clone.png)


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


#### Follow me

| Authors | GitHub | Twitter | Linkedin |
| :---: | :---: | :---: | :---: |
| Maria Fernanda Crespo | [mfcrespo](https://github.com/mfcrespo) | [@mafe_crespo](https://twitter.com/mafe_crespo) | [mariafernandacrespo](https://www.linkedin.com/in/mariafernandacrespo) |

<p>
<img src="https://pbs.twimg.com/profile_images/1116938743968149504/0TQ4K4r3_400x400.jpg" width="20%" height="20%">                                                       
</p>

[Maria Fernanda Crespo](https://twitter.com/mafe_crespo)

##### Holberton School - AirBnB clone
##### July 12, 2020. Cali, Colombia