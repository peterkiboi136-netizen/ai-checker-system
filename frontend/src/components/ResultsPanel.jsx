import SplitPdfViewer from "./SplitPdfViewer";

export default function ResultsPanel({ data }) {
  if (!data) return null;

  const originalUrl = `http://127.0.0.1:8000/${data.original_pdf}`;
  const highlightedUrl = `http://127.0.0.1:8000/${data.highlighted_pdf}`;

  return (
    <div className="mt-6">

      {/* TOP STATS */}
      <div className="grid grid-cols-3 gap-4 text-center">

        <div className="p-4 bg-blue-100 rounded">
          <h3 className="font-bold">AI Score</h3>
          <p>{(data.ai_score * 100).toFixed(2)}%</p>
        </div>

        <div className="p-4 bg-red-100 rounded">
          <h3 className="font-bold">Plagiarism Matches</h3>
          <p>{data.matches.length}</p>
        </div>

        <div className="p-4 bg-green-100 rounded">
          <h3 className="font-bold">Status</h3>
          <p>Analyzed</p>
        </div>

      </div>

      {/* SPLIT VIEW PDF */}
      <SplitPdfViewer
        originalUrl={originalUrl}
        highlightedUrl={highlightedUrl}
      />

    </div>
  );
}