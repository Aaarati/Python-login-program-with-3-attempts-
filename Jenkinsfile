pipeline {
    agent any

    stages {
        stage('version') {
            steps {
               python3 'python --version'
            }
        }
        
        stage('build') {
            steps {
               python3 'python login.py'
            }
        }
    }
}

