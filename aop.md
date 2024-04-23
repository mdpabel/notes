---
title: Aspect-Oriented Programming (AOP)
description: Aspect-Oriented Programming in spring boot
date: 03-28-2024
isPublished: true
priority: 997
---

Aspect-Oriented Programming provides a way for us to inject code into existing functions or objects, without modifying the target logic.

To give you a good example, imagine having written your business logic but now you realize that you have no logging code. The normal approach to this would be to centralize your logging logic inside a new module and the go function by function adding logging information.

However, if you could grab that same logger and inject it into every method you’re looking to log, at very specific points during their execution with a single line of code, then this would definitely give you a lot of value. Wouldn’t you agree?

AOP (Aspect-Oriented Programming) in Spring Boot allows developers to modularize cross-cutting concerns, such as logging, security, transaction management, and error handling, separately from the business logic of the application. This approach promotes cleaner code by separating concerns and promoting reusability.

> AOP in Spring Boot can be compared to middleware in Express.js in some aspects. Both AOP in Spring Boot and middleware in Express.js serve similar purposes:

- Cross-cutting Concerns
- Separation of Concerns
- Interceptor Mechanism

However, there are some differences, AOP is a programming paradigm that focuses on modularizing cross-cutting concerns, while middleware is a specific implementation pattern commonly used in web frameworks like Express.js.

The key components of AOP in Spring Boot include:

- Aspects (What): These are the “aspects” or behavior you’re looking to inject into your target code. In Spring Boot, aspects are typically defined as Java classes annotated with @Aspect.
- Advice (When): When do you want the aspect to run? They specify some common moments when you want your aspect’s code to be executed, such as “before”, “after”, “around”, “whenThrowing”, and the like. . In Spring Boot, advice methods are annotated with @Before, @After, @Around, @AfterReturning, or @AfterThrowing.
- Join Point: A join point is a point during the execution of the application where an aspect can be plugged in. In Spring Boot, join points are method invocations.
- Pointcut (Where): They reference the place in your target code where you want to inject the aspect. In Spring Boot, pointcuts are defined using expressions, such as method signatures or regular expressions.

```java
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println("Logging before method: " + joinPoint.getSignature().getName());
    }

    @After("execution(* com.example.service.*.*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Logging after method: " + joinPoint.getSignature().getName());
    }
}
```

- @Aspect marks the class as an aspect.
- @Before and @After are advice annotations specifying the pointcuts where the advice methods should be executed.
- execution(\* com.example.service._._(..)) is a pointcut expression targeting all methods in the com.example.service package.
- JoinPoint is a parameter of advice methods, providing metadata about the method being intercepted.

### Resources:

1. https://blog.bitsrc.io/aspect-oriented-programming-in-javascript-c4cb43f6bfcc
2. https://docs.spring.io/spring-framework/reference/core/aop.html
3. https://www.udemy.com/course/spring-5-with-spring-boot-2/
