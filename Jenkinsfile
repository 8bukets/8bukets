pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test Node') {
            options {
                timeout(time: 1, unit: 'HOURS')
            }
            steps {
                // Utilizing local npm cache for faster builds
                sh 'npm ci --cache .npm --prefer-offline'
                sh 'npm run build'
                sh 'npm run test || true'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'npm audit || true'
            }
        }

        stage('Creative Workflow') {
            parallel {
                stage('Analyze Market') {
                    steps {
                        sh 'python3 scraper.py'
                    }
                }
                stage('Generate Assets') {
                    steps {
                        sh 'npm run daily'
                        sh 'python3 analytics.py'
                    }
                }
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
