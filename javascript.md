---
title: Javascript
description: Javascript
date: 03-24-2024
status: JavaScript Concepts like Prototypes, Symbols, Generators and More
priority: 1
---

## Eexecution contexts

Whenever any JavaScript code is executed, it is executed inside an environment. This environment is known as the
**Execution Context**. Every time any JavaScript code is executed, an execution context is created
before its execution.

- Global execution context
- Function execution context

### Global execution context

Global code, i.e., the code that is not inside a function, is executed inside a global execution context.

- The global context contains the global variables, functions, etc.
- A reference to the outer environment, in the case of a global execution context, is null.
- Referennce to the outer environment, In the case of a global context, there is no outer environment, so reference to the outer environment is set to null.

### Function execution context

Every time a JavaScript function is called, a new execution context is created for the execution of that function. Just like the global execution context, the function execution context contains:

- The variables and functions are declared inside the function.
- The value of **this** inside the function for the current function call.
- A reference to the outer environment.

## Execution context phases

- Creation phase
- Execution phase

### Creation phase

The execution contexts (global and function) are created during the creation phase. During this phase,

- The variable declarations and references to functions are saved as key-value pairs inside the execution context. - The value of this and a reference to the outer environment are also set during this phase.

- The values for variables are not assigned during the creation phase.
- Variables declared using var are assigned undefined
- Variables declared using let or const are left uninitialized.

### Lexical and Variable environments

During the creation phase, the following two components are created:

- Variable environment: The variable environment only holds the key-value mappings of variables declared with the var keyword.
- Lexical environment: The function declarations and variables declared with let or const are inside the lexical environment.

Lexical and Variable environments are structures that are used internally to hold key-value mappings of variables, functions, reference to the outer environment, and the value of this.

```javascript
let name = 'A';
var age = 20;

function greet(name, age) {
  console.log('Hello, I am ' + name + ' and I am ' + age + ' years old');
}
```

Here,
**Lexical environment holds:**

```bash
name : uninitialized
greet: reference to greet function
outerEnvironment: null
this: Global object
```

**Variable environment holds:**

```bash
age: undefined,
outerEnvironment: null
this: Global object
```

### Execution phase

Different variables in the execution context are yet to be assigned their respective values. Assignments are done during the execution phase, and the code is finally executed.

**A call stack is a structure that is used internally by the JavaScript engine to keep track of the piece
of code that is currently executing.**

- Before executing any JavaScript code, a global execution context is created and pushed on the call
  stack.

```javascript
const A = () => console.log('hello world');
const B = () => A();
const C = () => B();
C();
```

```bash
Call Stack:

1. C()
2. B()
3. A()
```

1. C() is called first, so it's added to the stack.
2. Inside C(), B() is called, so it's added to the stack.
3. Inside B(), A() is called, so it's added to the stack.
4. Once A() completes, it's popped off the stack.
5. B() then completes, and it's popped off the stack.
6. Finally, C() completes, and it's popped off the stack.

## Hoisting

Hoisting in JavaScript is a process in which all the Variables, Functions and Class defination are declared BEFORE execution of the code. Variables are initialised to UNDEFINED when they are declared and the function’s name is registered as a variable in the scope containing the function declaration, and it is initialized with the function itself.

### var declarations

Hoisting in JavaScript allows variables and functions to be accessed before they are actually declared within their respective scopes. This behavior occurs because JavaScript preprocesses the code before executing it.

For example, if you have this code:

```js
console.log(result); // undefined
var result = 5 + 10;
```

During preprocessing, JavaScript treats **var result;** as if it's at the beginning of the scope. So, **console.log(result)** doesn't raise an error but logs undefined, as result has been declared but not yet assigned a value. Later in the code, result is assigned the value of 5 + 10, making it 15.

This is made possible because of the parsing step before the code is executed. The preprocessing of the JavaScript code before its execution allows the JavaScript engine to detect some errors early before any code is executed. The following code example shows this in action:

```js
function print(obj) {
  console.log(obj; // error
}
console.log("hello world");
```

In this code, there's a syntax error in the print function due to a missing closing parenthesis. Normally, if a function isn't called, JavaScript doesn't check its syntax errors until it's invoked. So, you might expect the code to log "hello world" without throwing any errors.
However, JavaScript's preprocessing detects syntax errors as it scans the code before execution.

### Function declarations

The function’s name is registered as a variable in the scope containing the function declaration, and it is initialized with the function itself.

```js
a();
function a() {}
```

### Class declarations

Like function declarations, class declarations are also hoisted, while we can access a function declaration before its declaration, we cannot do the same in the case of class declarations

```js
const A = 'TEST';

if (true) {
  console.log(A); // ReferenceError: Cannot access 'A' before initialization

  class A {}
}
```

If the class declarations weren’t hoisted, then the console.log function call should have logged "TEST" to the console, but that isn’t the case, and that is because the class declaration inside the if block is hoisted and any code, before or after the class A declaration inside the block, that accesses class A will access the class declaration and not the A variable declared above the if statement.

In JavaScript, class declarations themselves are not hoisted in the same way that function declarations are. However, the identifiers (class names) of class declarations are hoisted within the block scope. This means you can reference the class name before its declaration, but not its content.

So, if class declarations are hoisted, then why can’t we access them before their declaration? The answer to this question is the “Temporal Dead Zone (TDZ)”.

### Temporal Dead Zone

Temporal Dead Zone (TDZ)³⁵ is the area where the variables (let, const) or class declarations cannot be accessed. It starts from the start of the scope till the declaration is executed.

```js
// TDZ start
console.log('TEST');

let num = 1; // TDZ end
// can access the num after TDZ ends
```

As TDZ also applies to the let and const, are the variables declared using let or constants using const also hoisted? Yes, they are also hoisted, but, like the class declarations, they are hoisted differently because of the TDZ.

```js
const A = 'Outside';

if (true) {
  console.log(A); // ReferenceError: Cannot access 'A' before initialization

  const A = 'Inside';
}
```

### Function and class expressions

The function and class expression are not hoisted.

```js
console.log(A); // undefined
console.log(new A()); // TypeError: A is not a constructor

var A = class {};
```

We can access them before their declaration, and their value are undefined. This is because only the declarations are hoisted, not their values.
