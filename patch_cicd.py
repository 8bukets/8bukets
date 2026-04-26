with open('.github/workflows/ci-cd.yml', 'r') as f:
    code = f.read()

# Replace google-github-actions/auth@v1 with docker login actions
old_deploy_gcp = """    - name: Authenticate with GCP
      uses: google-github-actions/auth@v1
      with:
        credentials_json: ${{ secrets.GCP_KEY }}

    - name: Configure Docker to Use GCR
      run: gcloud auth configure-docker

    - name: Build and Push Backend Image
      run: |
        docker build -t gcr.io/${{ secrets.GCP_PROJECT }}/backend ./backend
        docker push gcr.io/${{ secrets.GCP_PROJECT }}/backend

    - name: Build and Push Frontend Image
      run: |
        docker build -t gcr.io/${{ secrets.GCP_PROJECT }}/frontend ./frontend
        docker push gcr.io/${{ secrets.GCP_PROJECT }}/frontend

    - name: Build and Push Scraper Image
      run: |
        docker build -t gcr.io/${{ secrets.GCP_PROJECT }}/scraper .
        docker push gcr.io/${{ secrets.GCP_PROJECT }}/scraper

    - name: Deploy to GKE or Cloud Run
      run: |
        # Example for Cloud Run Deployment
        gcloud run deploy backend \\
          --image gcr.io/${{ secrets.GCP_PROJECT }}/backend \\
          --platform managed \\
          --region us-central1 \\
          --allow-unauthenticated"""

new_deploy_docker = """    - name: Login to Docker Hub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and Push Backend Image
      uses: docker/build-push-action@v5
      with:
        context: ./backend
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/sor-backend:latest

    - name: Build and Push Frontend Image
      uses: docker/build-push-action@v5
      with:
        context: ./frontend
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/sor-frontend:latest

    - name: Build and Push Scraper Image
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/sor:latest"""

code = code.replace(old_deploy_gcp, new_deploy_docker)
code = code.replace("Build and Deploy to GCP", "Build and Push to Docker Hub")

with open('.github/workflows/ci-cd.yml', 'w') as f:
    f.write(code)
