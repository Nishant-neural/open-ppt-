export default function BulletSlide({ slide }) {
  return (
    <div style={{ padding: "40px" }}>
      <h2>{slide.heading}</h2>

      <ul>
        {slide.points?.map((p, i) => (
          <li key={i}>{p}</li>
        ))}
      </ul>
    </div>
  )
}