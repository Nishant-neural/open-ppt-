import { getImageUrl } from "../../services/image"

export default function ImageSlide({ slide }) {
  const imageUrl = getImageUrl(slide.image_query)

  return (
    <div className="h-screen w-full flex items-center justify-center px-24 bg-white text-black">
      
      <div className="grid grid-cols-2 gap-12 items-center max-w-6xl">
        
        <div>
          <h2 className="text-4xl font-bold mb-6">
            {slide.heading}
          </h2>

          <p className="text-xl opacity-90">
            {slide.text}
          </p>
        </div>

        <div>
          <img
            src={imageUrl}
            alt=""
            className="rounded-2xl shadow-2xl w-full max-h-[500px] object-cover"
          />
        </div>

      </div>
    </div>
  )
}