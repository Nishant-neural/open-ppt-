import { motion } from "framer-motion"
import TitleSlide from "./slides/TitleSlide"
import BulletSlide from "./slides/BulletSlide"

export default function SlideRenderer({ slide }) {
  if (!slide) return null

  let Component

  switch (slide.type) {
    case "title":
      Component = TitleSlide
      break
    case "bullets":
      Component = BulletSlide
      break
    default:
      Component = BulletSlide
  }

  return (
    <motion.div
      key={slide.heading}
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -50 }}
      transition={{ duration: 0.4 }}
    >
      <Component slide={slide} />
    </motion.div>
  )
}