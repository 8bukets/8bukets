# Configuration Instructions

Thank you for deploying this project! There are a couple of services you need to configure to get the application running properly.

## 1. Supabase
This project requires the **Netlify Supabase Extension**. The deployment process will guide you through installing it.
This extension will automatically populate the required Supabase environment variables for the application.

## 2. MongoDB
This project connects to an external MongoDB cluster.
Please ensure you have a MongoDB cluster running and provide your connection string during deployment for the `MONGODB_URI` environment variable.
