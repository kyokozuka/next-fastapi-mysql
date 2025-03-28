import { newSample } from "@/app/sample/fetch_sample";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { name, message } = await req.json();
  try {
    const result = await newSample(name, message);
    return NextResponse.json(result);
  } catch (error) {
    console.error("Create failed:", error);
    return NextResponse.json({ error: "Failed" }, { status: 500 });
  }
}