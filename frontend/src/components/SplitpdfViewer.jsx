import { useEffect, useRef, useState } from "react";

export default function SplitPdfViewer({
  originalUrl,
  highlightedUrl,
}) {
  const leftRef = useRef(null);
  const rightRef = useRef(null);

  const [zoom, setZoom] = useState(100);

  useEffect(() => {
    const left = leftRef.current;
    const right = rightRef.current;

    if (!left || !right) return;

    let syncing = false;

    const syncLeft = () => {
      if (syncing) return;

      syncing = true;

      right.scrollTop = left.scrollTop;

      setTimeout(() => {
        syncing = false;
      }, 5);
    };

    const syncRight = () => {
      if (syncing) return;

      syncing = true;

      left.scrollTop = right.scrollTop;

      setTimeout(() => {
        syncing = false;
      }, 5);
    };

    left.addEventListener("scroll", syncLeft);
    right.addEventListener("scroll", syncRight);

    return () => {
      left.removeEventListener("scroll", syncLeft);
      right.removeEventListener("scroll", syncRight);
    };
  }, []);

  const zoomIn = () => {
    setZoom((z) => Math.min(z + 10, 300));
  };

  const zoomOut = () => {
    setZoom((z) => Math.max(z - 10, 50));
  };

  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "12px",
        overflow: "hidden",
        background: "#fff",
      }}
    >
      {/* Toolbar */}

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "12px",
          borderBottom: "1px solid #ddd",
          background: "#f8f9fa",
        }}
      >
        <div>
          <strong>
            Turnitin Style Comparison Viewer
          </strong>
        </div>

        <div>
          <button
            onClick={zoomOut}
            style={{
              marginRight: "8px",
            }}
          >
            −
          </button>

          <span>{zoom}%</span>

          <button
            onClick={zoomIn}
            style={{
              marginLeft: "8px",
            }}
          >
            +
          </button>
        </div>
      </div>

      {/* Viewer */}

      <div
        style={{
          display: "flex",
          height: "900px",
        }}
      >
        {/* Original */}

        <div
          style={{
            flex: 1,
            borderRight: "1px solid #ddd",
          }}
        >
          <div
            style={{
              padding: "10px",
              fontWeight: "bold",
              background: "#f3f4f6",
              borderBottom: "1px solid #ddd",
            }}
          >
            Original Document
          </div>

          <div
            ref={leftRef}
            style={{
              height: "850px",
              overflowY: "auto",
            }}
          >
            <iframe
              title="Original PDF"
              src={`${originalUrl}#zoom=${zoom}`}
              width="100%"
              height="100%"
              style={{
                border: "none",
              }}
            />
          </div>
        </div>

        {/* Highlighted */}

        <div
          style={{
            flex: 1,
          }}
        >
          <div
            style={{
              padding: "10px",
              fontWeight: "bold",
              background: "#fef2f2",
              borderBottom: "1px solid #ddd",
              color: "#dc2626",
            }}
          >
            Similarity Report
          </div>

          <div
            ref={rightRef}
            style={{
              height: "850px",
              overflowY: "auto",
            }}
          >
            <iframe
              title="Highlighted PDF"
              src={`${highlightedUrl}#zoom=${zoom}`}
              width="100%"
              height="100%"
              style={{
                border: "none",
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}