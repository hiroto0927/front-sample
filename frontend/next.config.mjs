/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    HOST_RESOURCE_APP: "localhost",
    HOST_AUTH_APP: "localhost:81",
    PROTOCOL_AUTH_APP: "http",
  },
};

export default nextConfig;
