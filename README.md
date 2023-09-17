The programming framework or methodology known as object-oriented programming (OOP) employs objects as the basic building blocks for structuring and developing code. An object in OOP is a self-contained structure that combines data (attributes) and behavior (methods) to represent a real-world thing or concept. With the help of OOP, software may be made to be more modular, maintainable, and understandable by modeling it after the actual world.

The exercise was completed using Python and coding a program that reads from the inventory.txt file and to perform the following tasks. A file called inventory.py was created with a Shoe class defined with the attributes country, code, product, cost and quantity. The following methods are defined in the class, namely get_cost that returns the shoe cost, get_quantity returning the shoe quantity and __str__ which returns a string representation of a class. Outside of the class a variable was created with a variable with an empty list that stores a list of shoes objects. The following functions were defined outside of the class;
- read_shoes_data which opens the inventory.txt file and reads the data from this 
  file the create shoes object and add the object into the shoes list.
- capture_shoes allows the user to capture data on a shoe and use the data to 
  create a shoe object and append this object inside the shoes list.
- view_all iterates over the shoes list and print the details of the shoes returned 
  from the __str__ function.
- restock finds the shoe object with the least quantity thus need to be restocked.
- search_shoe searches for a specific shoe from the list using the shoe code and 
  returns the object that will be printed.
- value_per_item calculates the total value for each item.
- highest_qty determines the products with the highest quantity and print the shoe 
  as being for sale.
Lastly, a menu in a while was created in the main to executes each function.
