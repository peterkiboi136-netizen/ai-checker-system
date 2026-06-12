import { useState } from "react";
import { Document, Page } from "react-pdf";

function PDFViewer({ fileUrl }) {

  const [numPages, setNumPages] = useState(null);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  return (
    <div>

      <Document
        file={fileUrl}
        onLoadSuccess={onDocumentLoadSuccess}
      >

        {Array.from(
          new Array(numPages),
          (el, index) => (
            <Page
              key={index}
              pageNumber={index + 1}
            />
          )
        )}

      </Document>

    </div>
  );
}

export default PDFViewer;