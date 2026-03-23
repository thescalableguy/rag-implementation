import { useState } from "react";
import { streamAnswer, api } from "./api";

// 🔹 Pre-built prompts
const PRESET_PROMPTS = [
  "Explain Dharma in Mahabharata with modern relevance",
  "What does Bhagavad Gita teach about Karma?",
  "Leadership lessons from Lord Rama",
  "Compare Krishna and Rama as leaders",
  "Concept of Moksha in Upanishads"
];

function App() {
  const [topic, setTopic] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
  if (!topic) return;

  setResult("");
  setLoading(true);

  try {
    await api.ragStream(topic, (text) => {
      setResult(text); // 🔥 correct streaming
    });
  } catch (err) {
    console.error(err);
    setResult("Error fetching response");
  }

  setLoading(false);
};

  const handlePresetClick = async (prompt) => {
    setTopic(prompt);
    setResult("");
    setLoading(true);

    try {
      await streamAnswer(prompt, (chunk) => {
        setResult((prev) => prev + chunk);
      });
    } catch (err) {
      console.error(err);
      setResult("Error fetching response");
    }

    setLoading(false);
  };

  const handlePipeline = async () => {
    try {
      await api.pipeline();
      alert("Pipeline executed! Check Discord 🚀");
    } catch (err) {
      console.error(err);
      alert("Pipeline failed");
    }
  };

  return (
    <div
      style={{
        padding: "20px",
        fontFamily: "Georgia, serif",
        minHeight: "100vh",

        // 🌄 Mythological gradient background
        background: "linear-gradient(135deg, #f5e6c8, #e6c07b)",

        color: "#2c1810"
      }}
    >
      <h1 style={{ color: "#8B0000" }}>
        🕉️ Mythology Research Engine
      </h1>

      {/* 🔹 Pipeline Button */}
      <button
        onClick={handlePipeline}
        style={{
          marginBottom: "15px",
          padding: "10px",
          background: "#8B0000",
          color: "#FFD700",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      >
        Run Daily Pipeline
      </button>

      <hr />

      {/* 🔹 Pre-built prompts */}
      <h3 style={{ color: "#5a3e1b" }}>✨ Explore Topics</h3>

      <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
        {PRESET_PROMPTS.map((prompt, index) => (
          <button
            key={index}
            onClick={() => handlePresetClick(prompt)}
            style={{
              padding: "8px 12px",
              borderRadius: "20px",
              border: "1px solid #c9a66b",
              cursor: "pointer",
              background: topic === prompt ? "#d4af37" : "#fff8dc",
              color: "#2c1810",
              fontSize: "14px"
            }}
          >
            {prompt}
          </button>
        ))}
      </div>

      <hr />

      {/* 🔹 Input */}
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Enter topic (e.g. Dharma in Mahabharata)"
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "10px",
          marginBottom: "10px",
          border: "1px solid #c9a66b",
          borderRadius: "5px",
          background: "#fff8dc",
          color: "#2c1810"
        }}
      />

      {/* 🔹 Search button */}
      <button
        onClick={handleSearch}
        disabled={loading}
        style={{
          padding: "10px",
          background: "#5a3e1b",
          color: "#FFD700",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      >
        {loading ? "Contemplating..." : "Explore"}
      </button>

      {/* 🔹 Output */}
      <div
        style={{
          marginTop: "20px",
          padding: "15px",
          border: "1px solid #c9a66b",
          borderRadius: "10px",
          height: "350px",
          overflowY: "auto",
          whiteSpace: "pre-wrap",
          wordBreak: "break-word",
          background: "#fff8dc",
          color: "#2c1810"
        }}
      >
        {result || (loading ? "Channeling wisdom..." : "Start exploring...")}
      </div>
    </div>
  );
}

export default App;