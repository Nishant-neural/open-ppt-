import { useState, useEffect } from "react"
import SlideRenderer from "../components/SlideRenderer"
import { generateSlides } from "../services/api"

export default function Editor({ slides, setSlides }) {
  const [prompt, setPrompt] = useState("")
  const [index, setIndex] = useState(0)

  const handleGenerate = async () => {
    const data = await generateSlides(prompt)
    setSlides(data.slides || [])
    setIndex(0)
  }

  useEffect(() => {
    const handleKey = (e) => {
      if (e.key === "ArrowRight") setIndex((i) => i + 1)
      if (e.key === "ArrowLeft") setIndex((i) => i - 1)
    }

    window.addEventListener("keydown", handleKey)
    return () => window.removeEventListener("keydown", handleKey)
  }, [])

  return (
    <div className="w-full h-screen overflow-hidden">
      
      {/* Input */}
      <div className="fixed top-5 left-1/2 transform -translate-x-1/2 z-10">
        <input
          className="px-4 py-2 border rounded"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter topic..."
        />
        <button
          onClick={handleGenerate}
          className="ml-2 px-4 py-2 bg-black text-white rounded"
        >
          Generate
        </button>
      </div>

      {/* Slide */}
      {slides?.length > 0 && slides[index] && (
        <SlideRenderer slide={slides[index]} />
      )}

      {/* Navigation */}
      <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 flex gap-4">
        <button onClick={() => setIndex(index - 1)}>⬅</button>
        <button onClick={() => setIndex(index + 1)}>➡</button>
      </div>

    </div>
  )
}