pipeline {
    agent any

    environment {
        MACBOOK_CLOUD_SIMULATION = 'true'
        ARCH = 'amd64'
        DOCKER_ACCESS_TOKEN = credentials('docker-access-token')
        DOCKER_ACCOUNT = credentials('docker-account')
        CLOUD_BUILDER_NAME = 'sor'
        IMAGE_NAME = 'getanant/docker-build-cloud-demo'
    }

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

        stage('Engine Connection') {
            steps {
                sh 'npm run connect'
            }
        }

        stage('Test testservice') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/testservice.test.ts'
            }
        }

        stage('Test autonomous_resource_optimizer') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/autonomous_resource_optimizer.test.ts'
            }
        }

        stage('Test system_health_dashboard') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/system_health_dashboard.test.ts'
            }
        }

        stage('Test proactive_scalability') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/proactive_scalability.test.ts'
            }
        }

        stage('Test autonomous_ux_optimization') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/autonomous_ux_optimization.test.ts'
            }
        }

        stage('Test global_neural_sync_service_phase_12') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/global_neural_sync_service_phase_12.test.ts'
            }
        }

        stage('Test ai_strategy_advisor') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/ai_strategy_advisor.test.ts'
            }
        }

        stage('Test dynamic_schema_evolution') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/dynamic_schema_evolution.test.ts'
            }
        }

        stage('Test autonomous_documentation') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/autonomous_documentation.test.ts'
            }
        }

        stage('Test test_autonomous') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/test_autonomous.test.ts'
            }
        }

        stage('Creative Workflow') {
            parallel {
                stage('Analyze Market') {
                    steps {
                        sh 'npm run ingest:sor'
                        sh 'npm run ingest:forbes'
                    }
                }
                stage('Generate Assets') {
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

        stage('Docker Build') {
            environment {
                BUILDX_URL = sh(returnStdout: true, script: 'curl -s https://raw.githubusercontent.com/docker/actions-toolkit/main/.github/buildx-lab-releases.json | jq -r ".latest.assets[] | select(endswith(\"linux-$ARCH\"))"').trim()
                COMPOSE_URL = sh(returnStdout: true, script: 'curl -sL -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/docker/compose-desktop/releases | jq "[ .[] | select(.prerelease==false and .draft==false) ] | .[0].assets.[] | select(.name | endswith(\"linux-${ARCH}\")) | .browser_download_url"').trim()
            }
            steps {
                sh 'mkdir -vp ~/.docker/cli-plugins/'
                sh 'curl --silent -L --output ~/.docker/cli-plugins/docker-buildx $BUILDX_URL'
                sh 'curl --silent -L --output ~/.docker/cli-plugins/docker-compose $COMPOSE_URL'
                sh 'chmod a+x ~/.docker/cli-plugins/docker-buildx'
                sh 'chmod a+x ~/.docker/cli-plugins/docker-compose'
                sh 'echo "$DOCKER_ACCESS_TOKEN" | docker login --username $DOCKER_ACCOUNT --password-stdin'
                sh 'docker buildx create --use --driver cloud "${DOCKER_ACCOUNT}/${CLOUD_BUILDER_NAME}"'
                sh 'docker compose build || true'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results/**/*.md', allowEmptyArchive: true
        }
    }
}
