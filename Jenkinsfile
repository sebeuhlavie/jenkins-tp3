pipeline {
    agent any

    options {
        timeout(time: 10, unit: 'MINUTES')
        timestamps()
    }

    stages {
        stage('Préparation') {
            steps {
                sh '''
                    rm -rf reports .coverage .coverage.*
                    mkdir -p reports
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/pip install --quiet --upgrade pip
                    .venv/bin/pip install --quiet -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v --junitxml=reports/junit.xml'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                }
            }
        }
    }
}