import { motion } from "framer-motion"
import TitleSlide from "./slides/TitleSlide"
import BulletSlide from "./slides/BulletSlide"
import TwoColumnLayout from "./layouts/TwoColumnLayout"
import CenterLayout from "./layouts/CenterLayout"
import { themes } from "../theme/themes"
import ImageSlide from "./slides/ImageSlide"

export default function SlideRenderer({ slide }) {
  if (!slide) return null

  const theme = themes["gradient"]

 
  let Content

  switch (slide.type) {
    case "title":
      Content = TitleSlide
      break

    case "bullets":
      Content = BulletSlide
      break

    case "image_text":
      Content = ImageSlide
      break

    default:
      Content = BulletSlide
  }

 
  let Layout

  switch (slide.layout) {
    case "two_column":
      Layout = TwoColumnLayout
      break

    case "center":
    default:
      Layout = CenterLayout
  }

  return (
    <motion.div
      key={slide.heading}
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.4 }}
    >
      <Layout theme={theme}>
        <Content slide={slide} />
      </Layout>
    </motion.div>
  )
}