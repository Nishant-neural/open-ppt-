export default function SideLayout({ left, right }) {
  return (
    <div className="h-screen grid grid-cols-2 px-20">
      <div className="flex items-center">{left}</div>
      <div className="flex items-center">{right}</div>
    </div>
  )
}