import { updateSample } from "@/app/sample/fetch_sample";
import { NextResponse } from "next/server";


export async function PUT(req: Request) {
  const { id, name, message } = await req.json();
  try {
    const result = await updateSample(id, name, message);
    return NextResponse.json(result);
  } catch (error) {
    console.error("Update failed:", error);
    return NextResponse.json({ error: "Failed" }, { status: 500 });
  }
}