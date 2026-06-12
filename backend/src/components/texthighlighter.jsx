function TextHighlighter({ text, matches }) {

  if (!text) return null;

  const sentences = text.split(".");

  return (
    <div style={{ lineHeight: "1.8" }}>

      {sentences.map((s, i) => {

        const match = matches.find(
          (m) => m.text === s.trim()
        );

        let color = "black";

        if (match?.type === "exact") color = "red";

        if (match?.type === "partial") color = "orange";

        return (
          <span
            key={i}
            style={{
              backgroundColor:
                color === "red"
                  ? "#ffcccc"
                  : color === "orange"
                  ? "#ffe5b4"
                  : "transparent",
              padding: "2px"
            }}
          >
            {s}.
          </span>
        );

      })}

    </div>
  );
}

export default TextHighlighter;