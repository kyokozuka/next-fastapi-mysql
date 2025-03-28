"use client";
import "@/app/sample/sample.module.css";
import styles from "@/app/sample/sample.module.css";
import { SamplePost } from "@/types/sample_post.type";
import { useState } from "react";

export default function ClientSample({ initialPosts }: { initialPosts: SamplePost[] }) {
  const [inputValue, setInputValue] = useState("");
  const [posts, setPosts] = useState<SamplePost[]>(initialPosts);
  const userAccount = "sample_user";

  const listSamples = async () => {
    try {
      const res = await fetch("/api/sample/list");
      if (!res.ok) {
        throw new Error("Failed to fetch samples");
      }
      const data = await res.json();
      setPosts(data);
    } catch (error) {
      console.error("Error fetching samples:", error);
    }
  };

  const customerFetch = async (url: string, method: string, body: any) => {
    try {
      const res = await fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: body,
      });
      if (!res.ok) {
        throw new Error("Failed to fetch");
      }
      const data = await res.json();
      return data;
    }
    catch (error) {
      console.error("Error in custom fetch:", error);
      throw error;
    }
  };

  const handleNewSample = async (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    if (inputValue.trim() === "") return;
    const body = JSON.stringify({
      name: userAccount,
      message: inputValue,
    })
    await customerFetch("/api/sample/new", "POST", body);
    await listSamples();
    setInputValue("");
  };

  const handleDeleteSample = async (id: number) => {
    const body = JSON.stringify({ id: id });
    await customerFetch("/api/sample/delete", "DELETE", body);
    await listSamples();
  };

  const handleUpdateSample = async (post: SamplePost) => {
    const newMessage = prompt("Edit message", post.message);
    if (!newMessage) return;
    const body = JSON.stringify({
      id: post.id,
      name: post.name,
      message: newMessage,
    });
    await customerFetch("/api/sample/update", "PUT", body);
    await listSamples();
  };

  return (
    <div className={styles["sample-container"]}>

      <h1 className="text-lg font-bold">Hello Sample</h1>

      <div className={styles["sample-card"]}>
        <input
          type="text"
          className={styles["sample-input"]}
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          onClick={handleNewSample}
        >
          Submit
        </button>
      </div>

      <div className={styles["sample-post-container"]}>

        <h2>Post List</h2>

        {posts && posts.map((post: SamplePost) => (

          <div key={post.id} className={styles["sample-post"]}>

            <article className={styles["sample-post-article"]}>
              <header>
                <label>Name: {post.name}</label>
                <button
                  className={styles["sample-post-icon"]}
                  onClick={() => { handleDeleteSample(post.id) }}
                >
                  <img src="trash_icon.png" />
                </button>
                <button
                  className={styles["sample-post-icon"]}
                  onClick={() => handleUpdateSample(post)}
                >
                  <img src="pencil_icon.png" />
                </button>
              </header>
              <p>{post.message}</p>
            </article>

          </div>
        ))}
      </div>
    </div >
  );
}
