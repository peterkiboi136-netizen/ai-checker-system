export default function SimilaritySidebar({
  aiScore,
  riskLevel,
  sources = [],
}) {
  return (
    <div
      style={{
        width: "320px",
        background: "#fff",
        borderLeft: "1px solid #ddd",
        height: "100%",
        overflowY: "auto",
      }}
    >
      {/* Score */}

      <div
        style={{
          padding: "20px",
          borderBottom: "1px solid #ddd",
          textAlign: "center",
        }}
      >
        <div
          style={{
            fontSize: "60px",
            fontWeight: "bold",
            color:
              aiScore > 70
                ? "#dc2626"
                : aiScore > 40
                ? "#f59e0b"
                : "#16a34a",
          }}
        >
          {aiScore}%
        </div>

        <div
          style={{
            marginTop: "8px",
            fontWeight: "bold",
          }}
        >
          AI Similarity
        </div>

        <div
          style={{
            marginTop: "5px",
            color: "#666",
          }}
        >
          {riskLevel}
        </div>
      </div>

      {/* Sources */}

      <div
        style={{
          padding: "16px",
        }}
      >
        <h3>Matching Sources</h3>

        {sources.length === 0 ? (
          <p
            style={{
              color: "#888",
            }}
          >
            No sources detected
          </p>
        ) : (
          sources.map((source, index) => (
            <div
              key={index}
              style={{
                marginBottom: "12px",
                border: "1px solid #eee",
                borderRadius: "8px",
                padding: "10px",
              }}
            >
              <div
                style={{
                  fontWeight: "bold",
                }}
              >
                Match #{index + 1}
              </div>

              <div
                style={{
                  marginTop: "5px",
                  fontSize: "14px",
                }}
              >
                {source.text}
              </div>

              <div
                style={{
                  marginTop: "6px",
                  color: "#dc2626",
                  fontWeight: "bold",
                }}
              >
                {source.percent}% Match
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}