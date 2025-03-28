"use client";

import client from "@/lib/apollo_client";
import { ApolloProvider } from "@apollo/client";
import React, { type FC } from "react";

interface ProviderLayoutProps {
  children: React.ReactNode;
}

const ProviderLayout: FC<ProviderLayoutProps> = ({ children }) => (
  <ApolloProvider client={client}>{children}</ApolloProvider>
);

export default ProviderLayout;