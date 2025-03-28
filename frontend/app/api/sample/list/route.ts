import { listSample } from "@/app/sample/fetch_sample";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const posts = await listSample();
    return NextResponse.json(posts);
  } catch (error) {
    console.error("Fetch list failed:", error);
    return NextResponse.json({ error: "Failed" }, { status: 500 });
  }
}