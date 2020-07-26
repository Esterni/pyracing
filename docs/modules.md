#

# client
The `client` module contains the `Client()` class which makes up the bulk of pyracing.
Along with Client.authenticate(), it holds the class methods to query all of iRacing's web-data.

For a detailed description of each class method, see the [List of Functions](https://github.com/Esterni/pyracing/wiki/List-of-functions) wiki page.

# constants
The `constants` module contains all constants of iRacing. Since iRacing constants are
not always consistent in usage, we assign them to Class Attributes (not [instance attributes](https://www.python-course.eu/python3_class_and_instance_attributes.php)).
Which enables using the name "dirt_oval" instead of remembering that `4` is the index for it.

As an example, in any of the Client() methods that accept an argument of `category` you can
input "Dirt Oval" with `constants.Category.dirt_oval.value` and the correct value of `4` will be
used.

# response_objects
The `response_objects` sub-package is responsible for taking the JSON data returned from
iRacing endpoints and mapping them to instanced objects. When performing a query and
assigning it to a variable, it will be of the object type unique to that data. This means that
you don't have to parse any of the JSON data.

Getting the strength_of_field of a session:
```py
ir = client.Client('username', 'password')

session_data = await ir.subsession_data(subsession_id, cust_id=None)
print(session_data.strength_of_field)
```
Result:
```py
3051
```