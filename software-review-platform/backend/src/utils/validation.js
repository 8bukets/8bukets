export function isValidEmail(value) {
  return typeof value === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim());
}

export function normalizedString(value) {
  return typeof value === "string" ? value.trim() : "";
}

export function isValidPassword(value) {
  return typeof value === "string" && value.length >= 8;
}

export function isIntegerInRange(value, min, max) {
  const numeric = Number(value);
  return Number.isInteger(numeric) && numeric >= min && numeric <= max;
}
