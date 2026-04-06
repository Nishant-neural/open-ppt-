const headingStyle = {
  fontSize: "clamp(2rem, 4vw, 3.25rem)",
  fontWeight: 700,
  lineHeight: 1.15,
  margin: "0 0 24px",
}

const paragraphStyle = {
  fontSize: "1.25rem",
  lineHeight: 1.6,
  margin: "0 0 18px",
}

export default function BulletSlide({ slide }) {
  if (slide.layout === "two_column") {
    return (
      <>
        <div style={{ display: "flex", flexDirection: "column", justifyContent: "center" }}>
          <h2 style={headingStyle}>{slide.heading}</h2>

          {slide.left?.map((point, index) => (
            <p key={index} style={paragraphStyle}>
              {point}
            </p>
          ))}
        </div>

        <div style={{ display: "flex", flexDirection: "column", justifyContent: "center" }}>
          {slide.right?.map((point, index) => (
            <p key={index} style={paragraphStyle}>
              {point}
            </p>
          ))}
        </div>
      </>
    )
  }

  return (
    <div
      style={{
        width: "100%",
        maxWidth: "880px",
        margin: "0 auto",
      }}
    >
      <h2
        style={{
          ...headingStyle,
          textAlign: "center",
          marginBottom: "32px",
        }}
      >
        {slide.heading}
      </h2>

      <ul
        style={{
          listStyle: "disc",
          paddingLeft: "32px",
          margin: 0,
          display: "flex",
          flexDirection: "column",
          gap: "18px",
          textAlign: "left",
        }}
      >
        {slide.points?.map((point, index) => (
          <li
            key={index}
            style={{
              fontSize: "1.35rem",
              lineHeight: 1.6,
            }}
          >
            {point}
          </li>
        ))}
      </ul>
    </div>
  )
}
