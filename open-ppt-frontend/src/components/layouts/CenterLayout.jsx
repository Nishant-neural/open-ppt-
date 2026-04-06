export default function CenterLayout({ children, theme }) {
  const resolvedTheme = theme || {
    background: "#ffffff",
    text: "#111111",
  }

  return (
    <div
      style={{
        minHeight: "100vh",
        width: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "48px 96px",
        boxSizing: "border-box",
        background: resolvedTheme.background,
        color: resolvedTheme.text,
      }}
    >
      {children}
    </div>
  )
}
