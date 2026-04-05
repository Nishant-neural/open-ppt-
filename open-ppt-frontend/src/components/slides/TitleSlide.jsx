export default function TitleSlide({ slide }) {
  return (
    <>
      <h1 className="text-6xl font-bold mb-6 text-center">
        {slide.heading}
      </h1>

      <p className="text-2xl opacity-80 text-center">
        {slide.subheading || slide.points?.[0] || ""}
      </p>
    </>
  )
}
