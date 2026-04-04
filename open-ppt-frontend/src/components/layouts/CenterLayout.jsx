export default function CenterLayout({ children, theme }) {
  return (
    <div className={`h-screen w-full flex flex-col justify-center items-center px-24 ${theme.background} ${theme.text}`}>
      {children}
    </div>
  )
}