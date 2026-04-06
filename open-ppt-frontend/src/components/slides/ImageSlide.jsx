import { getImageUrl } from "../../services/image"

export default function ImageSlide({ slide }) {
  const imageUrl = getImageUrl(slide.image_query)

  return (
    <>
      <div style={{ display: "flex", flexDirection: "column", justifyContent: "center" }}>
        <h2
          style={{
            fontSize: "clamp(2rem, 4vw, 3.25rem)",
            fontWeight: 700,
            lineHeight: 1.15,
            margin: "0 0 24px",
          }}
        >
          {slide.heading}
        </h2>

        <p
          style={{
            fontSize: "1.25rem",
            lineHeight: 1.7,
            margin: 0,
            maxWidth: "520px",
          }}
        >
          {slide.text}
        </p>
      </div>

      <div style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
        <img
          src={imageUrl}
          alt={slide.heading || "Slide illustration"}
          style={{
            width: "100%",
            maxWidth: "560px",
            maxHeight: "420px",
            objectFit: "cover",
            borderRadius: "24px",
            boxShadow: "0 20px 40px rgba(0, 0, 0, 0.22)",
            background: "rgba(255, 255, 255, 0.18)",
          }}
        />
      </div>
    </>
  )
}
