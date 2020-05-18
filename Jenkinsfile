pipeline {
	agent {
		docker {
			image 'jayantha:1.0'
		}
	}
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
