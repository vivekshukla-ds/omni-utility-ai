"use client";
import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);

  async function upload() {
    if (!file) return;
    const form = new FormData();
    form.append("file", file);

    const res = await fetch(
      "https://omni-utility-ai.onrender.com/pdf/upload",
      { method: "POST", body: form }
    );
    setResult(await res.json());
  }

  return (
    <main style={{ padding: 40 }}>
      <h1>PDF Pricing Tool</h1>
      <input type="file" accept="application/pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)} />
      <button onClick={upload}>Upload</button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </main>
  );
}
