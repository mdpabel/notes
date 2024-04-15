---
title: Graph Data Structure
description: Implementations of graph data structures in Java
date: 03-24-2024
status: draft
priority: 1
---

## Cli

1. Install Nest CLI:

```ts
npm install -g @nestjs/cli
```

2. Create a New NestJS Application:

```ts
nest new project-name
```

3. Generate Module, Controller, Service, and DTO

```ts
nest generate module entity
nest generate controller entity
nest generate service entity
nest generate class entity/dto/create-dto
nest generate class entity/dto/update-dto
nest g class events/entities/event.entity --no-spec --flat
```

4. nest g resource command not only generates all the NestJS building blocks (module, service, controller classes) but also an entity class, DTO classes as well as the testing (.spec) files.

```ts
nest g resource
```

5. Run Your Application

```ts
npm run start:dev
```

## CRUD

1. The @Module() decorator in NestJS is used to define a module.

2. We define a Controller using the @Controller() decorator and specify the route prefix for all endpoints related to this controller using the 'coffees' string.

3. @Get(), @Post(), @Put(), and @Delete() decorators are used to define HTTP methods for CRUD operations.

4. @Body() decorator is used to extract the request body, and @Param() decorator is used to extract parameters from the request URL.

5. We inject the EntityService into the constructor using dependency injection to handle business logic.

6. We specify DTOs (Data Transfer Objects) for data validation and entity creation/update.

- coffees.module.ts

```ts
import { Module } from '@nestjs/common';
import { CoffeesController } from './coffees.controller';
import { CoffeesService } from './coffees.service';

@Module({
  controllers: [CoffeesController],
  providers: [CoffeesService],
})
export class CoffeesModule {}
```

- coffees.controller.ts

```ts
import {
  Controller,
  Get,
  Param,
  Post,
  Body,
  HttpStatus,
  HttpCode,
  Patch,
  Delete,
  Query,
} from '@nestjs/common';
import { CoffeesService } from './coffees.service';
import { CreateCoffeeDto } from './dto/create-coffee.dto';
import { UpdateCoffeeDto } from './dto/update-coffee.dto';

@Controller('coffees')
export class CoffeesController {
  constructor(private readonly coffeesService: CoffeesService) {}

  @Get('/')
  findAll(@Query() query) {
    const { limit, offset } = query;
    // Retrieve all coffees
  }

  @Get('/:id')
  @HttpCode(HttpStatus.OK)
  findOne(@Param('id') id: number) {
    // Retrieve a specific coffee by ID
  }
}
```

- coffees.service.ts

```ts
import { Injectable, NotFoundException } from '@nestjs/common';
import { CoffeeEntity } from './entities/coffee.entity';
import { CreateCoffeeDto } from './dto/create-coffee.dto';
import { UpdateCoffeeDto } from './dto/update-coffee.dto';

@Injectable()
export class CoffeesService {
  private coffees: CoffeeEntity[] = [];

  // Method to retrieve all coffees
  findAll() {}

  // Method to retrieve a coffee by ID
  findOne(id: number) {}
}
```

## DTO (Data Transfer Object):

DTOs are plain TypeScript classes used to define the structure of data transferred between different parts of the application, such as between the client and server.

1. CreateCoffeeDto defines the structure for creating a new coffee entity.

2. UpdateCoffeeDto extends PartialType(CreateCoffeeDto), creating a new class with all properties of CreateCoffeeDto set to optional.

3. ValidationPipe is used globally in the main.ts file to validate incoming data based on decorators like @IsString() from the class-validator package.

- whitelist: true: Only allows properties with decorators (validation rules) in DTO objects, stripping any extra properties.
- forbidNonWhitelisted: true: Rejects requests with properties not defined in DTO classes, enhancing security.
- transform: true: Automatically transforms incoming data to match DTO types, simplifying data handling.

```ts
// create-coffee.dto.ts
import { IsString } from 'class-validator';

export class CreateCoffeeDto {
  @IsString()
  readonly name: string;
  // ----
}

// update-coffee.dto.ts
import { PartialType } from '@nestjs/mapped-types';
import { CreateCoffeeDto } from './create-coffee.dto';

export class UpdateCoffeeDto extends PartialType(CreateCoffeeDto) {}

// main.ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(
    new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
    }),
  );
  await app.listen(3000);
}

bootstrap();
```
