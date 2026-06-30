pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        PYTHON = 'python'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    %PYTHON% -m pytest test_calculator.py -v --junitxml=pytest-report.xml
                """
            }
        }
    }

    post {

        always {
            junit allowEmptyResults: true, testResults: 'pytest-report.xml'
            archiveArtifacts artifacts: 'pytest-report.xml', fingerprint: true
        }

        success {
            echo "Build completed successfully."
        }

        failure {
            echo "Build failed. Sending webhook..."

            httpRequest(
                url: 'https://YOUR_NGROK_URL/webhook/jenkins',
                httpMode: 'POST',
                contentType: 'APPLICATION_JSON',
                customHeaders: [[
                    name: 'X-Jenkins-Signature',
                    value: 'YOUR_SIGNATURE'
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
        }
    }
}