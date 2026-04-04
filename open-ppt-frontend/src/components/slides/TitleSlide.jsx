export default function TitleSlide({ slide }) {
  return (
    <div className="h-screen flex flex-col justify-center items-center bg-black text-white">
      <h1 className="text-6xl font-bold">{slide.heading}</h1>
      <p className="text-2xl mt-4 opacity-80">{slide.subheading}</p>
    </div>
  )
}