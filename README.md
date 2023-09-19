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

The included models provide classes, along with class methods and instance methods, for the two tables and object types used in the application: Collaborative Pianists and Students. Many of the methods between these two models work similarly, with small differences in received parameters and specific assignments. A rough overview of how these methods work is below.

#### \_\_init__
As expected, the init methods receive parameters to set the appropriate attributes for newly created objects. It is worth noting the `@property` methods that follow, as they will be called to actually set and retrieve the values.

#### @property getters and setters
These methods are called whenever attributes are retrieved or set for instances of the class. As is often the case for property methods, the setters perform validation checks of the data before setting the attributes on the object, raising exceptions in case the check fails.

#### create_table/drop_table
These two class methods are called by the debug file, ensuring that `Collaborative_Pianist` and `Student` tables are cleared from the database and then re-recreated and inserted into the database, which is useful for debugging and starting from a clean slate. The `IF NOT EXISTS` designation prevents duplicate tables from being created.

#### get_all
These methods execute a SQL query of the database, retrieving all of the rows for their particular table. Once fetched, each of the rows is then passed through `make_instance_from_db`.

#### get_by_id
These class methods query the database table for a row whose ID matches in the id received as a parameter. If no match is found in the database, an exception is raised. If a match is found, the row is then passed into `make_instance_from_db`.

#### make_instance_from_db_row
These methods receive a row that has been retrieved from the database. First, they check if a local object has already been retrieved (and thus exists in the class's `all` dictionary); if it does, checks are done to ensure that the local object's attributes match the columns of the database row (in case a local object was partially updated before an exception was raised or something else prevented persistence to the database). If the `all` dictionary does not contain a key matching the row's id, then we know the row has not been previously retrieved. In this case, a new object is instantiated and saved to the local dictionary. This process prevents duplicate objects from being created on the front end.

#### create
`create` receives values for attributes, and then attempts to instantiate a new object with those attributes. The newly created object then has its `save_to_db` method called.

#### save_to_db
`save_to_db` receives an object, then executes a SQL query to persist the object's attributes to the database table as a new row.

#### delete_instance
This method receives an object, then executes a SQL query that deletes the row corresponding to that object's ID from the database. Importantly, the `Collaborative_Pianist` version of this method also calls `Student`'s `unassign_students` method with the ID, which ensures that the Students who had been previously assigned to that pianist will now automatically be re-assigned to the `No Pianist` row.

#### get_assigned_students
This `Collaborative_Pianist` method performs a SQL query to fetch all of the students from the database whose `pianist_id` column matches the id of the pianist passsed in. Each resulting row is passed through `make_instance_from_db`; the resulting objects are accumulated into a list and returned.

#### update_pianist / update_student
These methods execute a SQL query to find a row in the database whose ID matches the passed-in object's ID, then updates the other columns to the values passed into the method.

#### unassign_students
This method updates student's `pianist_id` column in the database to be `No Pianist` if their `pianist_id` column matches the id passed in. This is used to change a student's pianist assignment to `No Pianist`, rather than leaving them assigned to a pianist who no longer exists in the database.

#### get_unassigned_students
This method retrieves all students from the database who are assigned to `No Pianist`, which is useful for a user to see in case they would like to know which students to prioritize assigning in their work.

### Ideas for Future Development
* More flexible user inputs, i.e. by standardizing capitalization of entered data
* Adding some many-to-many relationships, perhaps by allowing students to have multiple pianist assignments for different projects. This would necessitate a new table to hold the relationships.
* Adding other tables for things like repertoire or events, and associating those things with both pianists and students

*****

Project created by Scott Schwab, 2023

Thanks to http://markdownlivepreview.com for markdown templating assistance in the creation of this README