export default function TitleSlide({ slide }) {
  return (
    <>
      <h1
        style={{
          fontSize: "clamp(2.75rem, 5vw, 4.5rem)",
          fontWeight: 700,
          lineHeight: 1.1,
          marginBottom: "24px",
          textAlign: "center",
          maxWidth: "900px",
        }}
      >
        {slide.heading}
      </h1>

      <p
        style={{
          fontSize: "1.5rem",
          lineHeight: 1.5,
          opacity: 0.9,
          textAlign: "center",
          maxWidth: "760px",
        }}
      >
        {slide.subheading || slide.points?.[0] || ""}
      </p>
    </>
  )
}
