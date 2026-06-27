---
title: Setting up Apollo Client | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/guides/websockets-and-subscriptions/setting-up-apollo-client/index
  md: https://docs.gethealthie.com/guides/websockets-and-subscriptions/setting-up-apollo-client/index.md
---

1. First, install the necessary dependencies and import them.

   * [ npm](#tab-panel-2)
   * [ yarn](#tab-panel-3)

   Install Dependencies

   ```
   npm install @rails/actioncable graphql-ruby-client
   ```

   Install Dependencies

   ```
   yarn add @rails/actioncable graphql-ruby-client
   ```

2. Next, let’s import all necessary modules

   ```
   import { ApolloClient, HttpLink, InMemoryCache, split } from '@apollo/client';
   import { getMainDefinition } from '@apollo/client/utilities';


   import * as ActionCable from '@rails/actioncable';
   import ActionCableLink from 'graphql-ruby-client/subscriptions/ActionCableLink';
   ```

3. Then define API endpoints. Please make sure to provide your API token to the WebSocket URL.

   ```
   const API_ENDPOINT = 'https://api.gethealthie.com/graphql';


   const WS_ENDPOINT = 'wss://ws.gethealthie.com/subscriptions?token=<YOUR_TOKEN_HERE>';
   ```

4. Use the HTTP Link as usual. Customize it to your needs, e.g. proivide authorization headers.

   ```
   const httpLink = new HttpLink({
     uri: API_ENDPOINT,
     headers: {
       // ...
     },
   });
   ```

5. Now, let’s use our Action Cable to configure the Websocket Link for Apollo Client.

   ```
   const cable = ActionCable.createConsumer(WS_ENDPOINT);
   const wsLink = new ActionCableLink({ cable });
   ```

6. Lastly, configure a split based on the operation type. We still want to send regular queries and mutations via the HTTP instead of Websockets.

   ```
   const link = split(
     // split based on operation type
     ({ query }) => {
       const { kind, operation } = getMainDefinition(query);
       return kind === 'OperationDefinition' && operation === 'subscription';
     },
     wsLink,
     httpLink
   );


   const client = new ApolloClient({
     link,
     cache: new InMemoryCache(),
   });
   ```

7. Your Apollo Client is ready to use.
