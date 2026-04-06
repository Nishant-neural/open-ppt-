export default function TwoColumnLayout({ children, theme }) {
  const resolvedTheme = theme || {
    background: "#ffffff",
    text: "#111111",
  }

  return (
    <div
      style={{
        minHeight: "100vh",
        width: "100%",
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: "40px",
        alignItems: "center",
        padding: "48px 80px",
        boxSizing: "border-box",
        background: resolvedTheme.background,
        color: resolvedTheme.text,
      }}
    >
      {children}
    </div>
  )
}
