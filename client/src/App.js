import React, { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const uploadFile = async () => {

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      alert("Upload successful");

      console.log(response.data);

    } catch (error) {

      console.error(error);
      alert("Upload failed");

    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Checker System</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={uploadFile}>
        Upload
      </button>
    </div>
  );
}

export default App;