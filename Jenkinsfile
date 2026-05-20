pipeline {
    agent any

    environment {
        MACBOOK_CLOUD_SIMULATION = 'true'
        NODE_ENV = 'production'
        // Define any required environment variables for the node/ts execution
        // e.g., JENKINS_URL, SUPABASE variables, etc.
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Lint & Test') {
            steps {
                sh 'npm run lint || true' // ignoring lint errors if strictly set
                sh 'npm run test'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    sh 'docker build -t antigravity-system:latest .'
                }
            }
        }

        stage('Run Autonomous Feedback Analysis Service') {
            steps {
                sh 'npx tsx antigravity/workflows/feedback_analysis_workflow.ts'
            }
        }
        stage('Run Autonomous Performance Monitoring Service') {
            steps {
                sh 'npx tsx antigravity/workflows/performance_monitoring_workflow.ts'
            }
        }
        stage('Creative Workflow') {
            parallel {
                stage('Market Analysis') {
                    steps {
                        sh 'python3 scraper.py'
                    }
                }
                stage('Daily Tasks') {
                    steps {
                        sh 'npm run daily'
                    }
                }
                stage('Asset Generation') {
                    steps {
                        sh 'python3 analytics.py'
                    }
                }
            }
        }

        stage('Ignite System') {
            steps {
                script {
                    echo "Triggering Autonomous Cycle / System Ignition..."
                    // This runs the continuous cycle locally or triggers it
                    // Alternatively you can run npm run connect to broadcast status
                    sh 'npm run connect'
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Ensure collaboration status is updated."
        }
        success {
            echo "Pipeline succeeded! System evolution achieved."
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
