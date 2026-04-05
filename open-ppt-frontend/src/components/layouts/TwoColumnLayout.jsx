export default function TwoColumnLayout({ children, theme }) {
  const resolvedTheme = theme || {
    background: "bg-white",
    text: "text-black",
  }

  return (
    <div className={`h-screen grid grid-cols-2 px-20 ${resolvedTheme.background} ${resolvedTheme.text}`}>
      {children}
    </div>
  )
}
