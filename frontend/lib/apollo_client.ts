import { ApolloClient, HttpLink, InMemoryCache } from '@apollo/client';

const ENDPOINT = process.env.NEXT_PUBLIC_GRAPHQL_ENDPOINT || 'http://localhost:8040/graphql/';

const client = new ApolloClient({
  link: new HttpLink({ uri: ENDPOINT }),
  cache: new InMemoryCache(),
});

export default client;