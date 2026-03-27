import { useState } from "react"
import Editor from "./pages/editor"

export default function App() {
  const [slides, setSlides] = useState([])

  return (
    <Editor slides={slides} setSlides={setSlides} />
  )
}