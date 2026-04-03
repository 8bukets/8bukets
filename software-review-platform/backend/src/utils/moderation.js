export function analyzeSentiment(content) {
  const normalized = content.toLowerCase();

  if (normalized.includes("terrible") || normalized.includes("awful") || normalized.includes("bad")) {
    return -0.7;
  }

  if (normalized.includes("great") || normalized.includes("excellent") || normalized.includes("love")) {
    return 0.8;
  }

  return 0.1;
}

export function detectSpam(content) {
  const normalized = content.toLowerCase();
  return normalized.includes("buy now") || normalized.includes("click here") || normalized.includes("http://");
}
