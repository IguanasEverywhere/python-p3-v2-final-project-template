# Collaborative Pianist CLI Project

## Project Description
The collaborative pianist CLI project is intended for an audience of collegiate music faculty. Music departments often need to manage the assignment of collaborative pianists who perform with and accompany music students in their program.

Via a Command Line Interface (CLI), users can interact with a database that contains tables for collaborative pianists, music students, and the relationships between them.

## Using the Application

To run the program, with Python installed on your machine, navigate to the home directory of the program and run the command `python lib/debug.py`, then `exit()` to exit the ipdb session, followed by `python lib/cli.py`.

Doing so will present the user with the Main Menu:
* 1\. Collaborative Pianists
* 2\. Students
* 3\. Exit the program

The user can then enter the number corresponding to their desired task menus, followed by the enter key to be taken to the respective menu.

The Collaborative Pianist and Student menus operate in a similar fashion, with displays of data and inputs as needed to create or retrieve appropriate data. The "Access by...id" menus bring up menus with more options for actions to take with particular pianists/students. Further details on how the code completes these actions is outlined below.

## Important Files

### cli.py
This file serves as the entry point for the application; because this is so, the `if` statement calls a function that displays the main menu (by calling imported `main()` function). within a `while` loop and prompts the user for input about which menu they would like to explore.

### pianist_menu.py

pianist_menu displays menu options within a `while` loop and prompts for user selection. The choices each correspond to a call for an appropriate imported menu function or helper function to complete the listed task.

### pianist_by_id_menu

If the user selects "Access pianist by ID", the `pianist_by_id_menu` function is called. This function prompts the user for an ID, then calls a helper function to retrieve the pianist from the database with that ID. If that pianist is verified as existing, the user is then displayed a menu of options to perform for that pianist data entry. Each option corresponds with the invocation of a helper function to perform the task (print pianist's info, get pianist's assigned students, update the pianist, delete the pianist).

### student_menu

Similar to `pianist_menu`, the `student_menu` displays menu options within a `while` loop while prompting for user input. Each input corresponds with an appropriate imported helper function. If the user selects `0`, then the `active` variable is set to `False`, which discontinues the display of the menu.

### student_by_id_menu

Similar to `pianist_by_id_menu`, the `student_by_id_menu` prompts the user to enter an ID, calls a helper function that retrieves a student from the database with a matching ID, and, once verified, displays a menu of options that the user can complete with said student. As with all the other menus in this program, the menu is run through a `while` loop which can be interrupted by setting `active` to `False` when the user decides to exit the menu.

### helpers.py

The helpers file contains functions that are invoked by selecting their corresponding options from the menus above.

#### get_all_pianists_from_db / get_all_students_from_db
These functions call `get_all` methods from their respective models, then loops over the results and prints the ID and name of each returned item.

#### retrieve_pianist_by_id / retrieve_student_by_id
These functions contain a `try` block that calls their model's `get_by_id` method, catching an exception if no matching item is found, and returns the item.

#### print_pianist_info / print_student_info
These functions receive a previously retrieved object, and then print the information of that object in an attractive format.

#### delete_pianist / delete_student
As the names imply, these functions receive an ID as input, and then delete the corresponding item from the database. They first attempt to retrieve the items from the database, and execute the deletion if an item is find.

#### add_new_pianist / add_new_student
These functions prompt the user for information about the new item, then call their respective model's `create` methods with that information within a `try` block. Exceptions from failed creations are handled, and in such cases, the add function is called again to give the user another attempt at entering valid information. The add_new_student function calls `get_all_pianists_from_db` so that the user is reminded of avaialble pianists to assign to their newly created student.

#### update_pianist_info / update_student_info
These methods take a pianist (or student) object. Within a `try` block, new information for the item is solicited from the user, and the appropriate model's update method is then called with the new information. In case of an exception, the pianist or student is retrieved from the database once more (in case the local object has been partially updated), and the function is called again with the retrieved object for another attempt at enterint valid information. `update_student_info` also checks that the newly assigned pianist ID exists in the database before allowing the update to take place.

#### get_assigned_students
This function takes a pianist object and calls the `Collaborative Pianist` model's `get_assigned_students` method with its id. The returned collection is then iterated over and has its information displayed to the user.

#### retrieve_assigned_pianist_for_student
This function takes in a student object, and calls the `retrieve_pianist_by_id` method with that student's `pianist_id` attribute.

#### unassigned_students
This function calls the `get_unassigned_students` method from the `Student` model, iterates over the collection and prints the details of each result.

#### exit_program
This program prints a farewell message and exits the CLI.

### Models





## Headers

# This is a Heading h1
## This is a Heading h2
###### This is a Heading h6

## Emphasis

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b

## Images

![This is an alt text.](/image/sample.png "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.
