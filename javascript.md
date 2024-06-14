---
title: Javascript
description: JavaScript Concepts like Prototypes, Symbols, Generators and More
date: 03-24-2024
status: published
priority: 1
---

## Table of contents

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

## Scope

The scope refers to the parts of the program where a particular variable, function, etc., can be accessed.

- Global scope
- Function scope
- Block scope
- Module scope

### Lexical scope

In JS, the scope is determined at compile time. This means that before the step-by-step execution of the JavaScript code starts, JavaScript engines determine the scopes of different declarations in the code. Scopes can be nested within other scopes, with each nested scope having access to the outer or parent scope.

```js
const name = 'MD'; // variable declaration

// function declaration
function greet() {
  const message = `name ${name}`; // variable declaration
  console.log(message);
}
```

The scope of the above declarations depends on where they are written in the code structure above.

- The myName variable and hello function are both in global scope, so they are available globally in the above code.
- The message variable declaration is inside the greet function, so its a local variable of greet().

Lexical scope is the ability for a function scope to access variables from the parent scope.

**In JavaScript, the global scope is the browser window. Variables created using the var keyword or function declarations declared in the global scope are added as properties on the window object**

```js
var name = 'A';
const age = 25;
function test() {}

window.hasOwnProperty('name'); // true
window.hasOwnProperty('test'); // true
window.hasOwnProperty('age'); // false
```

## Coercion

Type coercion is the automatic or implicit conversion of values from one data type to another (such as strings to numbers).

```js
console.log('20' - 10);
```

whereas type conversion involves explicitly converting data from one type to another.

```
Number("10")
```

Whenever JavaScript sees a value of one type in a context that expects a value of a different type, it tries to coerce or convert the value into the expected type. "20" is the unexpected value type because the operation is subtraction.

To deep dive into the world of coercion, let us understand the following:

- Abstract operations
- Abstract equality operator (==)
- Addition operation (+)
- Relational operators (<, >, <=, >=)

### Abstract operations:

There are many mechanisms that are used by the JavaScript language to convert one type of value into another type of value. These mechanisms are known as **abstract operations**. There are many abstract operations:

- ToPrimitive
- ToNumber
- ToString
- ToBoolean

#### ToPrimitive :

The ToPrimitive abstract operation is used to convert an object to a primitive value. This operation takes two arguments:

- input: an object that should be converted into a primitive value
- preferredType: an optional second argument that specifies the type that should be favored when converting an object into a primitive value.

This operation invokes another abstract operation known as OrdinaryToPrimitive to do the actual conversion, and it also takes two arguments:

- O: an object that should be converted into a primitive value
- hint: a type that should be favored when converting an object to a primitive value

Each object in JavaScript inherits the following two methods from the object that sits at the top of the inheritance hierarchy, i.e., the Object.prototype object:

**toString( )**: The toString method is used to convert an object into its string representation.

**valueOf( )**: The valueOf method is used to convert an object into a primitive value.

The OrdinaryToPrimitive abstract operation invokes the toString and the valueOf methods to convert an object into a primitive value. **The hint argument received by the OrdinaryToPrimitive abstract operation determines which of these two methods is called first.**

##### Prefer string:

If the hint argument is “string”, then the OrdinaryToPrimitive abstract operation first invokes
the toString method on the object. if the toString method doesn’t return a primitive value, the valueOf method
will be invoked to get a primitive representation of the object. . otherwise, a TypeError is thrown, indicating that the object couldn’t be converted to a primitive value.

```js
const obj = {
  toString() {
    return 'abc';
  },
  valueOf() {
    return 123;
  },
};

console.log(`${obj}`); // abc
```

we are trying to log obj, embedded in a template literal, to the console. In this case, the obj will be converted into a string. Here the hint argument of the OrdinaryToPrimitive abstract operation is “string”.

The next case we need to verify is what happens if the toString method doesn’t return a primitive value. The following code example demonstrates this case.

```js
const obj = {
  toString() {
    return {};
  },
  valueOf() {
    return 123;
  },
};

console.log(`${obj}`); // 123
```

if the toString method doesn’t return a primitive value, the valueOf method will be invoked to get a primitive representation of the object.

The valueOf method is invoked even if the toString is not defined for an object.

```js
const obj = {
  toString: undefined,
  valueOf() {
    return 123;
  },
};

console.log(`${obj}`);
```

The last case we need to verify is what happens when JavaScript can’t get a primitive value, even after invoking the toString and the valueOf method.

```js
const obj = {
  toString() {
    return [];
  },
  valueOf() {
    return [];
  },
};

console.log(`${obj}`); // TypeError: Cannot convert object to primitive value
```

##### Prefer number:

If the hint argument is “number”, then the OrdinaryToPrimitive abstract operation first invokes the valueOf method and then the toString method, if needed.

```js
const obj = {
  toString() {
    return 'abc';
  },
  valueOf() {
    return 123;
  },
};

console.log(1 + obj); //124
```

What will happen if the valueOf method returns a boolean value? It is a primitive value. It is not a number but still a primitive value. So JavaScript should accept it as a primitive representation of the obj.

```js
const obj = {
  toString() {
    return 'abc';
  },
  valueOf() {
    return true;
  },
};

console.log(1 + obj); // 2
```

##### No preference

#### ToNumber

| Value     | ToNumber(value) |
| --------- | --------------- |
| ""        | 0               |
| "0"       | 0               |
| "-0"      | -0              |
| " 123 "   | 123             |
| "45"      | 45              |
| "abc"     | NaN             |
| false     | 0               |
| true      | 1               |
| undefined | NaN             |
| null      | 0               |

#### ToString

| Value     | ToNumber(value) |
| --------- | --------------- |
| null      | "null"          |
| undefined | "undefined"     |
| 0         | "0"             |
| -0        | "0"             |
| true      | "true"          |
| false     | "false"         |
| 123       | "123"           |
| NaN       | "NaN"           |

#### ToBoolean

falsy values:

- false
- 0, -0, 0n
- undefined
- null
- NaN
- ""

##### 0 == false

1. As the types are not equal and one of the operands is a boolean, the boolean operand is
   converted into a number using the ToNumber⁷⁴ abstract operation.
2. Now the types are equal (0 == 0)
3. Now the types are equal.

##### "" == false

1. The boolean operand false is converted into a number using the ToNumber abstract operation, resulting in 0.
   "" == 0
2. Recall that the abstract equality operator and string operand is converted into a number using the ToNumber abstract operation. "" converted to 0.
   0 == 0
3. Now the types are equal.

##### 0 == []

1. The array is converted into a primitive value using the ToPrimitive abstract operation.
   0 == ""
2. Next, the string will be converted into a number.
   0 == 0
3. Now the types are equal.

##### [123] == 123

1. The array is converted into a primitive value using the ToPrimitive abstract operation.
   '123' == 123
2. Next, the string will be converted into a number.
   123 == 123
3. Now the types are equal.

##### [1] < [2]

1. The array is converted into a primitive value using the ToPrimitive abstract operation.
   "1" < "2"
2. Now the types are equal. "1" < "2", giving us true as an output because the strings are compared using their Unicode code points.

##### [] == ![]

The Not operator has a higher precedence than the equality operator, so the subexpression ![] is evaluated first.

1. The Not operator converts true into false, and vice versa using toBoolean() abstract operation.
   [] == false
2. [] == 0
3. "" == 0
4. 0 == 0
5. true

##### !!"true" == !!"false"

the precedence of the logical Not operator is higher, so the sub-expressions !!"true" and !!"false" will be evaluatedfirst.

1. true == true (using the toBoolean() abstract operation)
2. true

##### [1, 2, 3] + [4, 5, 6]

1. "1,2,3" + "4,5,6"
2. "1,2,34,5,6"

##### [undefined] == 0

1. "" == 0
2. 0 == 0
3. true

##### [[]] == ''

JavaScript converts Arrays elements into strings and then joins them using commas. So, first the nested empty array will be converted into a primitive value (empty string). Then the outer array is also converted into an empty string.

1. "" == ""

##### [] + {}

1. "" == "[object object]"
2. "[object object]"

## Closures

The closure is a a function along with a reference to the environment in which it is created.

1. A function
2. A reference to the environment/scope in which that function is created

Closures allow a nested function to access the declarations inside the parent function, even after the execution of the parent function has ended.

```javascript
// https://leetcode.com/problems/memoize-ii/description/
function keyGenerator() {
  let count = 0;
  const map = new Map();

  return function (input) {
    if (map.has(input)) {
      return map.get(input);
    }
    map.set(input, ++count);
    return count;
  };
}

function memoize(fn) {
  const cacheKeyGenerator = keyGenerator();
  const cache = new Map();

  return function (...args) {
    const numbers = args.map(cacheKeyGenerator);
    const key = numbers.join(',');

    if (cache.has(key)) {
      return cache.get(key);
    }
    const result = fn(...args);
    cache.set(key, result);

    return result;
  };
}


let callCount = 0;
const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
  return a + b;
})
memoizedFn(2, 3) // 5
memoizedFn(2, 3) // 5
console.log(callCount) // 1

```

### Scope chain

When you reference a variable within a function, JavaScript searches for that variable in a series of nested scopes, starting from the innermost function scope and moving outward until it finds the variable or reaches the global scope. This process forms what is known as the scope chain.

```js
var globalVar = "I'm global";

function outerFunction() {
  var outerVar = "I'm outer";

  function innerFunction() {
    var innerVar = "I'm inner";
    console.log(innerVar); // Accessible here
    console.log(outerVar); // Accessible here
    console.log(globalVar); // Accessible here
  }

  innerFunction();
  console.log(innerVar); // Not accessible here
}

outerFunction();
console.log(outerVar); // Not accessible here
console.log(globalVar); // Accessible here
```

**How are different scopes linked?**
The answer is the hidden internal slot named [[Environment]] or [[Scope]].

This [[Environment]] or [[Scope]] internal slot exists on the functions, and it contains a reference to the outer
scope/environment. In other words, this internal slot contains a reference to the scope on which the
containing function has closed over or formed a closure.

In the code example above, when the outer function is created, as it is created in the global scope, a reference to the global environment is saved in the internal [[Environment]] slot of the function object.

```js
const a = 10;
function outer() {
  function inner() {
    console.log(a);
  }
  inner();
}
```

In this code example, we have three different environments:

1. global environment
2. local environment of outer function
3. local environment of inner function

```bash
   .-----------------------------------------------------------.
   |                  Global Environment                      |
   |                  [[Environment]]                         |
   |                  a: 10                                   |
   '-----------------------------------------------------------'
             |
             | [[OuterEnv]]
             |
   .-----------------------------------------------------------.
   |               Outer Function Environment                  |
   |               [[Environment]]                            |
   |               inner: function                            |
   '-----------------------------------------------------------'
             |
             | [[OuterEnv]]
             |
   .-----------------------------------------------------------.
   |               Inner Function Environment                  |
   |               [[Environment]]                            |
   '-----------------------------------------------------------'
```

### Closures in loop

```js
for (var i = 1; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 1000);
}
// output
// 3;
// 3;
// 3;
```

The callback function of each setTimeout forms a closure over the same variable i. As there are a total of two
loop iterations in our example, setTimeout is called three times, so we have two callback functions, all having a closure over the same variable i.

The callback function of each setTimeout call is invoked after the loop execution has completed. The value of variable i after the last iteration of the loop is “3”, and because each callback function of the “setTimeout” has a closure over the same variable i, all two of them see “3” as the value of the i. This is the reason they all log “3” on the console.

```bash
   .-----------------------------------------------------------.
   |                  Global Environment                      |
   |                  [[Environment]]                         |
   |                  i: 3                                    |
   |                  setTimeout1: function() {...}           |
   |                  setTimeout2: function() {...}           |
   |                  setTimeout3: function() {...}           |
   '-----------------------------------------------------------'
       |                             |
       | [[OuterEnv]]                |
       |                             |
   .-------------------------.       |
   |setTimeout1 Environment  |       |
   |    [[Environment]]      |       |
   |     i: 3                |       |
   '-------------------------'       |
                                     |
                                     | [[OuterEnv]]
                                     |
   .-----------------------------------------------------------.
   |        setTimeout2 Callback Function Environment          |
   |               [[Environment]]                             |
   |               i: 3                                       |
   '-----------------------------------------------------------'
```

**Solution: 1**
with the use of an IIFE, we can pass the value of i in each iteration to the IIFE as a parameter.This solves the problem because the counter parameter is closed over by each callback function, and in each iteration, a new IIFE is created, along with the new callback function of setTimeout.

```js
for (var i = 1; i < 3; i++) {
  ((counter) => {
    setTimeout(() => {
      console.log(counter);
    }, 1000);
  })(i);
}
```

```bash
   .------------------------------------------------.
   |               Global Environment               |
   |                 [[Environment]]                |
   |                 i: undefined                   |
   '------------------------------------------------'
             |                                 |
             | [[OuterEnv]]                    |
             |                                 |
   .------------------------------.            |
   |   IIFE Environment (i=1)     |            |
   |      [[Environment]]         |            |
   |       counter: 1             |            |
   '------------------------------'            |
           |                                   |
           | [[OuterEnv]]                      |
           |                                   |
   .-----------------------------------.       |
   |    setTimeout1 Environment        |       |
   |      [[Environment]]              |       |
   |      (Captures IIFE environment)  |       |
   |      counter: 1                   |       |
   '-----------------------------------'       |
                                               |
                                               | [[OuterEnv]]
                                               |
   .-----------------------------------------------------------.
   |          Anonymous Function Environment (i=2)             |
   |                  [[Environment]]                         |
   |                  counter: 2                               |
   '-----------------------------------------------------------'
                     |
                     | [[OuterEnv]]
                     |
   .-----------------------------------------------------------.
   |        setTimeout2 Callback Function Environment          |
   |               [[Environment]]                            |
   |               (Captures anonymous function environment)  |
   |               counter: 2                                 |
   '-----------------------------------------------------------'
```

**Solution: 2**
Using the let keyword solves this problem because, unlike each callback function closing over the same variable i, the let being block-scoped causes each iteration of the loop to have a different copy of the variable i.

```js
for (let i = 1; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 1000);
}
```
