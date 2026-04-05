export default function CenterLayout({ children, theme }) {
  const resolvedTheme = theme || {
    background: "bg-white",
    text: "text-black",
  }

  return (
    <div className={`h-screen w-full flex flex-col justify-center items-center px-24 ${resolvedTheme.background} ${resolvedTheme.text}`}>
      {children}
    </div>
  )
}
