import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      // Upload file
      const uploadResponse = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      const filename = uploadResponse.data.filename;

      // Analyze file
      const analyzeResponse = await axios.get(
        `http://127.0.0.1:8000/analyze/${filename}`
      );

      setResult(analyzeResponse.data);

      alert("Analysis complete");

    } catch (error) {
      console.error(error);
      alert("Upload or analysis failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Checker System</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={uploadFile}
        style={{
          marginLeft: "10px",
          padding: "8px 16px",
          cursor: "pointer"
        }}
      >
        {loading ? "Processing..." : "Upload & Analyze"}
      </button>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Analysis Result</h2>

          <p>
            <strong>Filename:</strong> {result.filename}
          </p>

          <p>
            <strong>AI Score:</strong>{" "}
            {result.analysis.ai_score}
          </p>

          <p>
            <strong>Risk Level:</strong>{" "}
            {result.analysis.risk_level}
          </p>

          <p>
            <strong>Word Count:</strong>{" "}
            {result.analysis.word_count}
          </p>

          <p>
            <strong>Sentence Count:</strong>{" "}
            {result.analysis.sentence_count}
          </p>

          <p>
            <strong>Report:</strong>{" "}
            {result.report_url}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;


