---
title: Object oriented programming (OOP)
description: Overview of Encapsulation, inheritance, polymorphism, and abstraction - and other topics.
date: 03-28-2024
---

## Classes and Objects

A class is a blueprint for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods). An object is an instance of a class. Objects are instantiated from classes using the new keyword. A constructor in Java is a block of code similar to a method that's called when an instance of an object is created. Java allows multiple constructors as long as they have different parameters, this is called constructor Overloading.

### Memory Allocation:

In Java, memory for objects is allocated on the heap when they are created.

### Static members:

Static members belong to the class rather than any object instance, allowing Java to create methods and variables that belong to the class as a whole.

```java
public class House {
    private int windows;
    private int doors;
    private String address;

    // static member
    public static int totalHouses = 0;

    // Point 5: To Invoke Current Object's Constructor
    public House() {
        // Default constructor with default values
        this(0, 0, "No Address"); // Invoking another constructor
    }

    public House(int windows, int doors, String address) { // overloaded constructor
        // Point 1: To Refer to Current Object's Instance Variables
        this.windows = windows;
        this.doors = doors;
        this.address = address;
    }

    // Method that returns the House object itself, to demonstrate chaining
    public House setWindows(int windows) {
        this.windows = windows;
        // Point 4: To Return the Current Class Instance
        return this;
    }

    public House setDoors(int doors) {
        this.doors = doors;
        // Returns this for method chaining
        return this;
    }

    // Point 2: To Invoke Current Object's Method (indirectly via displayInfo())
    public void displayInfo() {
        // This method indirectly demonstrates invoking another method (describe()) on the same object using this
        this.describe(this); // Point 3: To Pass Current Object as a Parameter
    }

    private void describe(House house) {
        System.out.println("House at " + house.address + " has " + house.windows + " windows and " + house.doors + " doors.");
    }

    public static void main(String[] args) {
        House myHouse = new House();
        int totalHouses = House.totalHouses;
        myHouse.setWindows(5).setDoors(2).displayInfo(); // Method chaining example
    }
}
```

### this:

The this keyword in Java is a reference variable that refers to the current object.

1. To Refer to Current Object's Instance Variables
2. To Invoke Current Object's Method
3. To Pass Current Object as a Parameter
4. To Return the Current Class Instance
5. To Invoke Current Object's Constructor

### Method chaining:

Method chaining is a common syntax for invoking multiple method calls in object-oriented programming languages.

## 1. Encapsulation

Encapsulation is the bundling of data with the methods that operate on these data. The data is hidden from outside the class and can only be accessed through methods, which provides control over how the data can be manipulated and prevents unintended modification or access, these methods are called (public) setter and getter methods.

```java
public class Employee {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

```

## 2. Abstraction

Abstraction in Java refers to hiding the implementation details of a code and exposing only the necessary information to the user.

### abstract keyword

```java
abstract class Animal {
    abstract void makeSound();
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Bark");
    }
}
```

### Interfaces

Interfaces define a contract for classes to implement. They declare method signatures without providing implementations. Classes that implement an interface must provide implementations for all the methods declared in the interface.

```java
interface Animal {
    void makeSound();
}

class Dog implements Animal {
    public void makeSound() {
        System.out.println("Bark");
    }
}
```

### Differentiating Interfaces and Abstract Classes:

Interfaces cannot hold state and provide a contract for what a class can do. Abstract classes can hold state and can provide some implementation.

### Access Modifiers

Access modifiers such as public, protected, and private can also be used to achieve abstraction by controlling the visibility of members (fields and methods) of a class.

```java
class Animal {
    private String sound;

    public Animal(String sound) {
        this.sound = sound;
    }

    public void makeSound() {
        System.out.println(sound);
    }
}
```

1. public: Members (fields, methods, classes) marked as public are accessible from any other class.
2. protected: Members marked as protected are accessible within the same package or by subclasses (even if they are in different packages).
3. private: Members marked as private are accessible only within the same class.

### Coupling

Coupling refers to the degree of direct knowledge that one element has of another. Use interfaces and dependency injection to reduce coupling.

### Dependency Injection:

A technique where one object supplies the dependencies of another object, promoting loose coupling.

## 3. Inheritance

- Allows a class to inherit properties and methods from another class.
- Constructors of the base class can be called in the derived class using super().

```java
public class UIControl {
    private boolean isEnabled = true;

    public void enable() {
        isEnabled = true;
    }

    public void disable() {
        isEnabled = false;
    }

    public boolean isEnabled() {
        return isEnabled;
    }

    public void render() {
        System.out.println("Rendering UIControl...");
    }
}

public class TextBox extends UIControl {
    private String text = "";

    public void setText(String text) {
        this.text = text;
    }

    public String getText() {
        return text;
    }
}
```

### Upcasting and Downcasting:

Refers to casting a subclass object to a superclass reference and vice versa.

```java
public class UpCastingDownCasting {
  public static void main(String[] args) {
    // var control = new UIControl(true);
    var textBox = new TextBox(true);
    // print(control);
    print(textBox);
  }

  public static void print(UIControl control) {// upcasting
    if (control instanceof TextBox) { // Checking if the UIControl is actually a TextBox
      var box = (TextBox) control; // downcasting
      box.setText("Hello world");
    }

    System.out.println(control);
  }
}
```

### Final Classes and Methods:

Prevent classes and methods from being inherited/overridden.

### Multiple Inheritance:

Java does not support multiple inheritance with classes to avoid complexity and diamond problem.

## 4. Polymorphism

Ability of an object to take on many forms. It's a core concept that allows one interface to be used for a general class of actions. We can implemenet using method overriding where a child class overrides a method of its parent class.

There are two main types of polymorphism:

### Compile-Time Polymorphism (Method Overloading):

Method overloading allows a class to have multiple methods with the same name but with different parameters. The decision about which method to call is made at compile-time based on the number and type of arguments provided. It enables the same method name to perform different actions depending on the context.

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```

### Run-Time Polymorphism (Method Overriding):

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. The decision about which method to call is made at runtime based on the type of the object.

```java
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}
```

###

Nested classes in Java are classes that are defined within another class.

```java
public class LinkedList {
  private class Node {
    private int value;
    private Node next;

    public Node(int value) {
      this.value = value;
    }
  }
  //
}
```

References:

1. https://codewithmosh.com/p/ultimate-java-part-2

![OOP certificate](https://raw.githubusercontent.com/mdpabel/notes/main/images/oop_certificate.png?token=GHSAT0AAAAAACQABTY5RUORULFPRT72R4R6ZQFW26A)
