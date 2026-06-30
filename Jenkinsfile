pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest test_calculator.py -v'
            }
        }
    }

    post {
        failure {
            httpRequest(
                url: 'https://cobalt-confetti-turbofan.ngrok-free.dev/webhook/jenkins',
                httpMode: 'POST',
                contentType: 'APPLICATION_JSON',
                customHeaders: [[name: 'X-Jenkins-Signature', value: env.WEBHOOK_SECRET]],
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
