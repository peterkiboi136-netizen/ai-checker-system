import { useEffect, useState } from "react";
import API from "../api/client";

import SplitPdfViewer from "../components/SplitPdfViewer";
import SimilaritySidebar from "../components/SimilaritySidebar";

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const res = await API.get("/api/history");
      setHistory(res.data);
    } catch (err) {
      console.error("History load failed:", err);
    }
  };

  const uploadPDF = async () => {
    if (!file) {
      alert("Please select a PDF or DOCX file");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await API.post(
        "/api/pdf/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(res.data);

      await loadHistory();
    } catch (err) {
      console.error(err);

      setError(
        err?.response?.data?.detail ||
          "Upload failed. Check backend connection."
      );
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        padding: "24px",
        background: "#f5f7fb",
        minHeight: "100vh",
        fontFamily: "Arial, sans-serif",
      }}
    >
      {/* Header */}

      <div
        style={{
          marginBottom: "24px",
        }}
      >
        <h1
          style={{
            marginBottom: "6px",
          }}
        >
          AI Checker Dashboard
        </h1>

        <p
          style={{
            color: "#666",
          }}
        >
          Turnitin-Style AI & Similarity Detection Platform
        </p>
      </div>

      {/* Upload Card */}

      <div
        style={{
          background: "#fff",
          borderRadius: "12px",
          padding: "20px",
          marginBottom: "24px",
          boxShadow:
            "0 2px 10px rgba(0,0,0,0.05)",
        }}
      >
        <h2>Upload Document</h2>

        <div
          style={{
            marginTop: "15px",
            display: "flex",
            gap: "10px",
            alignItems: "center",
          }}
        >
          <input
            type="file"
            accept=".pdf,.docx"
            onChange={(e) =>
              setFile(e.target.files[0])
            }
          />

          <button
            onClick={uploadPDF}
            disabled={loading}
            style={{
              background: "#2563eb",
              color: "#fff",
              border: "none",
              padding: "10px 18px",
              borderRadius: "6px",
              cursor: "pointer",
            }}
          >
            {loading
              ? "Analyzing..."
              : "Upload & Analyze"}
          </button>
        </div>

        {file && (
          <p
            style={{
              marginTop: "12px",
              color: "#666",
            }}
          >
            Selected: {file.name}
          </p>
        )}
      </div>

      {/* Error */}

      {error && (
        <div
          style={{
            background: "#fee2e2",
            color: "#dc2626",
            padding: "12px",
            borderRadius: "8px",
            marginBottom: "20px",
          }}
        >
          {error}
        </div>
      )}

      {/* Analysis Result */}

      {result && (
        <div
          style={{
            background: "#fff",
            borderRadius: "12px",
            padding: "20px",
            marginBottom: "30px",
            boxShadow:
              "0 2px 10px rgba(0,0,0,0.05)",
          }}
        >
          <h2>Analysis Result</h2>

          {/* Stats */}

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(auto-fit, minmax(220px, 1fr))",
              gap: "15px",
              marginTop: "20px",
              marginBottom: "25px",
            }}
          >
            <div
              style={{
                background: "#eff6ff",
                padding: "16px",
                borderRadius: "8px",
              }}
            >
              <h3>AI Score</h3>

              <div
                style={{
                  fontSize: "32px",
                  fontWeight: "bold",
                  color:
                    result.ai_score > 70
                      ? "#dc2626"
                      : result.ai_score > 40
                      ? "#f59e0b"
                      : "#16a34a",
                }}
              >
                {result.ai_score}%
              </div>
            </div>

            <div
              style={{
                background: "#f9fafb",
                padding: "16px",
                borderRadius: "8px",
              }}
            >
              <h3>Risk Level</h3>

              <div
                style={{
                  fontSize: "24px",
                  fontWeight: "bold",
                }}
              >
                {result.risk_level}
              </div>
            </div>

            <div
              style={{
                background: "#f9fafb",
                padding: "16px",
                borderRadius: "8px",
              }}
            >
              <h3>Words</h3>

              <div
                style={{
                  fontSize: "24px",
                  fontWeight: "bold",
                }}
              >
                {result.word_count}
              </div>
            </div>

            <div
              style={{
                background: "#f9fafb",
                padding: "16px",
                borderRadius: "8px",
              }}
            >
              <h3>Sentences</h3>

              <div
                style={{
                  fontSize: "24px",
                  fontWeight: "bold",
                }}
              >
                {result.sentence_count}
              </div>
            </div>
          </div>

          {/* Turnitin Viewer */}

          {result.original_pdf &&
            result.highlighted_pdf && (
              <div
                style={{
                  display: "flex",
                  height: "950px",
                  border:
                    "1px solid #e5e7eb",
                  borderRadius: "12px",
                  overflow: "hidden",
                }}
              >
                <div
                  style={{
                    flex: 1,
                    minWidth: 0,
                  }}
                >
                  <SplitPdfViewer
                    originalUrl={`http://127.0.0.1:8000/${result.original_pdf}`}
                    highlightedUrl={`http://127.0.0.1:8000/${result.highlighted_pdf}`}
                  />
                </div>

                <SimilaritySidebar
                  aiScore={
                    result.ai_score
                  }
                  riskLevel={
                    result.risk_level
                  }
                  sources={
                    result.sources || [
                      {
                        text:
                          "Machine learning is transforming education",
                        percent: 87,
                      },
                      {
                        text:
                          "Deep learning models are powerful",
                        percent: 65,
                      },
                    ]
                  }
                />
              </div>
            )}
        </div>
      )}

      {/* History */}

      <div
        style={{
          background: "#fff",
          borderRadius: "12px",
          padding: "20px",
          boxShadow:
            "0 2px 10px rgba(0,0,0,0.05)",
        }}
      >
        <h2>Previous Reports</h2>

        {history.length === 0 ? (
          <p>No reports available.</p>
        ) : (
          history.map((item) => (
            <div
              key={item.id}
              style={{
                marginTop: "12px",
                border:
                  "1px solid #e5e7eb",
                borderRadius: "8px",
                padding: "12px",
              }}
            >
              <div
                style={{
                  fontWeight: "bold",
                }}
              >
                {item.filename}
              </div>

              <div
                style={{
                  marginTop: "6px",
                }}
              >
                AI Score:{" "}
                <strong>
                  {item.ai_score}%
                </strong>
              </div>

              <div>
                Document ID: {item.id}
              </div>

              <div
                style={{
                  fontSize: "12px",
                  color: "#666",
                  marginTop: "4px",
                }}
              >
                {item.created_at}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}