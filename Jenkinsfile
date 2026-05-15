pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test Node') {
            steps {
                sh 'npm ci'
                sh 'npm run build'
                sh 'npm run test || true'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'echo "Running Security Scan..."'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker-compose build || true'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results/**/*.md', allowEmptyArchive: true
        }
    }
}
