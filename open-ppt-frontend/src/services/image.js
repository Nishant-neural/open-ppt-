export function getImageUrl(query) {
  return `https://source.unsplash.com/800x600/?${encodeURIComponent(query)}`
}