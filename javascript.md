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
