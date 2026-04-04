export default function BulletSlide({ slide }) {
  return (
    <div className="h-screen w-full flex flex-col justify-center px-20 bg-white">
      <h2 className="text-4xl font-bold mb-8">{slide.heading}</h2>

      <ul className="space-y-4">
        {slide.points?.map((p, i) => (
          <li key={i} className="text-xl text-gray-700">
            • {p}
          </li>
        ))}
      </ul>
    </div>
  )
}