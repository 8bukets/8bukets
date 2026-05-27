import pkg from "pg";
const { Pool } = pkg;

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

export default {
  query: (text, params) => pool.query(text, params),
  healthcheck: async () => {
    await pool.query("SELECT 1");
    return true;
  },
};
