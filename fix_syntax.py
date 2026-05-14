with open('frontend/src/app/page.tsx', 'r') as f:
    content = f.read()

content = content.replace('''  useEffect(() => {
    async function fetchData() {
      try {
        const [statusRes, intelRes] = await Promise.all([
          fetch('/api/status'),
          fetch('/api/intelligence')
        ]);
        const statusData = await statusRes.json();
        const intelData = await intelRes.json();
        setStatus(statusData);
        setIntel(intelData);
      } catch (err) {
        console.error('Failed to fetch data', err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

export default function Chat() {''', '''  useEffect(() => {
    async function fetchData() {
      try {
        const [statusRes, intelRes] = await Promise.all([
          fetch('/api/status'),
          fetch('/api/intelligence')
        ]);
        const statusData = await statusRes.json();
        const intelData = await intelRes.json();
        setStatus(statusData);
        setIntel(intelData);
      } catch (err) {
        console.error('Failed to fetch data', err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);
''')

with open('frontend/src/app/page.tsx', 'w') as f:
    f.write(content)
