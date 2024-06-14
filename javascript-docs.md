---
title: Javascript
description: Javascript
date: 03-24-2024
status: draft
priority: 1
---

## Table of contents

## JavaScript Data Types:

1. Primitive:
   - Examples: numbers, strings, booleans, undefined, null, symbols.
   - Characteristics: Immutable, directly hold a value.
     When we say that primitives in JavaScript are immutable, it means that once a primitive value is assigned to a variable, that value cannot be changed. Instead, any operation that appears to modify the value actually creates a new value.
2. Reference:
   - Examples: objects, arrays, functions.
   - Characteristics: Mutable, hold a reference to a value.

## Floating-Point Arithmetic: Why 0.2 + 0.1 != 0.3

In JavaScript and other languages, we use floating-point arithmetic for decimal math. But computers struggle to represent decimal numbers perfectly in binary. This leads to small errors when working with numbers like 0.1 and 0.2.

Under the hood, the JavaScript engine converts these decimal numbers into their binary representations, performs the addition operation on the binary representations, and then converts the result back into decimal format. However, due to the limited precision of floating-point numbers in JavaScript (typically using 64-bit double-precision format), the result may not be exactly what we expect.

```js
   0.001100110011... (0.2) // Binary Representation of 0.2
+  0.0001100110011... (0.1) // Binary Representation of 0.1
-----------------------
=  0.010011001100... (≈ 0.30000000000000004) // Converted back into decimal format
```

## Variable Declaration: const, let, var:

1. const:
   - Characteristics: Block-scoped, immutable variable declaration.
   - Scope: Block-level.
   - Usage: Preferable for variables that do not need reassignment.
2. let:
   - Characteristics: Block-scoped, mutable variable declaration.
   - Scope: Block-level.
   - Usage: Suitable for variables that need reassignment within the same block.
3. var:
   - Characteristics: Function-scoped, mutable variable declaration.
   - Scope: Function-level.
   - Usage: Historically used but has issues with hoisting and scope.

## Passing Mechanisms: Value vs Reference:

1. Value:
   - Passing a copy of the variable's value.
   - Changes to the parameter inside the function do not affect the original variable.
   - Example: Passing a primitive type like a number or string.
2. Reference:
   - Passing a reference to the variable itself.
   - Changes to the parameter inside the function affect the original variable.
   - Example: Passing objects, arrays, or functions.
   - Modifications made to the object, array, or function inside the function will reflect outside the function as well.

## Array Methods: map(), filter(), reduce(), forEach():

1. map():
   - Characteristics: Creates a new array by applying a function to each element.
   - Usage: Transforming each element of an array.
2. filter():
   - Characteristics: Creates a new array with elements that pass a certain condition.
   - Usage: Filtering out elements based on a condition.
3. reduce():
   - Characteristics: Reduces an array to a single value by applying a function to each element.
   - Usage: Aggregating values of an array into a single result.
4. forEach():
   - Characteristics: Executes a provided function once for each array element.
   - Usage: Iterating through each element of an array.

## Falsy Values in JavaScript:

- Values that evaluate to false in a Boolean context: false, 0, "", null, undefined, NaN.

## Comparison Operators: == vs ===:

- == checks for equality after type coercion. It converts the operands to the same type before comparing.
- === checks for equality without type coercion. It compares both the value and the type of the operands without any conversion.

## JavaScript Coercion: Example "3 + 2 + '7'":

- In JavaScript, when the + operator is used with strings, it performs concatenation.

```js
> 3 + 2 + '7'
'57'
```

## Using Strict Mode in JavaScript:

- Enables stricter parsing and error handling to prevent common coding mistakes.
- Example:

  ```javascript
  // Without strict mode
  x = 10; // This creates a global variable 'x' unintentionally

  // With strict mode
  ('use strict');
  y = 20; // This will throw a ReferenceError: y is not defined
  ```

## Anonymous Functions:

- Functions without a name, often used as arguments to other functions or as immediately invoked function expressions (IIFE).
- Example:

  ```javascript
  // Anonymous function as an argument
  setTimeout(function () {
    console.log('This is an anonymous function.');
  }, 1000);

  // Immediately Invoked Function Expression (IIFE)
  (function () {
    console.log('This is an immediately invoked anonymous function.');
  })();
  ```

## Callback Functions:

- Functions passed as arguments to other functions, executed later, often asynchronously.

## Creating Empty Arrays:

- Arrays can be created using [], new Array(), or Array(length).

## Differences: undefined, null, and undeclared:

- undefined: Variable declared but not initialized.
- null: Represents intentional absence of any object value.
- Undeclared: Variable not declared at all in the current scope.

## The 'instanceof' Operator:

- Checks if an object is an instance of a particular class or constructor function.

## NaN (Not-a-Number):

- Special value returned when a mathematical operation is undefined, represents an invalid number.

## 'this' in JavaScript:

In JavaScript, the keyword this refers to the object that a function is a method of. Think of this as a way for functions to talk about the object they belong to. Here’s how it works:

- **In an object method**: this refers to the object. For example, in person.sayName(), this would refer to person.
- **Alone or in a regular function**: this refers to the global object, which is window in browsers and global in Node.js.
- **In an event**: this refers to the element that received the event, like a button you clicked.
- **In a constructor function**: this refers to the new object being created.
- **With call() or apply() methods**: You can specify what this refers to.
- **In arrow functions**: this is lexically inherited from the outer function where the arrow function is defined. An arrow function captures the this value of the function's surrounding context at the time it is created.

```javascript
function Timer() {
  this.seconds = 0;
  setInterval(() => {
    this.seconds++;
    console.log(this.seconds);
  }, 1000);
}

new Timer();
```

- Arrow Function as Method:

```javascript
const obj = {
  value: 42,
  getValue: () => {
    console.log(this.value);
  },
};

obj.getValue(); // Output will not be 42 if run in a global context like a browser
```

## Hoisting

Hoisting refers to the behavior in JavaScript where variable and function declarations are moved to the top of their containing scope during the compilation phase before code execution begins.

- **var**: Variables declared with var are hoisted to the top of their function or global scope if declared outside of a function. The variable is initialized with a value of undefined until the execution reaches the line of code where the value is actually assigned.

- **let and const:** While technically hoisted as well, let and const declarations do not initialize their variables at the top of the block. Instead, they remain in a "temporal dead zone" (TDZ) from the start of the block until the line where they are declared, meaning they cannot be accessed in any way until they are officially declared.

- var: A variable declared with var at the global level becomes a property of the global object (window in a browser).

- let: A variable declared with let at the global level does not attach itself to the global object. It remains separate, which can lead to different behaviors when you're expecting properties to be accessible as global object properties.

```javascript
Type ".help" for more information.
> let a = 1
undefined
> global.a
undefined
> var b = 1
undefined
> global.b
1
```

```javascript
var value = 10; // `value` is hoisted and attached to `window`

const obj = {
  value: 42,
  getValue: () => {
    console.log(this.value);
  },
};

obj.getValue(); // Outputs 10 because `this.value` refers to `window.value`
```

With var, since value is attached to the window object, this.value inside the arrow function resolves to window.value. In contrast:

```javascript
let value = 10; // `value` is in a temporal dead zone, then available but not on `window`

const obj = {
  value: 42,
  getValue: () => {
    console.log(this.value);
  },
};

obj.getValue(); // Outputs `undefined` in a browser, because `this.value` doesn't refer to `window.value`
```

If the arrow function is at the top level of your script (not inside any other function), then this inside the arrow function will refer to window because that's the global environment in a browser.

## Closure:

A closure in JavaScript is like a backpack that a function carries around wherever it goes. This backpack holds all the variables that were in scope when the function was created. Even after the outer function has finished running, the function still remembers and has access to these variables through its backpack.

```javascript
function createGreeting(greeting) {
  return function (name) {
    console.log(greeting + ', ' + name);
  };
}

const sayHello = createGreeting('Hello');
sayHello('Alice'); // Outputs: Hello, Alice
sayHello('MD'); // Outputs: Hello, MD
```

## Immediately Invoked Function Expressions (IIFE):

An Immediately Invoked Function Expression (IIFE) is a JavaScript function that runs as soon as it's defined.

```javascript
(function () {
  console.log('This function is invoked immediately!');
})();
```

## for-in, for-of, and traditional for

1. for-in loop: This loop iterates over the enumerable properties of an object. It's commonly used to iterate over the keys of an object.

This behavior can lead to unexpected results if the array object has been extended or modified with additional properties or methods. For example, if you or a library added properties or methods to the Array prototype, they would also be iterated over in a for-in loop, which is usually not the intended behavior when looping over array elements.Example:

```js
const arr = [1, 2];

Array.prototype.add = () => {};

for (const item in arr) {
  console.log(item); // // Output: 0, 1, add
}
```

2. for-of loop: Iterates over iterable objects, like arrays, strings, maps, and sets, accessing their values directly.

3. Traditional for loop: commonly used for iterating over arrays by index.

## Higher Order Functions and First-Class Functions

**First-Class Functions**: They can be passed around as values, assigned to variables, and returned from other functions.

**Higher-Order Functions**: Higher-order functions are functions that either take one or more functions as arguments or return a function as a result.

## functions are objects

In JavaScript, functions are objects, which means they can have properties and methods just like any other object.

```javascript
// Define a function
function greet(name) {
  console.log('Hello, ' + name + '!');
}

// Add a property to the function object
greet.language = 'English';

// Add a method to the function object
greet.sayHelloInLanguage = function (language) {
  if (language === 'English') {
    console.log('Hello!');
  } else if (language === 'Spanish') {
    console.log('¡Hola!');
  } else {
    console.log('Language not supported.');
  }
};

// Call the function
greet('John'); // Output: Hello, John!

// Access the property
console.log(greet.language); // Output: English

// Call the method
greet.sayHelloInLanguage('Spanish'); // Output: ¡Hola!
```

## AJAX

AJAX stands for Asynchronous JavaScript and XML. It's a technique used in web development to send and receive data from a server asynchronously without reloading the entire page. Instead, AJAX allows for the updating of parts of a web page without disrupting the user experience

In JavaScript, AJAX is typically implemented using the XMLHttpRequest object or more modern APIs like the fetch API. With AJAX, we can make HTTP requests to a server from our client-side code, typically in response to user actions or other events.

```javascript
const response = await fetch('https://api.example.com/data');
```

## Event delegation

Event delegation is a concept in JavaScript where instead of attaching event listeners to individual elements, you attach a single event listener to a parent element. This parent element then listens for events that bubble up from its descendants. When an event occurs, you can determine the target element and handle the event accordingly.

```html
<body>
  <ul id="item-list">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>

  <script>
    // Get the parent container
    const itemList = document.getElementById('item-list');

    // Add event listener to the parent container
    itemList.addEventListener('click', function (event) {
      // Check if the clicked element is an <li> element
      if (event.target.tagName === 'LI') {
        // Handle the click event
        console.log('Clicked on:', event.target.textContent);
      }
    });
  </script>
</body>
```

## Iterable

```ts
class Node {
  val: number;
  next: Node | null;

  constructor(val: number) {
    this.val = val;
    this.next = null;
  }
}

class LinkedList {
  root: Node | null;

  constructor() {
    this.root = null;
  }

  add(item: number) {
    let node = this.root;

    if (node === null) {
      this.root = new Node(item);
      return;
    }

    let temp = node;

    while (node != null) {
      temp = node;
      node = node.next;
    }

    temp.next = new Node(item);
  }

  // iterable;
  [Symbol.iterator]() {
    let node = this.root;
    return {
      next() {
        if (node) {
          const value = node.val;
          node = node.next;
          return {
            value: value,
            done: false,
          };
        } else {
          return {
            value: null,
            done: true,
          };
        }
      },
    };
  }
}

const list = new LinkedList();

list.add(1);
list.add(2);
list.add(3);

for (const item of list) {
  console.log(item);
}

export {};
```
