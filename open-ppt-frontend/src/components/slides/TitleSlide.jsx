export default function TitleSlide({ slide }) {
  return (
    <div style={{ height: "100vh", textAlign: "center" }}>
      <h1>{slide.heading}</h1>
      <p>{slide.subheading}</p>
    </div>
  )
}