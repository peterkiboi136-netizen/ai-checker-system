import { useState, useEffect } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [status, setStatus] = useState("");

  // backend health check
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/health")
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus("backend not connected"));
  }, []);

  // upload file
  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/api/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Checker System</h1>

      <p>
        <b>Backend Status:</b> {status}
      </p>

      <hr />

      <h3>Upload Document</h3>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Analyze File
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Result</h2>

          <p><b>File:</b> {result.filename}</p>

          <p><b>Embedding Score:</b> {result.embedding_score}</p>
          <p><b>Linguistic Score:</b> {result.linguistic_score}</p>
          <p><b>Final AI Score:</b> {result.final_score}%</p>
          <p><b>Verdict:</b> {result.verdict}</p>

          <h3>Preview</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>
            {result.extracted_text_preview}
          </pre>
        </div>
      )}
    </div>
  );
}

export default App;