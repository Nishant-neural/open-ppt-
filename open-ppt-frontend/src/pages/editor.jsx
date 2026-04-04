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
    
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter topic..."
      />

      <button onClick={handleGenerate}>
        Generate
      </button>

     
      <div className="w-full h-screen overflow-hidden">
  {slides?.length > 0 && slides[index] && (
    <SlideRenderer slide={slides[index]} />
  )}
</div>

      
     <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 flex gap-4">
  <button onClick={() => setIndex(index - 1)}>⬅</button>
  <button onClick={() => setIndex(index + 1)}>➡</button>
</div>
    </div>
  )
}