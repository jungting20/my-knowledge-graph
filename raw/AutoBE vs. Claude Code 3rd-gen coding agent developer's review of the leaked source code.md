---
title: "AutoBE vs. Claude Code: 3rd-gen coding agent developer's review of the leaked source code"
source: "https://dev.to/samchon/agentica-do-you-know-function-then-youre-ai-developer-1d9d"
author:
published: 2025-04-29
created: 2026-04-13
description: "TL;DR   Claude Code—source code leaked via an npm incident    while(true) + autonomous selection of... Tagged with ai, claudecode, opensource, programming."
tags:
  - "clippings"
---
> ## Summary
> 
> [![Agentica Banner](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdt9pe47p8xcokxh2feli.png)](https://github.com/wrtnlabs/agentica)
> 
> [Agentica](https://github.com/wrtnlabs/agentica) is a TypeScript AI framework specialized in Function Calling.
> 
> By simply listing functions, you can create an AI agent more easily than with any other AI framework, while maintaining a stable and flexible structure.
> 
> When you plug a TypeScript class into [Agentica](https://github.com/wrtnlabs/agentica), its functions are appropriately called by AI Function Calling. If you bring in React Native's Mobile API functions, you can create a mobile assistant with higher quality than Apple's Siri.
> 
> Additionally, if you import a Swagger/OpenAPI document, [Agentica](https://github.com/wrtnlabs/agentica) will appropriately call your backend APIs, and even when integrating with MCP, its stability will be in a different league compared to other AI frameworks.
> 
> You no longer need to fear AI. Anyone who knows how to create functions can become an AI developer. Take on the challenge of building an AI agent with [Agentica](https://github.com/wrtnlabs/agentica).

## 1\. Preface

Do you know how to create TypeScript functions? You can become an AI developer right now.

Are you a backend server developer? You're already better prepared than most to be an AI developer.

Simply import and list functions from the three protocols below. That's all you need to do to develop an AI agent. [Agentica](https://github.com/wrtnlabs/agentica) is an AI Function Calling Framework that's easier and more powerful than any AI agent framework you've seen before.

- TypeScript Class
- Swagger/OpenAPI Document
- MCP (Model Context Protocol) Server
```
import { Agentica, assertHttpLlmApplication } from "@agentica/core";
import OpenAI from "openai";
import typia from "typia";

import { MobileFileSystem } from "./services/MobileFileSystem";

const agent = new Agentica({
  vendor: {
    api: new OpenAI({ apiKey: "********" }),
    model: "gpt-4o-mini",
  },
  controllers: [
    // functions from TypeScript class
    {
      protocol: "class",
      name: "filesystem",
      application: typia.llm.application<MobileFileSystem, "chatgpt">(),
      execute: new MobileFileSystem(),
    },
    // functions from Swagger/OpenAPI
    {
      protocol: "http",
      name: "shopping",
      application: assertHttpLlmApplication({
        model: "chatgpt",
        document: await fetch(
          "https://shopping-be.wrtn.ai/editor/swagger.json",
        ).then(r => r.json()),
      }),
      connection: {
        host: "https://shopping-be.wrtn.ai",
        headers: { Authorization: "Bearer ********" },
      },
    },
  ],
});
await agent.conversate("I wanna buy MacBook Pro");
```

## 2\. AI Function Calling

[![Function Calling](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5ejm9jx80xy3b2eh4qs3.webp)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5ejm9jx80xy3b2eh4qs3.webp)

[https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)

When developers provide functions, AI selects appropriate functions and fills in parameter values for execution. This is the core concept of AI Function Calling.

AI Function Calling is a technology announced by OpenAI in June 2023, and when it was released, many AI developers had exactly the same future vision as [Agentica](https://github.com/wrtnlabs/agentica).

Within a three-minute walk from where I lived at the time, there were three companies attempting to create Super AI Chatbots using AI Function Calling.

> In the future, developers only need to create functions. The AI agent will take care of everything else.
> 
> You no longer need to build complex UI applications directly, so developers, focus only on functions. Functions are the alpha and omega.
> 
> Can you make function? Then you're AI developer.

[![Agent Workflow](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fudl2ugu62nc2eoqdkydr.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fudl2ugu62nc2eoqdkydr.png)

However, due to the complexity of AI Function Calling specifications and low success rates in parameter value composition, AI Function Calling failed to become the mainstream in the AI agent development ecosystem.

Instead of general-purpose, easy-to-develop AI Function Calling, the trend shifted towards special-purpose Agent Workflows that require extensive design and development time but focus on specific applications.

Recently, MCP (Model Context Protocol) servers have become popular, but they face criticism due to instability, causing AI researchers to return to Agent Workflow development methodologies.

[![Orchestration Strategy](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftk83ask9bydojdw3uy49.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftk83ask9bydojdw3uy49.png)

Today, [Agentica](https://github.com/wrtnlabs/agentica) aims to revive that future vision from June 2023.

[Agentica](https://github.com/wrtnlabs/agentica) uses four strategies to resolve the complexity of AI Function Calling specifications and dramatically improve success rates, ushering in a new era of AI Function Calling that is universal, expandable, and easy for anyone to create—instead of inflexible, difficult-to-develop, specific-purpose Agent Workflows.

Can you make function? Then you're AI developer.

- [Compiler Driven Development](https://wrtnlabs.io/agentica/docs/concepts/compiler-driven-development/): constructs function calling schema automatically by compiler skills without hand-writing
- [JSON Schema Conversion](https://wrtnlabs.io/agentica/docs/core/vendor/#schema-specification): automatically handles specification differences between LLM vendors, ensuring seamless integration regardless of your chosen AI model.
- [Validation Feedback](https://wrtnlabs.io/agentica/docs/concepts/function-calling/#validation-feedback): detects and corrects AI mistakes in argument composition, dramatically reducing errors and improving reliability
- [Selector Agent](https://wrtnlabs.io/agentica/docs/concepts/function-calling/#orchestration-strategy): filtering candidate functions to minimize context usage, optimize performance, and reduce token consumption.

## 3\. TypeScript Class

```
import { Agentica } from "@agentica/core";
import OpenAI from "openai";
import typia from "typia";

import { BbsArticleService } from "./services/BbsArticleService";

const agent = new Agentica({
  vendor: {
    model: "gpt-4o-mini",
    api: new OpenAI({ apiKey: "********" }),
  },
  controllers: [
    {
      protocol: "class",
      name: "bbs",
      application: typia.llm.application<BbsArticleService, "chatgpt">(),
      execute: new BbsArticleService(),
    },
  ],
});
await agent.conversate("I want to write an article.");
```

![](https://www.youtube.com/watch?v=pdsplQyok8k)

If you want to create an AI agent with [Agentica](https://github.com/wrtnlabs/agentica), define the tasks the agent should perform as class functions. Then, configure the controller with [`typia.llm.application<BbsArticleService, Model>()`](https://typia.io/docs/llm/application) as shown in the source code above.

You can perform a series of actions like writing, editing, and viewing posts on a bulletin board through "conversation." You can call the functions of `BbsArticleService` through "conversation." This is precisely AI Function Calling, and what [Agentica](https://github.com/wrtnlabs/agentica) does best.  

```
import fs from "fs";

export class FileSystem {
  public __dirname(): string {
    return __dirname;
  }

  public readdir(input: {
    path: string;
    options?:
      | {
          encoding: "utf-8";
          withFileTypes?: false | undefined;
          recursive?: boolean | undefined;
        }
      | "utf-8"
      | null;
  }): Promise<string[]> {
    return fs.promises.readdir(input.path, input.options);
  }

  public readFile(input: { path: string }): Promise<string> {
    return fs.promises.readFile(input.path, "utf8");
  }

  public writeFileSync(input: { 
    file: string; 
    data: string;
  }): Promise<void> {
    return fs.promises.writeFile(input.file, input.data);
  }
}
```

If you provide a `FileSystem` class like the one above to [Agentica](https://github.com/wrtnlabs/agentica), you can perform a series of tasks such as organizing, deleting, and categorizing old files on your computer, all through AI conversation.

You can create an AI agent that controls all files on your computer through chat alone. And it takes only 5 minutes to build this.  

```
import { Agentica } from "@agentica/core";
import OpenAI from "openai";
import typia from "typia";

import { GmailService } from "@wrtnlabs/connector-gmail";
import { GoogleScholarService } from "@wrtnlabs/connector-google-scholar";
import { NaverNewsService } from "@wrtnlabs/connector-naver-news";
import { NotionService } from "@wrtnlabs/connector-notion";

const agent = new Agentica({
  vendor: {
    model: "gpt-4o-mini",
    api: new OpenAI({ apiKey: "********" }),
  },
  controllers: [
    {
      protocol: "class",
      name: "gmail",
      application: typia.llm.application<GmailService, "chatgpt">(),
      execute: new GmailService({
        clientId: "********",
        clientSecretKey: "********",
        refreshToken: "********",
      }),
    },
    {
      protocol: "class",
      name: "scholar",
      application: typia.llm.application<GoogleScholarService, "chatgpt">(),
      execute: new GoogleScholarService({
        serpApiKey: "serpApiKey",
      }),
    },
    {
      protocol: "class",
      name: "news",
      application: typia.llm.application<NaverNewsService, "chatgpt">(),
      execute: new NaverNewsService(),
    },
    {
      protocol: "class",
      name: "notion",
      application: typia.llm.application<NotionService, "chatgpt">(),
      execute: new NotionService({
        secretKey: "********",
      }),
    },
  ],
});
await agent.conversate("I want to write an article.");
```

Furthermore, if you provide multiple TypeScript classes like [`GoogleScholarService`](https://wrtnlabs.io/agentica/tutorial/productivity/google-scholar/), [`NaverNewsService`](https://github.com/wrtnlabs/connectors/tree/main/packages/naver_news), [`NotionService`](https://wrtnlabs.io/agentica/tutorial/productivity/notion/), and [`GmailService`](https://wrtnlabs.io/agentica/tutorial/productivity/gmail/) simultaneously, you can give much more complex instructions to your AI agent. If you want to create a versatile yet universal AI agent, simply add more functions like this.

The functions you provide determine the strategy of your AI agent.

> Analyze recent US economic trends and also summarize and comment on academic papers.
> 
> Then write this in a Notion document and email the link to these 3 people:
> 
> - [john.doe@gmail.com](mailto:john.doe@gmail.com)
> - [kildong.hong@gmail.com](mailto:kildong.hong@gmail.com)
> - [sunrabbit@wrtn.io](mailto:sunrabbit@wrtn.io)

## 4\. Mobile Application

```
import { Agentica, assertHttpLlmApplication } from "@agentica/core";
import OpenAI from "openai";
import typia from "typia";

import { MobileFileSystem } from "./services/MobileFileSystem";

const agent = new Agentica({
  vendor: {
    api: new OpenAI({ apiKey: "********" }),
    model: "gpt-4o-mini",
  },
  controllers: [
    {
      type: "class",
      name: "battery",
      application: typia.llm.application<ReactNativeBattery, "chatgpt">(),
      execute: new ReactNativeBattery(),
    },
    {
      type: "class",
      name: "sms",
      application: typia.llm.application<ReactNativeSMS, "chatgpt">(),
      execute: new ReactNativeSMS(),
    },
    {
      type: "class",
      name: "gallery",
      application: typia.llm.application<ReactNativeGallery, "chatgpt">(),
      execute: new ReactNativeGallery(),
    }
  ]
});
await agent.conversate("How much my battery left?");
```

![](https://www.youtube.com/watch?v=18TyKUl7Tok)

If you want to build something like Apple's Siri, wrap the Mobile API functions from React Native. You can create an AI agent that's much more stable, superior, and versatile than Apple's Siri right now.

The application and video above were created by a 20-year-old developer colleague. Fresh out of high school, when asked to create a mobile application like Apple's Siri, he did it in just 20 minutes.

AI agent development is very easy. Just bring in the functions. That's all there is to it.

- Made by [Jaxtyn](https://github.com/kimulchan), 20yo developer
- React Native Function Calling Tutorial: [https://wrtnlabs.io/agentica/tutorial/react-native/sms/](https://wrtnlabs.io/agentica/tutorial/react-native/sms/)

## 5\. Swagger/OpenAPI Document

If you're a backend developer, you're already optimized for AI development.

You analyze requirements to design API specifications, create API documentation to share with front-end/client developers, and provide various explanations and examples to help them better understand your APIs. Now, do the same for your AI agent.

The AI agent you create will be more stable, superior, and useful than anything else.

Below is a case of turning a shopping mall backend server into an AI agent. All that was done was providing [Agentica](https://github.com/wrtnlabs/agentica) with the shopping mall backend's `swagger.json` file. This shopping mall consists of 289 API functions, and amazingly, the AI agent understands them all and calls the most appropriate function through the context of the conversation with the user, explaining everything along the way.

Actually, as a full-stack developer, I'm not a professional backend developer. If an AI agent based on my backend server works this well, one made by professionals like you will be even better.

Backend developers, take on the challenge of AI agents. You're already the best.

- Shopping mall backend project: [https://github.com/samchon/shopping-backend](https://github.com/samchon/shopping-backend)
- Shopping mall `swagger.json` file: [https://shopping-be.wrtn.ai/editor/swagger.json](https://shopping-be.wrtn.ai/editor/swagger.json)
- Shopping mall AI agent demo: [https://wrtnlabs.io/agentica/playground/shopping](https://wrtnlabs.io/agentica/playground/shopping)
- Swagger Playground: [https://wrtnlabs.io/agentica/playground/uploader](https://wrtnlabs.io/agentica/playground/uploader)
```
import { Agentica } from "@agentica/core";
import { HttpLlm, OpenApi } from "@samchon/openapi";
import typia from "typia";

const agent = new Agentica({
  model: "chatgpt",
  vendor: {
    api: new OpenAI({ apiKey: "*****" }),
    model: "gpt-4o-mini",
  },
  controllers: [
    {
      protocol: "http",
      name: "shopping",
      application: HttpLlm.application({
        model: "chatgpt",
        document: await fetch(
          "https://shopping-be.wrtn.ai/editor/swagger.json",
        ).then((r) => r.json()),
      }),
      connection: {
        host: "https://shopping-be.wrtn.ai",
        headers: {
          Authorization: "Bearer *****",
        },
      },
    },
  ],
});
await agent.conversate("I want to buy a MacBook Pro");
```

![](https://www.youtube.com/watch?v=RAzYo02HTXA)

## 6\. MCP Server

![](https://www.youtube.com/watch?v=jk54TBqJTOQ)

> Github MCP on Claude Desktop breaks down too much

MCP (Model Context Protocol) is currently trending. However, it simultaneously receives much criticism for its instability. But I'd like to counter: it's not MCP that's wrong, but the AI agent applications using it.

The same Github MCP server, when called through Claude Desktop, breaks down in eight out of ten cases without even knowing why. However, when integrating Github MCP with Agentica, it succeeds 100% of the time. The Github MCP has only about 30 functions, but Agentica works well even when the number of functions increases to 300 or 400.

![](https://www.youtube.com/watch?v=rLlHkc24cJs)

> 100% working Github agent by function calling with [Agentica](https://github.com/wrtnlabs/agentica)  

```
import { Agentica, assertMcpController } from "@agentica/core";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client({
  name: "shopping",
  version: "1.0.0",
});
await client.connect(new StdioClientTransport({
  command: "npx",
  args: ["-y", "@wrtnlabs/shopping-mcp"],
}));

const agent = new Agentica({
  model: "chatgpt",
  vendor: {
    api: new OpenAI({ apiKey: "********" }),
    model: "gpt-4o-mini",
  },
  controllers: [
    await assertMcpController({
      name: "shopping",
      model: "chatgpt",
      client,
    }),
  ],
});
await agent.conversate("I wanna buy a Macbook");
```

This is thanks to [Agentica](https://github.com/wrtnlabs/agentica) 's unique AI Function Calling strategies mentioned in Chapter 2, which enable [Agentica](https://github.com/wrtnlabs/agentica) to achieve 100% successful AI Function Calling.

MCP server developers, you too should validate and experiment with your MCP servers using [Agentica](https://github.com/wrtnlabs/agentica).

- [Compiler Driven Development](https://wrtnlabs.io/agentica/docs/concepts/compiler-driven-development/): constructs function calling schema automatically by compiler skills without hand-writing
- [JSON Schema Conversion](https://wrtnlabs.io/agentica/docs/core/vendor/#schema-specification): automatically handles specification differences between LLM vendors, ensuring seamless integration regardless of your chosen AI model.
- [Validation Feedback](https://wrtnlabs.io/agentica/docs/concepts/function-calling/#validation-feedback): detects and corrects AI mistakes in argument composition, dramatically reducing errors and improving reliability
- [Selector Agent](https://wrtnlabs.io/agentica/docs/concepts/function-calling/#orchestration-strategy): filtering candidate functions to minimize context usage, optimize performance, and reduce token consumption.

[![JSON Schema Specification](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcf8pd6g75yq85gf3hvs1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcf8pd6g75yq85gf3hvs1.png)