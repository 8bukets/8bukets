const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000/api";

export async function fetchJson(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    cache: "no-store",
  });

  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data.error || "Request failed");
  }

  return response.json();
}

export async function getSoftwareList() {
  try {
    return await fetchJson("/software");
  } catch {
    return [];
  }
}

export async function getSoftwareDetail(slug) {
  try {
    return await fetchJson(`/software/${slug}`);
  } catch {
    return null;
  }
}

export async function getReviewDetail(id) {
  try {
    return await fetchJson(`/reviews/${id}`);
  } catch {
    return null;
  }
}
