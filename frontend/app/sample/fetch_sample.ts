import client from "@/lib/apollo_client";
import { gql } from "@apollo/client";


const LIST_SAMPLE = gql`
  query listSample {
    listSample {
      id
      name
      message
    }
  }
`;

const NEW_SAMPLE = gql`
  mutation newSample($name: String!, $message: String!) {
    newSample(input: {name: $name, message: $message}) {
      id
      name
      message
    }
  }
`;

const UPDATE_SAMPLE = gql`
  mutation updateSample($id: ID!, $name: String!, $message: String!) {
    updateSample(input: {id: $id, name: $name, message: $message}) {
      id
      name
      message
    }
  }
`;

const DELETE_SAMPLE = gql`
  mutation deleteSample($id: ID!) {
    deleteSample(id: $id) {
      id
      name
      message
    }
  }
`;

export async function listSample() {
  const { data } = await client.query({ query: LIST_SAMPLE, fetchPolicy: "no-cache" });
  return data.listSample;
}

export async function newSample(name: string, message: string) {
  const { data } = await client.mutate({
    mutation: NEW_SAMPLE,
    variables: {
      name,
      message,
    },
  });
  return data.newSample;
}

export async function updateSample(id: string, name: string, message: string) {
  const { data } = await client.mutate({
    mutation: UPDATE_SAMPLE,
    variables: {
      id,
      name,
      message,
    },
  });
  return data.updateSample;
}

export async function deleteSample(id: string) {
  const { data } = await client.mutate({
    mutation: DELETE_SAMPLE,
    variables: {
      id,
    },
  });
  return data.deleteSample;
}