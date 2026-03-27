import TitleSlide from "./slides/TitleSlide"
import BulletSlide from "./slides/BulletSlide"

export default function SlideRenderer({ slide }) {
  if (!slide) return null

  switch (slide.type) {
    case "title":
      return <TitleSlide slide={slide} />

    case "bullets":
      return <BulletSlide slide={slide} />

    default:
      return <BulletSlide slide={slide} />
  }
}