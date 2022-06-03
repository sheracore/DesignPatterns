# DesignPatterns
DesignPatterns by mosh


Container in java is package and in .NET is namespace 


 ## Momento pattern
 #### Undo momento
 #### SOLOD (Single Responsibility Principle)

![momento uml](/momento_pattern/pictures/momento_1.png)

![momento uml](/momento_pattern/pictures/momento_2.png)

![momento uml](/momento_pattern/pictures/momento_3.png)

#### Cause of first principle of SOLOD (Single Responsibility Principle)

## State pattern
#### like photoshop type tools selection
#### SOLOD (Open Closed Principle)
![state uml](/state_pattern/pictures/state_pattern.png)
![state uml](/state_pattern/pictures/state_pattern2.png)



## Iterator pattern
#### like browser histroty when you go to previews url of next url
#### Single Responsibility Principle: It’s really easy to extract the huge algorithms into separate classes in the Iterator method.
#### Open/Closed Principle: Passing the new iterators and collections into the client code does not break the code can easily be installed into it.
#### Easy to use Interface: It makes the interface really simple to use and also supports the variations in the traversal of the collections.
![iterator uml](/iterator_pattern/pictures/iterator_pattern.png)


## Strategy pattern
#### Single Responsibility Principle and Open/Closed Principle
![iterator uml](/strategy_pattern/pictures/strategy_pattern1.png)
![strategy uml](/strategy_pattern/pictures/strategy_pattern2.png)
![strategy uml](/strategy_pattern/pictures/strategy_pattern3.png)

## Template pattern
![template uml](/template_pattern/pictures/template_pattern1.png)
![template uml](/template_pattern/pictures/template_pattern2.png)
![template uml](/template_pattern/pictures/template_pattern3.png)

## Command pattern
#### The Command pattern is a behavioural design pattern, in which an abstraction exists between an object that invokes a command, and the object that performs it.
#### E.g., a button will call the Invoker, that will call a pre-registered Command, that the Receiver will perform.
#### The command pattern is a good solution for implementing UNDO/REDO functionality into your application.
### Uses:

* GUI Buttons, menus
* Macro recording
* Multi-level undo/redo
* Networking — send whole command objects across a network, even as a batch
* Parallel processing or thread pools
* Transactional behaviour
* Wizards

![command uml](/command_pattern/pictures/command_pattern1.png)
![command uml](/command_pattern/pictures/command_pattern3.png)


