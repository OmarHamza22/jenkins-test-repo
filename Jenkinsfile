pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        PYTHON = 'C:\\Users\\lenovo\\AppData\\Local\\Python\\bin\\python.exe'
        WEBHOOK_URL = 'https://cobalt-confetti-turbofan.ngrok-free.dev/webhook/jenkins'
        WEBHOOK_SECRET = 'ba5bcf2a66f7042820997725120073cb078be39dfdf43c228ba665e52c12fd39'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat """
                    "%PYTHON%" -m pip install --upgrade pip
                    "%PYTHON%" -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    "%PYTHON%" -m pytest test_calculator.py -v --junitxml=pytest-report.xml
                """
            }
        }
    }

    post {

        always {
            junit allowEmptyResults: true, testResults: 'pytest-report.xml'

            archiveArtifacts(
                artifacts: 'pytest-report.xml',
                allowEmptyArchive: true
            )
        }

        success {
            echo '✅ Build completed successfully.'
        }

        failure {
            echo '❌ Build failed. Sending webhook...'

            httpRequest(
                url: "${WEBHOOK_URL}",
                httpMode: 'POST',
                contentType: 'APPLICATION_JSON',
                customHeaders: [[
                    name: 'X-Jenkins-Signature',
                    value: "${WEBHOOK_SECRET}"
                ]],
                requestBody: """
                {
                    "name": "${env.JOB_NAME}",
                    "repo_name": "OmarHamza22/jenkins-test-repo",
                    "build": {
                        "number": ${env.BUILD_NUMBER},
                        "phase": "FINISHED",
                        "status": "FAILURE",
                        "full_url": "${env.BUILD_URL}",
                        "scm": {
                            "branch": "main",
                            "commit": "${env.GIT_COMMIT}"
                        }
                    }
                }
                """
            )

            echo 'Webhook sent.'
        }
    }
}