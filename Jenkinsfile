pipeline {
    agent any

    stages {
        stage('version-check') {
            steps {
                sh 'python --version'
            }
        }

        stage('check-website') {
            steps {
                sh 'python test_website.py'
            }
        }
    }
}
