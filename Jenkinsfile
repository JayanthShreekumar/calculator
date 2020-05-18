pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python setup.py develop'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
            post {
              always {
                junit 'test-reports/*.xml'
              }
            }
        }
    }
}
