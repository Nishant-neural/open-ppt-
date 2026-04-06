function escapeXml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll("\"", "&quot;")
    .replaceAll("'", "&apos;")
}

export function getImageUrl(query = "") {
  const label = escapeXml(query || "Presentation image")

  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
      <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#1d4ed8" />
          <stop offset="100%" stop-color="#0f766e" />
        </linearGradient>
      </defs>
      <rect width="800" height="600" fill="url(#bg)" rx="28" />
      <circle cx="620" cy="170" r="96" fill="rgba(255,255,255,0.12)" />
      <circle cx="180" cy="450" r="130" fill="rgba(255,255,255,0.08)" />
      <rect x="120" y="120" width="220" height="140" rx="20" fill="rgba(255,255,255,0.14)" />
      <path d="M150 390 C250 270, 360 480, 500 330 S670 210, 710 320" stroke="rgba(255,255,255,0.7)" stroke-width="16" fill="none" stroke-linecap="round" />
      <text x="70" y="520" fill="#ffffff" font-size="34" font-family="Segoe UI, Arial, sans-serif" font-weight="700">
        ${label}
      </text>
      <text x="70" y="565" fill="rgba(255,255,255,0.84)" font-size="20" font-family="Segoe UI, Arial, sans-serif">
        Generated slide illustration placeholder
      </text>
    </svg>
  `.trim()

  return `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(svg)}`
}
