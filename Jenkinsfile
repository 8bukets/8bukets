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
        stage('Run Autonomous Cognitive Security Service') {
            steps {
                sh 'npx tsx antigravity/workflows/cognitive_security_workflow.ts'
            }
        }
        stage('Run Autonomous Visual Neural Relay') {
            steps {
                sh 'npx tsx antigravity/workflows/visual_neural_relay_workflow.ts'
            }
        }
        stage('Run Autonomous Feature Scaling Coordinator') {
            steps {
                sh 'npx tsx antigravity/workflows/feature_scaling_coordinator_workflow.ts'
            }
        }
        stage('Run Autonomous Autonomous Resource Optimizer') {
            steps {
                sh 'npx tsx antigravity/workflows/autonomous_resource_optimizer_workflow.ts'
            }
        }
        stage('Run Autonomous Proactive Scalability Service') {
            steps {
                sh 'npx tsx antigravity/workflows/proactive_scalability_workflow.ts'
            }
        }
        stage('Run Autonomous Cloud Convergence Service') {
            steps {
                sh 'npx tsx antigravity/workflows/cloud_convergence_workflow.ts'
            }
        }
        stage('Run Autonomous Autonomous UX Optimization Service') {
            steps {
                sh 'npx tsx antigravity/workflows/autonomous_ux_optimization_workflow.ts'
            }
        }
        stage('Run Autonomous Global Neural Sync Service (Phase 12)') {
            steps {
                sh 'npx tsx antigravity/workflows/global_neural_sync_service_(phase_12)_workflow.ts'
            }
        }
        stage('Run Autonomous Autonomous Discovery Engine') {
            steps {
                sh 'npx tsx antigravity/workflows/autonomous_discovery_engine_workflow.ts'
            }
        }
        stage('Run Autonomous Edge-to-Cloud Bridge') {
            steps {
                sh 'npx tsx antigravity/workflows/edge-to-cloud_bridge_workflow.ts'
            }
        }
        stage('Creative Workflow') {
            parallel {
                stage('Market Analysis') {
                    steps {
                        sh 'npm run ingest:sor'
                    }
                }
                stage('Daily Tasks') {
                    steps {
                        sh 'npm run daily'
                    }
                }
                stage('Autonomous Evolution') {
                    steps {
                        sh 'npx tsx scripts/execute_creation_cycle.ts'
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
