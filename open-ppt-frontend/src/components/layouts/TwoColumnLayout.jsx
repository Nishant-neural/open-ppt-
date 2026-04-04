export default function TwoColumnLayout({ children, theme }) {
  return (
    <div className={`h-screen grid grid-cols-2 px-20 ${theme.background} ${theme.text}`}>
      {children}
    </div>
  )
}