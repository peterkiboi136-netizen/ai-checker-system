import { useState } from "react";
import { uploadPDF } from "../api/client";

export default function UploadBox({ onResult }) {
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);

    try {
      const res = await uploadPDF(file);
      onResult(res.data);
    } catch (err) {
      console.error("Upload failed", err);
    }

    setLoading(false);
  };

  return (
    <div className="p-4 border rounded-lg">
      <input type="file" accept="application/pdf" onChange={handleUpload} />

      {loading && <p className="text-blue-500">Analyzing PDF...</p>}
    </div>
  );
}