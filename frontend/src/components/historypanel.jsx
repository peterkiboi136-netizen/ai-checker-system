import { useEffect, useState } from "react";
import API from "../api/client";

export default function HistoryPanel() {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    const res = await API.get("/api/history");
    setDocs(res.data);
  };

  return (
    <div>
      <h2>Previous Reports</h2>

      {docs.map((d) => (
        <div key={d.id}>
          <strong>{d.filename}</strong>
          <br />
          AI Score: {(d.ai_score * 100).toFixed(1)}%
        </div>
      ))}
    </div>
  );
}