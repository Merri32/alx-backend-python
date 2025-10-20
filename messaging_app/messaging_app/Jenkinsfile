pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📥 Cloning repository from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/Merri32/alx-backend-python.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                withPythonEnv("${VENV_DIR}") {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install --upgrade pip'
                    sh '. venv/bin/activate && pip install -r messaging_app/requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests using pytest...'
                withPythonEnv("${VENV_DIR}") {
                    sh '. venv/bin/activate && pytest messaging_app/tests/ --junitxml=report.xml'
                }
            }
            post {
                always {
                    echo '📊 Publishing test results...'
                    junit 'report.xml'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs and test report in Jenkins.'
        }
    }
}
