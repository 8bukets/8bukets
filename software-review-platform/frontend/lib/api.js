import { API_URL } from "./config";

function buildUrl(path, params = {}) {
  const searchParams = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== null && value !== "") {
      searchParams.set(key, value);
    }
  });

  const query = searchParams.toString();
  return `${API_URL}${path}${query ? `?${query}` : ""}`;
}

export async function fetchJson(path, options = {}) {
  const response = await fetch(buildUrl(path, options.params), {
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

export async function getSoftwareCatalogSnapshot(filters = {}) {
  const [allSoftware, filteredSoftware] = await Promise.allSettled([
    fetchJson("/software"),
    fetchJson("/software", { params: filters }),
  ]);

  const allSoftwareValue = allSoftware.status === "fulfilled" ? allSoftware.value : [];
  const filteredSoftwareValue = filteredSoftware.status === "fulfilled" ? filteredSoftware.value : [];

  return {
    allSoftware: allSoftwareValue,
    filteredSoftware: filteredSoftwareValue,
    isApiAvailable: allSoftware.status === "fulfilled" && filteredSoftware.status === "fulfilled",
  };
}

export async function getFilteredSoftwareList(filters = {}) {
  try {
    return await fetchJson("/software", { params: filters });
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
