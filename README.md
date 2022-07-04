# 0x00. AirBnB clone - The console

### Description of the project

This project is about creating a console for a future web application project. The console will be able to update, create, and save instances into a file using the JSON syntax for storing the data for the web site.

### How to use
* Download all part of the project

* Launch the console.py

* Enter any command

## Example
(hbnb) create User 

7ad92afc-c549-4b15-b97b-91071ffa3866 

(hbnb) update User 7ad92afc-c549-4b15-b97b-91071ffa3866 first_name "Juan" 

(hbnb) show User 7ad92afc-c549-4b15-b97b-91071ffa3866 

[User] (7ad92afc-c549-4b15-b97b-91071ffa3866) {'id': '7ad92afc-c549-4b15-b97b-91071ffa3866', 'created_at': datetime.datetime(2022, 7, 3, 20, 28, 21, 944913), 'updated_at': datetime.datetime(2022, 7, 3, 20, 29, 4, 862400), 'first_name': 'Juan'} 

(hbnb) destroy User 7ad92afc-c549-4b15-b97b-91071ffa3866 

(hbnb) show User 7ad92afc-c549-4b15-b97b-91071ffa3866 

** no instance found ** 

(hbnb) 

## Technologies
* Shell scripts tested using bash
* Python interpreter python3 version 3.8.5
* Tested on `Ubuntu 20.04 LTS`

## Tasks
The following files are programs or functions in Python:

| Filename | Description |
| -------- | ----------- |
| `base_model.py` | Class BaseModel that defines all common attributes/methods for other classes |
| `file_storage` | Class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances |
| `console.py` | Program that contains the entry point of the command interpreter |
| `user.py` | Class that inherits from BaseModel, there are other classes such as: `state.py`, `city.py`, `amenity.py`, `place.py` and `review.py` |

## AUTHORS:

| Name | Contact |
| ---- | ------- |
| Alejandro Reginensi | reginensia@gmail.com |
| Jesús Hernandez | jesusmanuel1843@gmail.com |
