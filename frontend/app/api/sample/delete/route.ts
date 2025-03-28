import { deleteSample } from "@/app/sample/fetch_sample";
import { NextResponse } from "next/server";


export async function DELETE(req: Request) {
  const { id } = await req.json();
  try {
    const result = await deleteSample(id);
    return NextResponse.json(result);
  } catch (error) {
    console.error("Delete failed:", error);
    return NextResponse.json({ error: "Failed" }, { status: 500 });
  }
}