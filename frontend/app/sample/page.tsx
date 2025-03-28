import ClientSample from "@/app/sample/client_sample";
import { listSample } from "@/app/sample/fetch_sample";
import { SamplePost } from "@/types/sample_post.type";

export default async function Page() {
  const posts: SamplePost[] = await listSample();
  return <ClientSample initialPosts={posts} />;
}

