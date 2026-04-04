import CenterLayout from "../layouts/CenterLayout"

export default function TitleSlide({ slide, theme }) {
  return (
    <CenterLayout theme={theme}>
      <h1 className="text-6xl font-bold mb-6 text-center">
        {slide.heading}
      </h1>

      <p className="text-2xl opacity-80 text-center">
        {slide.subheading}
      </p>
    </CenterLayout>
  )
}