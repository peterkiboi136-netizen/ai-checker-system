function PDFHighlightOverlay({ matches }) {

  return (
    <div style={{ position: "absolute", top: 0 }}>

      {matches.map((m, i) => (
        <div
          key={i}
          style={{
            backgroundColor:
              m.type === "exact"
                ? "rgba(255,0,0,0.3)"
                : "rgba(255,165,0,0.3)",
            margin: "5px 0",
            padding: "5px"
          }}
        >
          {m.text}
        </div>
      ))}

    </div>
  );
}

export default PDFHighlightOverlay;