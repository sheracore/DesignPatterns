# DesignPatterns


# Behavioral Patterns
 ## Momento pattern
 #### Undo momento
 #### SOLOD (Single Responsibility Principle)

![momento uml](/from_other_sources/momento_pattern/pictures/momento_1.png)

![momento uml](/from_other_sources/momento_pattern/pictures/momento_2.png)

![momento uml](/from_other_sources/momento_pattern/pictures/momento_3.png)

#### Cause of the first principle of SOLOD (Single Responsibility Principle)

## State pattern
#### like photoshop type tools selection
#### SOLOD (Open Closed Principle)
![state uml](/from_other_sources/state_pattern/pictures/state_pattern.png)
![state uml](/from_other_sources/state_pattern/pictures/state_pattern2.png)



## Iterator pattern
#### like browser history when you go to preview URL of the next URL
#### Single Responsibility Principle: It’s really easy to extract the huge algorithms into separate classes using the iterator method.
#### Open/Closed Principle: Passing the new iterators and collections into the client code does not break the code and can easily be installed into it.
#### Easy to use Interface: It makes the interface really simple to use and also supports the variations in the traversal of the collections.
![iterator uml](/from_other_sources/iterator_pattern/pictures/iterator_pattern.png)


## Strategy pattern
#### Single Responsibility Principle and Open/Closed Principle
![iterator uml](/from_other_sources/strategy_pattern/pictures/strategy_pattern1.png)
![strategy uml](/from_other_sources/strategy_pattern/pictures/strategy_pattern2.png)
![strategy uml](/from_other_sources/strategy_pattern/pictures/strategy_pattern3.png)

## Template pattern
![template uml](/from_other_sources/template_pattern/pictures/template_pattern1.png)
![template uml](/from_other_sources/template_pattern/pictures/template_pattern2.png)
![template uml](/from_other_sources/template_pattern/pictures/template_pattern3.png)

## Command pattern
#### The Command pattern is a behavioral design pattern, in which an abstraction exists between an object that invokes a command, and the object that performs it.
#### E.g., a button will call the Invoker, which will call a pre-registered Command, that the Receiver will perform.
#### The command pattern is a good solution for implementing UNDO/REDO functionality into your application.
### Uses:

* GUI Buttons, menus
* Macro recording
* Multi-level undo/redo
* Networking — send whole command objects across a network, even as a batch
* Parallel processing or thread pools
* Transactional behavior
* Wizards

![command uml](/from_other_sources/command_pattern/pictures/command_pattern1.png)
![command uml](/from_other_sources/command_pattern/pictures/command_pattern3.png)

## Observer pattern
#### The Observer pattern is a software design pattern in which an object, called the Subject (Observable), manages a list of dependents, called Observers, and notifies them automatically of any internal state changes by calling one of their methods.
#### The Observer pattern follows the publish/subscribe concept. A subscriber subscribes to a publisher. The publisher then notifies the subscribers when its necessary.
![observer uml](/from_other_sources/observer_pattern/pictures/observer_pattern.png)
![observer uml](/from_other_sources/observer_pattern/pictures/observer_pattern1.png)
![observer uml](/from_other_sources/observer_pattern/pictures/observer_pattern2.png)

## Mediator pattern
![mediator uml](/from_other_sources/mediator_pattern/pictures/mediator_pattern.png)
![mediator uml](/from_other_sources/mediator_pattern/pictures/mediator_pattern2.png)
![mediator uml](/from_other_sources/mediator_pattern/pictures/mediator_pattern3.png)
![mediator uml](/from_other_sources/mediator_pattern/pictures/mediator_pattern4.png)

* For example, a Chatroom application

# WIP...

