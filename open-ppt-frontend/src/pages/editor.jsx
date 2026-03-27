import { useState } from "react"
import { generateSlides } from "../services/api"
import SlideRenderer from "../components/SlideRenderer"

export default function Editor({ slides, setSlides }) {
  const [prompt, setPrompt] = useState("")
  const [index, setIndex] = useState(0)

 const handleGenerate = async () => {
  const data = await generateSlides(prompt)

  console.log("API response:", data)

  setSlides(data.slides || [])   
  setIndex(0)
}

  return (
    <div>
      {/* Input */}
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter topic..."
      />

      <button onClick={handleGenerate}>
        Generate
      </button>

      {/* Slide View */}
      {slides && slides.length > 0 && slides[index] &&  (
        <SlideRenderer slide={slides[index]} />
      )}

      {/* Navigation */}
      <button onClick={() => setIndex(index - 1)}>Prev</button>
      <button onClick={() => setIndex(index + 1)}>Next</button>
    </div>
  )
}