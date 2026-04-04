export default function BulletSlide({ slide }) {
  
  if (slide.layout === "two_column") {
    return (
      <>
        <div className="flex flex-col justify-center pr-10">
          <h2 className="text-4xl font-bold mb-6">{slide.heading}</h2>

          {slide.left?.map((p, i) => (
            <p key={i}>{p}</p>
          ))}
        </div>

        <div className="flex flex-col justify-center pl-10">
          {slide.right?.map((p, i) => (
            <p key={i}>{p}</p>
          ))}
        </div>
      </>
    )
  }

  
  return (
    <>
      <h2 className="text-5xl font-semibold mb-10 text-center">
        {slide.heading}
      </h2>

      <ul className="space-y-4 max-w-3xl">
        {slide.points?.map((p, i) => (
          <li key={i} className="text-2xl">
            • {p}
          </li>
        ))}
      </ul>
    </>
  )
}